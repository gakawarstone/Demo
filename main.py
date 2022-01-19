import telebot
import telebot, wikipedia, re

import config

# Создаем экземпляр бота

bot = telebot.TeleBot(config.TOKEN)

wikipedia.set_lang("ru")

# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])

def start(m, res=False):

    bot.send_message(m.chat.id, 'Здравствуйте мистер Романов, я ваш ассистент Нихао!')

    bot.send_message(m.chat.id, 'Если вам что-нибудь понадобится, то просто воспользуйтесь командой /help, и я сразу же прийду к вам на помощь!')

# Функция, обрабатывающая команду /help
@bot.message_handler(commands=["help"])

def help(m, res=False):

    bot.send_message(m.chat.id, 'Я рада, что вы воспользовались моим советом мистер Романов! Сейчас я вам покажу, что у нас есть в меню ;)')

    bot.send_message(m.chat.id, 'Пока что из доступных функций я могу предложить вам лишь вызов списка(для его вызова используйте команду /list), поиск на википедии(для его вызова используйте команду /wiki).')

# Функция, обрабатывающая команду /list
@bot.message_handler(commands=["list"])

def list(m, res=False):

    bot.send_message(m.chat.id, 'Ваш список: 1)Остальгия; 2)Microsoft word for windows(10). Для того чтобы получить доступ к фалам вышлите мне их номер в списке.')
    @bot.message_handler(content_types=["text"])
    def get_text_messages(message):
        print(message.text)
        answ(message)

    def answ(message):
        dict = {
            '1': 'Остальгия: берлинская стена - https://drive.google.com/drive/folders/1-kagrWnuxGG5ZAu4OW3R_WO0nISELn6m?usp=sharing',
            '2': 'Оффис для винды - https://drive.google.com/drive/folders/127lldOpiGAYAhgRD7kff6Pv_cmn6VO39?usp=sharing',
        }
        if message.text in dict:
            bot.send_message(message.chat.id, dict[message.text])


# Функция, обрабатывающая команду /wiki
@bot.message_handler(commands=["wiki"])
def wiki(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, wikiliks(message.text))

# Подфункция википедии
def wikiliks(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Запускаем бота

bot.polling(none_stop=True, interval=0)
