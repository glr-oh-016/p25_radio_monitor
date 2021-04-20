```
.radio(1)       GENERAL COMMANDS MANUAL

NAME
    .radio - a Discord bot to monitor P25 radio.

SYNOPSIS
    .radio [<command>] [<args>]

DESCRIPTION
    .radio is a Discord bot, written in Python, to monitor 
    P25-encoded radio traffic, for Ohio Wing Civil Air
    Patrol's Emergency Services.

    .radio works by receiving the signal with an RTL-SDR,
    connected to a Raspberry Pi, then streaming the 
    raw signal with rtl_tcp to a server, which decodes
    the P25 to audio, and steams it to Discord.

COMMANDS

  connect        Connect to your current voice channel.

  disconnect     Leave currently connected voice channel

  ping           Get latency of the bot. To run multiple,
                 append an integer with that value.

  channel        Sets radio channel. Zones will be
                 automatically selected. Append the
                 channel name as a string.

  start          Start receiver

  halt           Kill process on server running bot.

  help           View help page

  version        Show version

```