import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
from collections                import Counter


command_prefix = "p!" #CHANGE IT TO WHAT YOU WANT
description = "Pokéberry🍓" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()

gym = [385419569558323202, 307219837648764928, 220231135949619200, 349989345714896906, 247166156467732482, 333204266309255168]
pewter = []
cerulean = []
vermilion = []
celadon = []
fuschia = []
saffron = []
cinnabar = []
viridian = []
violet = [220231135949619200]
azalea = []
goldenrod = []
ecruteak = [247166156467732482]
cianwood = []
olivine = [307219837648764928]
mahogany = []
blackthorn = []
laverre = [385419569558323202]

pewter2 = [385419569558323202, 307219837648764928]
cerulean2 = [385419569558323202, 307219837648764928]
vermilion2 = [385419569558323202, 307219837648764928]
celadon2 = [385419569558323202, 307219837648764928]
fuschia2 = [385419569558323202, 307219837648764928]
saffron2 = [385419569558323202, 307219837648764928]
cinnabar2 = [385419569558323202, 307219837648764928]
viridian2 = [385419569558323202, 307219837648764928]
violet2 = [385419569558323202, 307219837648764928]
azalea2 = [385419569558323202, 307219837648764928]
goldenrod2 = [385419569558323202, 307219837648764928]
ecruteak2 = [385419569558323202, 307219837648764928]
cianwood2 = [385419569558323202, 307219837648764928]
olivine2 = [385419569558323202, 307219837648764928]
mahogany2 = [385419569558323202, 307219837648764928]
blackthorn2 = [385419569558323202, 307219837648764928]
laverre2 = [385419569558323202, 307219837648764928]

elite = [220231135949619200, 247166156467732482, 333204266309255168, 349989345714896906] 
elitelead = [385419569558323202] 

started = [385419569558323202]
master = [385419569558323202]
comp = [385419569558323202] 
	
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

###################################################################################
###################################################################################
###																				###
###																				###
###								   HELP COMMAND									###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['cmds', 'commands'], description = 'Sends a message with commands in DM')
async def help(ctx):

	developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xA522B3))
	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, icon_url = avi)
	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Pokéberry🍓** <:bot:389862148395761664> \nI started making that bot in <:pythonbot:392172368023388160> but I'm also a web designer & designer. \nI wanted to make this BOT because for each arenas we need to get a badge if we complete it."
	embed.add_field(name="Having Issues/Problems?", value=f"If you have any problems with **Pokéberry🍓** <:bot:389862148395761664>,\njust contact the Bot Developper **{developer.name}**", inline=False)

	help1 = discord.Embed(colour = discord.Colour(0xA522B3))
	help1.title = f"Pokéberry🍓  Commands List🍓"
	help1.description = f"**Pokéberry🍓** <:bot:389862148395761664>'s prefix is **p.**\nNeed more informations about a command? `p.help [command]`\n\n"
	help1.add_field(name="Core Commands", value="`p.help` **|** `p.setgame`", inline=False)
	help1.add_field(name="Utility Commands", value="`p.ping` **|** `p.badges` **|** `p.about` **|** `p.stats` **|** `p.complete`", inline=False)
	help1.add_field(name="Fun Commands", value="`p.snowball` **|** `p.sb`", inline=False)
	help1.set_footer(text = "Have fun using Pokéberry🍓")

	await ctx.send(embed = embed)
	await ctx.send(embed = help1)

###################################################################################
###################################################################################
###																				###
###																				###
###								   OWNER COMMAND								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['creator', 'dev', 'developer'], description = 'Who is my creator?')
async def owner(ctx):

	developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xA522B3))

	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, icon_url = avi)

	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Pokéberry🍓** <:bot:389862148395761664> \nI started making that bot in <:pythonbot:392172368023388160> but I'm also a web designer & designer. \nI wanted to make this BOT because for each arenas we need to get a badge if we complete it."

	await ctx.send(embed = embed)

###################################################################################
###################################################################################
###																				###
###																				###
###								   PING COMMAND									###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['ms'])
async def ping(ctx):
		pingms = "{}".format(int(bot.latency * 1000)) #MS
		pings = "{}".format(int(bot.latency * 1)) #S

		ping1 = discord.Embed(colour = discord.Colour(0xA522B3))
		ping1.description = f"My latency is actually **{pings}s** | **{pingms}ms**."
		ping1.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p"))
		await ctx.send(embed = ping1)

###################################################################################
###################################################################################
###																				###
###																				###
###								     GAME GROUP   								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.group()
async def game(self):

	if game == None:
		await self.send(f"Please use one of the following settings: `default`, `playing`, `streaming`, `watching`, `listenning` or `clear`")

@game.command(name = 'playing')
async def game_playing(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Playing **{game}**'")

@game.command(name = 'streaming')
async def game_streaming(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, url = "https://www.twitch.tv/spiritprod", type = 1))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Streaming **{game}**'")

@game.command(name = 'listenning')
async def game_listning(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 2))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Listenning to **{game}**'")

@game.command(name = 'watching')
async def game_watching(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 3))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Watching **{game}**'")

