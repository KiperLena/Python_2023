import json

world = {}

class CountryCapital:
    @staticmethod
    def add_country(file_name):
        new_country = input("Введите название страны (с заглавной буквы): ")
        new_capital = input("Введите назывние столицы (с заглавной буквы): ")
        try:
            world1 = json.load(open(file_name))
        except FileNotFoundError:
            world1 = {}

        world[new_country] = new_capital
        with open(file_name, 'w') as f:
            json.dump(world, f, indent=2)
        print("Файл сохранен")

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as f:
            print(json.load(f))

    @staticmethod
    def delete_country(file_name):
        del_country = input("Введите название страны: ")
        try:
            world1 = json.load(open(file_name))
        except FileNotFoundError:
            world1 = {}

        if del_country in world1:
            del world1[del_country]

            with open(file_name, 'w') as f:
                json.dump(world1, f, indent=2)

        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_data(file_name):
        try:
            world1 = json.load(open(file_name))
        except FileNotFoundError:
            world1 = {}

        country = input("Введите название страны: ")
        if country in world1:
            print(f"Страна {country}, столица {world1[country]} есть в словаре")
        else:
            print(f"Страны {country} с словаре нет!")

    @staticmethod
    def edit_data(file_name):
        try:
            world1 = json.load(open(file_name))
        except FileNotFoundError:
            world1 = {}

        country = input("Введите название страны для корректировки: ")
        new_cap = input("Введите новое название столицы: ")

        if country in world1:
            world1[country] = new_cap

            with open(file_name, 'w') as f:
                json.dump(world1, f, indent=2)
        else:
            print(f"Страны {country} с словаре нет!")

file = "world.json"


while True:
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
        CountryCapital.add_country(file)
    elif oper == "2":
        CountryCapital.delete_country(file)
    elif oper == "3":
        CountryCapital.search_data(file)
    elif oper == "4":
        CountryCapital.edit_data(file)
    elif oper == "5":
        CountryCapital.load_from_file(file)
    elif oper == "6":
        break
    else:
        print("некорректный номер")
print("работа завершена")

