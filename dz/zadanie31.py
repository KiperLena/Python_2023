# import json
#
#
# class World:
#
#     w1 = {"Russia": "Москва",
#           "США": "Нью-Йорк",
#           "Болгария": "Болгариа",
#           "Индонезия": "Бали"
#           }
#
#     with open('world.json', 'w') as fw:
#         json.dump(w1, fw, indent=4)
#
#     with open('world.json', 'r') as fw:
#         data1 = json.load(fw)
#     # def __init__(self, country, capital):
#     #     self.country = country
#     #     self.capital = capital
#     #
#     # def __str__(self):
#     #     return "{self.country}:{self.capital}"
#
#     @staticmethod
#     def dump_to_json(world, file_name):
#         try:
#             data = json.load(open('world.json'))
#         except FileNotFoundError:
#             data = []
#
#         # data.append({'self.country': 'self.capital'})
#         with open(file_name, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open('world.json', 'r') as f:
#             print(json.load(f))
#     @staticmethod
#     def info():
#         print("*" * 30)
#         print("Выбор действия:"
#               "\n1 - добавление данных"
#               "\n2 - удаление данных"
#               "\n3 - поиск данных"
#               "\n4 - редактирование данных"
#               "\n5 - просмотр данных"
#               "\n6 - завершение работы")
#         oper = input("Ввод: ")
#
#         if oper == "1":
#             num1 = input("Введите название страны (с заглавной буквы): ")
#             num2 = input("Введите назывние столицы (с заглавной буквы): ")
#         World.dump_to_json()
#        # elif oper == "2":
#        #      num1 = input("Введите название страны (с заглавной буквы): ")
#        #      num2 = input("Введите назывние столицы (с заглавной буквы): ")
#        # elif oper == "3":
#        #      num1 = input("Введите название страны (с заглавной буквы): ")
#        #      num2 = input("Введите назывние столицы (с заглавной буквы): ")
#        #
#        #  elif oper == "4":
#        #  num1 = input("Введите название страны (с заглавной буквы): ")
#        #  num2 = input("Введите назывние столицы (с заглавной буквы): ")
#        #
#        #  elif oper == "5":
#        #  num1 = input("Введите название страны (с заглавной буквы): ")
#        #  num2 = input("Введите назывние столицы (с заглавной буквы): ")
#        #
#        #  print("Файл сохранен")
#
#
#
#
# w = World()
# w.info()



import json

data = {}

class CountryCapital:

    @staticmethod
    def load(file_name):
        try:
            data = json.load(open(file_name))
        except FileNotFoundError:
            data = {}
        finally:
            return data

    @staticmethod
    def add_country(file_name):
        new_country = input("Введите название страны (с заглавной буквы): ")
        new_capital = input("Введите назывние столицы (с заглавной буквы): ")
        # try:
        #     data1 = json.load(open(file_name))
        # except FileNotFoundError:
        #     data1 = {}
        data1 = CountryCapital.load(file_name)

        data[new_country] = new_capital
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as f:
            print(json.load(f))

    @staticmethod
    def delete_country(file_name):
        del_country = input("Введите название страны: ")
        # try:
        #     data1 = json.load(open(file_name))
        # except FileNotFoundError:
        #     data1 = {}
        data1 = CountryCapital.load(file_name)

        if del_country in data1:
            del data1[del_country]

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)

        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_data(file_name):
        # try:
        #     data1 = json.load(open(file_name))
        # except FileNotFoundError:
        #     data1 = {}
        data1 = CountryCapital.load(file_name)

        country = input("Введите название страны: ")
        if country in data1:
            print(f"Страна {country}, столица {data1[country]} есть в словаре")
        else:
            print(f"Страны {country} с словаре нет!")

    @staticmethod
    def edit_data(file_name):
        # try:
        #     data1 = json.load(open(file_name))
        # except FileNotFoundError:
        #     data1 = {}
        data1 = CountryCapital.load(file_name)
        country = input("Введите название страны для корректировки: ")
        new_cap = input("Введите новое название столицы: ")

        if country in data1:
            data1[country] = new_cap

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print(f"Страны {country} с словаре нет!")

file = "list_capital.json"


while True:
    print("*" * 30)
    print("Выбор действия:"
        "\n1 - добавление данных"
        "\n2 - удаление данных"
        "\n3 - поиск данных"
        "\n4 - редактирование данных"
        "\n5 - просмотр данных"
        "\n6 - завершение работы")
    index = input("Ввод: ")
    if index == "1":
        CountryCapital.add_country(file)
    elif index == "2":
        CountryCapital.delete_country(file)
    elif index == "3":
        CountryCapital.search_data(file)
    elif index == "4":
        CountryCapital.edit_data(file)
    elif index == "5":
        CountryCapital.load_from_file(file)
    elif index == "6":
        break
    else:
        print("некорректный номер")



# try:
#     capitals = json.load(open('capitals.json'))
# except FileNotFoundError:
#     capitals = {}

#
# def add_entry(cntry, city):
#     capitals[cntry] = city
#     with open('capitals.json', 'w') as f:
#         json.dump(capitals, f, indent=2)
#     print("Файл сохранен")
#
#
# def delete_entry(cntry):
#     with open('capitals.json', 'w') as f:
#         if cntry in capitals:
#             capitals.pop(cntry)
#             json.dump(capitals, f, indent=2)
#             print("Файл сохранен")
#         else:
#             print("В файле нет такой страны")
#
#
# def find_entry(cntry):
#     with open('capitals.json') as f:
#         if cntry in capitals:
#             print(f"Страна: {cntry}, столица: {capitals[cntry]}")
#         else:
#             print("В файле нет такой страны")
#
#
# def edit_entry(cntry, city):
#     with open('capitals.json', 'w') as f:
#         capitals[cntry] = city
#         json.dump(capitals, f, indent=2)
#         print("Файл сохранен")
#
#
# while True:
#     choice = int(input("Выбор действия:\n1 - добавление данных\n2 - удаление данных"
#                        "\n3 - поиск данных\n4 - редактирование данных\n"
#                        "5 - просмотр данных\n6 - завершение работы\nВвод: "))
#     if choice == 1:
#         country = input("Введите название страны с заглавной буквы: ")
#         capital = input("Введите название столицы с заглавной буквы: ")
#         add_entry(country, capital)
#     elif choice == 2:
#         country = input("Введите страну, которую нужно удалить: ")
#         delete_entry(country)
#     elif choice == 3:
#         country = input("Введите страну, чтобы узнать столицу: ")
#         find_entry(country)
#     elif choice == 4:
#         country = input("Введите страну, чтобы изменить столицу: ")
#         if country in capitals:
#             capital = input("Введите новое название столицы: ")
#             edit_entry(country, capital)
#         else:
#             print("В файле нет такой страны")
#     elif choice == 5:
#         print(capitals)
#     elif choice == 6:
#         break
#     else:
#         print("Введите номер действия от 1 до 6")
# print("До свидания")