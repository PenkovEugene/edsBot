import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('5924667551:AAEsD66vrUQlUHvcJ638SipmUXpMXzhvNa0')

@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://edsgroup.ru')

@bot.message_handler(commands = ['information'])
def information(message):
    bot.send_message(message.chat.id, 'Я - бот EDS Group, EDSic. Моя задача - помочь инженерам получить информацию о том, как зайти в сервисный режим разных медицинских аппаратов и показываю пароли от них.')
    
@bot.message_handler(commands = ['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на официальный сайт EDS Group')
    btn2 = types.KeyboardButton('Информация о боте')
    btn3 = types.KeyboardButton('Получить пароль для входа в сервисный режим')
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'EDSic приветствует вас! Чем я могу помочь?', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на официальный сайт EDS Group':
        webbrowser.open('https://edsgroup.ru')
    elif message.text == 'Информация о боте':
        bot.send_message(message.chat.id, 'Я - бот EDS Group, Edsic. Моя задача - помочь инженерам получить информацию о том, как зайти в сервисный режим разных медицинских аппаратов и показываю пароли от них.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Получить пароль для входа в сервисный режим':
        markup = types.ReplyKeyboardMarkup()
        btn4 = types.KeyboardButton('GE')
        btn5 = types.KeyboardButton('Maquet')
        btn6 = types.KeyboardButton('Hamilton')
        btn7 = types.KeyboardButton('Mindray')
        btn8 = types.KeyboardButton('УОМЗ')
        btn9 = types.KeyboardButton('nGenuity')
        btn10 = types.KeyboardButton('Critikon')
        btn11 = types.KeyboardButton('Dräger')
        btn12 = types.KeyboardButton('Fresenius')
        btn14 = types.KeyboardButton('Nihon Kohden')
        btn15 = types.KeyboardButton('Nellcor')
        btn16 = types.KeyboardButton('Philips')
        btn17 = types.KeyboardButton('Siare')
        btn18 = types.KeyboardButton('Siemens')
        btn19 = types.KeyboardButton('Viasys-Carefusion')
        btn20 = types.KeyboardButton('NewPort')
        btn21 = types.KeyboardButton('Авента-М')
        markup.row(btn4, btn5, btn6)
        markup.row(btn7, btn8, btn9)
        markup.row(btn10, btn11, btn12)
        markup.row(btn14, btn15)
        markup.row(btn16, btn17, btn18)
        markup.row(btn19, btn20, btn21)
        bot.send_message(message.chat.id, 'Вы хотите получить пароль для входа в сервисный режим. Пожалуйста, выберите производителя медицинского аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_manufacturer)
        
def on_click_manufacturer(message):
    if message.text == 'GE':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: GE')
        markup = types.ReplyKeyboardMarkup()
        btn22 = types.KeyboardButton('Aespire 7100')
        btn23 = types.KeyboardButton('Aespire View')
        btn24 = types.KeyboardButton('AS3')
        btn25 = types.KeyboardButton('Aisys')
        btn26 = types.KeyboardButton('B20/B30/B40')
        btn27 = types.KeyboardButton('CARDIOCAP 5')
        btn28 = types.KeyboardButton('Centiva 5')
        btn29 = types.KeyboardButton('Corometrics 170')
        btn30 = types.KeyboardButton('Corometrics 250 CX')
        btn31 = types.KeyboardButton('Dash-3000/4000/5000')
        btn32 = types.KeyboardButton('Dinamap Compact')
        btn33 = types.KeyboardButton('Dinamap Pro 100/200/300/400')
        btn34 = types.KeyboardButton('Dinamap ProCare')
        btn35 = types.KeyboardButton('Engström')
        btn36 = types.KeyboardButton('IVENT 201')
        btn37 = types.KeyboardButton('R860')
        btn38 = types.KeyboardButton('S5 Avance')
        btn39 = types.KeyboardButton('S5 Light')
        markup.row(btn22, btn23, btn24, btn25)
        markup.row(btn26, btn27, btn28, btn29)
        markup.row(btn30, btn31, btn32, btn33)
        markup.row(btn34, btn35, btn36, btn37)
        markup.row(btn38, btn39)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_ge_model)
    elif message.text == 'Maquet':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Maquet')
        markup = types.ReplyKeyboardMarkup()
        btn40 = types.KeyboardButton('Flow-i')
        btn41 = types.KeyboardButton('Servo')
        markup.row(btn40, btn41)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_maquet_model)
    elif message.text == 'Hamilton':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Hamilton')
        markup = types.ReplyKeyboardMarkup()
        btn42 = types.KeyboardButton('G5')
        btn43 = types.KeyboardButton('Galileo')
        btn44 = types.KeyboardButton('C1/T1/MR1/C2/C3')
        markup.row(btn42, btn43)
        markup.row(btn44)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_hamilton_model)
    elif message.text == 'Авента-М':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите "Ручной вдох" и "Блокировка экрана" при включении аппарата. ')
    elif message.text == 'Mindray':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Mindray')
        markup = types.ReplyKeyboardMarkup()
        btn45 = types.KeyboardButton('E3/E5')
        btn46 = types.KeyboardButton('A3/A5')
        btn47 = types.KeyboardButton('EX-65')
        markup.row(btn45, btn46, btn47)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_mindray_model)
    elif message.text == 'УОМЗ':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: УОМЗ')
        markup = types.ReplyKeyboardMarkup()
        btn48 = types.KeyboardButton('МАИА - 01')
        markup.row(btn48)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_yom3_model)

    elif message.text == 'nGenuity':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: nGenuity')
        markup = types.ReplyKeyboardMarkup()
        btn49 = types.KeyboardButton('8100E')
        markup.row(btn49)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_ngenuity_model)

    elif message.text == 'Critikon':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Critikon')
        markup = types.ReplyKeyboardMarkup()
        btn50 = types.KeyboardButton('Dinamap Compact')
        btn51 = types.KeyboardButton('Dinamap Pro 110-400 V2')
        btn52 = types.KeyboardButton('Dinamap Pro 1000')
        btn53 = types.KeyboardButton('Dinamap Procare 400')
        markup.row(btn50, btn52)
        markup.row(btn51, btn53)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_critikon_model)

    elif message.text == 'Dräger':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Dräger')
        markup = types.ReplyKeyboardMarkup()
        btn54 = types.KeyboardButton('Evita 4')
        btn55 = types.KeyboardButton('Fabius GS/Plus/Tiro/MRI')
        markup.row(btn54)
        markup.row(btn55)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_drager_model)

    elif message.text == 'Fresenius':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Fresenius')
        markup = types.ReplyKeyboardMarkup()
        btn56 = types.KeyboardButton('multiFiltrate')
        markup.row(btn56)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_fresenius_model)

    elif message.text == 'Nihon Kohden':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Nihon Kohden')
        bot.send_message(message.chat.id, 'Для всех аппаратов данного производителя инструкция по входу в сервисный режим одинаковая.')
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим, пожалуйста, зажмите кнопку "Silence alarms" и включите аппарат.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

    elif message.text == 'Nellcor':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Nellcor')
        markup = types.ReplyKeyboardMarkup()
        btn57 = types.KeyboardButton('N-3000')
        btn58 = types.KeyboardButton('N-3900')
        markup.row(btn57, btn58)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_nellcor_model)

    elif message.text == 'Philips':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Philips')
        markup = types.ReplyKeyboardMarkup()
        btn59 = types.KeyboardButton('Respironics V60')
        btn60 = types.KeyboardButton('Avalon FM20/30/40/50')
        btn61 = types.KeyboardButton('C3')
        btn62 = types.KeyboardButton('CMS')
        btn63 = types.KeyboardButton('M1205')
        btn64 = types.KeyboardButton('M3046')
        btn65 = types.KeyboardButton('MP 2/5/20/40/50/60/80/90/MX450')
        btn68 = types.KeyboardButton('Respironics BiPAP Focus')
        btn69 = types.KeyboardButton('Respironics Esprit')
        btn70 = types.KeyboardButton('SureSigns VM')
        btn71 = types.KeyboardButton('V200')
        markup.row(btn59, btn60, btn61)
        markup.row(btn62, btn63, btn64)
        markup.row(btn65)
        markup.row(btn68)
        markup.row(btn69)
        markup.row(btn70, btn71)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_philips_model)

    elif message.text == 'Siare':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Siare')
        markup = types.ReplyKeyboardMarkup()
        btn72 = types.KeyboardButton('SLE1000')
        markup.row(btn72)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_siare_model)

    elif message.text == 'Siemens':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Siemens')
        markup = types.ReplyKeyboardMarkup()
        btn73 = types.KeyboardButton('Kion Multigas 2000/SC7000/8000/9000/9000XL')
        btn74 = types.KeyboardButton('SC5000/6000/6002')
        btn75 = types.KeyboardButton('SC6002XL/6802X')
        btn76 = types.KeyboardButton('Servo Screen 390')
        markup.row(btn73)
        markup.row(btn74, btn75, btn76)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_siemens_model)

    elif message.text == 'Viasys-Carefusion':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: Viasys-Carefusion')
        markup = types.ReplyKeyboardMarkup()
        btn77 = types.KeyboardButton('Alaris')
        btn78 = types.KeyboardButton('Vela')
        markup.row(btn77, btn78)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_viasys_carefusion_model)

    elif message.text == 'NewPort':
        bot.send_message(message.chat.id, 'Вы выбрали производителя аппарата: NewPort')
        markup = types.ReplyKeyboardMarkup()
        btn79 = types.KeyboardButton('HT-70')
        markup.row(btn79)
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель аппарата...', reply_markup = markup)
        bot.register_next_step_handler(message, on_click_newport_model)

    elif message.text == 'Авента-М':
        bot.send_message(message.chat.id, 'Вы выбрали аппарат: Авента-М')
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим, пожалуйста, зажмите кнопки "Ручной вдох" и "Блокировка экрана", и включите аппарат.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_ge_model(message):
    if message.text == 'Aespire 7100':
        bot.send_message(message.chat.id, 'Комментарий: Зажмите энкодер и включите аппарат')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Aespire View':
        bot.send_message(message.chat.id, 'Комментарий: Зажмите энкодер и включите аппарат')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'AS3':
        bot.send_message(message.chat.id, 'Пароль: 16 4 34;\nДалее 26 23 8')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Aisys':
        bot.send_message(message.chat.id, 'Пароль: 16 4 34;\nДалее 26 23 8')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'B20/B30/B40':
        bot.send_message(message.chat.id, 'Пароль: 16 4 34;\nДалее 26 23 8')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'CARDIOCAP 5':
        bot.send_message(message.chat.id, 'Пароль: 16 4 34;\nДалее 26 23 8')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Centiva 5':
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим нажмите следующую последовательность кнопок в течение 1 секунды:\n1. Левая сторона кнопки Adult;\n2. Правая сторона кнопки Adult;\n3. Энкодер.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Corometrics 170':
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим нажмите и удерживайте следующие кнопки: \n1. Setup button (календарь с часами);\n2. Power button (кнопка включения).')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Corometrics 250 CX':
        bot.send_message(message.chat.id, 'Комментарий: Паролем является установленная дата на мониторе. \nНапример: April 23 - 0423')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dash-3000/4000/5000':
        bot.send_message(message.chat.id, 'Комментарий: Паролем является установленная дата на мониторе. \nНапример: July 4 - 0407')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap Compact':
        bot.send_message(message.chat.id, 'Пароль: 2213')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap Pro 100/200/300/400':
        bot.send_message(message.chat.id, 'Пароль: 2213')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap ProCare':
        bot.send_message(message.chat.id, 'Комментарий: Держите кнопку Cycle и ON/OFF 3 секунды. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Engström':
        bot.send_message(message.chat.id, 'Пароль: 23-17-21; \nДалее 34-22-14. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'IVENT 201':
        bot.send_message(message.chat.id, 'Комментарий: Откройте меню, в самом конце выберите "Maintenance". ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'R860':
        bot.send_message(message.chat.id, 'Пароль администратора: 101867; \nПароль сервисный: 189004. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'S5 Avance':
        bot.send_message(message.chat.id, 'Пароль: 16-4-34; \nДалее 26-23-8. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')       
    elif message.text == 'S5 Light':
        bot.send_message(message.chat.id, 'Пароль: 16-4-34; \nДалее 26-23-8. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
        
def on_click_maquet_model(message):
    if message.text == 'Flow-i':
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим вам потребуется специальная сервисная карта. \nПароль: 8306. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Servo':
        bot.send_message(message.chat.id, 'Пароль БИОМЕД: 1973/1407. ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_hamilton_model(message):
    if message.text == 'G5':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, подключите аппарат к электросети. Включите Hamilton G5. После запуска отображается экран режима ожидания. \nНажмите кнопки "100% О2" и "Manual breath", чтобы активировать вкладку "Конфигурация". \nНажмите кнопки "Nebulizer on/off" и кнопку слева, чтобы активировать вкладку "Test mode". ')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Galileo':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, подключите аппарат к электросети. Включите Hamilton Galileo, одновременно удерживая кнопки "MANUAL BREATH"  и "100% O2" 5 секунд')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.test == 'C1/T1/MR1/C2/C3':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, подключите аппарат к электросети. Включите Hamilton, одновременно удерживая кнопки "MANUAL BREATH" и "100% O2" некоторое время пока не появится надпись о запуске сервисного режима')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_mindray_model(message):
    if message.text == 'E3/E5':
        bot.send_message(message.chat.id, 'Пароль: 1103')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'A3/A5':
        bot.send_message(message.chat.id, 'Пароль: 789789')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'EX-65':
        bot.send_message(message.chat.id, 'Пароль: 0611')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_yom3_model(message):
    if message.text == 'МАИА - 01':
        bot.send_message(message.chat.id, 'Пароль: ABCDE')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_ngenuity_model(message):
    if message.text == '8100E':
        bot.send_message(message.chat.id, 'Пароль: PIA418')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_critikon_model(message):
    if message.text == 'Dinamap Compact':
        bot.send_message(message.chat.id, 'Пароль: 2213')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap Pro 110-400 V2':
        bot.send_message(message.chat.id, 'Пароль: 2213')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap Pro 1000':
        bot.send_message(message.chat.id, 'Пароль: 2213')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Dinamap Procare 400':
        bot.send_message(message.chat.id, 'Комментарий: Для входа в сервисный режим нажмите и удерживайте кнопку "CYCLE", одновременно нажимая кнопку "ON/OFF" в течение 3 секунд')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_drager_model(message):
    if message.text == 'Evita 4':
        bot.send_message(message.chat.id, 'Комментарий: При включенном аппарате нажмите на кнопку "Конфигурация"; \nВыберите меню "Основные настройки"; \nВыберите меню "Сервисная диагностика"; \nВведите пароль; \nПароль: 4655')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Fabius GS/Plus/Tiro/MRI':
        bot.send_message(message.chat.id, 'Комментарий: В режиме ожидания одновременно нажмите кнопки "Home" и энкодер')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    
def on_click_fresenius_model(message):
    if message.text == 'multiFiltrate':
        bot.send_message(message.chat.id, 'Комментарий: При выключенном аппарате зажмите кнопки "I/O" и "Start reset"; \nПароль: 2211')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_nellcor_model(message):
    if message.text == 'N-3000':
        bot.send_message(message.chat.id, 'Комментарий: Включите аппарат при зажатых кнопках "Upper alarm limit" и "Lower alarm limit"')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'N-3900':
        bot.send_message(message.chat.id, 'Пароль: 215')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_philips_model(message):
    if message.text == 'Avalon FM20/30/40/50':
        bot.send_message(message.chat.id, 'Configuration Mode: 71034; \nDemo mode: 14432; \nService mode: 1345.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'C3':
        bot.send_message(message.chat.id, 'Пароль: 2-1-5')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'CMS':
        bot.send_message(message.chat.id, 'Configuration Mode: 1245; \nDemo mode: 14432; \nService mode: 4311, \nMaster Password: 14432.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'M1205':
        bot.send_message(message.chat.id, 'Пароль: 14432')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'M3046':
        bot.send_message(message.chat.id, 'Configuration Mode: 13251; \nDemo mode: 42351; \nService mode: 2553.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'MP 2/5/20/40/50/60/80/90/MX450':
        bot.send_message(message.chat.id, 'Configuration Mode: 71034; \nDemo mode: 14432; \nService mode: 1345')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    
    elif message.text == 'Respironics BiPAP Focus':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите кнопки "Сброс тревог" и "Заглушение тревог", и включите аппарата.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Respironics Esprit':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите кнопки "Сброс тревог" и "100% O2", и включите аппарата.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Respironics V60':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите энкодер и включите аппарат.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'SureSigns VM':
        bot.send_message(message.chat.id, 'Пароль: 2-1-5; \nДалее 2-1-9')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'V200':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите кнопки "Сброс тревог" и "100% O2", и включите аппарата.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_siare_model(message):
    if message.text == 'SLE1000':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, зажмите кнопки "Заглушение тревог", "Буст", энкодер, и включите аппарата.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_siemens_model(message):
    if message.text == 'Kion Multigas 2000/SC7000/8000/9000/9000XL':
        bot.send_message(message.chat.id, 'Пароль: 4712')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'SC5000/6000/6002':
        bot.send_message(message.chat.id, 'Пароль: 7412')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'SC6002XL/6802X':
        bot.send_message(message.chat.id, 'Пароль: 375')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Servo Screen 390':
        bot.send_message(message.chat.id, 'Пароль: 300')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_viasys_carefusion_model(message):
    if message.text == 'Alaris':
        bot.send_message(message.chat.id, 'Пароль: 376')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')
    elif message.text == 'Vela':
        bot.send_message(message.chat.id, 'Комментарий: Для перехода в сервисный режим вам требуется снять корпус и перевести переключатель DIP 1 в положение ON')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')

def on_click_newport_model(message):
    if message.text == 'HT-70':
        bot.send_message(message.chat.id, 'Комментарий: Пожалуйста, нажмите и удерживайте кнопку "Manual inflation" и включите аппарат.')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
        bot.send_message(message.chat.id, 'Для нового запроса отправьте мне "/start" ')



bot.polling(none_stop = True)
