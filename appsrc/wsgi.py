from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/health")
def hello():
    return "OK"

if __name__ == "__main__":
    application.run()