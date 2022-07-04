from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """ Mange The Bot """
    def __init__(self, bot):
        self.bot = bot 

    # @bot.event => commands.Cog.listener()
    @commands.Cog.listener() # Add evento pro bot
    async def on_ready(self):
        print(f"I'm ready! I'm logged in as {self.bot.user}")

    # @bot.event => commands.Cog.listener()
    @commands.Cog.listener() 
    async def on_message(self, message):
        """
        -> Faz o evento de uma mensagem acontecer
        PARÂMETROS:
            self    ->
            message -> Enviar uma mensagem para a função
        """
        if message.author == self.bot.user:
            return

        if "palavrão" in message.content:
            await message.channel.send(f"Por Favor! {message.author}, não ofenda os outros usuários.")
            await message.delete()

    # @bot.event => commands.Cog.listener()
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        -> Faz o evento de uma mensagem acontecer
        PARÂMETROS:
            self  ->
            ctx   -> Saber onde a mensagem foi enviada
            error -> Saber o tipo do erro
        """
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite '!help' para ver os parâmetros de cada comando.")
        elif isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe. Digite '!help' para ver os comandos existêntes.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))