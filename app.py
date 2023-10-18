from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
   {
      "id": 1,
      "title": "Data Analyst",
      "location": "Remote",
      "salary": "$14000 month"
   },
   {
      "id": 2,
      "title": "Senior Python Developer",
      "location": "Remote",
      "salary": "$16000 month"
   },
   {
      "id": 3,
      "title": "Senior React Developer",
      "location": "Remote",
      "salary": "$17000 month"
   }
]

@app.route("/")
def init_app():
    return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def get_jobs():
   return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)