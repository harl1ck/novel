import random
from Data import lox_inven


def tema():
    print("Не повезло ему оказаться в трэп-хате банана...\n"
          "В холодильнике 3 бутылки молока стоявшие несколько месяцев и давно скисли. Прочие продукты тоже сгнили.\n"
          "Под кроватью в спальне лежат давно забытые носки.\n"
          "- Ох зря я сюда полез... - чуть не плача сказал Тёма, глаза слезились, но из-за вони.\n"
          "- Надо выбираться, пока меня не накуканил банан!!!")
    while True:
        try:
            choose = int(input("Выберите, что будет делать Тёма:\n\t"
                               "1. Плакать\n\t"
                               "2. Дождётся банана и использует на нём смертельные объятия\n\t"
                               "3. Оценит расстояние от окна до земли\n\t"
                               "4. Будет писать ультра-код на spring\n"
                               "Вариант: "))
            if choose == 0 or choose > 4:
                print("Такого варианте не существует, выберите заново!")
                continue
        except ValueError:
            print("Число напиши, дЭб1L!".upper())
            continue
        match choose:
            case 1:
                print("Удивительно, но такой стойкий человек не выдержал напряжения\n"
                      "и давящей атмосферы данного помещения и разревелся как девчонка!")
                temacry()
                return
            case 2:
                print(
                    "После долгого ожидания банана и подготовки к его приходу,\n"
                    "Тёма схватил его и использовал смертельные объятия.\n"
                    "Банан не выдержал давления и умер.\n"
                    "Поздравляем! Тёма сбежал!!!")
                return
            case 3:
                print("Бросив взгляд на окно, Тёма подошёл к нему и выглянул наружу.\n"
                      "Так он выяснил, что находится на 15 этаже.\n"
                      "Он мог бы снять свои штаныи и использовать как парашют...")
                choice = str(input("Использовать штаны? (Да/Нет): ")).upper()
                match choice:
                    case "ДА":
                        print("Тёма тяжело вздохнул, ведь выбора не оставалось и снял штаны.\n"
                              "Открыв окно, он перекрестился и прыгнул, раскрыв импровизированный парашют...")
                        temawindow()
                        return
                    case "НЕТ":
                        print("- Придётся искать другой способ...")
                    case _:
                        print("Выберите заново...")
            case 4:
                print(
                    "Решив, что время нужно потратить с пользой Тёма достал ноут и начал писать ультра-код на spring.\n"
                    "Так время пролетело незаметно...\n"
                    "Тёма запушил код на гит, но от банана его это не спасло, ВЫ ПРОИГРАЛИ!")
                return


def temacry():
    chanse = random.randint(0, 1)
    match chanse:
        case 0:
            print("Тёму накуканил банан, ВЫ ПРОИГРАЛИ!")
        case 1:
            print("Плач этого кита услышали соседи и вызвали 112, Тёму спасли, ПОБЕДА!!!")


def temawindow():
    chanse = random.randint(0, 1)
    match chanse:
        case 0:
            print("Штаны оказались ненадёжным парашютом и Тёма разбился, ВЫ ПРОИГРАЛИ!")
        case 1:
            print("Удивительно, но штаны парашюты спасли его жизнь. ПОБЕДА!!!")


def naska():
    print("Не удивительно, что она оказалась в такой ситуации, ведь дичь следует за ней по пятам всю жизнь...\n"
          "Решив осмотреться, Наська поняла, что вариантов у неё не много,\n"
          f'так как в карманах только: {lox_inven["Наська"]}.')
    while True:
        try:
            choose = int(input("Выберите, что будет делать Наська:\n\t"
                               "1. Подумать, как можно использовать жвачку\n\t"
                               "2. Позвонить 102\n"
                               "Вариант: "))
            if choose == 0 or choose > 2:
                print("Такого варианте не существует, выберите заново!")
                continue
        except ValueError:
            print("Число напиши, дЭб1L!".upper())
            continue
        match choose:
            case 1:
                print("Ничего на ум, кроме того, как съесть её не приходил, но может стоит подумать подольше?")
                choice = str(input("Подумать подольше? (Да/Нет): ")).upper()
                match choice:
                    case "ДА":
                        print(
                            "Осмотрев комнату ещё раз, Наська заметила, что что-то торчит из-за шкафа,\n"
                            "но руками это не достать...")
                        choice = str(input("Подумать как достать это нечто? (Да/Нет): ")).upper()
                        match choice:
                            case "ДА":
                                print("На ум пришла идея: соединить с помощью жвачки вешалку и доску,\n"
                                      "которая лежит рядом со шкафом, после чего поддеть неизвестный предмет."
                                      "Воплотив идею в реальность, вытащенный предмет оказался...")
                                naskajavka()
                                return
                            case "НЕТ":
                                print("- Придётся искать другой способ...")
                            case _:
                                print("Выберите заново...")
                    case "НЕТ":
                        print("- Придётся искать другой способ...")
                    case _:
                        print("Выберите заново...")
            case 2:
                print("В кое-то веке включив мозг Наська набрала 102 и сообщила о своём местонахождении,\n"
                      "которое она посмотрела в Яндекс.Картах. Ей сказали, что в ближайшее время будут на месте.")
                naska_102()
                return


