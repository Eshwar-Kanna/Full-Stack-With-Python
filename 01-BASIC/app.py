import subprocess

from flask  import Flask, render_template

app = Flask("kanna")

@app.route("/search")
def mysearch() :
    print("hello")
    return "hiiiii"

@app.route("/mail") 
def mymail() :
    return "this is mail "

@app.route("/form")
def myform() :
    return  "<h1> this is form  </h1> "

@app.route("/file")
def file() :
    return render_template("one.html")

app.run(port = 5000 ,debug = True )

