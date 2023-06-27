#10.# Example 10: CWE-23 Cross-site Scripting (XSS)

from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return "<h1>Hello, " + escape(name) + "!</h1>"

if __name__ == "__main__":
    app.run()

This example is similar to the previous one, but uses the `escape()` function to prevent XSS attacks. The vulnerable line is still `return "<h1>Hello, " + escape(name) + "!</h1>".