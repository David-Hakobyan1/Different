from flask import Flask,render_template,url_for,request
import os

app = Flask(__name__)
DATA = {}

if os.path.isfile('textovil.txt'):
    f = open('textovil.txt','r')
    s = f.read().strip()
    for l in s.split("\n"):
        DATA[l.split(',')[0].split(':')[1]] = {}
        for el in l.split(','):
            DATA[l.split(',')[0].split(':')[1]][el.split(':')[0]] = el.split(":")[1]
    f.close()

@app.route('/register')
def register():
    global DATA
    print DATA 
    return render_template('register.html')

@app.route('/checksubmit')
def checksubmit():
    global DATA
    print DATA 
    if str(request.args["login"]) not in DATA:
        return "login " + str(request.args["login"]) + " dos not exists"
    else:
        if str(request.args["parol"]) == DATA[str(request.args["login"])]['parol']:
            return render_template('home.html',info=DATA[str(request.args["login"])])
        else:
            return "wrong password for " + str(request.args["login"])


@app.route('/submit')
def submit():
    print DATA 
    return render_template('submit.html')

@app.route('/checkregister')
def checkregister():
    global DATA
    print DATA 
    if request.args["login"] not in DATA:
        DATA[str(request.args["login"])] = {}
        DATA[str(request.args["login"])]['login'] = str(request.args["login"])
        DATA[str(request.args["login"])]['parol'] = str(request.args["parol"])
        DATA[str(request.args["login"])]['fname'] = str(request.args['fname'])
        DATA[str(request.args["login"])]['lname'] = str(request.args["lname"])
        text = "login:" + str(request.args["login"]) + ",parol:" + \
               str(request.args["parol"]) + ",fname:" + str(request.args['fname']) + \
               ",lname:" + str(request.args["lname"]) + "\n"
        print (text)
        if not os.path.isfile('textovil.txt'):
            f = open("textovil.txt", "w+")
            f.write(text)
            f.close()
            print "---wwwwwww-------"
        else:
            f = open("textovil.txt", "a")
            f.write(text)
            f.close()
            print ("++++++++++++")
        return str(request.args["login"]) + " is registered"
    else:
        return str(request.args["login"]) + " allready exists"

if __name__ == "__main__":
    app.run(debug=True)

