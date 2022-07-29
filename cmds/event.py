import discord
from discord.ext import commands
from core.classes import Cog_Extantion


class event(Cog_Extantion): 
    @commands.Cog.listener()
    async def on_message(self,*msg,):
        if msg.author==self.bot.user:
                return
        if msg.content.startswith('n'): 
            await msg.channel.send(f'https://nhentai.net/g/{msg}/')
            
                


        





def setup(bot):
    bot.add_cog(event(bot))