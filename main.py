import time
from googletrans import Translator

translator = Translator()

if __name__ == '__main__':
    line_count = 0
    while True:
        lines = []
        with open("Client.txt", 'r', encoding="utf-8") as file:
            for i, x in enumerate(file):
                if i > line_count and line_count:
                    lines.append(x)
        line_count = i
        for line in lines:
            message_start_index = line.find('@From')
            if message_start_index > -1:
                full_string_en = line[message_start_index+6:]
                nickname = full_string_en.split(':')[0]
                message_en = ":".join(full_string_en.split(':')[1:])
                translated_text = translator.translate(message_en, dest='ru')
                print("{}: {}".format(nickname, translated_text.text))
        time.sleep(5)
