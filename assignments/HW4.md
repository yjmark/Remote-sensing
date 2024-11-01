# MUSA 650 Homework 4: EuroSAT Land Use and Land Cover Classification using Deep Learning

In this homework, we will build off of the lessons from last homework. Your task is to implement deep learning models to solve a typical problem in satellite imaging using a benchmark dataset. The homework was designed to make you work on increasingly more complex models. We hope that the homework will be very helpful to improve your skills and knowledge in deep learning!

You are responsible for figuring out the code independently and may refer to tutorials, code examples, or use AI support, but **please cite all sources**.

Submit a single Jupyter Notebook containing code, narrative text, visualizations, and answers to each question. Open a pull request from your fork of this repository to the main repository for submission.

## Data Loading and Exploration

Visit [the EuroSAT data description page](https://github.com/phelber/eurosat) and download the data. Perform basic exploratory data analysis, assessing the class distribution across the dataset and plotting one image from each class in a 2x5 grid.

## Greyscale Images

### Preprocessing

Convert each RGB image to greyscale and flatten the images into a data matrix (n x p: n = #samples, p = #pixels in each image). Load the images and labels into numpy arrays. Then, plot three random grayscale images with their labels, followed by a histogram of the label distribution across the samples. Split the data into training (50%) and testing sets (50%), stratified on class labels (equal percentage of each class type in train and test sets). Flatten the images into a shape appropriate for use in the deep learning models that follow.

**Bonus:** Before splitting the data into training and testing sets, apply data augmentation to increase the size of the dataset, appending the new samples to the original greyscale images. Indicate the augmentation approach(es) that you used and the total size of the new dataset. Again, plot three random images and a histogram of the label distribution across the full dataset.
Load images and labels into numpy arrays

### Model One

Implement a first deep learning model (M.1) using a fully connected network with a single fully connected layer (i.e: input layer + fully connected layer as the output layer). Calculate classification accuracy on the test data. (Hint: what kind of pre-processing might be necessary so that this model and the subsequent ones can handle categorical labels? Why?)

### Model Two

Implement a second deep learning model (M.2) adding an additional fully connected hidden layer (with an arbitrary number of nodes) to the previous model. Calculate classification accuracy on the test data.

### Model Three

Implement a third deep learning model (M.3) adding two additional fully connected hidden layers (with arbitrary number of nodes) for a total of four, as well as drop-out layers to the previous model. Calculate classification accuracy on the test data.

### Model Comparison

Compare models one through three. Which model was the "best"? Why? How did adding dropout layers to the model affect its accuracy? For each model, what is the impact of increasing the number of training epochs?

**Bonus:** Implement an ensemble model that incorporates the predictions of models one through three. Calculate its classification accuracy on the test data. How does this compare to the accuracies of the three individual model?

## RGB Images

Take the original RGB images and do not vectorize them. Use these images as the data input for the following models (M.4 and M.5).

### Model Four

Implement a fourth CNN model (M.4) that includes the following layers: Conv2D, MaxPooling2D, Dropout, Flatten, Dense. Calculate classification accuracy on the test data. Compare against previous models. Which model was the "best"? Why? Did you notice any limitations in terms of training speed compared to the previous models?

### Model Five

Implement a fifth deep learning model (M.5) targeting accuracy that will outperform all previous models. You are free to use any tools and techniques, including ensemble models and pre-trained models for transfer learning. Calculate classification accuracy on the test data. Compare against previous models. Which model was the "best"? Why?

What are the two classes with the highest labeling error? Explain using data and showing mis-classified examples. Why do you think this is? Can you think of any strategies or approaches that might help to address this issue?

## Multispectral Images

Apply your best model on multispectral images. You may use whichever image channels you wish, so long as you use more than just RGB (although you are not required to use any color channels). Calculate classification accuracy on the test data. Compare against results using RGB images.

It took me a long time to get these loaded properly, but I managed it eventually. Because of how much memory the dataset takes up, I chose not to augment it. This will likely cost me accuracy but will allow me to run my models faster.

## Reflection Questions

What are your takeaways from tuning the parameters of the different models? What are your observations about increasing the number of training epochs? Did you run into any challenges or limitations when doing this? What was the impact of using dropout? If you answered the bonus questions, how did the ensemble models compare to the other models? What kinds of challenges or limitations did you encounter when preparing and training the models for this assignment, and how might you address them in the future?
