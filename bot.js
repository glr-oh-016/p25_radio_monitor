/*
*   Rewriting it in NodeJS because I want to learn that.
*	
*	This is a discord bot to listen for radio traffic
*	from an RTL-SDR and rebroadcast it on discord.
*
*	NOTE: DON'T PUT THE SECRETS IN THE PUBLIC REPO
*	Depends: @discordjs/opus, ffmpeg,
*
*
*/

// includes
const Discord = require('discord.js');	// discord bot
const fs = require('fs');	// filesystem module, for reading files

// some vars
const client = new Discord.Client();	// create discord clientt

// open config file (add more stuff later on)
const config = require('./config.json');

// notify when ready
client.once('ready', () => {
	console.log('Ready');
});


// login by opening token file
client.login(readFileSync('./token', 'utf8'));

