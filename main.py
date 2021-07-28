from contentFiltering import get_recommendations
from flask import Flask, jsonify
import csv

allData = []

with open("articles.csv",encoding = "utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allData = data[1:]

likedArticles = []
dislikedArticles = []

app = Flask(__name__)
@app.route("/get-article")

def getArticle():
    return jsonify({
        "data":allData[0],
        "status":"success"
    })

@app.route("/liked-article",methods = ["POST"])

def likedArticle():
    article = allData[0]
    allData = allData[1:]
    likedArticles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-article",methods = ["POST"])

def dislikedArticle():
    article = allData[0]
    allData = allData[1:]
    dislikedArticles.append(article)
    return jsonify({
        "status":"success"
    }),201
        
@app.route("/popular-movies")

def popularMovies():
    articlesData = []
    for article in output:
        _d = {
            "title":article[11],
        }

        allData.append(_d)
    return jsonify({
        data:articlesData,
        "status":"success"
    }),201

@app.route("/recommended-articles")

def recommendedArticles():
    allRecommended = []
    for likedArticle in likedArticles:
        output = get_recommendations(likedArticles[19])
        

if __name__ == "__main__":
    app.run()