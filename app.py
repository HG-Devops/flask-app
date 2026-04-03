from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="mydb"
        )
        return "Connected to MySQL Database 🚀"
    except:
        return "Failed to connect to MySQL ❌"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
