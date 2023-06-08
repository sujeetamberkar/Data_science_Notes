from flask import Flask, redirect,request
# https://orange-receptionist-jdbiz.pwskills.app:5000/test2/test2?x=4
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World! This is sujeet </h1>"


@app.route("/hello_world2")
def hello_world2():
    a=5
    b=6
    c=a+b

    return "<h1>Hello, World2! This is sujeet </h1> {}".format(c)



@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    data2=int(data)+1
    return  "this is a data input form my url {}".format(data2)

@app.route("/hello_world3")
def hello_world3():
    return redirect("/")


if __name__=="__main__":
    app.run(host="0.0.0.0")
