#!/usr/bin/env python3
#
# NOTE: DO NOT PUT THE SECRETS ON THE PUBLIC REPO
# 
# This is a discord bot to listen to radio traffic from an RTL-SDR
# and rebroadcast it to discord. 
#
# NOTE:
# You will need a file named 'token' with 
# your token in the same directory of the bot

# version number
VERSION = '0.0.1'


# imports
import os           # not sure what this is
import discord      # for the bot
from discord.ext import commands	# to use commands to control bot

# variables
client = commands.Bot(command_prefix = '.radio ') # the prefix to the command

# get token (make sure token file is added to git ignore)
token = open('token', 'r')

# COMMANDS:

# print start message on bot start
@client.event
async def on_ready(): # start when bot is in ready state
	print('Bot is ready')

# get bot latency
@client.command()
async def ping(ctx):
	# get latency
	await ctx.send(f'\nPING OHWG-Radio-Monitor (#7044): \nTook {client.latency * 1000}ms to respond.')
	print(f'Responding to ping. Took {client.latency * 1000}ms')

# print basic manpage
@client.command(aliases=['--help','-h'])
async def get_help(ctx):
	# list all commands
	await ctx.send(
		'\n `.radio` Commands:' +
		'\n```connect        Connect to your current voice channel. ' +
		'\ndisconnect     Leave currently connected voice channel' +
		'\nping           Get ping of bot' +
		'\nchannel        Set channel of radio' +
		'\nstart          Start receiver' + 
		'\nhalt           Kill process on server running bot.' +
		'\n-h, --help     View help page```' +
		'\n-v, --version' +
		'\n*Visit https://ben-p.dev/p/ohwg-radio-monitor for full documentation*'
		)
	
	print('Printing help page')

# kill bot
@client.command()
async def halt(ctx):
	await ctx.send('\nExiting. Program restart required on server.')
	print('Exiting')
	exit()

# set zone of radio
#@client.command()
#async def zone(ctx, arg):
#	# add stuff to send command to set radio zone
#	await ctx.send(f'Setting zone to {arg}')

# set channel of radio
@client.command()
async def channel(ctx, arg):
	# add stuff to set radio channel
	await ctx.send(f'Setting channel to {arg}')

@client.command()
async def version(ctx):
	await ctx.send(f'Radio Monitor Version {version}')

# connect to VC
@client.command(pass_context = True)
async def connect(ctx):
	
	if (ctx.author.voice):
		# connect to channel
		channel = ctx.message.author.voice.channel
		await channel.connect()
		# logging
		await ctx.send(f'Connecting to channel {channel}')
		print(f'Connecting to VC.')
	
	else:
		await ctx.send('Unable to connect. Are you connected to a VC?')
		print(f'Unable to connect to VC')
		

# disconnecting from VC
@client.command(pass_context = True)
async def disconnect(ctx):
	
	if (ctx.voice_client):
		await ctx.guild.voice_client.disconnect()
		await ctx.send('Leaving VC')

	else:
		await ctx.send('No VC to leave')


# run the bot
client.run(token.read()) # read the contents of the token file

