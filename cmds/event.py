import discord
from discord.ext import commands
from core.classes import Cog_Extantion

class event(Cog_Extantion):
    @commands.Cog.listener()
    async def on_message(self,msg):       
        if msg.author==self.bot.user:
            return  
        if msg.content.startswith('n'): 
            await msg.channel.send(f'https://nhentai.net/g/{msg.content[1:]}/')
        if msg.content=="hi":
            await msg.channel.send(f"Hi Hi你好{msg.author.display_name}")
        if self.bot.user in msg.mentions:
            await msg.channel.send(f"tag三小{msg.author.display_name}")

    

def setup(bot):
    bot.add_cog(event(bot))