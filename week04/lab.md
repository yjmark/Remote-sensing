# Lab: Multisensor Data Fusion and Clustering for Tehran (August 2024)

## Objective

In this lab, you will:

1. Retrieve Sentinel-1 and Sentinel-2 data for Tehran during August 2024.
2. Create cloud-free, median composites for Sentinel-1 and Sentinel-2.
3. Visualize Sentinel-1 and Sentinel-2 images and their fusion using matplotlib.
4. Perform K-means clustering on Sentinel-1, Sentinel-2, and fused data arrays.
5. Apply PCA to the fused image and analyze the results.
6. Compare the clustering results to the 2021 ESA WorldCover land cover map.

---

## Instructions

### 1. Query and Process Sentinel-1 and Sentinel-2 Data

- Define the bounding box and date range for Tehran:
  - `bbox = [51.2196, 35.5384, 51.6759, 35.8456]`
  - `datetime = "2024-08-01/2024-08-31"`
- Query Sentinel-1 (collection: `sentinel-1-rtc`) for VV and VH bands.
- Query Sentinel-2 (collection: `sentinel-2-l2a`) for red, green, and blue bands.
- Filter for cloud coverage below 10% for Sentinel-2 data.
- Merge spatial tiles for each dataset and compute median composites for the bounding box.

### 2. Visualize the Composites

- For Sentinel-1, apply a logarithmic stretch to VV and VH bands for better visualization. Visualize both bands individually using a palette like `viridis`, and then make a pseudo-RGB composite.
- Visualize the Sentinel-2 composite as a true-color image using red, green, and blue bands.
- Fuse Sentinel-1 and Sentinel-2 composites into a single data array (10m resolution).

**Analytic Question**:  
How does Sentinel-1 differ from Sentinel-2? What strengths and limitations do they have individually and when fused?

### 3. K-Means Clustering

- Normalize and scale Sentinel-1, Sentinel-2, and fused data arrays.
- Iteratively pply K-means clustering with varying cluster counts (3 through 7) to:
  - Sentinel-1 composite
  - Sentinel-2 composite
  - Fused composite
- Visualize the clustering results for each case.

**Analytic Question**:  
How effective is K-means for this context? What are its strengths and limitations? Why might it be useful in contexts with limited labeled data?

### 4. PCA and Clustering on Fused Data

- Apply PCA to the fused dataset to reduce its dimensionality.
- Visualize the first three principal components with bar graphs to understand the variance explained.
- Apply K-means clustering to the PCA-transformed data and compare results with clustering on the raw fused data.

**Analytic Questions**:

- What benefits does PCA offer for larger datasets or multispectral vs. hyperspectral imagery?
- How do PCA-transformed clustering results compare to raw clustering results?

### 5. Compare with ESA WorldCover

- Map the 2021 ESA WorldCover land cover data for the bounding box.
- Compare the clustering results from Sentinel data to the WorldCover classification.

**Analytic Question**:  
How well do the clustering results align with WorldCover land cover classifications? What insights or discrepancies stand out?

---

## Deliverables

1. A Jupyter Notebook with all code, visualizations, and analyses.
2. Responses to analytic questions embedded in the notebook.

## Collaboration Policy

Work in groups of 2-3 people.
