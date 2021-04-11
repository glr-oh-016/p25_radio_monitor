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

# print start message on bot start
@client.event
async def on_ready(): # start when bot is in ready state
	print('Bot is ready')

@client.command()
async def ping(ctx):
	# get latency
	await ctx.send(f'\nPING OHWG-Radio-Monitor (#7044): \nTook {client.latency * 1000}ms to respond.')
	print(f'Responding to ping. Took {client.latency * 1000}ms')

@client.command(aliases=['--help','-h'])
async def get_help(ctx):
	# list all commands
	await ctx.send(
		'\n `.radio` Commands:' +
		'\n```ping   Get ping of bot\nstart   Start receiver\nhalt   Kill process on server running bot.\n-h, --help   View help page```' +
		'\n*Visit https://ben-p.dev/p/ohwg-radio-monitor for full documentation*'
		)
	
	print('Printing help page')

@client.command()
async def halt(ctx):
	await ctx.send('\nExiting. Program restart required on server.')
	print('Exiting')
	exit()


client.run(token.read()) # read the contents of the token file

