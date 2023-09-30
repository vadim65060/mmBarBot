import json
import os

CONFIG_TEMPLATE = """{
  "tg_bot_token": "",
  "request_chat_id": ""
}
"""


class Config:
    def __init__(self, config_path: str):
        self.config_path: str = config_path
        self.bot_token: str = ''
        self.request_chat: int | None = None

        if os.path.exists(config_path):
            self.__load_settings()
        else:
            self.create_file()
            raise FileNotFoundError("Создан файл config.json, заполните его")

    def create_file(self):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            file.write(CONFIG_TEMPLATE)

    def update_request_chat(self, chat_id: int):
        self.request_chat = chat_id
        self.__save_setting('request_chat_id', chat_id)

    def __load_settings(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            config = json.loads(file.read())
            self.bot_token = config['tg_bot_token']
            self.request_chat = config['request_chat_id']

    def __save_setting(self, setting_name: str, setting):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            data[setting_name] = setting
            with open(self.config_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as exception:
            raise exception
