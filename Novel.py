import json
import Functions
from Functions import tema, naska, katuha
from Data_Saves import loxi, lox_inven
game = True

print("Вы заспустили НОВЕЛЛУ \"Побег от банана с обосранной жэпой\"...\n"  # экранирование строки
      "В N-городе завёлся мама-ама-криминал, которого прозвали \"БАНАН\"\n"
      "и так уж вышло, что его штаны, в которых он вершил грязные делишки, были обосраны. Всегда...\n"
      "На прошлой неделе он совершил ряд нападений на граждан РФ и притащил их в свою трэп-хату.\n"
      "Вам предстоит выбрать лоха, за которого Вы будете убегать."
      f"Так называемые лохи:\n\t1. {loxi[0]}\n\t2. {loxi[1]}\n\t3. {loxi[2]}") #f-строка

while (game != False):
    try:
        persona = int(input("Выберите лоха: "))
        if persona == 0 or persona > 3:
            print("Такого варианте не существует, выберите заново!")
            continue
    except ValueError:
        print("Число напиши, дЭб1L!".upper())
        continue
    match persona:
          case 1:
              print("Тёма: мама-java под 2 метра.\n"
                    "Характеристика: \"Лучший среди худших\", прямолинеен.\n"
                    "Говнокод = криптонит.\n"
                    "Характер скверный.\n"
                    "Не женат.\n"
                    f'Предметы: {lox_inven["Тёма"]}')
              choice = str(input(f"Сбежать за: {loxi[0]}? (Да/Нет) OR (Yes/No): ")).upper()
              match choice:
                      case "ДА" | "YES":
                          data = {
                              "loxi": {
                                  "select_char": persona,
                                  "choice": choice,
                                  "ending": tema()
                              }
                          }
                          with open('gg.json', 'w', encoding='utf-8') as file:
                              json.dump(data, file, indent=2, ensure_ascii=False)
                          game = False
                          print("Спасибо за прохождение!")
                      case "НЕТ" | "NO":
                          print("- Ты офигело? Быдло.")
                      case _:
                          print("Выберите заново...")
          case 2:
              print("Наська: золотые руки, плохая память и говнокод - незыблимые факты.\n"
                    "Характеристика: Яркая личность, немного кринжа и сумасшествия.\n"
                    "Чаще всего описывается людьми, как милый ксёк либо е******я ****.\n"
                    "На всё в жизни реагирует так, словно подобное дерьмо уже часть её ежедневного расписания, что отчасти является правдой.\n"
                    "Характер пойдёт (КУДА?????????).\n"
                    f'Предметы: {lox_inven["Наська"]}')
              choice = str(input(f"Сбежать за: {loxi[1]}? (Да/Нет) OR (Yes/No): ")).upper()
              match choice:
                    case "ДА" | "YES":
                        data = {
                            "loxi": {
                                "select_char": persona,
                                "choice": choice,
                                "ending": naska()
                            }
                        }
                        with open('gg.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, indent=2, ensure_ascii=False)
                        game = False
                        print("Спасибо за прохождение!")
                    case "НЕТ" | "NO":
                        print("- Я НЕ ХОЧУ УМИРАТЬ!!!!!!")
                    case _:
                        print("Выберите заново...")
          case 3:
              print("Катюха: КРУГЛАЯ отличница ))ООО)))О)ОО.\n"
                    "Характеристика: Слишком умная для этой ситуации.\n"
                    "С осторожностью подходит к любым задачам.\n"
                    "Любит ксёков.\n"
                    "Характер с переменным успехом.\n"
                    f'Предметы: {lox_inven["Катюха"]}')
              choice = str(input(f"Сбежать за: {loxi[2]}? (Да/Нет) OR (Yes/No): ")).upper()
              match choice:
                    case "ДА" | "YES":
                        data = {
                            "loxi": {
                                "select_char": persona,
                                "choice": choice,
                                "ending": katuha()
                            }
                        }
                        with open('gg.json', 'w', encoding= 'utf-8') as file:
                            json.dump(data, file, indent=2, ensure_ascii= False)
                        game = False
                        print("Спасибо за прохождение!")
                    case "НЕТ" | "NO":
                        print("- Упаси Боже.")
                    case _:
                        print("Выберите заново...")
