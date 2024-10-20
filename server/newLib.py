import re
import json


class FindWords():
    def __init__(self):
        self.two_keys = []
        self.there_keys = []
        self.one_negative_phrases = []
        self.two_negative_phrases = []
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

    async def check_one_negative_key(self, message):
        for key in self.one_negative_phrases:
            pattern = r'\b{}\b'.format(re.escape(key))
            if re.search(pattern, message, re.IGNORECASE):
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
                        return 'success'
        else:
            return 'failure'


    async def check_two_keys(self, message):
        for key in self.two_keys:
            for f_key in key[0]:
                for s_key in key[1]:
                    pattern = r'\b{}\b.*?\b{}\b'.format(re.escape(f_key), re.escape(s_key))
                    if re.search(pattern, message, re.IGNORECASE):
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
                            return 'success'
        else:
            return 'failure'

    async def checker(self, message):
        check_plus = await self.check_two_keys(message)
        if check_plus == 'success':
            print('Пройдена проверка на PLUS слова')
            check_negative = await self.check_one_negative_key(message)
            if check_negative == 'failure':
                return 'success'
            else:
                print('Провалена проверка на MINUS слова')