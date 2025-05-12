from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def log_input(ip, username, password):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip} | Username: {username} | Password: {password}\n"
    print(log_entry.strip())
    with open("honeypot_log.txt", "a") as log_file:
        log_file.write(log_entry)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr
        log_input(ip, username, password)
        return "Access Denied. This activity has been logged."
    return render_template("login.html")

@app.route("/logs")
def view_logs():
    with open("honeypot_log.txt", "r") as file:
        logs = file.read()
    return f"<pre>{logs}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
