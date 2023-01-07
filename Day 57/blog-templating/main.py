from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", blog_posts= blog_response)


@app.route("/blog/<int:num>")
def get_blog(num):
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", blog_post=blog_response[num-1])



if __name__ == "__main__":
    app.run(debug=True)
