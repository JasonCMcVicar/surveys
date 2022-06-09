from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses =[]

@app.get("/begin")
def generate_start_page():
    """Generates landing page

    """

    return render_template(
        "survey_start.html",
        title= survey.title,
        instructions= survey.instructions)

@app.post("/begin")
def handle_post_request_and_redirect():
    """Displays the Title and Instructions for the Survey and the option to begin
        Redirects the user to the first question of the survey

    """
    return redirect ('/questions/0')

@app.get("/questions/<question_number>")
def generate_question_page(question_number):
    """Generates Question Page
     Takes a number to generate the question at the index of survey's question list
     Returns the Question Template/Form
    
    """
    global next_question
    next_question = int(question_number) + 1

    return render_template(
        "question.html",
        question = survey.questions[int(question_number)])

@app.post('/answer')
def handle_answers_and_redirect():
    """Adds the question answer to a list of responses and checks if the survey has any more questions
        if the survey has more questions it will redirect the user to the next question. 
        if there are no more questions it will redirect the user to the Thank You page.

    """
    responses.append(request.form["answer"])
    if next_question == len(survey.questions):
        print(responses)
        return render_template("completion.html")
    else:
        return redirect (f'/questions/{next_question}')
    
