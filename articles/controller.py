from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()  # экземпляр класса model
        self.user_interface = UserInterface()  # экземпляр класса view

    def run(self):
        answer = None  # ответ пользователя
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()  # то что ввел пользователь
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            article = self.user_interface.add_user_article()
            self.article_model.add_article(article)
        elif answer == "2":
            articles = self.article_model.get_all_articles()  # будет возвращать то что лежит в словарев модели
            self.user_interface.show_all_articles(articles)  # показывает все элементы статьи
        elif answer == "3":
            article_title = self.user_interface.get_user_article() #вызов статьи
            try:
                article = self.article_model.get_single_article(article_title) #взять из модели по названию статьи
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title) # если нет такой статьи
            else:
                self.user_interface.show_single_article(article) #отображение данных по статье
        elif answer == "4":
            article_title = self.user_interface.get_user_article()  # вызов статьи
            try:
                title = self.article_model.remove_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.remove_single_article(title)
        elif answer == 'q':
            self.article_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
