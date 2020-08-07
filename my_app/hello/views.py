
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Blueprint
hello = Blueprint('hello', __name__)

@hello.route('/')
@hello.route('/hello')
def hello_world():
    return 'hello'

@hello.route('/show')
def get_message(key):
    return 'message'

@hello.route('/add')
def add_or_update_message():
    return "added" 
