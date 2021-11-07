from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import datetime

app = Flask(__name__)

@app.route('/home')
def new_user():
    return render_template('user.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            dob = request.form['dob']

            with sql.connect("user.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user(name,dob) VALUES (?,?)", (nm,dob))

                con.commit()

                msg = "User added successfully"
        except Exception as e:
            con.rollback()
            msg = 'error while inserting the User'
        
        finally:
            return jsonify({'Status': msg})
            con.close()

    
@app.route('/hello/<string:name>')
def get_user(name):
    con = sql.connect("user.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    query = "SELECT name, dob FROM user WHERE name=?"
    cur.execute(query, (name,))
    

    rows = cur.fetchall()
    dict_key = list(dict(rows).keys())[0]
    dict_value = datetime.date.fromisoformat(list(dict(rows).values())[0])
    
    today = datetime.date.today()
    
    now = datetime.datetime.now()
    birthday = datetime.datetime(now.year, dict_value.month, dict_value.day)
    days_left = abs(birthday - now.today()).days

    if datetime.datetime.fromisoformat(str(birthday)) == datetime.datetime.fromisoformat(str(today)):
        return jsonify({'message': 'Hello, ' + str(dict_key) + '! Happy birthday!'})

    if dict_value > today:
        return jsonify({'message': 'Date of birth must be before the today date.'})

    else:
        return jsonify({'message': 'Hello, ' + str(dict_key) + '! your birthday is in ' + str(days_left) +' day(s)'})

    return jsonify({'message':'None'})


if __name__ == '__main__':
    app.run(debug=True)
