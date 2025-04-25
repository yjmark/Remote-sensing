# sentinel_tensor.py
import ee
import numpy as np
import torch
from PIL import Image
import urllib.request
import io

ee.Initialize(project='yjmark-rs')

def get_s2_patch(lat, lon, size=256, start_date="2020-07-01", end_date="2020-10-31", scale=10, bands=None):
    """
    특정 위경도 주변에서 Sentinel-2 패치 (torch tensor) 반환
    """
    if bands is None:
        bands = ['B2', 'B3', 'B4', 
                 'B8', 'B11']  # 전체 12 밴드

    #point = ee.Geometry.Point([lon, lat])
    #buffer_size = size * scale / 2
    half_size = (size * scale) / 2
    region = ee.Geometry.Rectangle(
        [lon - half_size/111320, lat - half_size/111320, 
         lon + half_size/111320, lat + half_size/111320]
    )
    #region = point.buffer(buffer_size).bounds  # size = 128픽셀 → 반지름 범위

    s2 = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterDate(start_date, end_date)
        .filterBounds(region)
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))
        .select(bands)
        .median()
       
    )

    # getInfo 방식으로 픽셀 값 가져오기
    projection = ee.Projection('EPSG:4326').atScale(scale)
    data = s2.reduceRegion(
        reducer=ee.Reducer.toList(),
        geometry=region,
        scale=scale,
        maxPixels=1e9
    ).getInfo()
    # values = s2.sampleRectangle(region=region, defaultValue=0, properties=[]).getInfo()
    # print("Sampled patch shapes:", {band: np.array(values["properties"][band]).shape for band in bands})
    # 각 밴드마다 (size, size) 값이 들어 있는 dict → numpy stack
    # band_arrays = [np.array(values["properties"][band]) for band in bands]
    band_arrays = []
    for band in bands:
        if band in data and data[band] is not None:
            # 1차원 리스트를 2D 배열로 변환
            band_data = np.array(data[band])
            if len(band_data) > 0:
                band_array = np.reshape(band_data, (size, size))
                band_arrays.append(band_array)
            else:
                print(f"Empty data for band {band}, using zeros")
                band_arrays.append(np.zeros((size, size)))
        else:
            print(f"Band {band} not available, using zeros")
            band_arrays.append(np.zeros((size, size)))
        # try:
        #     arr = np.array(values["properties"][band])
        #     band_arrays.append(arr)
        # except KeyError:
        #     print(f"⚠️ Warning: Band {band} not found. Filling with zeros.")
        #     band_arrays.append(np.zeros((size, size)))  # 또는 예상되는 기본 shape

    img_array = np.stack(band_arrays, axis=0)  # (C, H, W)
    return torch.from_numpy(img_array.astype(np.float32))

    # url = s2.getThumbURL({
    #     "region": region,
    #     "dimensions": f"{size}x{size}",
    #     "format": "png",
    #     "min": 0,
    #     "max": 3000
    # })

    # # 이미지 불러오기
    # with urllib.request.urlopen(url) as response:
    #     img = Image.open(response)
    #     img_array = np.array(img).transpose(2, 0, 1).astype(np.float32)   # [HWC] → [CHW]
    #     return torch.from_numpy(img_array)
    
   