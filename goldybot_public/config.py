﻿import disnake as discord
import os
from io import open
prefix = ["gg.", "gg!", "gb.", "gb!"]
with open("token.txt", encoding = "utf-8") as f:
    token =  f.read()
intents = discord.Intents.all()
logs_ch = канал логов
statuses = [
        "Привет! Я GoldyBot || gg.help", 
        "Хм... Зачем ты это читаешь?", 
        "Факт Дня: У меня ежедневные обновления!", 
        "Факт Недели: У Бота есть сайт: goldymine.tk",
        "Главное в Боте - его производительность...",
        "Факт дня: я был создан [ТАБ]LET[04]KA и MrGoldy",
        "Хотите шутку? А шутка вас нет", 
        "Бот вряд ли будет переведён на другие языки", 
        "MrGoldy Не делал бота, лишь командовал"
        ]
goldy = айди 2 владельца

cmds = []
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        cmds.append(f"{filename[:-3]}")
welcome = [ "приветик", "привет",  "здравствуйте", "здравствуй", "добрый день", "доброе утро", "добрый вечер"]
