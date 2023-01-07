from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():    
    curent_year = datetime.now().year
    random_number = random.randint(1,10)

    return render_template("index.html", num=random_number, year= curent_year)


@app.route("/guess/<name>")
def genderize(name):
    genderize_response = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = genderize_response["gender"]
    agify_response = requests.get(f"https://api.agify.io?name={name}").json()
    age = agify_response["age"]
     
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blog_post=blog_response)

if __name__ == "__main__":
    app.run(debug=True)

