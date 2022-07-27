import imp


import discord
from discord.ext import commands
from core.classes import Cog_Extantion

class Main(Cog_Extantion):
    @commands.command()
    async def ping(seif,ctx): #啟動ping函數
        await ctx.send(f'{round(seif.bot.latency*1000)}'"(ms)") #發送延遲毫秒數
def setup(bot):
    bot.add_cog(Main(bot))

