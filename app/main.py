from app.client import TgClient

APP_ID = 123456
API_HASH = 'abcdefg1234567'
TOKEN = '1234567:abcdefg1234567'

if __name__ == '__main__':
    client = TgClient(APP_ID, API_HASH, TOKEN).start
    print(client)
