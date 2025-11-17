from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Todo



#routes
@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete=incomplete, complete=complete)

#add route
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    todo = Todo(title=title, complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


#complete route
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))