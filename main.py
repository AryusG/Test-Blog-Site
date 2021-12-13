from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    p = Post("https://api.npoint.io/c790b4d5cab58020d391")
    # iterate through len of p.json to create cards for main page 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
