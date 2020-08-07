from flask import Flask, render_template, request, redirect, url_for, flash,Blueprint
from Flask_CRUD_APP import model
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import sql

users = Blueprint('users',__name__)

@users.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees = all_data)

#this route is for inserting data to mysql database via html forms
@users.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('users.Index'))

#this is our update route where we are going to update our employee
@users.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('users.Index'))

#This route is for deleting our employee
@users.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('users.Index'))