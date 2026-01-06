from core.client import Bot
from core.enums import LoginMethod
from core.ffi import  enet_initialize

if enet_initialize() != 0:
    print("Failed to initialize ENet.")

if __name__ == "__main__":
    print("Enter your legacy account:")
    username = input("Input your GrowID: ")
    password = input("Input your password: ")

    bot = Bot(login_method=LoginMethod.LEGACY, username=username, password=password)
    bot.connect()