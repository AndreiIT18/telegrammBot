import telebot
from telebot import types
bot = telebot.TeleBot("6207705030:AAGpN6hKdnNWZtPA9MH9VkDzkKEBWYFAV1M")



@bot.message_handler(commands={'start'})
def start(message):
     markup = types.ReplyKeyboardMarkup()
     kpoi1 =types.KeyboardButton('Перейти на сайт')
     markup.row(kpoi1)
     kpoi2 = types.KeyboardButton('Удалить фото!')
     kpoi3 = types.KeyboardButton('Изменить текст')
     markup.row(kpoi2, kpoi3)
     bot.send_message(message.chat.id, 'Привет', reply_markup = markup)
     bot.register_next_step_handler(message, on_click)
     
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Переход на веб-сйт')
    elif message.text == 'Удалить фото!':
         bot.send_message(message.chat.id, 'Удалено')
    
def send_welcome(message):
	bot.send_message(message.chat.id, f'Пивет, {message.from_user.first_name} {message.from_user.last_name}' )
 
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    kpoi1 =types.InlineKeyboardButton('Перейти на сайт', url='https://ya.ru/?banerid=0758004923%3a634c79735ab74d99246c3f30&clid=2270453&nr=1&redirect_ts=1686819759.00000&win=564')
    markup.row(kpoi1)
    kpoi2 = types.InlineKeyboardButton('Удалить фото!', callback_data='delete')
    kpoi3 = types.InlineKeyboardButton('Изменить текст', callback_data='text')
    markup.row(kpoi2, kpoi3)
    bot.reply_to(message,'Красивое фото', reply_markup = markup )
    
@bot.callback_query_handler(func= lambda callback: True)
def  callback_messege(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'text':
        bot.edit_message_text('Новый текст', callback.message.chat.id, callback.message.messege_id)
	
bot.polling(non_stop=True)