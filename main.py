import functions

def main():
    chat=functions.chat
    print('Добро пожаловать! Я помогу сделать Вам презенатцию по теме исследования.\n')
    user_input=input('Введите расположение файла с статьей (формат docx/pdf) или тему исследования \n')
    try:
        text=functions.read_file(user_input)
        summorized_answer = functions.summarise_text(chat, text)
    except:
        text=user_input
        summorized_answer = functions.summarise_topic(chat, text)
    profitable_answer = functions.get_profits(chat, summorized_answer)
    pres = functions.make_presention(chat, summorized_answer + profitable_answer)
    functions.generate_slides(pres)
if __name__=="__main__":
    main()