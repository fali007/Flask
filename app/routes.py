from flask import render_template, flash, redirect,request
from app import app
from app.forms import LoginForm

from .models import DB,DB_e
from datetime import date

from .figure import pmo

class flag:
    def __init__(self):
        self.var=False


b=flag()
print(b.var)
@app.route('/')
@app.route('/index')
def index():
    if b.var==False:
        return redirect('/login')
    user = {'username': 'Felix'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data,form.password.data)
        if form.username.data=='admin' and form.password.data=='admin':
            b.var=True
            print(b.var)
            return redirect('/index')
    return render_template('login.html', user={'username':'Felix'}, form=form)

from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class IncomeForm(Form):
   name = TextField("Source",[validators.Required("Please enter the source of income.")])      
   amount = IntegerField("Amount")
   submit = SubmitField("Enter")

class ExpenseForm(Form):
   name = TextField("Spend On",[validators.Required("Please enter what you spend on.")])      
   amount = IntegerField("Amount")
   submit = SubmitField("Enter")

@app.route('/income', methods = ['GET', 'POST'])
def income():
    if b.var==False:
        return redirect('/login')
    form = IncomeForm()
    if form.validate_on_submit():
        print(form.name.data,form.amount.data)
        a=DB()
        # a.create_table()
        time=date.today()
        day=time.day
        dat=time.month
        year=time.year
        mem=str(day) + '-' + str(dat) + '-' + str(year)
        a.insert_table(form.name.data,mem,form.amount.data)
        a.fetch()
        # a.update_table(4000,'2019-5-18','alex')
        # a.delete('ravi')
        # row=a.fetch()
        return redirect('/index')
    return render_template('income.html', user={'username':'Felix'}, form=form)

@app.route('/expense', methods = ['GET', 'POST'])
def expense():
    if b.var==False:
        return redirect('/login')
    form = ExpenseForm()
    if form.validate_on_submit():
        print(form.name.data,form.amount.data)
        a=DB_e()
        # a.create_table()
        time=date.today()
        day=time.day
        dat=time.month
        year=time.year
        mem=str(day) + '-' + str(dat) + '-' + str(year)
        a.insert_table(form.name.data,mem,form.amount.data)
        a.fetch()
        # a.update_table(300,'2019-5-18','alex')
        # a.delete('ravi')
        # row=a.fetch()
        return redirect('/index')
    return render_template('expense.html', user={'username':'Felix'}, form=form)

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route('/chart')
def chart():
    if b.var==False:
        return redirect('/login')
    form = ExpenseForm()
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    x=DB_e()
    cursor=x.conn.cursor()
    cursor.execute('SELECT * FROM expense')
    rows=cursor.fetchall()
    amount=[]
    date=[]
    for row in rows:
        print(row)
        amount.append(row[2])
        date.append(row[1])
    cursor.close()
    # axis = fig.add_subplot(1, 1, 1)
    # axis.plot(date,amount)

    y=DB()
    cursor=y.conn.cursor()
    cursor.execute('SELECT * FROM income')
    rows_e=cursor.fetchall()
    amount_e=[]
    date_e=[]
    for row in rows_e:
        print(row)
        amount_e.append(row[2])
        date_e.append(row[1])
    cursor.close()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(date,amount,date_e,amount_e)
    return fig