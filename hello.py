from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html>
        <head>
            <style>
                /* Add CSS styles here */
                body {
                    background-color: lightblue;
                }
                .container {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                h1 {
                    color: blue;
                    font-size: 40px;  /* Increase font size here */
                }
                p {
                    color: blue;
                    font-size: 28px;  /* Increase font size here */
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello World, We are the Itians! &#127881;</h1>
                <p>Always Proud &#127881;&#127882;</p>
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
