#discord bot made by pb2 diamond
#diamond pb2 - youtube
#@pb2 diamond#1544 - discord
 
##IMPORTS##
import discord                      #MAKE SURE YOU DO "py -m pip install discord" IN COMMAND PROMPT!
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
import random
 
##PREFIX##
bot = commands.Bot(command_prefix='pg!')

##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Execute Commands")
    print ("Logged In As")
    print (bot.user.name)
    print (bot.user.id)
    await bot.change_presence(game=discord.Game(name='pg!_help'))
 
##COMMAND##
@bot.command(pass_context=True)
async def _help(ctx): 
    if True:
        await bot.say(" ``help:\n pg!nou\n _pg!givecookie\n`` ") #NOTE - you need the \n (new lines)
        print("Command [_Help] Has Been Called")
        
##COMMAND##
@bot.command(pass_context=True)
async def givecookie(ctx):
    if True:
        userMention = discord.user.mention
        await bot.say("You Gave <@%s> A Cookie!\n" % (userMention)) #NOTE - you need the \n (new lines)
        print("Command [Givecookie] Has Been Called")

##COMMAND##
@bot.command(pass_context=True)
async def nou(ctx):
    if True:
        await bot.say(" **NOU!** ")#NOTE - you need the \n (new lines)
        print("Command [Nou] Has Been Called")

##COMMAND##
@bot.command(past_context=True)
async def yesu(ctx):
    if True:
        await bot.say(" **YESU!** ")
        print("Command [Yesu] Has Been Called")
 
#TOKEN
bot.run(process.env.BOT_TOKEN)
