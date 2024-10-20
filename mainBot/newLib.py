import re
import json
import telebot


class FindWords():
    def __init__(self):
        self.two_keys = []
        self.there_keys = []
        self.one_negative_phrases = []
        self.two_negative_phrases = []
        self.attempts_send = 0
        self.loadDump()


    def loadDump(self):
        with open('two_keys.json', 'r', encoding='utf-8') as f:
            x = 0
            data = json.load(f)
            for i in data:
                self.two_keys.append((data[str(x)][0], data[str(x)][1]))
                x += 1
        with open('there_keys.json', 'r', encoding='utf-8') as f:
            x = 0
            data = json.load(f)
            for i in data:
                self.there_keys.append((data[str(x)][0], data[str(x)][1], data[str(x)][2]))
                x += 1
        with open('two_negative_keys.json', 'r', encoding='utf-8') as f:
            x = 0
            data = json.load(f)
            for i in data:
                self.two_negative_phrases.append((data[str(x)][0], data[str(x)][1]))
                x += 1
        with open('one_negative_keys.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data["0"]:
                self.one_negative_phrases.append(i)


        print(self.two_keys)
        print('')
        print(self.there_keys)
        print('')
        print(self.one_negative_phrases)
        print('')
        print(self.two_negative_phrases)
        print('')
        print('dump loaded')
        print('---------------------------------------------')


    async def check_one_negative_key(self, message):
        for key in self.one_negative_phrases:
            pattern = r'\b{}\b'.format(re.escape(key))
            if re.search(pattern, message, re.IGNORECASE):
                print('check_one_negative_key - [найдено]')
                return 'success'
        else:
            then_check = await self.check_two_negative_key(message)
            if then_check == 'failure':
                return 'failure'


    async def check_two_negative_key(self, message):
        for key in self.two_negative_phrases:
            for f_key in key[0]:
                for s_key in key[1]:
                    pattern = r'\b{}\b.*?\b{}\b'.format(re.escape(f_key), re.escape(s_key))
                    if re.search(pattern, message, re.IGNORECASE):
                        print('check_two_negative_key - [найдено]')
                        return 'success'
        else:
            return 'failure'


    async def check_two_keys(self, message):
        for key in self.two_keys:
            for f_key in key[0]:
                for s_key in key[1]:
                    pattern = r'\b{}\b.*?\b{}\b'.format(re.escape(f_key), re.escape(s_key))
                    if re.search(pattern, message, re.IGNORECASE):
                        print('check_two_keys - [найдено]')
                        return 'success'
        else:
            then_check = await self.check_there_keys(message)
            if then_check == 'success':
                return 'success'

    async def check_there_keys(self, message):
        for key in self.there_keys:
            for f_key in key[0]:
                for s_key in key[1]:
                    for t_key in key[2]:
                        pattern = r'\b{}\b.*?\b{}\b.*?\b{}\b'.format(re.escape(f_key), re.escape(s_key), re.escape(t_key))
                        if re.search(pattern, message, re.IGNORECASE):
                            print('check_there_keys - [найдено]')
                            return 'success'
        else:
            return 'failure'

    async def checker(self, message):
        print('Проверка сообщения...')
        check_plus = await self.check_two_keys(message)
        if check_plus == 'success':
            print('Пройдена проверка на PLUS слова')
            check_negative = await self.check_one_negative_key(message)
            if check_negative == 'failure':
                return 'success'
            else:
                print('Провалена проверка на MINUS слова')
        print('Проверка не пройдена...')
        return 'failure'



    def createMessage(self, message, chatType):
        data_user = None
        data_chat = None
        if chatType == 'Group':
            data_user = {
                "message": message.text,
                "user_id": message.from_user.id,
                "user_name": message.from_user.username,
                "message_id": message.id,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
            }

            data_chat = {
                "chat_id": abs(message.chat.id),
                "chat_name": message.chat.title

            }
        elif chatType == 'SuperGroup':
            data_user = {
                "message": str(message.text),
                "user_id": message.from_user.id,
                "user_name": message.from_user.username,
                "message_id": message.id,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
            }

            data_chat = {
                "chat_id": str(message.chat.id)[4:],
                "chat_name": message.chat.title

            }

        message_link = f't.me/c/{data_chat["chat_id"]}/{data_user["message_id"]}'
        cr_message = f"<blockquote>test</blockquote>\n\nUserName - <code>{data_user['user_name']}</code>\nUserID - <code>{data_user['user_id']}</code>\nNameChat <code>{data_chat['chat_name']}</code>\nMessageLink - <a href='{message_link}'>ТЫК</a>"

        return cr_message


    def sendMessageManger(self, message, chatType):
        msg = self.createMessage(message, chatType)
        if self.attempts_send == 0: # 1
            botF = telebot.TeleBot('7799964843:AAGgp_mMQzNFJX2gDLISHSGhGBtSypXvjY4')
            botF.send_message(-1002338015635, msg, parse_mode='HTML')

        # elif self.attempts_send == 1: # 2
        #     botS = telebot.TeleBot('7507382901:AAGpkWlFUabpwncaB0-akyRjLEd1RrU2LIA')
        #     botS.send_message(-1002338015635, msg, parse_mode='HTML')
        #
        # elif self.attempts_send == 2: # 3
        #     botT = telebot.TeleBot('7943859972:AAGpQCYtuJb3qxaa3rV0fI8O8u3uoJv0Z6Y')
        #     botT.send_message(-1002338015635, msg, parse_mode='HTML')
        #
        # elif self.attempts_send == 3:
        #     self.sendMessageManger(message, chatType)
        #     self.attempts_send = 0
        #
        # self.attempts_send += 1





