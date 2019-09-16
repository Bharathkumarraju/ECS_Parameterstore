from flask import Flask, render_template, request
import os
from pymysql import connections

app = Flask(__name__)

DBHOST = os.environ.get("DBHOST")
DBPORT = os.environ.get("DBPORT")
DBPORT = int(DBPORT)
DBUSER = os.environ.get("DBUSER")
DBPWD = os.environ.get("DBPWD")
DATABASE = os.environ.get("DATABASE")


db_conn = connections.Connection(
    host=DBHOST,
    port=DBPORT,
    user=DBUSER,
    password=DBPWD,
    db=DATABASE
)

@app.route("/")
def home():
    return "Not in the correct page. Go to '/GetEmp'"

@app.route("/GetEmp", methods=['GET', 'POST'])
def getastronautinfo():
    return render_template("GetEmp.html")


@app.route("/fetchdata", methods=['GET','POST'])
def fetchdata():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']

    output = {}
    select_sql = "SELECT emp_id, first_name, last_name, primary_skills, location from Employee where emp_id=%s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(select_sql,(emp_id))
        result = cursor.fetchone()

        output["emp_id"] = result[0]
        output["first_name"] = result[1]
        output["last_name"] = result[2]
        output["primary_skills"] = result[3]
        output["location"] = result[4]

        return render_template("GetEmpOutput.html",id=output["emp_id"],fname=output["first_name"],
                               lname=output["last_name"],interest=output["primary_skills"],location=output["location"])

    except Exception as e:
        print(e)

    finally:
        cursor.close()


if (__name__) == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)