from flask import Flask, request, redirect, session
import twilio.twiml

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+14155686292": "Curious Unathi",
    "+13102546839": "Ryan"
}

# subjects = [
#     "math", "science", "english"
# ]
#
# math_grades = [
#     "Grade 1", "Grade 2", "Grade 3", "Grade 4"
# ]

@app.route("/", methods=['GET', 'POST'])
def answering_algorithm():
    """Respond to incoming calls with a simple text message."""

    from_number = request.values.get('From')
    if from_number in callers:
        message = callers[from_number]
        + ", which subject are you looking for?"
        + "Type in Math, English or Science"
        resp = twilio.twiml.Response()
        resp.message(message)
        return str(resp)
    else:
        message = "Welcome to Maarifa sms service center!"
        resp = twilio.twiml.Response()
        resp.message(message)
        return str(resp)

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
