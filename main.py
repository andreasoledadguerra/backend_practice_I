
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Kasparov Quote</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Georgia', serif;
                text-align: center;
                color: #f5f5f5;
                background: url('https://upload.wikimedia.org/wikipedia/commons/5/57/Chess-king.JPG') no-repeat center center fixed;
                background-size: cover;
            }
            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.6); /* Transparencia oscura */
                z-index: 1;
            }
            .quote {
                position: relative;
                z-index: 2;
                font-size: 2.5em;
                line-height: 1.5;
                max-width: 900px;
                padding: 20px;
                animation: fadeIn 2s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="overlay"></div>
        <div class="quote">
            "The best way to predict the future is to create it on the chessboard." <br>
            <strong>- Garry Kasparov</strong>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
