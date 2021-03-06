from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+13102546839": "Ryan"
}

@app.route("/", methods=['GET', 'POST'])
def hello():
    body = request.values.get('Body', None).lower()
    resp = twilio.twiml.Response()
    if body == "hi":
        resp.message("Hello there! What subject do you want to get lessons for? We have Math, Science, and English.")
    if body == "math":
        resp.message("Okay, Math. What grade level? We have from grade 1 through grade 6. Ex, type '1'.")
    # if body == "1":
    #     resp.message("We currently have Addition Part 1,2,3 and Subtraction Part 1,2,3. Ex, type 'Addition-Part-1'.)
    # if body == "addition-part-1":
    #     resp.message("Here is a quick link to the material! http://www.maarifa.xyz/Math/1/Addition%20Part%201.")
    #     users = requests.get('http://maarifa.herokuapp.com/api/lesson')
        # lesson_list = []
        # lesson_data = users.json()
        # for lessons in lesson_data["objects"]:
        #     lesson_list.append(lessons["lessson_title"])
        # resp.message(enumerate(lesson_list))
        # resp.message("Choose a lesson")
        # resp.message(lesson_data["objects"][body]["lesson_content"])

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
