from os import path, getcwd
from app.client import TgClient


if __name__ == '__main__':
    conf_path = path.join(getcwd(), 'app', 'config.ini')

    client = TgClient(conf_path).start
    print(client.api_id)
