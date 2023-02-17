import os
# Задача №1

# with open("dz_20_1.txt", "w") as f:
#     f.write("Домашнее задание")
#
# with open("dz_20_2.txt", "w") as f:
#     f.write("№20 выполнено")
#
# with open("dz_20_1.txt") as f:
#     text = f.read()
#     print(text)
# with open("dz_20_2.txt") as f:
#     text2 = f.read()
#     print(text2)
#
# text += text2
# with open("dz_20.txt", "w") as f:
#     f.write(text)

# Задача №2


# def search(file):
#     if os.path.exists(file):
#         dirs, name = os.path.split(file)
#         atime = os.path.getatime(file)
#         print(f"{name} ({dirs}) - last access time {atime} sec")
#     else:
#         print(f"Файл  {file} не существует!")
#
# search(r'C:\Users\Вениамин\Desktop\Пайтон\Project Python\test\text1.txt')
