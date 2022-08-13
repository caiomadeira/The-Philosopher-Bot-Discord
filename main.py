"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from classes.scenes.discord.pb_discord import *


def ler_token_test():
    with open(os.getenv("token_test"), "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


TOKEN = 'NzU5Njc3MTIyNjk5ODUzODI2.GUkznv.oQYPalOWOqF3FPR-clNghXU__ka9Y5B24ry4bg'


if __name__ == '__main__':
    client.run(TOKEN)