@game.command(name = 'default')
async def game_default(self):

	bot_prefix = "st"
	server = self.guild

	await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Default'")

	games = [f"Use {bot_prefix}help for help!", f"{sum(1 for _ in self.bot.get_all_members())} users | {len(self.bot.guilds)} servers", f"Wanna invite {self.bot.user.name}? Use: {bot_prefix}inv", f"Give us feedback? Use: {bot_prefix}feedback [message]"]
	current_number = 0
	while True:
		if current_number == len(games):
			current_number = 0
		await self.bot.change_presence(game=discord.Game(name = games[current_number], url = "https://www.twitch.tv/spiritprod", type = 1))
		await asyncio.sleep(20)
		current_number += 1

@game.command(name = 'clear')
async def game_clear(self, *, game = None):
	await self.bot.change_presence(game=discord.Game(name = None))
	await self.send(f"Cleared the status of **{self.bot.user.name}**")

###################################################################################
###################################################################################
###																				###
###																				###
###								    GYM COMPLETE   								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command()
async def complete(ctx, *, member : discord.Member=None):

	author = ctx.message.author.mention
	author2 = ctx.author
	mention = member.mention

	if not member:
		await ctx.send(f"Please **mention** the person who **reached/finished** your gym !")

	else:
		if author2.id in gym:
			if author2.id in pewter:
				pewter2.append(member.id)
			elif author2.id in cerulean:
				cerulean2.append(member.id)
			elif author2.id in vermilion:
				vermilion2.append(member.id)
			elif author2.id in celadon:
				celadon2.append(member.id)
			elif author2.id in fuschia:
				fuschia2.append(member.id)
			elif author2.id in saffron:
				saffron2.append(member.id)
			elif author2.id in cinnabar:
				cinnabar2.append(member.id)
			elif author2.id in viridian:
				viridian2.append(member.id)
			elif author2.id in violet:
				violet2.append(member.id)
			elif author2.id in azalea:
				azalea2.append(member.id)
			elif author2.id in goldenrod:
				goldenrod2.append(member.id)
			elif author2.id in ecruteak:
				ecruteak2.append(member.id)
			elif author2.id in cianwood:
				cianwood2.append(member.id)
			elif author2.id in olivine:
				olivine2.append(member.id)
			elif author2.id in mahogany:
				mahogany2.append(member.id)
			elif author2.id in blackthorn:
				blackthorn2.append(member.id)
			elif author2.id in laverre:
				laverre2.append(member.id)
			else:
				return

			embed = discord.Embed(colour = discord.Colour(0xA522B3))
			embed.description = f"{mention} now have your **gym badge** for reaching/finishing your gym!"
			await ctx.send(embed = embed)

		else:
			await ctx.send(f"You aren't a **Gym Leader**, {author} !")

###################################################################################
###################################################################################
###																				###
###																				###
###								   LEAGUE ACCESS  								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['league', 'access', 'la', 'al'])
async def leagueaccess(ctx, *, member: discord.Member = None):

	guild = ctx.guild
	author = ctx.message.author.mention
	author2 = ctx.author
	role = discord.utils.get(guild.roles, name='League Access')

	if author2.id in laverre2:
		started.append(author2.id)
		await member.add_roles(role)

###################################################################################

@bot.command(aliases = ['master', "mf", "fm"])
async def masterfight(ctx, *, member: discord.Member = None):

	author = ctx.message.author.mention
	author2 = ctx.author

	if author2.id in elitelead:
		master.append(member.id)

###################################################################################

@bot.command(aliases = ['comp', 'leaguec', 'cleague'])
async def leaguecompleted(ctx, *, member: discord.Member = None):

	author = ctx.message.author.mention
	author2 = ctx.author

	if author2.id in elitelead:
		comp.append(member.id)

