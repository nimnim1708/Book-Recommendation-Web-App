# Book Recommendation Web Application

**Name:** Nimya Thekkumthala
**Matriculation Number:** 20-721-965
**University:** University of St. Gallen
**Course:** Skills: Programming with Advanced Computer Languages (7,789,1.00)
**Semester:** Spring Semester 2026

---

# Project Overview

This project implements a web-based book recommendation system using Python, Flask, and machine learning techniques.

The application allows users to:

* Browse the Top 50 most popular books
* Search for books using an autocomplete search bar
* Receive personalized book recommendations based on collaborative filtering
* Explore book covers, authors, and ratings through an interactive web interface

---

# Technologies Used

* Python 3.11
* Flask
* Pandas
* NumPy
* Scikit-learn
* Bootstrap 5
* HTML
* CSS

---

# Python Version

This project was developed and tested using **Python 3.11**.

Some dependencies may not work correctly with older or newer Python versions. Therefore, Python 3.11 is recommended.

---

# Dataset

The project uses the **Book Recommendation Dataset** available on Kaggle:

https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

The dataset consists of:

* Books.csv
* Users.csv
* Ratings.csv

---

# Project Structure

```text
Book-Recommendation-Web-App/

├── data/
│   ├── Books.csv
│   ├── Users.csv
│   └── Ratings.csv

├── models/
│   ├── popular.pkl
│   ├── books.pkl
│   ├── pt.pkl
│   └── similarity_scores.pkl

├── notebooks/
│   └── book_recommendation_system.ipynb

├── templates/
│   ├── index.html
│   └── recommend.html

├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Recommendation Approach

## Popularity-Based Recommendation

The homepage displays the Top 50 books based on:

* Number of ratings
* Average rating

To ensure reliable rankings, only books with at least 250 ratings are considered.

This approach provides users with highly rated and widely recognized books.

## Collaborative Filtering

For personalized recommendations, an item-based collaborative filtering approach is implemented.

The process consists of:

1. Creating a user-book rating matrix (pivot table)
2. Filling missing values with zeros
3. Computing cosine similarity between books
4. Identifying books that are most similar to the selected title

When a user enters a book title, the application recommends books with similar rating patterns among readers.

---

# Design Choices

Several design decisions were made to improve usability and performance:

* Flask was used to build the web application.
* Bootstrap was used to create a responsive user interface.
* An autocomplete search feature helps users find valid book titles.
* Computationally expensive calculations are performed beforehand in a Jupyter Notebook.
* The resulting objects are stored as Pickle files and loaded directly into the Flask application.

This approach improves runtime performance and keeps the application responsive.

# How to Run the Project

## Prerequisites

Before running the application, ensure that **Python 3.11** is installed on your system.

## Step 1: Download the Project

Download or clone the repository and extract the project folder.

## Step 2: Open a Terminal

Navigate to the project directory:

```bash
cd Book-Recommendation-Web-App
```

## Step 3: Create a Virtual Environment

```bash
py -3.11 -m venv venv
```

## Step 4: Activate the Environment

Windows:

```bash
.\venv\Scripts\Activate.ps1
```

## Step 5: Install Required Libraries

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```
Note: The installation may take several minutes because large libraries such as NumPy, Pandas, SciPy, and Scikit-learn need to be downloaded and installed. Please wait until the installation is completed before proceeding to the next step.

## Step 6: Run the Application

```bash
.\venv\Scripts\python.exe app.py
```

## Step 7: Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

To stop the application:

```text
CTRL + C
```


# Learning Process and Use of AI

I am a beginner in machine learning and web development. During the development process, I used tutorials, technical articles, official documentation, and artificial intelligence tools to better understand concepts and solve implementation challenges.

ChatGPT was primarily used as a learning assistant for:

* Understanding machine learning concepts
* Debugging code
* Improving code structure
* Explaining Flask functionality
* Troubleshooting development and dependency issues

The project reflects my learning process and combines concepts from educational resources with my own implementation and adaptations.

---

# References

## Dataset

* Kaggle – Book Recommendation Dataset
  https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

## Video Tutorials

* Complete Book Recommender System Project | Collaborative Filtering Based
  https://www.youtube.com/watch?v=k1onjsTO9qg

* Book Recommendation System Using Machine Learning | Python | Project For Beginners
  https://www.youtube.com/watch?v=WVAghgxDYS4

* Learn Flask for Python – Full Tutorial
  https://www.youtube.com/watch?v=Z1RJmh_OqeA

## Articles and Documentation

* Introduction to Recommender Systems
  https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada

* How to Build a Book Recommendation System
  https://www.analyticsvidhya.com/blog/2021/06/build-book-recommendation-system-unsupervised-learning-project/

* Collaborative Filtering in Machine Learning
  https://www.geeksforgeeks.org/machine-learning/collaborative-filtering-ml/

* Building a Book Recommendation System Using Python
  https://weclouddata.com/blog/book-recommendation-system-using-python/

* Scikit-learn Documentation
  https://scikit-learn.org/stable/

* Pandas Documentation
  https://pandas.pydata.org/docs/

* Flask Documentation
  https://flask.palletsprojects.com/
