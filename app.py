from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses =[]
#survey_questions = {"0": survey.questions[0], ""}


@app.get("/begin")
def generate_start_page():
    """Generates landing page"""

    return render_template(
        "survey_start.html",
        title= survey.title,
        instructions= survey.instructions)

@app.post("/begin")
def handle_post_request():
    return redirect ('/questions/0')

@app.get("/questions/<question_number>")
def generate_questions(question_number):
    #number = request.args.get()
    global number
    number = 0

    #question_number = request.args["question_number"]

    return render_template(
        "question.html",
        question = survey.questions[int(question_number)])

@app.post('/answer')
def handle_answer_submit(number):

    number += 1
    responses.append(request.form["answer"])

    return redirect (f'/questions/{number}')
