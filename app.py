# Flask is used to build the web application
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load precomputed data and models
# (created beforehand in the Jupyter notebook)
popular_df = pickle.load(open("models/popular.pkl", "rb"))
pt = pickle.load(open("models/pt.pkl", "rb"))
books = pickle.load(open("models/books.pkl", "rb"))
similarity_scores = pickle.load(open("models/similarity_scores.pkl", "rb"))

# List of all book titles used for search suggestions
ALL_TITLES = list(pt.index)

#Home page: display Top 50 popular Books
@app.route("/")
def index():
    return render_template(
        "index.html",
        # Data passed to the template
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=list(popular_df["Image-URL-L"].values),
        votes=list(popular_df["num_ratings"].values),
        rating=list(popular_df["avg_rating"].values),
    )

# Page tat displays the recommendation search interface
@app.route("/recommend")
def recommend_ui():
    # initially blank page without recommendations
    return render_template("recommend.html", data=None)

# Autocomplete endpoint
@app.route("/suggest")
def suggest():
    # Get search query from URL parameters
    q = request.args.get("q", "").strip().lower()
    if not q:
        return jsonify([])

# Find matching book titles
    matches = [t for t in ALL_TITLES if q in t.lower()]
    return jsonify(matches[:10]) # return top 10 matches

# Handle recommendation request after form submission
@app.route("/recommend_books", methods=["POST"])
def recommend():
    user_input = request.form.get("user_input", "").strip()
    data = []
    # proceed only if the book exists in the pivot table
    if user_input and user_input in pt.index:
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:9] # skip the book itself and show 8 similiar books

        # collect metadata for recommended books
        for i in similar_items:
            title = pt.index[i[0]]

            temp_df = books[books["Book-Title"] == title].drop_duplicates("Book-Title")
            item = [
                temp_df["Book-Title"].values[0],
                temp_df["Book-Author"].values[0],
                temp_df["Image-URL-M"].values[0],
            ]
            data.append(item)

    return render_template("recommend.html", data=data)

# run the web application
if __name__ == "__main__":
    app.run(debug=True)

