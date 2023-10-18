from flask import Flask, render_template, request


sports = Flask(__name__) # initializng the flask app


@sports.route('/')
def helloworld():
    return render_template("index.html")

if __name__== '__main__':
   sports.run(debug = False,port = 5000)