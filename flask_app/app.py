from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# desired hostname users should use
PREFERRED_HOST = 'chibibyte.local:5000'

@app.before_request
def enforce_hostname():
    host = request.host
    # if incoming host is not the preferred one, redirect
    if host != PREFERRED_HOST:
        # preserve path and query
        dest = f"http://{PREFERRED_HOST}{request.path}"
        qs = request.query_string.decode()
        if qs:
            dest += f"?{qs}"
        return redirect(dest, code=301)

# simple in-memory store for demo
students = []

youtube_video_id = "dQw4w9WgXcQ"  # placeholder video

@app.route('/')
def home():
    query = request.args.get('q')
    engine = request.args.get('engine', 'bing')
    results = []
    if query:
        # mock search for engines; in real use, call respective APIs
        results = [f"{engine.capitalize()} result for '{query}' #1", f"{engine.capitalize()} result for '{query}' #2"]
    return render_template('home.html', youtube_id=youtube_video_id, bing_results=results, query=query, engine=engine)

@app.route('/students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            students.append({'name': name})
        return redirect(url_for('manage_students'))
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
