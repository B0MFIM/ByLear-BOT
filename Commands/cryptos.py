import requests
from discord.ext import commands
 
class Cryptos(commands.Cog):
    """ Works With Crypto """
    def __init__(self, bot):
        self.bot = bot

    # @bot.command => commands.command()
    @commands.command()
    async def binance(self, ctx, coin, base):
        """
        -> Faz a verificação de um preço na binance. Arg: moeda, base
        PARÂMETROS:
            ctx  -> Saber onde a mensagem foi enviada
            coin -> Moeda utilizada
            base -> Base de conversão
        """
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"[{coin}-{base}]: {float(price):.2f}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido!")
        except Exception as error:
            await ctx.send("Ops... Deu algum erro!")
            print(error)

def setup(bot):
    bot.add_cog(Cryptos(bot))