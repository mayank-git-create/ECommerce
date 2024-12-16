from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("item_home_page.html")

if __name__ == '__main__':
    app.run()
