import json



class FindWords():
    def __init__(self):
        self.two_keys = []
        self.there_keys = []
        self.one_negative_phrases = []
        self.two_negative_phrases = []


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
            self.one_negative_phrases.append(data['0'])


    def initWords(self, data_init, switch):
        if switch == 'two_keys':
            self.two_keys = data_init
        elif switch == 'there_keys':
            self.there_keys = data_init
        elif switch == 'one_negative_phrases':
            self.one_negative_phrases = data_init
        elif switch == 'two_negative_phrases':
            self.two_negative_phrases = data_init


    def checkPlusWords(self, check_data):
        message = []
        for i in check_data.split(' '):
            b = i.replace(',', '').replace('.', '').replace('ё', 'е').replace('Ё', 'Е').lower()
            message.append(b)
        i = len(check_data)
        x = 0
        while True:
            try:
                firs_key = message[x]
                second_key = message[x + 1]
            except:
                pass
            if firs_key == 'по':
                if second_key == 'чем':
                    try:
                        message[x] = 'почем'
                        del message[x + 1]
                    except:
                        pass
            x += 1
            if i == x:
                print(message)
                break

        for first_keys, second_keys in self.two_keys:
            if any(i in first_keys for i in message) and any(j in second_keys for j in message):
                return 'success'
        else:
            for first_keys, second_keys, threed_key in self.there_keys:
                if any(i in first_keys for i in message) and any(j in second_keys for j in message) and any(k in threed_key for k in message):
                    return 'success'
            return 'failure'


    def checkMinusWords(self, check_data):
        message = []
        for i in check_data.split(' '):
            b = i.replace(',', '').replace('.', '').replace('ё', 'е').replace('Ё', 'Е').lower()
            message.append(b)
        x = 0
        i = len(check_data)
        while True:
            try:
                firs_key = message[x]
                second_key = message[x + 1]
            except:
                pass
            if firs_key == 'по':
                if second_key == 'чем':
                    try:
                        message[x] = 'почем'
                        del message[x + 1]
                    except:
                        pass
            x += 1
            if i == x:
                print(message)
                break
        for i in self.one_negative_phrases:
            for j in message:
                if i == j:
                    return 'failure'


        for first_keys, second_keys in self.two_negative_phrases:
            if any(i in first_keys for i in message) and any(j in second_keys for j in message):
                return 'failure'
        else:
            return 'success'


    def createMessage(self, data, msg):
        try:
            link = f't.me/c/{data.message.peer_id.chat_id}/{data.message.id}'
            return f'{link}:{msg}'
        except:
            try:
                link = f't.me/c/{data.message.peer_id.channel_id}/{data.message.id}'  # public
                return f'{link}:{msg}'
            except:
                pass  # member message
                return 'None'
