from core.client import Bot
from core.ffi import  enet_initialize

if enet_initialize() != 0:
    print("Failed to initialize ENet.")

if __name__ == "__main__":
    print("Enter your legacy account:")
    username = input("Input your GrowID: ")
    password = input("Input your password: ")

    bot = Bot(username=username, password=password)
    bot.connect()