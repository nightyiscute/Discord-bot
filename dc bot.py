import asyncio
import discord
import json
from pixivpy3 import *
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import os

global jdata
with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

REFRESH_TOKEN="Dv72iY_Mv2vqfcAhSB98x9K_0W85PYOy7h3t9PLe_Aw"
intents=discord.Intents.all()
bot=commands.Bot(command_prefix='!',intents=intents)
tree=bot.tree



def recommend():
    api= AppPixivAPI()
    api.auth(refresh_token=REFRESH_TOKEN)

# @tree.command(name='test',description='just text')
# async def test(interaction: discord.Interaction):
#     """hello!"""
#     await interaction.response.send_message('hihi')

@bot.event #發送啟動訊息
async def on_ready(): 
    channel=bot.get_channel(int(jdata['channel_id']))
    await channel.send('機器人上線啦!') #發送訊息
    print("bot上線拉") #在終端發送訊息

@bot.command() #載入檔案
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command() #卸載檔案
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command() #重載檔案
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')
    
if os.system("git pull")==0:
    async def reload(ctx,extension):
        bot.reload_extension(f'cmds.{extension}')
    
async def main(): #啟用Cog
    async with bot:
        for Filename in os.listdir('./cmds'):
            if Filename.endswith('.py'):
                await bot.load_extension(f"cmds.{Filename[:-3]}")

        await bot.start(jdata['token'])


if __name__=="__main__": #啟動bot
    asyncio.run(main())

