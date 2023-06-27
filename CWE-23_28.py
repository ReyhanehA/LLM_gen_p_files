#9.# Example 9: CWE-23 Cross-site Scripting (XSS)

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return "<h1>Hello, " + name + "!</h1>"

if __name__ == "__main__":
    app.run()

In this example, an attacker can input a name with a script tag to execute arbitrary JavaScript code in the user's browser. The vulnerable line is `return "<h1>Hello, " + name + "!</h1>"`.