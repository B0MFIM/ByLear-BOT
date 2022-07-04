from discord.ext import commands
 
class Reactions(commands.Cog):
    """ Work With Reactions """
    def __init__(self, bot):
        self.bot = bot

    # @bot.event => commands.Cog.listener()
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """
        -> Faz o bot add um cargo para um usuário (a partir de uma reação).
        PARÂMETROS:
            self     ->
            reaction -> Saber o tipo de reação
            User     -> Saber quem é o User
        """
        if reaction.emoji == "👍":
            role = user.guild.get_role(993299588792451152)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(993299987242942576)
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))