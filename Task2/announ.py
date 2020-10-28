from datetime import date

class Announ:

    def __init__(self, heading, description, author):
        self.__heading = heading
        self.__description = description
        self.__author = author
        self.__views = 0
        self.__dates = date.today()

    def __str__(self):
        return f'Заголовок: {self.__heading}, Описание: {self.__description}, Автор: {self.__author}, Количество просмотров: {self.__views}, Дата: {self.__dates}'

    def get_heading(self):
        return self.__heading
    def get_description(self):
        return self.__description
    def get_author(self):
        return self.__author


    def set_heading(self, heading):
        self.__heading = heading

    def set_description(self, description):
        self.__description = description

    def viewing_ads(self):
        self.__views = self.__views + 1

        return self.__heading, self.__description, self.__author, self.__views, "{}.{}.{}".format(self.__dates.day, self.__dates.month, self.__dates.year)

    def write_in_file(self):
        with open("C:\python\Homework\Task2\\announs.txt", 'a') as somefile:

            somefile.write(self.__heading + '\t ')
            somefile.write(self.__description + '\t ')
            somefile.write(self.__author + '\t ')
            somefile.write(str(self.__views) + '\t ')
            somefile.write(str(self.__dates) + '\n')





