import sqlite3
import time
import math
import re
from flask import url_for

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self): #достает данные из БД (кнопки меню)
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def well(self, field, num, text, depth):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO wells VALUES(NULL, ?, ?, ?, ?, ?)", (field, num, text, depth, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления скважины в БД" + str())
            return False
        return True

    def get_well(self, field_id): #вызов из БД
        try:
            self.__cur.execute(f"SELECT field, num, text, depth FROM wells WHERE id={field_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка вывода скважины из БД" + str(e))

        return False, False, False, False

    def get_wells_anonce(self):
        try:
            self.__cur.execute(f"SELECT id, field, num, text, depth FROM wells ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка вывода скважин из БД" + str(e))

        return []






