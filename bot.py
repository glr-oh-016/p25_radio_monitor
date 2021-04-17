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
#
# TODO: Add audio functionality, logging, squelch control.
#

# version number
VERSION = '0.0.1'

# imports
import os           # not sure what this is
import discord      # for the bot
from discord.ext import commands	# to use commands to control bot
from sultan.api import Sultan		# run commands to start p25 decoder
import datetime		# for logging

# variables
client = commands.Bot(command_prefix = '.radio ') # the prefix to the command

# welcome message
print(f'OHWG-Radio-Monitor V.{VERSION}')

# COMMANDS:

# print start message on bot start
@client.event
async def on_ready(): # start when bot is in ready state
	print('Ready \n')


# get bot latency
@client.command(aliases=['--get-latency','--ping','-p'])
async def ping(ctx, arg):
	
	# get latency
	await ctx.send(f'\n PING OHWG-Radio-Monitor (#7044):')
	
	# TODO" Add stuff to catch wrong datatype
	#TYPE_ERROR_DIALOG = 'TypeError: Please enter an integer.'
	#SYNTAX_ERROR_DIALOG = 'SyntaxError: Check Formatting.'

	latency = f' latency={round(client.latency * 1000)}ms'

	for i in range(int(arg)):
		print(latency) # also printing to console
		await ctx.send(f'try={str(i) + latency}')


# print basic manpage
@client.command(aliases=['--help','-h'])
async def get_help(ctx):
	
	# list all commands
	await ctx.send(open('help.md','r').read())
	print('Printing help page')


# kill bot
@client.command(aliases=['-H', '--halt'])
async def halt(ctx):
	
	await ctx.send('\nExiting. Program restart required on server.')
	print('Exiting')
	exit()

# set channel of radio
@client.command()
async def channel(ctx, arg):
	
	# TODO: Add stuff to send frequency change to op25
	await ctx.send(f'\nSetting channel to {arg}')


@client.command(aliases=['-v','--version'])
async def version(ctx):
	await ctx.send(VERSION)


# connect to VC
@client.command(aliases=['-c', '--connect'], pass_context = True)
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
@client.command(aliases=['-D','--disconnect'], pass_context = True)
async def disconnect(ctx):
	
	if (ctx.voice_client):
		# if connected, don't be
		await ctx.guild.voice_client.disconnect()
		await ctx.send('Leaving VC')

	else:
		await ctx.send('No VC to leave')


# run the bot
client.run(open('token', 'r').read()) # read the contents of the token file