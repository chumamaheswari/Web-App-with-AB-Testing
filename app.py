# app.py
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
import random, csv, os, datetime

BASE_DIR = os.path.dirname(__file__)
METRICS_FILE = os.path.join(BASE_DIR, 'metrics.csv')
# default split 0.5 (50% A). You can change via env var AB_SPLIT
AB_SPLIT = float(os.environ.get('AB_SPLIT', '0.5'))

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret-123')  # change for production
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(BASE_DIR, 'flask_session')
Session(app)


@app.route("/")
def intro():
    return render_template("intro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "guest").strip() or "guest"
        session["username"] = username

        # Assign A or B once per session (stickiness)
        if "version" not in session:
            session["version"] = "A" if random.random() < AB_SPLIT else "B"

        return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    version = session.get("version", "A")
    if version == "A":
        return render_template("home_a.html", username=session["username"])
    else:
        return render_template("home_b.html", username=session["username"])


@app.route("/track_click", methods=["POST"])
def track_click():
    username = session.get("username", "guest")
    version = session.get("version", "unknown")
    ip = request.remote_addr or "unknown"
    timestamp = datetime.datetime.utcnow().isoformat()

    file_exists = os.path.isfile(METRICS_FILE)
    with open(METRICS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Version", "IP", "Timestamp"])
        writer.writerow([username, version, ip, timestamp])

    return "OK", 200


@app.route("/metrics")
def metrics():
    rows = []
    if os.path.isfile(METRICS_FILE):
        with open(METRICS_FILE, newline='') as f:
            import csv
            reader = csv.DictReader(f)
            rows = list(reader)
    return render_template("metrics.html", rows=rows)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("intro"))


if __name__ == "__main__":
    app.run(debug=True)
