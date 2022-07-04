import discord
from discord.ext import commands
 
class Images(commands.Cog):
    """ Work With Images """
    def __init__(self, bot):
        self.bot = bot

    # @bot.command => commands.command()
    @commands.command(name="foto")
    async def get_random_image(self, ctx):
        """
        -> Faz a exibição de uma imagem aleatória
        PARÂMETROS:
            self ->
            ctx  -> Saber onde a mensagem foi enviada
        """
        url_image = "https://picsum.photos/1920/1080"
        embed = discord.Embed(
            title = "Resultado da busca",
            description = "PS: A imagem é aleatória",
            color = 0x0000FF
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name="API", value="Usamos a API do picsum.photos")
        embed.add_field(name="Parâmetros", value="{largura}/{altura}")
        embed.add_field(name="Exemplo", value=url_image,  inline=False)
        embed.set_image(url=url_image)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Images(bot))