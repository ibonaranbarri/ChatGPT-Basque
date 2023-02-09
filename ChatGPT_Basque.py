import telebot
import openai
from deep_translator import GoogleTranslator

#configuracion
API_KEY = 'YOUR TELEGRAM API KEY'
bot = telebot.TeleBot(API_KEY)
openai.api_key = 'YOUR OPEN AI API KEY'

#start
@bot.message_handler(commands=['start','help'])
def start(message):
    print('/start')
    bot.reply_to(message,'Galdetu zer nahi duzun eta itxaron.')

#responder a los mensages
@bot.message_handler(content_types=['text'])
def respuesta(message):
    peticion_eus = message.text
    traductor = GoogleTranslator(source='eu', target='es')
    peticion = traductor.translate(peticion_eus)
    respuesta = openai.Completion.create(engine='text-davinci-002',temperature = 0.5, prompt = peticion, max_tokens = 750)
    answer = respuesta.choices[0]['text']
    traductor = GoogleTranslator(source='es', target='eu')
    answer_eus = traductor.translate(answer)
    bot.reply_to(message, answer_eus)


#main
if __name__ == '__main__':
    print('bot en marcha')
    bot.infinity_polling()
    print('fin')