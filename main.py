from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home():
    web = "<h1>Guess a number between 0 and 9</h1>" \
          "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    return web


@app.route("/<number>")
def guess(number):
    int_number = int(number)
    if int_number == random_number:
        web = "<h1>You Found me!</h1>" \
              "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif int_number < random_number:
        web = "<h1>Too low, try again!</h1>" \
              "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        web = "<h1>Too high, try again!</h1>" \
              "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    return web


if __name__ == "__main__":
    app.run(debug=True)






