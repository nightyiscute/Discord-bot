import discord
from discord.ext import commands
from core.classes import Cog_Extantion


class event(Cog_Extantion): 
    @commands.Cog.listener()
    async def on_message(self,msg):
       
        if msg.content.startswith('n'):
            tmp=msg.content.split("",2)
            if len(tmp)==1:
                await msg.channel.send('hi 你好 你很可愛')
            else:
                await msg.channel.send("https://nhentai.net/g/tmp[1]/")


        





def setup(bot):
    bot.add_cog(event(bot))