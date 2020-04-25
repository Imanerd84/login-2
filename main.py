import flask
from flask import *
from accounts import *

init()

app = flask.Flask(__name__)

highscore = 0;

week = 60 * 60 * 24 * 7


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/signupPage', methods = ["GET", "POST"])
def su():
  if request.method == "GET":
    return render_template("signup.html")
  elif request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if signup(username, password):
      return "Logged in as " + username
    else:
      return "fool"
@app.route('/loginPage', methods = ["GET", "POST"])
def signin():
  if request.method=='GET':
    return render_template("login.html")
  elif request.method == 'POST':
    username = request.form["username"]
    password = request.form["password"]
    if login(username, password):
      resp = make_response(render_template("game.html", user = username))
      resp.set_cookie("username", username, max_age = week)
      resp.set_cookie("password", password, max_age = week)
      
      return resp
    else:
      return "nah"

@app.route('/login', methods = ["POST"])
def _login():
  if request.method == "POST":
    data = request.json
    username = data['username']
    password = data['password']
    if login(username, password):
      resp = make_response(render_template("game.html", user = username))
      resp.set_cookie("username", username, max_age = week)
      resp.set_cookie("password", password, max_age = week)
      return resp
    else:
      return "nah"

@app.route('/score/<n>', methods = ["POST"])
def newScore(n):
  global highscore
  if int(n) > highscore:
    highscore = int(request)
    print(highscore)

@app.route('/settings', methods = ["GET", "POST"])
def settings():




if __name__ == "__main__":
  app.run(host="0.0.0.0")