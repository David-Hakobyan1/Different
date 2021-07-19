from flask import Flask,render_template,url_for,request
import random

app = Flask(__name__)

tvyalner = [{'harc': 'eleq qajer...?', 'pat': 'haykazun', 'cur': [i for i in '########']},
            {'harc': 'gexecik(homanish)?', 'pat': 'sirun', 'cur': [i for i in '#####']},
            {'harc': 'Zaveni ...?', 'pat': 'smbo', 'cur': [i for i in '####']}]
patahakan = random.randrange(0,len(tvyalner))
cur_harc  =  tvyalner[patahakan]

@app.route('/')
@app.route('/pole')
def pole():
    return render_template('barev.html',info=cur_harc)


@app.route('/stugum')
def stugum():
    global cur_harc
    e = 0
    cs = 0
    c = 0
    if len(str(request.args["fname"])) == 1:
        for h in range (len(cur_harc['pat'])):
            if str(request.args["fname"]) == cur_harc['pat'][h]:
                cur_harc['cur'][h] = request.args["fname"]
                for gh in cur_harc['cur']:
                    if "#" not in gh:
                        cs += 1
                        if cs == len(cur_harc['cur']):
                            cs = 0
                            tvyalner = [{'harc': 'eleq qajer...?', 'pat': 'haykazun', 'cur': [i for i in '########']},
                                        {'harc': 'gexecik(homanish)?', 'pat': 'sirun', 'cur': [i for i in '#####']},
                                        {'harc': 'Zaveni ...?', 'pat': 'smbo', 'cur': [i for i in '####']}]
                            patahakan = random.randrange(0,len(tvyalner))
                            cur_harc  =  tvyalner[patahakan]
                            return render_template('barev.html',info=cur_harc)
        return render_template('barev.html',info=cur_harc)
    return render_template('barev.html',info=cur_harc)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
