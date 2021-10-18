import discord
from discord.ext import commands

eavesdropLibrary = ["caleb", "professor", "dumpling", "proffessor", "proffesor"]
summon = "caleb"

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.name != "Bruh-Bot":
			contains = False
			for i in range(0, len(eavesdropLibrary), 1):
				if eavesdropLibrary[i] in message.content.lower():
					contains = True
			if contains == True: #and message.content.lower().startswith("hey "+summon) == False:
				channel = self.bot.get_channel(897979535495155762)
				sender = message.author
				senderName = message.author.nick
				link = message.jump_url
				await channel.send(link+"\n"+str(sender)+"\nAKA "+senderName+":"+"\n\n"+message.content)

def setup(bot):
	bot.add_cog(Events(bot))
