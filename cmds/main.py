import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import datetime


class Main(Cog_Extantion):
    @commands.command()
    async def ping(self,ctx): #啟動ping函數
        await ctx.send(f'{round(self.bot.latency*1000)}'"(ms)") #發送延遲毫秒數

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command()
    async def my(self,ctx):
        embed=discord.Embed(title=f"{ctx.author.display_name}", url="https://youtu.be/dQw4w9WgXcQ", description="好康的", color=0x00ff6e,timestamp=datetime.datetime.now())
        embed.set_author(name="Information")
        embed.add_field(name="11", value="1", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="22", value="2", inline=False)
        embed.set_footer(text=f"{ctx.author.display_name}寫於")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))

