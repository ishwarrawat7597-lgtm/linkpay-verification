from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>LINKPAY Verification</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="background:#101827;color:white;text-align:center;
                 font-family:Arial;padding:40px 15px">
        <h1>LINKPAY EARN</h1>
        <h2>Verification Service</h2>
        <p>Verification server is running.</p>
        <p>Demo points only. No cash value.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
