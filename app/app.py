from typing import List, Dict

import pytz
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flask import url_for, flash, make_response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import secrets
import datetime


app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'CheckInData'
mysql.init_app(app)
eastern = pytz.timezone("US/Eastern")


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Eric Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM LogTable ORDER BY CheckInTime DESC')
    result = cursor.fetchall()
    # print(result)
    return render_template('index.html', title='Home', user=user, Logs=result)


@app.route('/CheckIn', methods=['GET'])
def form_CheckIn_get():
    if not request.cookies.get('CheckInCookie'):
        res = make_response(render_template('new.html', title='Check In'))
    else:
        cookie = request.cookies.get('CheckInCookie')
        res = make_response(render_template('new.html', title='Check In', cookie=cookie))
    return res


@app.route('/CheckIn', methods=['POST'])
def CheckIn_post():
    cursor = mysql.get_db().cursor()
    GenCookie = secrets.token_urlsafe(32)

    # Update Input
    CheckTime = datetime.datetime.now(tz=eastern).strftime('%Y-%m-%d %H:%M:%S')
    inputData = (request.form.get('FirstName'), request.form.get('LastName'),
                 request.form.get('PhoneNumber'), request.form.get('Reason'), GenCookie, CheckTime)
    # Update Insert
    sql_insert_query = """INSERT INTO LogTable (FirstName, LastName, PhoneNumber, ReasonForVisit, LoginCookieID, CheckInTime) VALUES (%s, %s,%s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    res = make_response(redirect('/', code=302))
    res.set_cookie('CheckInCookie', GenCookie, max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/CheckOut', methods=['GET'])
def form_CheckOut_get():
    cookie = request.cookies.get('CheckInCookie')
    return render_template('CheckOut.html', title='Check Out', cookie=cookie)


@app.route('/CheckOut', methods=['POST'])
def CheckOut_post():
    cursor = mysql.get_db().cursor()
    GenCookie = request.cookies.get('CheckInCookie')
    # Update Input
    CheckTime = datetime.datetime.now(tz=eastern).strftime('%Y-%m-%d %H:%M:%S')
    inputData = (CheckTime, GenCookie)
    sql_update_query = """UPDATE LogTable l SET l.CheckOutTime = %s WHERE l.LoginCookieID = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    # res = make_response("Cookie Removed")
    # request.cookies.update('CheckInCookie', GenCookie, max_age=0)
    # res.set_cookie('CheckInCookie', GenCookie, max_age=0)
    response = make_response(redirect('/'))
    response.delete_cookie('CheckInCookie')
    return response


@app.route('/Previous', methods=['GET'])
def getPrevious():
    cookie = request.cookies.get('CheckInCookie')
    user = {'username': 'Eric Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM LogTable WHERE LoginCookieID = %s') % cookie
    result = cursor.fetchall()
    # print(result)
    return render_template('new.html', title='Check In', user=user, Logs=result)


@app.route('/Search', methods=['GET'])
def form_Search_get():
    return render_template('search.html', title='Search Times')


@app.route('/Search', methods=['POST'])
def searchFunction():
    user = {'username': 'Eric Project'}
    cursor = mysql.get_db().cursor()
    timeIn = request.form.get('dateStart') + ' ' + request.form.get('timeStart')
    timeOut = request.form.get('dateEnd') + ' ' + request.form.get('timeEnd')
    inputData = (timeIn, timeOut, timeOut, timeIn)
    # cursor.execute('SELECT * FROM LogTable WHERE   ')
    cursor.execute('SELECT * FROM LogTable WHERE (CheckInTime >= %s AND CheckInTime <= %s) OR (CheckOutTime <= %s '
                   'AND CheckOutTime >= %s )')
    result = cursor.fetchall()
    print(result)
    return render_template('search.html', title='Search', user=user, Logs=result)


'''@app.route('/delete-cookie')
def delete_cookie():
    if request.cookies.get('CheckInCookie'):
        res = make_response("Setting a cookie")
        GenCookie = secrets.token_urlsafe(32)
        res.set_cookie('CheckInCookie', GenCookie, expires=0)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('CheckInCookie')))
    res = make_response("Cookie Removed")
    #render_template('index.html', title='Processing')
    return redirect("/", code=302, co)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
