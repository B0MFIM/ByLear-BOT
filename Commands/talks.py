import discord
from discord.ext import commands
 
class Talks(commands.Cog):
    """ Talks With User """
    def __init__(self, bot):
        self.bot = bot

    # @bot.command => commands.command()
    @commands.command(name="oi")
    async def send_hello(self, ctx):
        """
        -> Faz a exibição de uma mensagem (Olá, User)
        PARÂMETROS:
            self ->
            ctx  -> Saber onde a mensagem foi enviada
        """
        name = ctx.author.name
        response = "Olá, " + name
        await ctx.send(response)

    # @bot.command => commands.command()
    @commands.command(name="segredo")
    async def secret(self, ctx):
        """
        -> Faz a exibição de uma mensagem privada (segredo)
        PARÂMETROS:
            self ->
            ctx  -> Saber onde a mensagem foi enviada
        """
        try:
            await ctx.author.send("Eu sou lindo!")
            await ctx.author.send("E bolo de maracuja é o melhor que existe!")
        except discord.errors.Forbidden:
            await ctx.send("Erro em enviar o segredo")

def setup(bot):
    bot.add_cog(Talks(bot))