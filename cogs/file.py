import discord
from discord.ext import commands


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.name != "Weezer(;)":
			print()

def setup(bot):
	bot.add_cog(Events(bot))
