import asyncio
import threading

from telethon import TelegramClient, events
from flask import Flask, request, jsonify
from flask_cors import CORS
from bot.lib import FindWords
import json


lib = FindWords()

two_keys = []
there_keys = []
one_negative_phrases = []
two_negative_phrases = []
threds_list = []

app = Flask(__name__)
CORS(app)


@app.route('/getKeys', methods=['POST'])
def sendKeys():
    data_request = request.json

    if data_request.get('keys-type') == 'negative-one':
        return jsonify({'keys': one_negative_phrases})

    elif data_request.get('keys-type') == 'negative-two':
        return jsonify({'keys': two_negative_phrases})

    elif data_request.get('keys-type') == 'plus-two':
        return jsonify({'keys': two_keys})

    elif data_request.get('keys-type') == 'plus-there':
        return jsonify({'keys': there_keys})


@app.route('/updateKeys', methods=['POST'])
def updateKeys():
    global one_negative_phrases
    data_request = request.json
    if data_request.get('keys-type') == 'negative-one':
        one_negative_phrases = data_request.get('data').split(',')
        createDump('negative-one')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request.get('keys-type') == 'negative-two':
        two_negative_phrases[data_request.get('index')] = (data_request.get('data-f-keys').split(','),
                                                           data_request.get('data-s-keys').split(','))
        createDump('negative-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request.get('keys-type') == 'plus-two':
        two_keys[data_request.get('index')] = (data_request.get('data-f-keys').split(','),
                                               data_request.get('data-s-keys').split(','))
        createDump('plus-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request.get('keys-type') == 'plus-there':
        there_keys[data_request.get('index')] = (data_request.get('data-f-keys').split(','),
                                                 data_request.get('data-s-keys').split(','),
                                                 data_request.get('data-t-keys').split(','))
        createDump('plus-there')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    else:
        return jsonify({'message': 'Error'}), 400


@app.route('/deleteKeysList', methods=['POST'])
def deleteKeysList():
    data_request = request.json

    if data_request['type-list'] == 'negative-two':
        del two_negative_phrases[data_request.get('index')]
        createDump('negative-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request['type-list'] == 'plus-two':
        del two_keys[data_request.get('index')]
        createDump('plus-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request['type-list'] == 'plus-there':
        del there_keys[data_request.get('index')]
        createDump('plus-there')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    else:
        return jsonify({'message': 'success'}), 400


@app.route('/appendKeysLists', methods=['POST'])
def appendKeysList():
    data_request = request.json
    if data_request.get('type-list') == 'negative-two':
        two_negative_phrases.append((['NaN'], ['NaN']))
        createDump('negative-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request.get('type-list') == 'plus-two':
        two_keys.append((['NaN'], ['NaN']))
        createDump('plus-two')
        initMainFuncs()
        return jsonify({'message': 'success'}), 200

    elif data_request.get('type-list') == 'plus-there':
        there_keys.append((['NaN'], ['NaN'], ['NaN']))
        createDump('plus-there')
        initMainFuncs()

        return jsonify({'message': 'success'}), 200

    else:
        return jsonify({'message': 'Error'}), 400


def createDump(switch):
    if switch == 'plus-two':
        x = 0
        to_json = {}
        for i in two_keys:
            to_json[x] = i
            x += 1
        with open('two_keys.json', 'w', encoding='utf-8') as f:
            json.dump(to_json, f, indent=4)
    elif switch == 'plus-there':
        x = 0
        to_json = {}
        for i in there_keys:
            to_json[x] = i
            x += 1
        with open('there_keys.json', 'w', encoding='utf-8') as f:
            json.dump(to_json, f, indent=4)

    elif switch == 'negative-one':
        to_json = {"0": one_negative_phrases}
        with open('one_negative_keys.json', 'w', encoding='utf-8') as f:
            json.dump(to_json, f, indent=4)

    elif switch == 'negative-two':
        x = 0
        to_json = {}
        for i in two_negative_phrases:
            to_json[x] = i
            x += 1
        with open('two_negative_keys.json', 'w', encoding='utf-8') as f:
            json.dump(to_json, f, indent=4)


def loadDump():
    with open('two_keys.json', 'r', encoding='utf-8') as f:
        x = 0
        data = json.load(f)
        for i in data:
            two_keys.append((data[str(x)][0], data[str(x)][1]))
            x += 1
    with open('there_keys.json', 'r', encoding='utf-8') as f:
        x = 0
        data = json.load(f)
        for i in data:
            there_keys.append((data[str(x)][0], data[str(x)][1], data[str(x)][2]))
            x += 1
    with open('two_negative_keys.json', 'r', encoding='utf-8') as f:
        x = 0
        data = json.load(f)
        for i in data:
            two_negative_phrases.append((data[str(x)][0], data[str(x)][1]))
            x += 1
    with open('one_negative_keys.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        one_negative_phrases.append(data['0'])

    print(two_keys)
    print(there_keys)
    print(one_negative_phrases)
    print(two_negative_phrases)



def initMainFuncs():
    lib.initWords(two_keys, 'two_keys')
    lib.initWords(there_keys, 'there_keys')
    lib.initWords(one_negative_phrases, 'one_negative_phrases')
    lib.initWords(two_negative_phrases, 'two_negative_phrases')



if __name__ == "__main__":
    loadDump()
    initMainFuncs()
    app.run(debug=True)

