import discord
import random
from keep_alive import keep_alive
from discord.ext import commands
import datetime as dt

#Prefix
client = commands.Bot(command_prefix=';', help_command=None)

class Example2(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def on_command_error(ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			msg = '**Still on cooldown**, please try again in {:.2f}s'. format(error.retry_after)
			await ctx.send(msg)
			
	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def on_ready():
		await commands.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name='with ur mom'))

		
def setup(client):
	client.add_cog(Example2(client))
