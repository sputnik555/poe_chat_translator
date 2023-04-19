import time
from googletrans import Translator

translator = Translator()

if __name__ == '__main__':
    line_count = 0
    while True:
        lines = []
        with open("Client.txt", 'r', encoding="utf-8") as file:
            for i, x in enumerate(file):
                if line_count and i > line_count:
                    lines.append(x)
        line_count = i
        for line in lines:
            message_start_index = line.find('@From')
            if message_start_index > -1:
                message_with_nickname = line[message_start_index+6:]
                nickname = message_with_nickname.split(':')[0]
                message_text_en = ":".join(message_with_nickname.split(':')[1:])
                translated_text = translator.translate(message_text_en, dest='ru')
                print("{}: {}".format(nickname, translated_text.text))
        time.sleep(5)
