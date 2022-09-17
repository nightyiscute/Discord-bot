import discord
import json
from pixivpy3 import *
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import os
with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

REFRESH_TOKEN="Dv72iY_Mv2vqfcAhSB98x9K_0W85PYOy7h3t9PLe_Aw"
intents=discord.Intents.all()
bot=commands.Bot(command_prefix='!',intents=intents)
tree=bot.tree



def recommend():
    api= AppPixivAPI()
    api.auth(refresh_token=REFRESH_TOKEN)

@tree.command(name='test',description='just text')
async def test(interaction: discord.Interaction):
    """hello!"""
    await interaction.response.send_message('hihi')

@bot.event #觸發事件
async def on_ready(): #啟動on_ready函數
    channel=bot.get_channel(int(jdata['channel_id']))
    await channel.send('機器人上線啦!') #發送訊息
    print("bot上線拉") #在終端發送訊息

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f"cmds.{Filename[:-3]}")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

if __name__=="__main__":
    bot.run(jdata['token'])

