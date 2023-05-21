from flask import Flask, render_template, url_for

app = Flask(__name__) #экземляр класса фласк

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О компании", "url": "about"},
    {"name": "Контакты", "url": "contact"},
    {"name": "Новые скважины", "url": "well"},
    {"name": "Архив", "url": "archive"}
]


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О компании", menu=menu)

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/well")
def well():
    return render_template('well.html', title="Новые скважины", menu=menu)

@app.route("/archive")
def archive():
    return render_template('archive.html', title="Архив", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu) #, 404


if __name__ == '__main__':
    app.run(debug=True)


