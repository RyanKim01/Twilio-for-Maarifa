from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+13102546839": "Ryan",
}

subjects = ["math", "science", "english"]

@app.route("/", methods=['GET', 'POST'])
def answering_algorithm():
    body = request.values.get('Body', None).lower()
    from_number = request.values.get('From', None)
    # if from_number in callers:
    #     message = callers[from_number]
    #     + ", which subject do you want to select?"
    #     + "We have Math, Science, and English"
    # else:
    #     message = "Welcome to Maarifa!"
    #     + "Which subject do you want to select?"
    #     + "We have Math, Science, and English"

    if from_number in callers:
        if body in subjects:
            if body == "math":
                message = "You have selected Math."
                + " We have from Grade 1 to Grade 6."
                + " Which Grade do you want to view?"
                + " Type like following example: math grade 1"

    if from_number in callers:
        if body == "math grade 1":
            message = "Welcome to Math Grade 1."
            + "We have Addition, Addition Part 2, Addition Part 3, "
            + "Subtraction, Subtraction Part 2."
            + " Please input the lesson you want to view. Ex) Addition."

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
