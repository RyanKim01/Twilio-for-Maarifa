from flask import Flask, request, redirect
import twilio.twiml
import requests

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14155686292": "Curious Unathi",
    "+13102546839": "Ryan"
}
subjects = ["math", "science", "english"]
math_grades = ["Grade 1", "Grade 2", "Grade 3", "Grade 4"]

# def request_data(subject, lesson_id):
#     r = requests.get('http://9722c1ea.ngrok.io/api/lesson')
#     data = r.json()
#     for lessons in data['objects']:
#         if subject in lessons.values():
#             if lessons["lesson_id"] == lesson_id:
#                 return lessons["lesson_content"]

@app.route("/", methods=['GET', 'POST'])
def answering_algorithm():
    resp = twilio.twiml.Response()
    body = request.values.get('Body', None).lower()
    from_number = request.values.get('From', None)
    # users = requests.get('http://9722c1ea.ngrok.io/api/user')
    # user_data = users.json()

    if from_number in callers:
        # message = callers[from_number] + ", which subject are
        # you looking for?"
        # + "We have Math, Science, and English"
        # resp.message(message)
        if body == "math":
            message = "Which grade are you looking for?"
            + "We have grade 1 through grade 6."
            resp.message(message)
            if body == "grade 1":
                message = "Which content do you want to access?"
                + "We have addition, subtraction, and prime number."
                resp.message(message)
    else:
        message = "Welcome to Maarifa. Which subject are you looking for?"
        + "We have Math, Science, and English"
        resp.message(message)

    return str(resp)

# @app.route("/", methods=['GET', 'POST'])
# def answering_algorithm():
#     """Respond to incoming calls with a simple text message."""
#
#     from_number = request.values.get('From')
#     if from_number in callers:
#         message = callers[from_number]
#         + ", which subject are you looking for?"
#         + "Type in Math, English or Science"
#         resp = twilio.twiml.Response()
#         resp.message(message)
#         return str(resp)
#     else:
#         message = "Welcome to Maarifa sms service center!"
#         resp = twilio.twiml.Response()
#         resp.message(message)
#         return str(resp)

    # from_subject = request.values.get('Body')
    # if from_subject in subjects:
    #     message = subjects[from_subject] + "currently has "
    #     + str(math_grades, sep='\n') + "."
    #     + "Type in grade 1, grade 2, grade 3, or grade 4."
    #     resp = twilio.twiml.Response()
    #     resp.message(message)
    #     return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
