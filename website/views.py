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

def file_upload(userid, file):
    _, ext = os.path.splitext(file.filename)
    fn = str(userid) + str(datetime.now().isoformat(timespec='seconds')) + ext
    fn = secure_filename(fn)
    file.save(os.path.join('C:/Users/Kim/Documents/PythonProjects/flask_test-1/website/static/upload-images', fn))
    return fn

def split_string(input_str, max_length=20):
    words = input_str.split()
    result = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            current_line += word + " "
        else:
            result.append(current_line.strip())
            current_line = word + " "
    
    # Add the last line
    result.append(current_line.strip())
    
    return result


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
            filename = file_upload(current_user.id, file)           

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(note=note, image=filename, user_id=current_user.id)  #providing the schema for the note 
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
        if (note.user_id == current_user.id) or (current_user.nickname == '관리자'):
            flash('삭제되었습니다.', category='success')
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/teanote_form', methods=['GET', 'POST'])
@login_required
def teanote_form():
    if request.method == 'POST': 
        teaname = request.form.get('teaname')
        sailer = request.form.get('sailer')
        country = request.form.get('country')
        type_of_tea = request.form.getlist('tea-types')[0]

        tea_quantity = request.form.get('tea_quantity')
        tea_temprature = request.form.get('tea_temprature')
        tea_brew_time = request.form.get('tea_brew_time')

        grade = request.form.get('grade')
        dry_leaf_appearence = request.form.get('dry_leaf_appearence')
        brew_leaf_appearence = request.form.get('brew_leaf_appearence')
        dry_leaf_perfume = request.form.get('dry_leaf_perfume')
        brew_leaf_perfume = request.form.get('brew_leaf_perfume')

        strength_of_taste = request.form.get('strength_of_taste')
        t1 = request.form.get('t1')
        t2 = request.form.get('t2')
        t3 = request.form.get('t3')
        t4 = request.form.get('t4')
        t5 = request.form.get('t5')
        t6 = request.form.get('t6')
        t7 = request.form.get('t7')
        t8 = request.form.get('t8')
        t9 = request.form.get('t9')
        t10 = request.form.get('t10')
        t11 = request.form.get('t11')
        t12 = request.form.get('t12')

        strength_of_perfume = request.form.get('strength_of_perfume')
        p1 = request.form.get('p1')
        p2 = request.form.get('p2')
        p3 = request.form.get('p3')
        p4 = request.form.get('p4')
        p5 = request.form.get('p5')
        p6 = request.form.get('p6')
        p7 = request.form.get('p7')
        p8 = request.form.get('p8')
        p9 = request.form.get('p9')
        p10 = request.form.get('p10')
        p11 = request.form.get('p11')
        p12 = request.form.get('p12')
        p12 = request.form.get('p12')

        colors = {"off-white-leaf" : "미색",
                  "light-green-leaf":"연두",
                  "yellow-leaf":"노랑",
                  "amber-leaf":"호박",
                  "orange-leaf":"주황",
                  "red-leaf":"빨강",
                  "brown-leaf":"갈색"}

        leaf_color = request.form.getlist('leaf-color')[0]

        transparency = request.form.get('transparency')
        finish = request.form.get('finish')
        note = request.form.get('note')
        splited_note = split_string(note, 20)

        brief_note1 = " "
        brief_note2 = " "
        brief_note3 = " "
        brief_note4 = " "
        if len(splited_note) <= 1:
            brief_note1 = splited_note[0]
        elif len(splited_note) == 2:
            brief_note1 = splited_note[0]
            brief_note2 = splited_note[1]
        elif len(splited_note) == 3:
            brief_note1 = splited_note[0]
            brief_note2 = splited_note[1]
            brief_note3 = splited_note[2]
        else:
            brief_note1 = splited_note[0]
            brief_note2 = splited_note[1]
            brief_note3 = splited_note[2]
            brief_note4 = "..."

        date =  datetime.now().replace(microsecond=0)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file', category="error")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file_upload(current_user.id, file)       
        
        if len(teaname) < 1:
            flash('Title is too short!', category='error') 
        else:
            new_note = Note(teaname=teaname, sailer=sailer, country=country, type_of_tea=type_of_tea,
                            tea_quantity=tea_quantity, tea_temprature=tea_temprature,
                            tea_brew_time=tea_brew_time, grade=grade, dry_leaf_appearence=dry_leaf_appearence,
                            brew_leaf_appearence=brew_leaf_appearence, dry_leaf_perfume=dry_leaf_perfume,
                            brew_leaf_perfume=brew_leaf_perfume, strength_of_taste=strength_of_taste, t1=t1, t2=t2,
                            t3=t3, t4=t4, t5=t5, t6=t6, t7=t7, t8=t8, t9=t9, t10=t10, t11=t11, t12=t12,
                            strength_of_perfume=strength_of_perfume, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5,
                            p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, leaf_color=leaf_color, 
                            transparency=transparency, finish=finish, note=note, brief_note1=brief_note1, 
                            brief_note2=brief_note2, brief_note3=brief_note3, brief_note4=brief_note4, 
                            image=filename, date=date, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')


        return redirect(url_for('views.home', _method='POST', notes=Note.query.all(), user=current_user, users=User))

    return render_template("teanote_form.html", user=current_user)


@views.route('/teanote/<noteid>')
@login_required
def show_note(noteid):
    note = Note.query.filter_by(id = noteid).first()
    return render_template('tea-note.html', note=note, user=current_user)
