from flask import Flask
import math

app = Flask(__name__)

@app.route("/")
def index():
    # processus intensif qui consomme du CPU
	
    return "processus demarre"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)