from flask import Flask, render_template, request
import requests
import smtplib


blog_response = requests.get("https://api.npoint.io/5140b693af8574dc2ead").json()
app = Flask(__name__)

@app.route("/")
def home():   
    return render_template("index.html", blog_post=blog_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html",is_successful=False)
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        my_email = "xxxxxxxxxx@gmail.com"
        my_password = "xxxxxxxxxx"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Form\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}"
            )
        return render_template("contact.html", is_successful=True)


@app.route("/post/<num>")
def get_blog(num):
    id=int(num)
    return render_template("post.html", blog_post=blog_response[id-1])


if __name__ == "__main__":
    app.run(debug=True)