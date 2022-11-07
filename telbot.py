import telegram


bot=telegram.Bot(token='2081633148:AAHT53UQUP_e0raz82jOzovx6-3e8OM7Iik')
bot.send_message(chat_id='@AVMChannel', text="Привет, проверка связи")
bot.send_document(chat_id='@AVMChannel',document=open('nasa_epic_images/nasa_epic_0.png','rb'))