import datetime
from discord.ext import commands, tasks

class Dates(commands.Cog):
    """ Work With Dates """
    def __init__(self, bot):
        self.bot = bot

    # @bot.event => commands.Cog.listener()
    @commands.Cog.listener()
    async def on_ready(self):   # Para saber se o bot está conectado
        self.curret_time.start()     # Iniciar task 'curret_time'
     
    @tasks.loop(hours=1)
    async def curret_time(self):
        """
        -> Faz o bot executar uma tarefa (exibir data e hora).
        PARÂMETROS:
            self ->
        """
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S")
        channel = self.bot.get_channel(993252657500258437)
        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))
    