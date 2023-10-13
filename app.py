from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bangaluru',
    'salary': 'Rs. 1,00,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 3,
    'title': 'FullStack Engineer',
    'location': 'Remote',
    },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Pune',
    'salary': 'Rs. 1,00,00,000'
    } 
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)