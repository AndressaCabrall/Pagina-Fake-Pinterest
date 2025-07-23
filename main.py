from flask import Flask
app = Flask(__name__)

@app.route("/")

def homepage():
    return "Fake do Pinterest -Bem vindo ao meu primeiro site no Ar!"

if __name__ == "__main__":
    app.run(debug = True)



