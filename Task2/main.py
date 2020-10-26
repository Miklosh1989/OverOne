from Task2.announ import Announ

def main():
        announ1 = Announ("Продаю авто", "В хорошом качестве, автопробег меньше 1000", "Андрей")
        announ1.viewing_ads()
        announ1.viewing_ads()
        print(announ1)

        announ1.set_heading("продаю жену")
        print(announ1)

main()