from flask import Flask, request, redirect
import twilio.twiml
import requests

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+13102546839": "Ryan"
}

subjects = ["math", "science", "english"]

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond and greet the caller by name."""

    """from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "You are a new user. Would you like to be subscribed?"
        sub_q = request.values.get('Body', None).lower()
        sub_a = twilio.twiml.Response()
        if sub_q == "yes":
            sub_a.message("Thanks, you've been added!")
        else:
            sub_a.message("Okay!")"""
    body = request.values.get('Body', None).lower()
    resp = twilio.twiml.Response()
    if body == "hi":
        resp.message("Hello there! What subject do you want to get lessons for?")
    if body == "math":
        resp.message("Okay, Math. What grade level?")
    if body == "1":
        users = requests.get('http://maarifa.herokuapp.com/api/lesson')
        user_data = users.json()
        resp.message(user_data["lesson_content"])
    return str(resp)

# @app.route("/", methods=['GET', 'POST'])
# def respond():
#     """Respond and greet the caller by name."""
#     body = request.values.get('Body', None).lower()
#     from_number = request.values.get('From', None)
#     if from_number in callers:
#         if body in subjects:
#             if body == "math":
#                 message = "You have selected Math."
#                 + " We have from Grade 1 to Grade 6."
#                 + " Which Grade do you want to view?"
#                 + " Type like following example: math grade 1"
#
#     if from_number in callers:
#         if body == "math grade 1":
#             message = "Welcome to Math Grade 1."
#             + "We have Addition, Addition Part 2, Addition Part 3, "
#             + "Subtraction, Subtraction Part 2."
#             + " Please input the lesson you want to view. Ex) Addition."
#
#     resp = twilio.twiml.Response()
#     resp.message(message)
#
#     return str(resp)

# @app.route("/", methods=['GET', 'POST'])
# def answering_algorithm():
#     body = request.values.get('Body', None).lower()
#     from_number = request.values.get('From', None)
    # if from_number in callers:
    #     message = callers[from_number]
    #     + ", which subject do you want to select?"
    #     + "We have Math, Science, and English"
    # else:
    #     message = "Welcome to Maarifa!"
    #     + "Which subject do you want to select?"
    #     + "We have Math, Science, and English"

    # if from_number in callers:
    #     if body in subjects:
    #         if body == "math":
    #             message = "You have selected Math."
    #             + " We have from Grade 1 to Grade 6."
    #             + " Which Grade do you want to view?"
    #             + " Type like following example: math grade 1"
    #
    # if from_number in callers:
    #     if body == "math grade 1":
    #         message = "Welcome to Math Grade 1."
    #         + "We have Addition, Addition Part 2, Addition Part 3, "
    #         + "Subtraction, Subtraction Part 2."
    #         + " Please input the lesson you want to view. Ex) Addition."

    # resp = twilio.twiml.Response()
    # resp.message(message)
    #
    # return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
