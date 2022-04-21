import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

# 2u8VI6VypGAvdSBpFEPsVw
# \/ Answer Key in order \/
# ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C"]

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  
                                         #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.


@app.route('/')
def renderMain():
    return render_template('index.html')

@app.route('/retake')
def retake():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/question1',methods=['GET','POST'])
def renderQuestion1():
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    session["question1"]=request.form['answer1']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    session["question2"]=request.form['answer2']
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    session["question3"]=request.form['answer3']
    return render_template('question4.html')

@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    session["question4"]=request.form['answer4']
    return render_template('question5.html')
    
@app.route('/results' ,methods=['GET','POST'])
def renderResults():
    session["question5"]=request.form['answer5']
    return render_template('results.html')
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C"]
    response1 = ""
    response2 = ""
    response3 = ""
    response4 = ""
    response5 = ""
    score = ""
    letter_grade = ""
    
    for n in range(1,6):
        if "question" + str(n) in session:
            if session[("question" + str(n))] == answer_key[n - 1]:
                locals()["response" + str(n - 1)] = "Correct"
            else:
                locals()["response" + str(n - 1)] = "Incorrect"
                
    
if __name__=="__main__":
    app.run(debug=False)