def naska_102():
    chanse = random.randint(0, 1)
    match chanse:
        case 0:
            print("Полиция не успела до прихода маньяка. ВЫ ПРОИГРАЛИ!")
        case 1:
            print("Полиция приехала вовремя, Наську спасли. ПОБЕДА!!!")


def naskajavka():
    chanse = random.randint(0, 1)
    match chanse:
        case 0:
            print("Старый носок...Теперь отсюда не выбраться......")
        case 1:
            print("Связкой ключей для дверей!!!\n"
                  "Наська спешно открыла дверь и сбежала.\n"
                  "Победа!!!")


def katuha():
    print("Почему именно Катюха? За что так с ней?\n"
          "Так как же ей выбраться с трэп-хаты? Здесь почти ничего нет, только кровать, окно, дверь.\n"
          "Надо придумать что-то пока не стало поздно, ведь завтра ещё и в шарагу о_0!")
    while True:
        try:
            choose = int(input("Выберите, что будет делать Катюха:\n\t"
                               "1. Подумать, как можно выбраться\n\t"
                               "2. Подумать, как можно выбраться\n\t"
                               "3. Подумать, как можно выбраться\n"
                               "Вариант: "))
            if choose == 0 or choose > 3:
                print("Такого варианте не существует, выберите заново!")
                continue
        except ValueError:
            print("Число напиши, дЭб1L!".upper())
            continue
        match choose:
            case 1 | 2 | 3:
                chanse = random.randint(0, 1)
                match chanse:
                    case 0:
                        print(
                            "Размышления о том, как же выбраться привели Катюху к мыслям "
                            "о незаполненом электронном журнале,\n"
                            "незаконченной практической по C# и было не плохо сделать всё это, "
                            "пока не прилетело как старосте.\n"
                            "Минус только в том, что телефона нет. "
                            "Зато есть документация по шарпам, так что код можно написать на листочке))))))))))")
                        try:
                            choose = int(input("Выберите, что будет делать Катюха:\n\t"
                                               "1. Продолжить думать\n\t"
                                               "2. Сделать практические работы по С-шапке на листочке\n"
                                               "Вариант: "))
                            if choose == 0 or choose > 2:
                                print("Такого варианте не существует, выберите заново!")
                                continue
                        except ValueError:
                            print("Число напиши, дЭб1L!".upper())
                            continue
                        match choose:
                            case 1:
                                print("Мысли в голове так и не появились...")
                                continue
                            case 2:
                                print("Не самое приятное и интересное дело, но важное и не то, чтобы отложное.\n"
                                      "Так, час за часом были сделаны тортики, проводник и конвертер.\n"
                                      "За дверью послышались шорохи, а значит вернулся банан.\n"
                                      "Покрепче схватив толтенную и тяжёлую документацию,\n"
                                      "Катюха ударила, что есть сил стоило тирану войти в помещение.")
                                chanse = random.randint(0, 1)
                                match chanse:
                                    case 0:
                                        print(
                                            "Банан не выстоял и пал ниц. Катюха схватила "
                                            "сделанные практы и сбежала...Победа!!!")
                                    case 1:
                                        print("Банана такой удар не взял и Катюха пала смертью храбрых...Проигрыш!")
                    case 1:
                        print(
                            "Думать пришлось долго, но в итоге было принято решение "
                            "пождечь хату с помощью документации.\n"
                            "Риски велики, но делать нечего.\n"
                            "Как первобытный человек Катюха добывала огонь...\n"
                            "Документация вспыхнула через минут 5 и огонь начал расходиться по комнате.")
                        chanse = random.randint(0, 1)
                        match chanse:
                            case 0:
                                print("Соседи вызвали пожарных и Катюху спасли! Победа!!!")
                            case 1:
                                print("Катюха не подумала о путях отхода сгорела...Проигрыш!")
                return
