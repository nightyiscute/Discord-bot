import discord
from discord.ext import commands
from core.classes import Cog_Extantion

class Main(Cog_Extantion):
    @commands.command()
    async def ping(self,ctx): #啟動ping函數
        await ctx.send(f'{round(self.bot.latency*1000)}'"(ms)") #發送延遲毫秒數

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command()
    async def em(self,ctx):
    embed=discord.Embed(title="text", url="https://www.pixiv.net/artworks/100074466", description="好康的", color=0x00ff6e)
    embed.set_author(name="owo", url="https://youtu.be/dQw4w9WgXcQ", icon_url="https://www.pixiv.net/artworks/100074522")
    embed.set_thumbnail(url="https://www.pixiv.net/artworks/100064198")
    embed.add_field(name="11", value="1", inline=False)
    embed.add_field(name="22", value="2", inline=False)
    embed.set_footer(text="dfdfs")
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))

