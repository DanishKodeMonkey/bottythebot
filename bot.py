#Import os to interact across files
import os
#Import discord for vast library of interactive commands with discord bot API
import discord
#import the extended discord library function: commands
from discord.ext import commands

#Import dotenv to mess with "secret" .env files for sensitive stuff like bot tokens. (security)
from dotenv import load_dotenv

#Load the dotenv interaction
load_dotenv()
#Pull token from env file, assign to TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')
#Set intents of the discord bot in accordance with the requirements of the API (defaults work fine for testing)
intents = discord.Intents.default()
#Send message_content request, to allow for interacting with discord through messages.
intents.message_content = True

#Create a commands bot object with intents from above variable, assign to client for easy reference
#bot is an extended subclass of client. Anything client can do, bot can do, and then some.
bot = commands.Bot(command_prefix='£', intents=intents)

#create event, using bot, this listens for somethign to happen..
@bot.event
#define asynchronous function from discord.py, called "on_ready"(), executes when caches from bot are loaded
async def on_ready():
    #When done loading, print this.
    print(f'{bot.user} has arrived, chooms!')
    print(f'I am at {bot.user.name} now!')
    print(f'I am called {bot.user.id}')

#create command event, using bot, this will be evoked using the pre-determined command prefix £
@bot.command()
#define asynchronous functionction called choomtest (to invoke, use £choomtest)
#ctx is required for commands, listens for user, message, etc. Argument is a normal python argument. Singular for now.
# * as second parameter, invokes keyword-only arguments, removing the need to use quotes for multi word arguments.
async def choomkwo(ctx, *, arg):
    #await, when invoked(ctx), send (arg).
    await ctx.send(arg)
    #This will basically just send whatever the user types back to the user.
    #eg: User: £choomtest "Hello friend" ... bot: Hello friend

#Lets try again
@bot.command()
#This time, use *args, for unlimited arguments!
async def choomargs(ctx, *args):
    #Pile all the arguments into a list, divide each argument by ,
    arguments = ', '.join(args)
    #Send the result. first the length of the args tuple(how many?), then type out each argument with a , to seperate them.
    await ctx.send(f'{len(args)} arguments received: {arguments}')

#Lets test some converters this time, botty, lets add some numbers!
@bot.command()
async def choomadd(ctx)


bot.run(TOKEN)