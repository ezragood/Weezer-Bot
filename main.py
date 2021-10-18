import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands
from youtube_dl import YoutubeDL
import datetime as dt
import requests
import json

client = commands.Bot(command_prefix=';', help_command=None)

extensions = ['cogs.comms', 'cogs.events', 'cogs.api', 'cogs.music']

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		client.load_extension(extension)  # Loades every extension.

keep_alive()
client.run('TOKEN')
