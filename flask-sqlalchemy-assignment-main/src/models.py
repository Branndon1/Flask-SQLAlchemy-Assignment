# TODO - Create SQLAlchemy DB and Movie model
from src.models import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Instructor(db.Model):
 instructor_id = db.Column(db.Integer, primary_key=True)
first_name = db.Column(db.String(255), nullable=False)
last_name = db.Column(db.String(255), nullable=False)
tenured = db.Column(db.Boolean, nullable=False)

class Student(db.Model):
 student_id = db.Column(db.Integer, primary_key=True)
first_name = db.Column(db.String(255), nullable=False)
last_name = db.Column(db.String(255), nullable=False)
class_rank = db.Column(db.String, nullable=False)
year_admitted = db.Column(db.Integer, nullable=False)
advisor_id = db.Column(db.Integer, db.ForeignKey('instructor.instructor_id'), nullable=True)
advisor = db.relationship('Instructor', backref='advisees', lazy=True)
