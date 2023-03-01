from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)
