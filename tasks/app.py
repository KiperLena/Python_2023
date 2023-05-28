from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy #исморт СКЮЛэлкхеми
from datetime import datetime #импорт даты

app = Flask(__name__) #экземпляр класса фласк
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' #присваеваем название БД
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] #что будет сохраняться в task_content
        new_task = Todo(content=task_content) #данные попадут в new_task, но пока не сохранились в БД

        try:
            db.session.add(new_task) #добавляем данные в БД
            db.session.commit() # подстверждение сохранения в БД
            return redirect('/') # перенаправляем на туже страницу
        except Exception as e:
            return f"Не удалось добавить вашу задачу {e}"

    else:
        tasks = Todo.query.all() #взять все данные из таблицы
        return render_template('index.html', tasks=tasks) #что отобразается на странице

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) #get_or_404(id)возвращает ошибку если нет id

    try:
        db.session.delete(task_to_delete) #то что удаляем
        db.session.commit() #активируем удаление
        return redirect('/') #возврат на главную страницу
    except Exception as e:
        return f"Не удалось удалить задачу {e}"



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Не удалось обновить задачу {e}"
    else:
        return render_template('update.html', task=task)





if __name__ == '__main__':
    with app.app_context(): #содержимое внутри берет
        db.create_all() #запустит создание БД и создаст таблицу если ее нет.
    app.run(debug=True) #запуск

