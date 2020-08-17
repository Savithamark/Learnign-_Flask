from flask import render_template, url_for, redirect

from . import site
from ..models import User, db
from ..forms import NameForm


# custom 404 handler
@site.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@site.route('/', methods=['GET', 'POST'])
def index():
    name = None
    new = False
    form = NameForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        form.firstname.data = ''
        form.lastname.data = ''
        form.email.data = ''
        form.password.data = ''
        if User.query.filter_by(name=name).first() is None:
            db.session.add(User(firstname=firstname, lastname=lastname,email=email,password=password))
            db.session.commit()
            new = True
    return render_template('site/index.html', form=form, name=name, new=new)


@site.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('site/users.html', users=users)


@site.route('/users/<int:id>', methods=['GET'])
def user_details(id):
    user = User.query.get_or_404(id)
    return render_template('site/user_details.html', user=user)


@site.route('/users/delete/<int:id>', methods=['POST'])
def user_delete(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('site.users'))
