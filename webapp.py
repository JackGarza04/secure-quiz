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
# ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C", "2cos(2x)", "6x^8", "16x^3 + 8x", "e^(x + 1)", "y = 2x - 13"]


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
    if "answer1" not in session:
        session["answer1"]=request.form['answer1']
    else:
        pass
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    if "answer2" not in session:
        session["answer2"]=request.form['answer2']
    else:
        pass
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    if "answer3" not in session:
        session["answer3"]=request.form['answer3']
    else:
        pass
    return render_template('question4.html')

@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    if "answer4" not in session:
        session["answer4"]=request.form['answer4']
    else:
        pass
    return render_template('question5.html')
    
@app.route('/question6',methods=['GET','POST'])
def renderQuestion6():
    if "answer5" not in session:
        session["answer5"]=request.form['answer5']
    else:
        pass
    return render_template('question6.html')
    
@app.route('/question7',methods=['GET','POST'])
def renderQuestion7():
    if "answer6" not in session:
        session["answer6"]=request.form['answer6']
    else:
        pass
    return render_template('question7.html')
    
@app.route('/question8',methods=['GET','POST'])
def renderQuestion8():
    if "answer7" not in session:
        session["answer7"]=request.form['answer7']
    else:
        pass
    return render_template('question8.html')

@app.route('/question9',methods=['GET','POST'])
def renderQuestion9():
    if "answer8" not in session:
        session["answer8"]=request.form['answer8']
    else:
        pass
    return render_template('question9.html')

@app.route('/question10',methods=['GET','POST'])
def renderQuestion10():
    if "answer9" not in session:
        session["answer9"]=request.form['answer9']
    else:
        pass
    return render_template('question10.html')

@app.route('/results' ,methods=['GET','POST'])
def renderResults():
    if "answer10" not in session:
        session["answer10"]=request.form['answer10']
    else:
        pass
    return render_template('results.html', response1 = calculate_response(1), response2 = calculate_response(2), response3 = calculate_response(3), response4 = calculate_response(4), response5 = calculate_response(5), response6 = calculate_response(6), response7 = calculate_response(7), response8 = calculate_response(8), response9 = calculate_response(9), response10 = calculate_response(10), style1 = assign_response_css(1), style2 = assign_response_css(2), style3 = assign_response_css(3), style4 = assign_response_css(4), style5 = assign_response_css(5), style6 = assign_response_css(6), style7 = assign_response_css(7), style8 = assign_response_css(8), style9 = assign_response_css(9), style10 = assign_response_css(10), percentage = calculate_percentage(), letterGrade = calculate_letter_grade(), finalResult = final_result_style())
    
def calculate_response(num):
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C", "2cos(2x)", "6x^8", "16x^3 + 8x", "e^(x + 1)", "y = 2x - 13"]
    response = ""
    
    if "answer" + str(num) in session:
        if session[("answer" + str(num))].replace(" ", "") == answer_key[num - 1].replace(" ", ""):
            response = "Correct!"
        else:
            response = "Incorrect!"
    return response
    
def assign_response_css(num):
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C", "2cos(2x)", "6x^8", "16x^3 + 8x", "e^(x + 1)", "y = 2x - 13"]
    style_snippit = ""

    if "answer" + str(num) in session:
        if session[("answer" + str(num))].replace(" ", "") == answer_key[num - 1].replace(" ", ""):
            style_snippit = style_snippit + Markup('correct')
        else:
            style_snippit = style_snippit + Markup('wrong')
    return style_snippit

def final_result_style():
    result = ""
    if calculate_letter_grade() == "A+" or calculate_letter_grade() == "A" or calculate_letter_grade() == "A-":
        result = result + Markup('class="green"')
    elif calculate_letter_grade() == "B+" or calculate_letter_grade() == "B" or calculate_letter_grade() == "B-":
        result = result + Markup('class="yellow"')
    elif calculate_letter_grade() == "C+" or calculate_letter_grade() == "C" or calculate_letter_grade() == "C-":
        result = result + Markup('class="orange"')
    elif calculate_letter_grade() == "D+" or calculate_letter_grade() == "D":
        result = result + Markup('class="dark orange"')
    elif calculate_letter_grade() == "F":
        result = result + Markup('class="red"')
    else:
        pass
       
    return result

def calculate_percentage():
    answer_key = ["2x^2 + 2x + C", "36x^2 + 14x + 5", "6x^3 + 3x^2 + 3x + C", "3e^x + C", "5x + C", "2cos(2x)", "6x^8", "16x^3 + 8x", "e^(x + 1)", "y = 2x - 13"]
    percentage = 0.0
    
    for i in range(1,11):
        if "answer" + str(i) in session:
            if session[("answer" + str(i))].replace(" ", "") == answer_key[i - 1].replace(" ", ""):
                percentage += 1
            else:
                pass

    percentage = int((percentage / 10) * 100)
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
