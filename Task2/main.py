from Task2.announ import Announ

def main():

        announ1 = Announ("Продаю авто", "В хорошом качестве, автопробег меньше 1000", "Андрей")

        print(announ1.viewing_ads())
        print(announ1.viewing_ads())
        print(announ1.viewing_ads())
        announ1.set_heading("Меняю жену на нормальную бабу")
        print(announ1.viewing_ads())
        announ1.write_in_file()
        print(announ1.viewing_ads())
        announ1.write_in_file()

main()