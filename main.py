from flask import Flask, render_template ,request
import requests
import smtplib
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
MY_EMAIL = "xristakos167@gmail.com"
MY_PASSWORD = "tqmx fdnv payq qwpm"

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html",flag=1)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.post("/form-entry")
def receieve_data():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg=f"Subject: letsgooo\n\n  {request.form['name']}\n {request.form['email']}\n {request.form['phone']}\n {request.form['message']}\n "
        )

    return render_template("contact.html", flag=2,)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
