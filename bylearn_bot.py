import os
from decouple import config
from discord.ext import commands


# PREFIXO P/ COMANDOS
bot = commands.Bot("!")

# CHAMAR CÓDIGO
def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("Tasks.dates")

    for file in os.listdir("Commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Commands.{cog}")

load_cogs(bot)
 
# EXECUTAR O BOT
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)
