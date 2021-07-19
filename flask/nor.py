from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("myhome.html")

@app.route('/about')
def about():
    log = request.args.get("login")
    pas = request.args.get("password")
    nam = request.args.get("name")
    fname = request.args.get("surname")
    info = None
    if log == "":
        return render_template("myhome.html",info="please enter your login")
    elif pas == "":
        return render_template("myhome.html",info="please enter your password")
    elif nam == "":
        return render_template("myhome.html",info="please enter your name")
    elif fname == "":
        return render_template("myhome.html",info="please enter your surname")
    return render_template("myabout.html",nam = nam,fname = fname)

if __name__=="__main__":
    app.run(debug=True)
