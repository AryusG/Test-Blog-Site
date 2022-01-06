from flask import Flask, render_template
from post import Post

app = Flask(__name__)

p = Post("https://api.npoint.io/c790b4d5cab58020d391")
json = p.json

@app.route('/')
def home():
    return render_template("index.html", json=json)

@app.route('/post/<int:index>')
def post(index):
    return render_template("post.html", json=json, index=index)

if __name__ == "__main__":
    app.run(debug=True)
