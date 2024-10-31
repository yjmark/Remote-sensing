# MUSA 650 Homework 1: Basics of Machine Learning

In this assignment, you’ll explore fundamental machine learning concepts and techniques, with a focus on data preprocessing, image manipulation, and model evaluation. You are responsible for figuring out the code independently and may refer to tutorials, code examples, or use AI support, but **please cite all sources**.

Submit a single Jupyter Notebook containing code, narrative text, visualizations, and answers to each question. Open a pull request from your fork of this repository to the main repository for submission.

## Important Notes

- **Sample Size Considerations**: If experiments take too long with the complete dataset, start with a smaller sample for timely execution. For your final submission, use the full dataset if feasible, but if processing is still too intensive, note your sample sizes clearly. Sample size variations will not affect grading if documented appropriately.
- **Data Reshaping**: To switch between 2D and 1D representations, use functions like `numpy.flatten()` or `numpy.resize()` as needed.

## Assignment Structure

Each section represents a stage of analysis and model development. Insert your code in the designated cells and answer the questions in text cells.

### S1. Data Exploration

1. What is the number of features in the training dataset?
2. What is the number of samples in the training dataset?
3. What is the number of features in the testing dataset?
4. What is the number of samples in the testing dataset?
5. What is the dimensionality of each data sample?

**Comprehension Questions**

- What does the `.shape` attribute of a NumPy array represent, and how can you interpret each element of this attribute for a 3D array?
- If an array has a shape of `(100, 28, 28)`, what does each number represent in the context of image data, and how would it change if you flattened it to a 2D array?

### S2. Viewing the Data

- Select one random example from each category in the testing set, display each 2D image, and label it with the corresponding category name.

### S3. Subsampling the Data

- Create a 10% random subset of each training and testing set:
  - What is the distribution of each label in the initial train data?
  - What is the distribution of each label in the reduced train data?

**Comprehension Questions**

- Why might subsampling a dataset be beneficial when developing machine learning models? Discuss the trade-offs.
- When reducing dataset size, what differences might you see in results between randomly selecting samples versus selecting the first portion of the dataset?

### S4. Subsampling the Data (Again)

- Create a 10% subset using the first 10% of the initial samples.
  - What is the distribution of each label in the initial train data?
  - What is the distribution of each label in the reduced train data?

### S5. Reshaping Data for Model Input

- Experiment with reshaping your data to understand how to prepare it for input into machine learning models.

**Comprehension Questions**

- Explain why it’s necessary to reshape data when transitioning from raw images to model input, particularly in neural networks. What are the implications of reshaping an image array into a vector (1D array) for each sample?
- How would you convert a 3D array into a 2D array without changing the total number of elements? Describe how `flatten()` and `reshape()` can be used for this purpose.

### S6. Exploring Features and Outputs

- Answer the following to deepen your understanding of the features (input) vs. output (label) distinction:
  - What are the features versus the output in this assignment? Why is it important to distinguish between features (inputs) and outputs (labels) in a machine learning model?
  - How do pixel values in an image serve as “features” that relate to an output label, like the digit "7"?

### S7. Binarization of Images

- Binarize images by converting pixel values to 0 or 1 based on a threshold and assess the implications.

**Comprehension Questions**

- What is binarization, and why might we binarize an input image? Discuss how binarizing images could impact factors like data types, storage size, and computational efficiency.
- How does binarization of images (converting pixel values to 0 or 1 based on a threshold) affect the representation of features, and what might be the benefits and limitations of this approach?

### S8: Calculating Averages and Standard Deviations

- Pixel-wise Averaging and Standard Deviation:
  - Calculate and plot mean and standard deviation images for category "3".
  - Repeat for another selected category (e.g., "7").

**Comprehension Questions**

- Describe how calculating a pixel-wise mean or standard deviation for a set of images can help you understand variations within a category. What does a high standard deviation indicate in this context?
- If the mean image of category "3" has strong features visible, what does this imply about the sample variation within that category?

### S9: Image Distances

1. What is the index of the most dissimilar image in category "3" in the training set?
2. Plot the most dissimilar image in 2D.
3. Plot the most similar image in 2D and provide its index.

### S10: Model Training - Evaluation and Interpretation

- Train and evaluate models using your processed data.

**Comprehension Questions**

- Explain why it’s important to have separate training and testing datasets. What potential issues arise if you use the same data for both training and evaluation?
- If you achieve a high accuracy on the training set but a lower accuracy on the testing set, what might this indicate about your model’s performance and generalization?

### S11: Model Limitations and Interpretation

- Reflect on potential challenges in model classification.

**Comprehension Question**

- Based on the patterns in the pixel values for each category, which labels (numbers) do you think the model might struggle to identify or distinguish from one another? Explain why certain labels might be more challenging to separate, considering the similarity in pixel patterns or shapes.
