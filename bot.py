#!/usr/bin/env python3
#
# REMINDER: DO NOT PUT THE SECRETS ON THE PUBLIC REPO
# 
# This is a discord bot to listen to radio traffic from an RTL-SDR
# and rebroadcast it to discord. 


# imports
import os           # not sure what this is
import discord      # for the bot
from discord.ext import commands	# to use commands to control bot

# variables
client = commands.Bot(command_prefix = '.radio') # the prefix to the command

# get token (make sure token file is added to git ignore)
token = open('token', 'r')


@client.event
async def on_ready(): # start when bot is in ready state
	print('Bot is ready')

client.run(token.read()) # read the contents of the token file