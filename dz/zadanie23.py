import re

#1 вариант

# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # []
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))  # КиперьЕленаАлександровна
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО Можно использовать только буквы и дефиз")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, new_fio):
#         self.__fio = new_fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
# p1 = UserDate("Киперь Елена Александровна", 35, '1234 567891', 49.5)
# print(p1.__dict__)
# p1.old = 22
# p1.fio = "Сидоров Иван Иванович"
# p1.password = "2222 236532"
# p1.weight = 55.6
# print(p1.__dict__)


#2 вариант
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # []
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))  # КиперьЕленаАлександровна
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО Можно использовать только буквы и дефиз")
#
#     def get_fio(self):
#         return self.__fio
#
#     def set_fio(self, new_fio):
#         self.__fio = new_fio
#
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, new_old):
#         self.__old = new_old
#
#     def get_ps(self):
#         return self.__password
#
#     def set_ps(self, new_ps):
#         self.__password = new_ps
#
#     def get_weight(self):
#         return self.__weight
#
#     def set_weight(self, new_weight):
#         self.__weight = new_weight
#
# p1 = UserDate("Киперь Елена Александровна", 35, '1234 567891', 49.5)
# print(p1.__dict__)
# p1.set_fio("Сидоров Иван иванович")
# print(p1.__dict__)
# p1.set_old(26)
# print(p1.__dict__)
# p1.set_ps('3333 444444')
# print(p1.__dict__)
# p1.set_weight(60.5)
# print(p1.__dict__)
