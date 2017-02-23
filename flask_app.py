from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


import tools


app = Flask(__name__)

# Flask-SQLAlchemy options, as per cs50
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# define a Message
class Message(db.Model):
	__tablename__ = 'messages'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	gender = db.Column(db.Text)
	message = db.Column(db.Text)
	
	def __init__(self, first_name, last_name, gender, message):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.message = message


# offer to submit a message
@app.route('/')
def route():
	return render_template('submit.html')

# submit a message
@app.route('/submit', methods=["POST"])
def submit():
	if (request.form["first_name"] == "" or request.form["last_name"] == "" or 
	request.form["message"] == "" or len(request.form["message"]) > 55):
		return render_template('failure.html')
	message = Message(request.form["first_name"], request.form["last_name"], request.form["gender"], request.form["message"])
	db.session.add(message)
	db.session.commit()
	return render_template("succes.html")

# show the message board
@app.route('/board')
def board():
	rows = Message.query.all()
	return render_template("board.html", messages=rows)
	
# show the pie chart for fluff
@app.route('/chart')
def chart():
	# get the number of message per gender
	no_gender = Message.query.filter(Message.gender == "").count()
	male = Message.query.filter(Message.gender == "male").count()
	female = Message.query.filter(Message.gender == "female").count()
	apache_helicopter = Message.query.filter(Message.gender == "apache_helicopter").count()
	tardigrade = Message.query.filter(Message.gender == "tardigrade").count()
	
	# generate the chart
	chart = tools.chart(no_gender, male, female, apache_helicopter, tardigrade)
	
	return render_template("chart.html", chart=chart)