import discord
import random
from discord.ext import commands

  #Variables

school_Ment = ['<@!653413227010457631>', '<@!794617743453454336>', '<@!336547516336177153>', '<@!398277901101039616>', '<@!257005783307255809>', '<@!415624580087021569>', '<@!483377420494176258>', '<@!550613223733329920>', '<@!736888501026422855>', '<@!760888900435574784>', '<@!680602751109169213>', '<@!735317122896494684>', '<@!686736631532748805>', '<@!797880128209289237>', '<@!755529010250907738>', '<@!473889399289937923>', '<@!747988511902269460>', '<@!475406418976047105>', '<@!554435790046887947>', '<@!571716049867898900>', '<@!467405918842126358>', '<@!616003943427735569>', '<@!797988425415393300>', '<@!720673212354265168>', '<@!705974178565849141>', '<@!752997627347599432>', '<@!366638134592667648>', '<@!694576336466870302>', '<@!789292431963193345>', '<@!675803459592650822>', '<@!727992775966064761>', '<@!750033837769097227>', '<@!576606819234086914>', '<@!721105326098612265>', '<@!745613767190118463>']

Random = [
  'a drop of water', 'chanclas', 'jellyfish go BRRRRR', '3 dots', 'bat discloses', "quack https://imgur.com/gallery/PwN6Jw5", "no u", "sus amogus", "joe... joe mama xd", "why should i give u rand??", "your gay", "bruh"]

  #Thingy
