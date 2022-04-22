import os
from flask import Flask, url_for, render_template, request, flash, Markup
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
    return redirect(url_for('renderMain'))

@app.route('/question1',methods=['GET','POST'])
def renderQuestion1():
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    session["answer1"]=request.form['answer1']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    session["answer2"]=request.form['answer2']
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    session["answer3"]=request.form['answer3']
    return render_template('question4.html')

@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    session["answer4"]=request.form['answer4']
    return render_template('question5.html')
    
@app.route('/results' ,methods=['GET','POST'])
def renderResults():
    session["answer5"]=request.form['answer5']
    return render_template('results.html', response1 = calculate_response(1), response2 = calculate_response(2), response3 = calculate_response(3), response4 = calculate_response(4), response5 = calculate_response(5), percentage = calculate_percentage(), letterGrade = calculate_letter_grade())
    
def calculate_response(num):
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C"]
    response = ""
    
    if "answer" + str(num) in session:
        if session[("answer" + str(num))].replace(" ", "") == answer_key[num - 1].replace(" ", ""):
            response = "Correct"
        else:
            response = "Incorrect"
    return response

def calculate_percentage():
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C"]
    percentage = 0.0
    
    for i in range(1,6):
        if "answer" + str(i) in session:
            if session[("answer" + str(i))].replace(" ", "") == answer_key[i - 1].replace(" ", ""):
                percentage += 1
            else:
                pass
                
    percentage = int((percentage / 5) * 100)
    return percentage
    
def calculate_letter_grade():
    letter_grade = ""
    
    if calculate_percentage() >= 98:
        letter_grade = "A+"
    elif calculate_percentage() >= 94 and calculate_percentage() < 98:
        letter_grade = "A"
    elif calculate_percentage() >= 90 and calculate_percentage() < 94:
        letter_grade = "A-"
    elif calculate_percentage() >= 87 and calculate_percentage() < 90:
        letter_grade = "B+"
    elif calculate_percentage() >= 84 and calculate_percentage() < 87:
        letter_grade = "B"
    elif calculate_percentage() >= 80 and calculate_percentage() < 84:
        letter_grade = "B-"
    elif calculate_percentage() >= 77 and calculate_percentage() < 80:
        letter_grade = "C+"
    elif calculate_percentage() >= 74 and calculate_percentage() < 77:
        letter_grade = "C"
    elif calculate_percentage() >= 70 and calculate_percentage() < 74:
        letter_grade = "C-"
    elif calculate_percentage() >= 67 and calculate_percentage() < 70:
        letter_grade = "D+"
    elif calculate_percentage() >= 64 and calculate_percentage() < 67:
        letter_grade = "D"
    elif calculate_percentage() >= 0 and calculate_percentage() < 64:
        letter_grade = "F"
    else:
        pass
        
    return letter_grade
    
    
if __name__=="__main__":
    app.run(debug=False)
