from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Note, User
from datetime import datetime
from . import db, ALLOWED_EXTENSIONS
import json
import os

views = Blueprint('views', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if 'file' not in request.files:
            flash('No file part', category='error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', category="error")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            _, ext = os.path.splitext(file.filename)
            filename = str(current_user.id) + str(datetime.now().isoformat(timespec='seconds')) + ext
            filename = secure_filename(filename)
            file.save(os.path.join('C:/Users/Kim/Documents/PythonProjects/flask_test/website/static/upload-images', filename))

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, image=filename, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", notes=Note.query.all(), user=current_user, users=User)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            flash('삭제되었습니다.', category='success')
            db.session.delete(note)
            db.session.commit()
        else:
            flash('작성자만 삭제할 수 있습니다.', category='error')

    return jsonify({})

@views.route('/teanote_form', methods=['GET', 'POST'])
@login_required
def teanote_form():
    if request.method == 'POST': 
        note=request.form.get('title')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', category="error")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('C:/Users/Kim/Documents/PythonProjects/flask_test/website/static/upload-images', filename))
        
        if len(note) < 1:
            flash('Title is too short!', category='error') 
        else:
            new_note = Note(data=note, image=filename, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')


        return redirect(url_for('views.home', _method='POST', notes=Note.query.all(), user=current_user, users=User))

    return render_template("teanote_form.html", user=current_user)

@views.route('/test')
@login_required
def test():
    return render_template('tea-notes.html', user=current_user)