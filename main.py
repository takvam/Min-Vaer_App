#main.py er serveren som ruter brukeren til hjemmesiden og til resultatsidenself.
#weather.py lager en funksjon med API som henter vær-data basert på hvilken by du velgerself.
#Funksjonen populerer resultatsiden.

#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Oslo'}, {'name':'Stockholm'}, {'name':'Trondheim'},
        {'name':'Bergen'}, {'name':'Sandvika'}, {'name':'Stabekk'},
        {'name':'Drammen'}, {'name':'Tromsø'}, {'name':'Svelvik'},
        {'name':'Kristiansand'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)
