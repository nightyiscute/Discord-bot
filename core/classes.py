from lib2to3.pgen2.grammar import opmap
import discord
from discord.ext import commands
from core.classes import Cog_Extantion

class event(Cog_Extantion):
class Cog_Extantion(commands.Cog):
    def __init__(self,bot):
        self.bot=bot