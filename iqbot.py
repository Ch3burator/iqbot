import telebot

from telebot import types

bot = telebot.TeleBot("2119220921:AAH6I2AxwpFWxERgjulXaBIIAUNRg7w_QuU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Type @howsmartamibot in any chat and hit \"Share my IQ\"")

@bot.message_handler(commands=['donate'])
def donate(message):
	bot.reply_to(message, "Type @howsmartamibot in any chat and hit \"Share my IQ\"")

@bot.inline_handler(lambda query: len(query.query) > -1)
def default_query(inline_query):
    IQ = (inline_query.from_user.id + 26) % 151 + 50
    if IQ == 67:
        IQ = 200
    ruhist = "В конце 2021 группой российских учёных была разработана технология определения IQ с помощью ботов Telegram. Такой способ измерения очень удобен, для того, чтобы узнать ваш результат, достаточно написать @howsmartamibot в любом чате в телеграме и нажать на кнопку \"Share your IQ\". Точность данного метода измерения достаточно высока (погрешность не превышает половины процента). Нормальный результат - около 100 баллов, результат менее 70 баллов свидетельствует об умственной отсталости, людей с IQ 150 считают гениями. \n \nСейчас учёные активно работают над совершенствованием технологии определения IQ с помощью ботов Telegram. Данной разработке находят новые применения, она уже часто применяется для разрешения споров и объективного определения крутости.\n \nЕсли вы хотите поддержать исследования в данной области, то присылайте пожертвования: 2202 2018 3143 9894"
    enhist = "At the end of 2021, a group of russian scientists developed a technology of determining IQ using Telegram bots. This method of determining the intelligence quotient is very convenient, in order to find out your result, you should simply write @howsmartamibot in any Telegram chat and click \"Share your IQ\". The accuracy of this method of measurement is quite high (margin of error is less than half a percent). The normal result is about 100 points, a score of less than 70 points indicates mental retardation, people with a score of over 150 are considered geniuses. \n \nNow scientists are actively working on improving the technology of determining IQ with the help of Telegram bots. This development is finding new applications, it is already often used to resolve disputes and objectively determine coolness. \n \nIf you want to support research in this area, send donations: 2202 2018 3143 9894"
    try:
        r = types.InlineQueryResultArticle('1', 'Share your IQ', types.InputTextMessageContent('My IQ is '+ str(IQ)+ ' 🧠') , description='Send your IQ to this chat', thumb_url="https://i.imgur.com/fkriOEF.png")
        r2 = types.InlineQueryResultArticle('2', 'How does it work?', types.InputTextMessageContent(enhist) , description='Know more about the technology of precise IQ determining using Telegram bots', thumb_url="https://i.imgur.com/X59Nl5X.png")
        r3 = types.InlineQueryResultArticle('3', 'Как это работает?', types.InputTextMessageContent(ruhist) , description='Узнайте больше о технологии точного определения IQ с помощью ботов Telegram', thumb_url="https://i.imgur.com/X59Nl5X.png")
        bot.answer_inline_query(inline_query.id, [r, r2, r3], cache_time=1)
    except Exception as e:
        print(e)

bot.polling(none_stop=True)