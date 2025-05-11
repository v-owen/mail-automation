from mail_automation.send_message import MailAutomation
bot = MailAutomation()
print(bot.send('text', 'hm','webscraping00000@gmail.com').status_code)
