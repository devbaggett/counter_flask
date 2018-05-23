from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "unicorns" # secret key for security purposes
# our index route will handle rendering our form

@app.route('/')
def index():
   if 'count' not in session:
      session['count'] = 0
   session['count'] += 1
   return render_template("index.html", count=session['count'])

@app.route('/plus2')
def plus2():
   session['count'] += 1
   return redirect('/')

@app.route('/reset')
def reset():
   session['count'] = 0
   return redirect('/')

app.run(debug=True)

