import json


class World:

    w1 = {"Russia": "Москва",
          "США": "Нью-Йорк",
          "Болгария": "Болгариа",
          "Индонезия": "Бали"
          }

    with open('world.json', 'w') as fw:
        json.dump(w1, fw, indent=4)

    with open('world.json', 'r') as fw:
        data1 = json.load(fw)
    # def __init__(self, country, capital):
    #     self.country = country
    #     self.capital = capital
    #
    # def __str__(self):
    #     return "{self.country}:{self.capital}"

    @staticmethod
    def dump_to_json(world, file_name):
        try:
            data = json.load(open('world.json'))
        except FileNotFoundError:
            data = []

        # data.append({'self.country': 'self.capital'})
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open('world.json', 'r') as f:
            print(json.load(f))
    @staticmethod
    def info():
        print("*" * 30)
        print("Выбор действия:"
              "\n1 - добавление данных"
              "\n2 - удаление данных"
              "\n3 - поиск данных"
              "\n4 - редактирование данных"
              "\n5 - просмотр данных"
              "\n6 - завершение работы")
        oper = input("Ввод: ")

        if oper == "1":
            num1 = input("Введите название страны (с заглавной буквы): ")
            num2 = input("Введите назывние столицы (с заглавной буквы): ")
        World.dump_to_json()
       # elif oper == "2":
       #      num1 = input("Введите название страны (с заглавной буквы): ")
       #      num2 = input("Введите назывние столицы (с заглавной буквы): ")
       # elif oper == "3":
       #      num1 = input("Введите название страны (с заглавной буквы): ")
       #      num2 = input("Введите назывние столицы (с заглавной буквы): ")
       #
       #  elif oper == "4":
       #  num1 = input("Введите название страны (с заглавной буквы): ")
       #  num2 = input("Введите назывние столицы (с заглавной буквы): ")
       #
       #  elif oper == "5":
       #  num1 = input("Введите название страны (с заглавной буквы): ")
       #  num2 = input("Введите назывние столицы (с заглавной буквы): ")
       #
       #  print("Файл сохранен")




w = World()
w.info()