###################################################################################
###################################################################################
###																				###
###																				###
###								   BADGES COMMAND  								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['badge', 'profile'])
async def badges(ctx, *, member: discord.Member = None):

	e = discord.Embed(colour = discord.Colour(0xA522B3))
	
	if member is None:
		member = ctx.author

	if member.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
	else:
		avi = member.avatar_url

	if avi:
		e.set_thumbnail(url = avi)
		e.set_author(name = str(member), icon_url = avi)
	else:
		e.set_thumbnail(url = member.default_avatar_url)
		e.set_author(name = str(member), icon_url = member.default_avatar_url)

	features = "ㅤㅤ"
	features1 = "ㅤㅤ"
	features2 = "ㅤㅤ"
	features3 = "ㅤㅤ"
	features4 = "ㅤㅤ"
	features5 = "ㅤㅤ"
	features6 = "ㅤㅤ"
	features7 = "ㅤㅤ"
	features8 = "ㅤㅤ"
	features9 = "ㅤㅤ"
	features10 = "ㅤㅤ"
	features11 = "ㅤㅤ"
	features12 = "ㅤㅤ"
	features13 = "ㅤㅤ"
	features14 = "ㅤㅤ"
	features15 = "ㅤㅤ"
	features16 = "ㅤㅤ"
	features17 = "ㅤㅤ"

	if member.id in gym:
		if member.id in elite:
			if member.id in elitelead:
				features17 = "Lead"
			else:
				features17 = "Elite"
		elif member.id in elitelead:
			features17 = "Lead"
		else:
			features17 = "Gym"

	if member.id in pewter2:
		features = "<:Pewter:449610408060518410>"
		if member.id in cerulean2:
			features1 = "<:Cerulean:449610403178217491>"
			if member.id in vermilion2:
				features2 = "<:Vermilion:449610409692102666>"
				if member.id in celadon2:
					features3 = "<:Celadon:449610403266297859>"
					if member.id in fuschia2:
						features4 = "<:Fuchsia:449610407347355659>"
						if member.id in fuschia2:
							features4 = "<:Fuchsia:449610407347355659>"
							if member.id in saffron2:
								features5 = "<:Saffron:449610409637576714>"
								if member.id in cinnabar2:
									features6 = "<:Cinnabar:449610408177958914>"
									if member.id in viridian2:
										features7 = "<:Viridian:449610409549365248> "
										if member.id in violet2:
											features8 = "<:Violet:449610409755017216>"
											if member.id in azalea2:
												features9 = "<:Azalea:449610403782066177>"
												if member.id in goldenrod2:
													features10 = "<:Goldenrod:449610409364684800>"
													if member.id in ecruteak2:
														features11 = "<:Ecruteak:449610409138454542>"
														if member.id in cianwood2:
															features12 = "<:Cianwood:449610404566401035>"
															if member.id in olivine2:
																features13 = "<:Olivine:449610409528393728>"
																if member.id in mahogany2:
																	features14 = "<:Mahogany:449610411260772362>"
																	if member.id in blackthorn2:
																		features15 = "<:Blackthorn:449610403987849216>"
																		if member.id in laverre2:
																			features16 = "<:Laverre:449610407422722069>"
																		else:
																			features = "ㅤㅤ"
																			features1 = "ㅤㅤ"
																			features2 = "ㅤㅤ"
																			features3 = "ㅤㅤ"
																			features4 = "ㅤㅤ"
																			features5 = "ㅤㅤ"
																			features6 = "ㅤㅤ"
																			features7 = "ㅤㅤ"
																			features8 = "ㅤㅤ"
																			features9 = "ㅤㅤ"
																			features10 = "ㅤㅤ"
																			features11 = "ㅤㅤ"
																			features12 = "ㅤㅤ"
																			features13 = "ㅤㅤ"
																			features14 = "ㅤㅤ"
																			features15 = "ㅤㅤ"
																			features16 = "ㅤㅤ"
	b1 = "ㅤ"
	b2 = "ㅤ"
	league = "ㅤ"

	if member.id in laverre2:
		b1 = "No Badges Left!"
		b2 = "You can access the League."
	else:
		b1 = "Badges Left"
		if member.id in pewter2:
			b2 = "16 badges left"
			if member.id in cerulean2:
				b2 = "15 badges left"
				if member.id in vermilion2:
					b2 = "14 badges left"
					if member.id in celadon2:
						b2 = "13 badges left"
						if member.id in fuschia2:
							b2 = "12 badges left"
							if member.id in saffron2:
								b2 = "11 badges left"
								if member.id in cinnabar2:
									b2 = "10 badges left"
									if member.id in viridian2:
										b2 = "9 badges left"
										if member.id in violet2:
											b2 = "8 badges left"
											if member.id in azalea2:
												b2 = "7 badges left"
												if member.id in goldenrod2:
													b2 = "6 badges left"
													if member.id in ecruteak2:
														b2 = "5 badges left"
														if member.id in cianwood2:
															b2 = "4 badges left"
															if member.id in olivine2:
																b2 = "3 badges left"
																if member.id in mahogany2:
																	b2 = "2 badges left"
																	if member.id in blackthorn2:
																		b2 = "1 badge left"

	if member.id in laverre2:
		league = "<:Didnt_Start:449628615999488000>"
		if member.id in started:
			league = "<:Elite_4_Fight:449629015872110592>"
			if member.id in master:
				league = "<:Elite_Master_Fight:449628615156564015>"
				if member.id in comp:
					league = "<:Completed:449628616284831744>"


	e.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y at %H:%M:%S')}")#.timestamp = member.joined_at
	e.add_field(name = 'Account created at', value = member.created_at.__format__('Date: **%d %b %Y**\nTime: **%H:%M:%S**\nㅤ'))
	e.add_field(name = 'User ID', value = member.id)
	e.add_field(name = b1, value = b2, inline=True)
	e.add_field(name = "League Status", value = league)
	e.add_field(name = 'Pokébadges', value = f"{features}ㅤ{features1}ㅤ{features2}ㅤ{features3}ㅤ{features4}ㅤ{features5}\n\n{features6}ㅤ{features7}ㅤ{features8}ㅤ{features9}ㅤ{features10}ㅤ{features11}\n\n{features12}ㅤ{features13}ㅤ{features14}ㅤ{features15}ㅤ{features16}", inline = True)

	await ctx.send(embed=e)

###################################################################################

if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))

#https://discordapp.com/oauth2/authorize/?permissions=2138569983&scope=bot&client_id=448885364275281931
