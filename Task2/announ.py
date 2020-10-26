from datetime import datetime

class Announ:
    def __init__(self, heading, description, author, views = 1, dates=datetime.now()):
        self.__heading = heading
        self.__description = description
        self.__author = author
        self.__dates = dates
        self.__views = views

    def __str__(self):
        return f'Заголовок: {self.__heading}, Описание: {self.__description}, Автор: {self.__author}, Дата: {self.__dates}, Количество просмотров: {self.__views}'

    def get_heading(self):
        return self.__heading
    def get_description(self):
        return self.__description
    def get_author(self):
        return self.__author
    def get_views(self):
        self.__views = self.__views + 1
        return self.__views
    def get_dates(self):
        return self.__dates

    def set_heading(self, heading):
        self.__heading = heading

    def set_description(self, description):
        self.__description = description



    def viewing_ads(self):
        self.__views = self.__views + 1
        return self.__heading, self.__description, self.__author, self.__dates





