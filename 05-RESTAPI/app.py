from flask import Flask , request , render_template

app = Flask("restapi")

db = [
{
    "id" : 1 ,
    "name" : "kanna" , 
    "mobile" :[
        {
            "name" :"landline" ,
            "number" : 1111 ,
        } ,
        {
            "name" : "cell" ,
            "number" : 2564 
        } ,
    ]

} ,
{
    "id" : 2 ,
    "name" :"tom" ,
    "surname" : "xyz"
}
]

@app.route( '/spost' , methods = ["GET"])
def f1() :
    return "read a post" 

@app.route("/spost" , methods = ["DELETE"]) 
def f2() :
    return "delete a post"

@app.route("/spost" , methods = ["PUT"])
def f3() :
    return  "update a post"

app.run(port = 5555 , debug = True)
