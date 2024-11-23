# Lab: Creating a Cloud-Free Composite for Philadelphia with Sentinel-2 (Summer 2024)

## Objective

In this lab, you will:

1. Query Sentinel-2 data for Philadelphia during the summer of 2024 (June–August) using the STAC API.
2. Create a cloud-free composite by taking the median of images over this time period.
3. Calculate NDVI, NDBI, and NDWI from the composite.
4. Visualize the indices on a map for Philadelphia.

### Why This Matters

The indices calculated in this lab—NDVI, NDBI, and NDWI—are key tools in environmental analysis:

- **NDVI (Normalized Difference Vegetation Index):** Measures vegetation health and coverage by comparing near-infrared (NIR) and red light absorption, as plants strongly absorb red light for photosynthesis while reflecting NIR.
- **NDBI (Normalized Difference Built-up Index):** Highlights built-up areas by comparing shortwave infrared (SWIR) and NIR reflectance. Built-up surfaces like concrete and asphalt reflect SWIR more than NIR.
- **NDWI (Normalized Difference Water Index):** Detects water features by comparing green and NIR reflectance, as water absorbs NIR and reflects green light.

By the end of this lab, you'll have a cloud-free image composite and calculated indices that provide insight into Philadelphia’s summer 2024 conditions, such as vegetation health, urbanization patterns, and water distribution.

---

## Instructions

Use the tutorial from the following link as the basis for your work:  
[Project Pythia Landsat ML Cookbook - Data Ingestion](https://projectpythia.org/landsat-ml-cookbook/notebooks/1.0_Data_Ingestion-Geospatial.html)

While the tutorial provides an interactive visualization option, we recommend using regular `matplotlib` for your visualizations in this lab, as it's simpler to use in a Jupyter Notebook.

### 1. Query and Process Sentinel-2 Data

This step retrieves the raw data you'll need for analysis. Sentinel-2 provides high-resolution imagery with multispectral bands, allowing detailed environmental analysis. You’ll filter for summer 2024 to capture seasonal patterns while excluding images with excessive cloud cover to ensure accuracy.

- Define the area of interest (AOI) as a bounding box or for Philadelphia (`bbox = [-75.2803, 39.8670, -74.9557, 40.1379]`).
- Query imagery for the date range `2024-06-01/2024-08-31` with less than 10% cloud cover. This ensures you’re working with clear images for better results.
- Use the collection `sentinel-2-l2a` and filter using `eo:cloud_cover`.
- Note that your query for this bounding box will return multiple tiles, which you will need to merge (e.g., `ds_merged = xr.concat(datasets, dim="time")`). This step combines spatial tiles into a single image.
- Hint: don't forget to set the `attrs` of your data array, including your CRS, to ensure spatial consistency.
- Extract necessary bands (`red`, `green`, `blue`, `nir`, and `swir16`) from filtered imagery. These bands are needed for calculating the indices.
- Compute a median composite for each band to minimize the influence of outliers like clouds.
- Normalize your band values to correctly calculate the indices in later steps.

### 2. Calculate Indices

Once you have the cloud-free composite, you’ll compute the indices to analyze specific environmental features:

- **NDVI**: `(nir - red) / (nir + red)`
  - This highlights vegetation, with higher values indicating healthier, denser vegetation.
- **NDBI**: `(swir16 - nir) / (swir16 + nir)`
  - This differentiates urbanized areas from natural land cover, helping identify built-up regions.
- **NDWI**: `(green - nir) / (green + nir)`
  - This detects water bodies, which is useful for understanding water distribution in the city.
- Mask invalid or missing data for accurate results, ensuring indices represent real conditions.

### 4. Visualize the Indices

Visualizing the indices helps interpret the results and draw insights from the data. For example, NDVI can reveal areas of urban greenery, NDBI can show the extent of urban sprawl, and NDWI can identify water retention issues.

- Generate separate maps for NDVI, NDBI, and NDWI:
  - Use appropriate color scales for each index to highlight key features (e.g., green for vegetation in NDVI, blue for water in NDWI).
  - Add legends or titles for clarity.
  - Use `matplotlib` for plotting to ensure reproducibility and avoid issues with interactive visualizations in Jupyter Notebooks.

---

## Deliverables

All code, visualizations, and analyses should be included in a single Jupyter Notebook.

## Collaboration Policy

Work in groups of 2-3 people.

## Important Note

We will reuse code and concepts from this assignment in future labs and homeworks. Completing this lab thoroughly and saving your work will significantly benefit you later in the course.
