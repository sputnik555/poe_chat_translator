import time
from googletrans import Translator

translator = Translator()


if __name__ == '__main__':
    max_index = -1
    while True:
        lines = []
        index = -1
        with open('D:\Games\PoE\logs\Client.txt', 'r', encoding='utf-8') as file:
            for index, line in enumerate(file):
                if index > max_index > -1:
                    lines.append(line)
        max_index = index
        for line in lines:
            message_start_index = line.find('@From')
            is_message_from_trade = "Hi, I'd like to buy your" in line \
                                    or "Hi, I would like to buy your" in line
            if message_start_index > -1 and not is_message_from_trade:
                message_with_nickname = line[message_start_index+6:]
                nickname = message_with_nickname.split(':')[0]
                message_text_en = ":".join(message_with_nickname.split(':')[1:])
                translated_text = translator.translate(message_text_en, dest='ru')
                print("{}: {}".format(nickname, translated_text.text))
        time.sleep(5)
