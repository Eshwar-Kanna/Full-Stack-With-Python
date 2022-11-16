from flask import Flask , render_template , request
import subprocess
app = Flask("webui")

@app.route("/form")
def myform() :
    return render_template("form.html")

@app.route("/run" , methods = ["GET"])
def run() :
    cmd = request.args.get("x")
    print(cmd)
    return subprocess.getoutput(cmd)

app.run(port = 5000 , debug = True)