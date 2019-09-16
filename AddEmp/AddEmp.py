from flask import Flask
from flask import render_template, request
from pymysql import connections
import os

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
output = {}

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/AddEmp", methods=['POST'])
def updatedatabase():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    location = request.form['location']
    # image_file = request.form['image_file']

    insert_sql = "INSERT INTO Employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql,(emp_id, first_name, last_name, pri_skill, location))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name
        return render_template('AddEmpOutput.html', name=emp_name)


    except Exception as e:
        output["message"] = e
        return output

    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)