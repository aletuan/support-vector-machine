# Support Vector Machine (SVM) Basics (Linear SVM)

Support Vector Machines (SVMs) are a type of machine learning model used for classification. Imagine you have a bunch of data points, and you want to draw a line to separate them into different groups. That's what an SVM does!

## What is a Linear SVM?

A Linear SVM is used when your data can be separated by a straight line (in 2D) or a flat plane (in 3D or higher dimensions). This line or plane is called a **hyperplane**.

### The Goal: Find the Best Separating Line

The main idea behind a Linear SVM is to find the "best" possible straight line (or hyperplane) that separates your data points. But what makes a line "best"?

It's the line that has the **largest margin**.

### What is the Margin?

Imagine you draw a line to separate two groups of points. Now, imagine drawing two more lines, parallel to your first line, that just touch the closest points from each group. The space between these two parallel lines is called the **margin**.

An SVM tries to make this margin as wide as possible. Why? Because a wider margin generally means the model is more robust and will do a better job at classifying new, unseen data.

### Support Vectors: The Key Points

The data points that are closest to the separating line (the ones that the margin lines touch) are called **Support Vectors**. These points are super important! If you move or remove a support vector, the separating line might change.

Think of them as the "support beams" that hold up the separating line.

## How it Works (Simplified):

1.  **Look at the data**: The SVM looks at all your data points, which are labeled as belonging to one group or another.
2.  **Find the closest points**: It identifies the points from each group that are closest to each other.
3.  **Draw the margin**: It draws two parallel lines that pass through these closest points, one for each group.
4.  **Draw the separating line**: It then draws the main separating line exactly in the middle of these two margin lines.
5.  **Maximize the margin**: The SVM adjusts this main line until the distance between the two margin lines (the margin) is as big as possible.

## In Summary:

A Linear SVM is a simple yet powerful classifier that finds the best straight line (or hyperplane) to separate your data by maximizing the distance (margin) between the closest data points of different classes. These closest points are called Support Vectors.

This project uses a Linear SVM to classify Iris flowers, which is a good example of how this concept works in practice.