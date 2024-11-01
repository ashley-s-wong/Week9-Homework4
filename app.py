from flask import Flask, render_template, request
import google.generativeai as genai
from textblob import TextBlob
import os
import random

# api = os.getenv("MAKERSUITE_API_TOKEN")
# palm.configure(api_key = api)
genai.configure(api_key = "AIzaSyAoZL9Vi7joGfF9D-cIO4IkphC2-8-jJF8")

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods = ["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods = ["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = model.generate_content(q + "Limit your response to a maximum of two sentences.")
    return(render_template("makersuite.html", r = r.text))

@app.route("/prediction", methods = ["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke", methods = ["GET","POST"])
def joke():
    randomNum = random.randint(0,1)
    if randomNum == 0:
        r = model.generate_content("Tell me a Singaporean joke! Limit your response to a maximum of two sentences.")
    else:
        r = model.generate_content("Give me an insight on the current financial news! Limit your response to a maximum of two sentences.")
    return(render_template("index.html", r = r.text))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/TM",methods=["GET","POST"])
def TM():
    return(render_template("TM.html"))

@app.route("/SAR",methods=["GET","POST"])
def SAR():
    q = request.form.get("q")
    r=TextBlob(q).sentiment
    return(render_template("SAR.html",r=r))

if __name__ == "__main__":
    app.run()