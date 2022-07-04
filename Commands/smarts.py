from discord.ext import commands
 
class Smarts(commands.Cog):
    """ A Lot Of Smart Commands """
    def __init__(self, bot):
        self.bot = bot

    # @bot.command => commands.command()
    @commands.command(name="calcular")
    async def calculate_expression(self, ctx, *expression):
        """
        -> Faz o calculo de uma expressão qualquer. Arg: expressão
        PARÂMETROS:
            self        ->
            ctx         -> Saber onde a mensagem foi enviada
            expression  -> Calcula a expressão inserida
        """
        expression = "".join(expression)
        response = eval(expression)  # eval() - tomar cuidado com esta função, procurar não utiliza-la
        await ctx.send("Resposta: " +  str(response))

def setup(bot):
    bot.add_cog(Smarts(bot))