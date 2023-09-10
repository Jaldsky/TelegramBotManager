from telethon import events


# class Events:
#
#     @client.on(events.NewMessage(pattern='/send'))
#     async def send_message(self, event):
#
#         args = event.message.text.split(' ')
#
#         user = args[1]
#         message = ' '.join(args[2:])
#
#         await client.send_message(user, message)