from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14155686292": "Curious Unathi",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", where are your home girls?!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
