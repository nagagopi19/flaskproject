from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
<<<<<<< HEAD
    return "<p>Hello, Devops!</p>"
=======
    return "<p>Hello, World!</p>"
    return "<p>Hello, Checkred!</p>
>>>>>>> d7c1ae90e942844449533018811e1ac62a11fe29
