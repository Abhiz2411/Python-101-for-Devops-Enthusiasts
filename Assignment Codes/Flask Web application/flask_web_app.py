from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Here is a Demo Flask app by Abhijit Zende</h1><p>Happy learning!</p>"

if __name__ == '__main__':
    app.run(debug=True)
