from flask import Flask, render_template
import requests


blog_response = requests.get("https://api.npoint.io/5140b693af8574dc2ead").json()
app = Flask(__name__)

@app.route("/")
def home():   
    return render_template("index.html", blog_post=blog_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def get_blog(num):
    id=int(num)
    return render_template("post.html", blog_post=blog_response[id-1])


if __name__ == "__main__":
    app.run(debug=True)