class Commands(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

  #Events
	@commands.Cog.listener()
	async def on_ready(self):
		print('Weezer is up and running!')

  #Commands
	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def test(ctx):
		await ctx.channel.send("Test Complete")

	@commands.command()
	async def ping(self, ctx):
		await ctx.send("pong")

	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def gayrate(self, ctx):
		embed=discord.Embed(title="***Gay r8***", color=discord.Color.blue())
		
		rand_ = random.randint(1, 100)
		if ctx.author.name == "Professor Dumpling":
			rand_ = 0

		embed.add_field(name= f"{ctx.author.name} you are {rand_}% gay :gay_pride_flag:", value=f"{rand_}% gay?? dang.")
		await ctx.channel.send(embed=embed)

	@commands.command()
	async def Ppsize(self, ctx):
		ctx.channel.send(ctx.author.name)
		if ctx.author.name == "Professor Dumpling" or ctx.author.name == "erodecode":
			for i in range(0, 20, 1):
				if i == 0:
					await ctx.channel.send("8=================================================")
				elif i == 19:
					await ctx.channel.send("=================================================D")
				else:
					await ctx.channel.send("==================================================")

	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def ppsize(self, ctx):
		if ctx.author.name != "Professor Dumpling":
			embed=discord.Embed(title="***PP Size***", color=discord.Color.blue())
			
			rand_ = random.randint(0, 10)

			if ctx.author.name == "erodecode":
				rand_ = 10

			penis = ""
			for i in range(0,rand_,1):
				penis = penis+"="
			penis = "8"+penis+"D"

			embed.add_field(name= f"{ctx.author.name}s' pp is {penis} long", value="bruh")
			await ctx.channel.send(embed=embed)

	@commands.command()
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def bsmeter(self, ctx):
		embed=discord.Embed(title="***Bullshit Rate***", color=discord.Color.blue())
		
		bs_perc = random.randint(0, 100)

		if ctx.author.name == "Professor Dumpling":
			bs_perc = 100

		embed.add_field(name= f"Thats {bs_perc}% bullshit. :poop:", value="Bruh")
		await ctx.channel.send(embed=embed)

	'''@client.command()
	@commands.cooldown(1,86400, commands.BucketType.user)
	@client.has_role("Bot access")
	async def rand_m(ctx):
		await ctx.channel.send(random.choice(school_Ment))'''

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def rand(self, ctx):
		await ctx.channel.send(random.choice(Random))

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def ded(self, ctx):
		await ctx.channel.send("stfu im awake")

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def corner(self, ctx):
		await ctx.channel.send("https://imgur.com/gallery/jIEZZbJ")

	@commands.command()
	@commands.cooldown(1,5, commands.BucketType.user)
	async def gibadmin(ctx):
		await ctx.channel.send("you are now admin")

	@commands.command(pass_context=False)
	async def giverole(self, ctx, user: discord.Member, role: discord.Role):
			await user.add_roles(role)
			await ctx.send(f"hey {ctx.author.name}, {user.name} has been given a role called: {role.name}")

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def pizza(self, ctx):
		await ctx.channel.send("https://imgur.com/gallery/OUOwFru")

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def bby(self, ctx):
		await ctx.channel.send("stfu "+ ctx.author.mention+ " u stinky bby")

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def uwu(self, ctx):
		await ctx.channel.send("uwu :3 u so poggy woggy "+ ctx.author.mention)

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def L(self, ctx):
		await ctx.channel.send("<@!653413227010457631> go die in a hole")

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def shut(ctx):
		await ctx.channel.send("no u")


	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def help(self, ctx):

		embed=discord.Embed(title="***OPTIONS***", description="help for "+ ctx.author.mention, color=discord.Color.blue())

		embed.add_field(name="**NOTE - MOST OPTIONS MAY NOT BE AVAILIBLE RIGHT NOW**", value=None)

		embed.add_field(name="Prefix - ;", value="Use this in front of any command", inline=False)

		embed.add_field(name="**-Commands-**", value="All commands are lowercase")

		embed.add_field(name="*;rand*", value="speshal serpryse :>")

		embed.add_field(name="*;corner*", value="shows very sayisfying gif")

		#embed.add_field(name="*$i got kids*", value="threatens u >:)")

		embed.add_field(name="*;pizza*", value="delicious! :p")

		embed.add_field(name=";L", value="Threatens cameron :)")

		embed.add_field(name=";uwu", value="pog")

		embed.add_field(name=";bby", value=".")

		embed.add_field(name=";rand_m", value="Mention someone random :)")

		await ctx.channel.send(embed=embed)

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def abtme(self, ctx):
		embed=discord.Embed(title="***About You***", description="haha i have ur info", color=discord.Color.red())
		embed.add_field(name= "Username - "+ ctx.author.name+ "#"+ ctx.author.discriminator, value= "-----------------------------------")
		embed.add_field(name="Profile Picture - "+ ctx.author.avatar_url, value="-----------------------------------")
		await ctx.channel.send(embed=embed)

	@commands.command(name='avatar', help='fetch avatar of a user')
	@commands.cooldown(1,5, commands.BucketType.user)
	async def dp(self, ctx, *, member: discord.Member = None):
		if ctx.content == "av":
				if not member:
						member = ctx.message.author
				userAvatar = member.avatar_url
				await ctx.send(userAvatar)

	@commands.command()
	@commands.cooldown(1,10, commands.BucketType.user)
	async def randw(self, ctx):
		with open('ewitel.txt') as a:
				wordList = a.readlines()
				response = random.choice(wordList)
				await ctx.channel.send(f"1 word in the english dictionary: {response} - u stupid if u dont know what this means")

	@commands.command()
	async def on_cmd_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
					await ctx.send('Please pass in all requirements :rolling_eyes:.')
			if isinstance(error, commands.MissingPermissions):
					await ctx.send("You dont have all the requirements :laughing:")

	@commands.command()
	async def kick(self, ctx, member:discord.User=None, reason=None):
		if ctx.author.name == "erodecode" or "Professor Dumpling":
			if member == None or member == ctx.message.author:
					await ctx.channel.send("shithead tryna ban himself, smh")
					return
			if reason == None:
					reason = 'being naughty boy'
			message = f"You have been kicked from {ctx.guild.name} for {reason}"
			await member.send(message)
			await ctx.guild.kick(member, reason = reason)
			await ctx.channel.send(f'Kicked {member} for {reason}')
      

	@commands.command()
	async def ban(self, ctx, member:discord.User=None, reason =None):
			if member == None or member == ctx.message.author:
					await ctx.channel.send("shithead tryna ban himself, smh")
					return
			if reason == None:
					reason = 'for being bad'
			message = f"You have been banned from {ctx.guild.name} for {reason}"
			await member.send(message)
			await ctx.guild.ban(member, reason = reason)
			await ctx.channel.send(f'banned {member} for {reason}')


def setup(bot: commands.Bot):
  bot.add_cog(Commands(bot))
