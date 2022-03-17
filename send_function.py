import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5011174642:AAGeyUXzC-ELAhM0TzM73fJCYDr4yxVsX44'
    bot_chatID = '-759346901'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.post(send_text)

    response.json()

telegram_bot_sendtext("Test")