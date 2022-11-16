from flask import Flask , render_template , request
app = Flask("routeapp")
@app.route('/form')
def myform() :
    return render_template("basic.html")

@app.route('/name/<y>')
def myname (y) :
    return y.upper

@app.route("/data" , methods =["GET"])
def mydata() :
    if request.method == "GET" :
        data = request.args.get("x")
        print(data)
        return data

app.run(port = 5500 , debug = True)

"""
@app.route("/data" , methods =["POST"])
def mydata() :
    if request.method == "POST" :
        data = request.form.get("x")
        print(data)
        return data.upper()
"""