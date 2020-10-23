class Auto:
    def __init__(self, color, speed, model):
        self.__color = color
        self.__model = model
        self.__speed = speed

    def __str__(self):
        return f'model - {self.__model}, color - {self.__color}, speed - {self.__speed}'

    def get_color(self):
        return self.__color

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def set_color(self, color):
        if type(color) == str:
            self.__color = color

    def set_speed(self, speed):
        if type(speed) == int:
            self.__speed = speed
        else:
            print("Enter valid info")

    def increase_speed(self, speed):
        if type(speed) == int and speed >0:
            self.__speed += speed
            return True
        return False
    def decrease_speed(self, speed):
        if type(speed) == int and speed >0:
            self.__speed -= speed
            return True
        return False