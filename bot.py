import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/commando1':
        bot.sendMessage(jee)
    elif command == '/commando2':
        bot.sendMessage(chat_id,"hallo allemaal")

bot = telepot.Bot('*** VOEG API KEY IN ***')

MessageLoop(bot, handle).run_as_thread()
print 'Ik luister'

while 1:
    time.sleep(10)