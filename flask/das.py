from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return render_template('das.html')

@app.route("/about")
def about():
    if request.args["lname"]=="+":
        c = int(request.args["fname"])+int(request.args["login"])
    elif request.args["lname"]=="-":
        c = int(request.args["fname"])-int(request.args["login"])
    elif request.args["lname"]=="/":
        c = int(request.args["fname"]) / int(request.args["login"])
    elif request.args["lname"]=="*":
        c = int(request.args["fname"]) * int(request.args["login"])
    return render_template('about2.html',info = c)

if __name__ == "__main__":
    app.run(debug=True)
