from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Optional
from wtforms.widgets import TextArea


class NameForm(FlaskForm):
    firstname = StringField(
        'Add user first name:', validators=[Required(), Length(1, 16)])
    lastname = StringField(
        'Add user last name:', validators=[Required(), Length(1, 16)])
    email = StringField(
        'Add user email id:', validators=[Required(), Length(1, 16)])
    password = StringField(
        'Add password:', validators=[Required(), Length(1, 16)])
    submit = SubmitField('Submit')
