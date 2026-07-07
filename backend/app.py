from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="../23b0771", static_url_path="")

BOOKINGS_FILE = "bookings.json"
CONTACTS_FILE = "contacts.json"

def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/api/book", methods=["POST"])
def book_appointment():
    data = request.get_json()
    bookings = load_data(BOOKINGS_FILE)
    bookings.append(data)
    save_data(BOOKINGS_FILE, bookings)
    return jsonify({"status": "ok"})

@app.route("/api/contact", methods=["POST"])
def contact_form():
    data = request.get_json()
    contacts = load_data(CONTACTS_FILE)
    contacts.append(data)
    save_data(CONTACTS_FILE, contacts)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
