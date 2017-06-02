from flask import render_template, flash, redirect
from flask import request
from flask import url_for
from app.app import app
from .calcdef import direct_pr, angle, grad, inverse_pr
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title = 'Home')

@app.route('/dir_pr', methods = ['GET', 'POST'])
def dir_pr():
    if request.method == 'GET':
        return render_template('dir_pr.html', res = 'Bad')
    else:
        d_pr = direct_pr(
            float(request.form["Alpha_g"]),
            float(request.form["Alpha_m"]),
            float(request.form["Alpha_s"]),
            float(request.form["X_a"]),
            float(request.form["Y_a"]),
            float(request.form["D"])
        )
    return render_template('dir_pr.html', d_x=d_pr["delta_x"], d_y=d_pr["delta_y"], x=d_pr["x_b"], y=d_pr["y_b"])

@app.route('/fromgrad', methods = ['GET', 'POST'])
def fromgrad():
    if request.method == 'GET':
        return render_template('fromgrad.html')
    else:
        gon = float(request.form["Gon"])
        g = gon*0.9
        grad = g//1
        min = int((g % 1)*60)
        sec = round((g % 1)*60%1*60)
    return render_template('fromgrad.html', grad=int(grad), min=int(min), sec=int(sec))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)