from flask import Flask, render_template, url_for, g, request, flash, abort
import os
import sqlite3
from FDataBase import FDataBase


DATABASE = '/tmp/zd42.bd'
DEBUG = True
SECRET_KEY = '85f6bb1efc408144d9a2e5799bb3cce8e1955912'

app = Flask(__name__) #экземляр класса фласк
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'zd42.db')))  #создание БД(имя)


def connect_db():  # функция соединение с БД
    con = sqlite3.connect(app.config['DATABASE']) # объект соединения
    con.row_factory = sqlite3.Row   # указываем что работаем как со словарем
    return con

def create_db(): #создание БД, создание таблиц внутри БД
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О компании", "url": "about"},
    {"name": "Контакты", "url": "contact"},
    {"name": "Новые скважины", "url": "well"},
    {"name": "Архив", "url": "archive"}
]


def get_db(): # функция соединения
    if not hasattr(g, 'link_db'): #если нет соединения с БД
        g.link_db = connect_db() #то устанавливаем соединение
    return g.link_db #возвращаем g.link_db


@app.route("/")
def index():
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    return render_template('index.html', title="Главная", menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    return render_template('about.html', title="О компании", menu=dbase.get_menu())

@app.route("/contact")
def contact():
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    return render_template('contact.html', title="Обратная связь", menu=dbase.get_menu())


@app.route("/well", methods=["POST", "GET"])
def well():
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase

    if request.method == 'POST':
        if len(request.form['name']) > 6 and len(request.form['num']) > 3 and len(request.form['post']) > 10 \
                and len(request.form['depth']) > 3:
            res = dbase.well(request.form['name'], request.form['num'], request.form['post'], request.form['depth'])
            if not res:
                flash('Ошибка добавления скважины', category='error')
            else:
                flash('Скважина добавлена в архив', category='seccess')
        else:
            flash('Ошибка добавления скважины', category='error')
    return render_template('well.html', title="Новые скважины", menu=dbase.get_menu())


@app.route('/archive/<int:id_field>')
def show_well(id_field):
    db = get_db()  # соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    field, num, text, depth = dbase.get_well(id_field)
    if not field:
        abort(404)
    return render_template('archive.html', field=field, num=num, text=text, depth=depth, menu=dbase.get_menu())



@app.route("/archive")
def archive():
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    return render_template('archive.html', title="Архив", menu=dbase.get_menu(), wells=dbase.get_wells_anonce())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db() #соединение с БД
    dbase = FDataBase(db)  # экземпляр класса FDataBase
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext #декаратор закрывающий соединение с БД
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)


