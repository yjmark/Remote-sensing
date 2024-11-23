# Lab: Creating a Cloud-Free Composite for Philadelphia with Sentinel-2 (Summer 2024)

## Objective

In this lab, you will:

1. Query Sentinel-2 data for Philadelphia during the summer of 2024 (June–August) using the STAC API.
2. Create a cloud-free composite by taking the median of images over this time period.
3. Calculate NDVI, NDBI, and NDWI from the composite.
4. Visualize the indices on a map for Philadelphia.

---

## Instructions

Use the tutorial from the following link as the basis for your work:  
[Project Pythia Landsat ML Cookbook - Data Ingestion](https://projectpythia.org/landsat-ml-cookbook/notebooks/1.0_Data_Ingestion-Geospatial.html)

While the tutorial provides an interactive visualization option, we recommend using regular `matplotlib` for your visualizations in this lab, as it's simpler to use in a Jupyter Notebook.

### 1. Query Sentinel-2 Data

- Define the area of interest (AOI) as a bounding box or GeoJSON file for Philadelphia (`bbox = [-75.2803, 39.8670, -74.9557, 40.1379]`).
- Query imagery for the date range `2024-06-01/2024-08-31` with less than 10% cloud cover.
- Use the collection `sentinel-2-l2a` and filter using `eo:cloud_cover`.
- Note that your query for this bounding box will return multiple tiles, which you will need to merge (e.g., `ds_merged = xr.concat(datasets, dim="time")`). This merges **spatially**, while the median composite (in the next step) is calculated **across time**.
- Hint: don't forget to set the `attrs` of your data array, including your CRS.
- Normalize your band values to correctly calculate the indices.

### 2. Create a Cloud-Free Composite

- Extract necessary bands (`red`, `green`, `blue`, `nir`, and `swir16`) from filtered imagery.
- Align all images to a common spatial reference system if required.
- Compute a median composite for each band to reduce cloud effects.

### 3. Calculate Indices

- Calculate the following indices:
- **NDVI**: `(nir - red) / (nir + red)`
- **NDBI**: `(swir16 - nir) / (swir16 + nir)`
- **NDWI**: `(green - nir) / (green + nir)`
- Mask invalid or missing data for accurate results.

### 4. Visualize the Indices

- Generate separate maps for NDVI, NDBI, and NDWI:
- Use appropriate color scales.
- Add legends or titles for clarity.
- Use `matplotlib` for plotting to avoid issues with interactive maps in Jupyter Notebooks.

---

## Deliverables

All code, visualizations, and analyses should be included in a single Jupyter Notebook.

## Collaboration Policy

Work in groups of up to **4 people**. Collaborate to split tasks and share findings within your group.

## Important Note

We will reuse code and concepts from this assignment in future labs and homeworks. Completing this lab thoroughly and saving your work will significantly benefit you later in the course.
