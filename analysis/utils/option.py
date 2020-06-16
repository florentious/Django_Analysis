import json

fileName = 'analysis/utils/config.json'


class Options:
    def __init__(self):
        jsonObj = json.loads(open(fileName, 'rb').read().decode('utf-8'))

        self.stop_word        = jsonObj['stop_word']
        self.max_count        = jsonObj['max_count']
        self.background_color = jsonObj['background_color']
        self.font_path        = jsonObj['font_path']
        self.txt_dir_path     = jsonObj['txt_dir_path']