from flask import Flask, render_template, request, jsonify, redirect,url_for
from usedb import WorkerDB

app = Flask(__name__)

@app.route("/")
def entry():
    return render_template("login.jinja")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn=worker_db.db_conn

        # SQL Vulnerabile (SQL Injection)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        user = conn.execute(query).fetchone()

        if user is not None:
            return redirect(url_for('home'))
        else:
            return render_template('login.jinja', error="Invalid credentials")

    return render_template('login.jinja')


@app.route("/home")
def home():
    return render_template("home.jinja")

@app.route("/html/list")
def list():
    return render_template("list.jinja", workerlist=worker_db.get_all())

@app.post("/worker/search")
def worker_search():
    try:
        both_good = worker_db.look_for_both(request.form["firstname"],
                                            request.form["lastname"])
        fn = worker_db.look_for_firstname(request.form["firstname"])
        ln = worker_db.look_for_lastname(request.form["lastname"])
        either_good = fn + ln
        return render_template('results.jinja',
                               both = both_good,
                               either = either_good)
    except KeyError as k:
        print(k)
        raise k
    except Exception as e:
        print(e)
        raise e

@app.post("/worker/add")
def worker_add():
    try:
        worker_db.insert(request.form["firstname"], request.form["lastname"])
        updated_workers = worker_db.get_all()
        return render_template('list.jinja', workerlist=updated_workers)
    except KeyError as k:
        print(k)
        raise k
    except Exception as e:
        print(e)
        raise e

if __name__ == "__main__":
    worker_db= WorkerDB()
    worker_db.gendb()
    app.run(debug=True, host="0.0.0.0", port=5010)