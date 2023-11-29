import telebot

bot = telebot.TeleBot('6762699174:AAG7YkcmjjzzsXV-yrdmvJVpRvlZmoFYEVc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я Вовчик и мне 13, и я хочу выиграть макбук💻. Заранее спасибо🙂. Напишите /help чтобы узнать о всех командах', parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Это бот для того, чтобы вы выучили даты и праздники🎉🎄. Надеюсь, вам понравится мой бот🎮🤖.', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Напишите /winter чтобы узнать о зимних праздниках❄️⛄',parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Напишите /autumn чтобы узнать об осенних праздниках🍁🍂',parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Напишите /spring чтобы узнать о весенних праздниках🍃🥬', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Напишите /summer чтобы узнать о летних праздниках🌅🍹🏖️', parse_mode='Markdown')
@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Это [ссылка](https://ru.pinterest.com/#top)', parse_mode='Markdown')

@bot.message_handler(commands=['winter'])
def main(message):
    bot.send_message(message.chat.id,'Это все зимние праздники❄️⛄.')
    bot.send_message(message.chat.id, 'Новый год — 1 января❄🎄⛄.')
    bot.send_message(message.chat.id, 'Рождество Христово — 7 января❄️🎄.')
    bot.send_message(message.chat.id, 'День защитника отечества — 23 февраля❄️🎖️.')
    bot.send_message(message.chat.id, 'Старый Новый год — 14 января❄️🎖🌨️.')
    bot.send_message(message.chat.id, 'День святого Валентина | День всех влюбленных — 14 февраля❄💝🌨️.')
    bot.send_message(message.chat.id, 'День полного освобождения Ленинграда от фашистской блокады — 27 января❄️⚔️.')
    bot.send_message(message.chat.id, 'День Республики Крым — 20 января🏙️🌨️.')
    bot.send_message(message.chat.id, 'А ещё зимой у меня день рождения🏙️🎂🎁.')

@bot.message_handler(commands=['autumn'])
def main(message):
    bot.send_message(message.chat.id, 'Это все осеннние праздники🍁🍂')
    bot.send_message(message.chat.id, '13 сентября – День программиста.💻🖱️')
    bot.send_message(message.chat.id, '30 сентября – День Всемирной сети Интернет.💻🎮')
    bot.send_message(message.chat.id, '6 октября – Международный день учителя.👨‍🏫‍🏫📖')
    bot.send_message(message.chat.id, '10 ноября – День милиции, а также Всемирный день молодёжи.👮📕')
    bot.send_message(message.chat.id, 'Хэллоуин — 31 октября🎃🧹🪣')
    bot.send_message(message.chat.id, 'День матери в России — 26 ноября 👩‍🍼')
    bot.send_message(message.chat.id, 'День машиностроителя — 24 сентября🚂')
    bot.send_message(message.chat.id, '1 сентября - день знаний📚')

@bot.message_handler(commands=['summer'])
def main(message):
    bot.send_message(message.chat.id, 'Это все летние праздники🌅🍹🏖️')
    bot.send_message(message.chat.id, 'Международный день защиты детей — 01 июня.🛡️🍼️')
    bot.send_message(message.chat.id, 'День молодежи России — 27 июня.🧑‍🦱👨‍🦰')
    bot.send_message(message.chat.id, 'День Военно-Морского Флота России — 30 июля в 2023 году⚓🚢')
    bot.send_message(message.chat.id, 'День Воздушно-десантных войск России — 2 августа✈️')
    bot.send_message(message.chat.id, 'День Крещения Руси (Памятная дата России) — 28 июля☦️')
    bot.send_message(message.chat.id, 'Иван Купала — 7 июля')
    bot.send_message(message.chat.id, 'А ущё все лето у школьников каникулы.🎉🎊🥳')

@bot.message_handler(commands=['spring'])
def main(message):
    bot.send_message(message.chat.id, 'Это все весенние праздники🍃🥬')
    bot.send_message(message.chat.id, 'Международный женский день - 8 марта🌹🏵️')
    bot.send_message(message.chat.id, '11 - 17 марта, Пн-Вс - Масленица🥞')
    bot.send_message(message.chat.id, 'Праздник Весны и Труда - 1 мая🛠️')
    bot.send_message(message.chat.id, '5 мая, Вс - Пасха🥚')
    bot.send_message(message.chat.id, 'День Победы — 9 мая🏅')
    bot.send_message(message.chat.id, 'Час Земли (экологическая акция) — 25 марта🌏🌐')
    bot.send_message(message.chat.id, 'День смеха (День дурака) — 1 апреля😆😄')

bot.infinity_polling()

