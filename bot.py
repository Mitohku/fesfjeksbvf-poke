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

gym = [385419569558323202, 307219837648764928, 220231135949619200, 349989345714896906, 247166156467732482, 333204266309255168, 186195192301223936]
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

pewter2 = [385419569558323202, 307219837648764928, 332892224738295808]
cerulean2 = [385419569558323202, 307219837648764928, 332892224738295808]
vermilion2 = [385419569558323202, 307219837648764928, 332892224738295808]
celadon2 = [385419569558323202, 307219837648764928, 332892224738295808]
fuschia2 = [385419569558323202, 307219837648764928, 332892224738295808]
saffron2 = [385419569558323202, 307219837648764928, 332892224738295808]
cinnabar2 = [385419569558323202, 307219837648764928, 332892224738295808]
viridian2 = [385419569558323202, 307219837648764928, 332892224738295808]
violet2 = [385419569558323202, 307219837648764928, 332892224738295808]
azalea2 = [385419569558323202, 307219837648764928, 332892224738295808]
goldenrod2 = [385419569558323202, 307219837648764928, 332892224738295808]
ecruteak2 = [385419569558323202, 307219837648764928, 332892224738295808]
cianwood2 = [385419569558323202, 307219837648764928, 332892224738295808]
olivine2 = [385419569558323202, 307219837648764928, 332892224738295808]
mahogany2 = [385419569558323202, 307219837648764928, 332892224738295808]
blackthorn2 = [385419569558323202, 307219837648764928, 332892224738295808]
laverre2 = [385419569558323202, 307219837648764928, 332892224738295808]

elite = [220231135949619200, 247166156467732482, 333204266309255168, 349989345714896906] 
elitelead = [385419569558323202] 

started = [385419569558323202, 332892224738295808]
master = [385419569558323202, 332892224738295808]
comp = [385419569558323202, 332892224738295808] 
	
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
async def helpme(ctx):

	developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xA522B3))
	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, icon_url = avi)
	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Pokéberry🍓** <:bot:453635744960086026> \nI started making that bot in <:Python:453634265197051934> but I'm also a web designer & designer. \nI wanted to make this BOT because for each arenas we need to get a badge if we complete it."
	embed.add_field(name="Having Issues/Problems?", value=f"If you have any problems with **Pokéberry🍓** <:bot:453635744960086026>,\njust contact the Bot Developper **{developer.name}**", inline=False)

	help1 = discord.Embed(colour = discord.Colour(0xA522B3))
	help1.title = f"Pokéberry🍓  Commands List"
	help1.description = f"**Pokéberry🍓** <:bot:453635744960086026>'s prefix is **p!**\nNeed more informations about a command? `p!help [command]`\n\n"
	help1.add_field(name="Core Commands", value="`p!helpme`", inline=False)
	help1.add_field(name="Utility Commands", value="`p!ping` **|** `p!badges` **|** `p!about` **|** `p!stats` **|** `p!leagueaccess`", inline=False)
	help1.add_field(name="Fun Commands", value="`p!snowball`", inline=False)
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

	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Pokéberry🍓** <:bot:453635744960086026> \nI started making that bot in <:Python:453634265197051934> but I'm also a web designer & designer. \nI wanted to make this BOT because for each arenas we need to get a badge if we complete it."

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

@bot.command(aliases = ['ping', 'ms'])
async def latency(ctx):
	pingms = "{}".format(int(ctx.bot.latency * 1000))
	message = await ctx.send("Ping - Calculating connection.")
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection....")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection.")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(1.50)
	await message.edit(content = f"Pong! - My latency is **{pingms}**ms")

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

	bot_prefix = "p!"
	server = self.guild

	await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Default'")

	games = [f"Use {bot_prefix}help for help!", f"{sum(1 for _ in self.bot.get_all_members())} users", f"Give us feedback? Use: {bot_prefix}feedback [message]"]
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

			await ctx.send(f"{mention} now have your **gym badge** for reaching/finishing your gym!")

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
		await author2.add_roles(role)
		await ctx.send(f"{author}, you have been given access to enter the League!")

###################################################################################

@bot.command(aliases = ['master', "mf", "fm"])
async def masterfight(ctx, *, member: discord.Member = None):

	author = ctx.message.author.mention
	author2 = ctx.author
	channel = bot.get_channel(449660215298621470)

	if author2.id in elitelead:
		master.append(member.id)
		await channel.send(f"{member.mention} has beaten all **Elite Four** members, they can now fight against the **Elite Master** !")

###################################################################################

@bot.command(aliases = ['comp', 'leaguec', 'cleague'])
async def leaguecompleted(ctx, *, member: discord.Member = None):

	author = ctx.message.author.mention
	author2 = ctx.author
	channel = bot.get_channel(449660215298621470)

	if author2.id in elitelead:
		comp.append(member.id)
		await channel.send(f"{member.mention} has cleared the **League**! Everyone give them a warm GG!")

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
			features17 = "Elite Four"
		elif member.id in elitelead:
			features17 = "Elite Master"
		else:
			if member.id in pewter:
				features17 = "Gym Leader (Pewter - Rock)"
			elif member.id in cerulean:
				features17 = "Gym Leader (Cerulean - Water)"
			elif member.id in vermilion:
				features17 = "Gym Leader (Vermilion - Electrik)"
			elif member.id in celadon:
				features17 = "Gym Leader (Celadon - Grass)"
			elif member.id in fuschia:
				features17 = "Gym Leader (Fuchsia - Poison)"
			elif member.id in saffron:
				features17 = "Gym Leader (Saffron - Psychic)"
			elif member.id in cinnabar:
				features17 = "Gym Leader (Cinnabar - Fire)"
			elif member.id in viridian:
				features17 = "Gym Leader (Viridian - Ground)"
			elif member.id in violet:
				features17 = "Gym Leader (Violet - Flying)"
			elif member.id in azalea:
				features17 = "Gym Leader (Azalea - Bug)"
			elif member.id in goldenrod:
				features17 = "Gym Leader (Goldenrod - Normal)"
			elif member.id in ecruteak:
				features17 = "Gym Leader (Ecruteak - Ghost)"
			elif member.id in cianwood:
				features17 = "Gym Leader (Cianwood - Fighting)"
			elif member.id in olivine:
				features17 = "Gym Leader (Olivine - Steel)"
			elif member.id in mahogany:
				features17 = "Gym Leader (Mahogany - Ice)"
			elif member.id in blackthorn:
				features17 = "Gym Leader (Blackthorn - Dragon)"
			elif member.id in laverre:
				features17 = "Gym Leader (Laverre - Fairy)"
			else:
				features17 = "Gym Leader"
	else:
		features17 = "No Specific Role"

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
	league1 = "<:Didnt_Start:449628615999488000>"
	league2 = "Didn't start the League"

	if member.id in laverre2:
		b1 = "No Badges Left!  "
		number = "(17/17)"
		if member.id in comp:
			b2 = "You finished the League."
		else:
			b2 = "You can access the League."
	else:
		b1 = "Badges Left:  "
		number = "(0/17)"
		if member.id in pewter2:
			b2 = "16 badges left"
			number = "(1/17)"
			if member.id in cerulean2:
				b2 = "15 badges left"
				number = "(2/17)"
				if member.id in vermilion2:
					b2 = "14 badges left"
					number = "(3/17)"
					if member.id in celadon2:
						b2 = "13 badges left"
						number = "(4/17)"
						if member.id in fuschia2:
							b2 = "12 badges left"
							number = "(5/17)"
							if member.id in saffron2:
								b2 = "11 badges left"
								number = "(6/17)"
								if member.id in cinnabar2:
									b2 = "10 badges left"
									number = "(7/17)"
									if member.id in viridian2:
										b2 = "9 badges left"
										number = "(8/17)"
										if member.id in violet2:
											b2 = "8 badges left"
											number = "(9/17)"
											if member.id in azalea2:
												b2 = "7 badges left"
												number = "(10/17)"
												if member.id in goldenrod2:
													b2 = "6 badges left"
													number = "(11/17)"
													if member.id in ecruteak2:
														b2 = "5 badges left"
														number = "(12/17)"
														if member.id in cianwood2:
															b2 = "4 badges left"
															number = "(13/17)"
															if member.id in olivine2:
																b2 = "3 badges left"
																number = "(14/17)"
																if member.id in mahogany2:
																	b2 = "2 badges left"
																	number = "(15/17)"
																	if member.id in blackthorn2:
																		b2 = "1 badge left"
																		number = "(16/17)"
		else:
			b2 = "No badges acquired."

	if member.id in laverre2:
		if member.id in started:
			league1 = "<:Elite_4_Fight:449629015872110592>"
			league2 = "Started the League"
			if member.id in master:
				league1 = "<:Elite_Master_Fight:449628615156564015>"
				league2 = "Fighting VS. Elite Master"
				if member.id in comp:
					league1 = "<:Completed:449628616284831744>"
					league2 = "Completed the League"
		if member.id in master:
				league1 = "<:Elite_Master_Fight:449628615156564015>"
				league2 = "Fighting VS. Elite Master"
				if member.id in comp:
					league1 = "<:Completed:449628616284831744>"
					league2 = "Completed the League"
		if member.id in comp:
					league1 = "<:Completed:449628616284831744>"
					league2 = "Completed the League"


	e.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y at %H:%M:%S')}")#.timestamp = member.joined_at
	e.add_field(name = 'Account created at', value = member.created_at.__format__('Date: **%d %b %Y**\nTime: **%H:%M:%S**\nㅤ'))
	e.add_field(name = 'User ID', value = member.id)
	e.add_field(name = f"{b1}{number}", value = b2, inline=True)
	e.add_field(name = f"Social Status/Role {league1}", value = f"{features17}\n{league2}", inline=True)
	e.add_field(name = 'Pokébadges', value = f"{features}ㅤ{features1}ㅤ{features2}ㅤ{features3}ㅤ{features4}ㅤ{features5}\n\n{features6}ㅤ{features7}ㅤ{features8}ㅤ{features9}ㅤ{features10}ㅤ{features11}\n\n{features12}ㅤ{features13}ㅤ{features14}ㅤ{features15}ㅤ{features16}", inline = True)

	await ctx.send(embed=e)

###################################################################################
###################################################################################
###																				###
###																				###
###								   CUSTOM EMBEDS  								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command()
async def erules(ctx):

	e = discord.Embed(colour = discord.Colour(0x7289DA))
	e2 = discord.Embed(colour = discord.Colour(0x7289DA))

	guild = ctx.guild
	avi = guild.icon_url
	berry = bot.get_user(385419569558323202)
	general = bot.get_channel(457860924515155969)
	international = bot.get_channel(457860854017294336)
	suggestion = bot.get_channel(449199119148253195)
	announcement = bot.get_channel(447492742315114496)
	faq = bot.get_channel(450039051169300500)
	pokemon = bot.get_channel(457860659095535626)
	trading1 = bot.get_channel(450040365555122187)
	trading2 = bot.get_channel(450040431686713367)

	e.set_author(name = "Welcome to Pokémon Universe", icon_url = avi)
	e.add_field(name = "Server Rules", value = "**#1.** No need for personal attacks. If you have a problem with someone contact one of the Admins/Mods, we will help you.", inline=False)
	e.add_field(name = "ㅤ", value = "**#2.** Spam of any kind will not be tolerated and may result in a server mute.", inline=False)
	e.add_field(name = "ㅤ", value = "**#3.** No NSFW content.", inline=False)
	e.add_field(name = "ㅤ", value = "**#4.** Don't impersonate other players.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#5.** Don't use commands other than `p!catch` and `p!info` in {general.mention} or {international.mention}.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#6.** Try to keep swearing to a minimum in {general.mention}, some swearing will be tolerated but try not to.", inline=False)
	e.add_field(name = "ㅤ", value = "**#7.** Don't advertise your servers in chat or in DMs *(3 day mute in the server, if repeated you will be banned - DM advertising = ban)*", inline=False)
	e.add_field(name = "ㅤ", value = f"**#8.** {suggestion.mention} is not for having conversations or using the bot commands, it's for suggestions, use the correct channels.", inline=False)
	e.add_field(name = "ㅤ", value = "**#9.** No racial slurs.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#10.** Don't tag {berry.mention} or Admins unless there is an urgent issue. Try messaging a Moderator first. Doing so for no reason will result in a 2 hour mute.", inline=False)
	e.add_field(name = "ㅤ", value = "**#11.** Try not to beg for credits/redeems/pokemons.", inline=False)
	e.add_field(name = "ㅤ", value = "**#12.** Don't joke about suicide.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#13.** Keep chat in English or use {international.mention}.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#14.** Read {faq.mention} and {announcement.mention} before messaging a staff member, chances are the answer to your question is in there.", inline=False)
	e.add_field(name = "ㅤ", value = "**#15.** Do not repeatedly use a bot command for no reason.", inline=False)
	e.add_field(name = "ㅤ", value = f"**#16.** Don't use `p!info <pokemon>` in general use {pokemon.mention} please.", inline=False)
	e.add_field(name = "ㅤ", value = "**#17.** Follow Discord [Terms of Service](https://discordapp.com/terms) and [Community Guidelines](https://discordapp.com/guidelines)", inline=False)

	e2.add_field(name = "Trading Rules", value = "**#1.** As it is easy to guess, scamming is forbidden.", inline=False)
	e2.add_field(name = "ㅤ", value = f"**#2.** Use {trading1.mention} and {trading2.mention} only to advertise your offers.", inline=False)
	e2.add_field(name = "ㅤ", value = "**#3.** If your trading message is considered too long a mod may warn you for it, and if repeated you will be muted.", inline=False)
	e2.add_field(name = "ㅤ", value = "**#4.** Posting more than ONE trading message per minute will result in a mute/warn.", inline=False)
	e2.set_footer(text = "If a rule is broken and no Admins or Moderators see it, please mention a Moderator.", icon_url=avi)

	await ctx.send(embed = e)
	await ctx.send(embed = e2)

###################################################################################

@bot.command()
async def eroles(ctx):

	e = discord.Embed(colour = discord.Colour(0x7289DA))

	guild = ctx.guild
	avi = guild.icon_url
	mee = bot.get_user(159985870458322944)
	poke = bot.get_user(448885364275281931)

	e.set_author(name = "Self-Assignable Roles", icon_url = avi)
	e.description= "If you want a role, just click the correct emoji dedicated to that role you'd like to have to assign it to yourself.\nIf you would like to take it off, just click the emoji again to remove it!"
	e.add_field(name="Leveled Roles", value=f"Those are automatically assigned by {mee.mention} when you meet the correct level.", inline=False)
	e.add_field(name="Other Roles", value=f"Those are assigned by Gym Leaders/Elite Fours using {poke.mention} when you beat their arena.", inline=False)
	e.set_footer(text = "Custom Roles can be bought by donating at least 1$.")

	await ctx.send(embed = e)

###################################################################################

@bot.command()
async def efaq(ctx):

	e = discord.Embed(colour = discord.Colour(0x7289DA))
	e2 = discord.Embed(colour = discord.Colour(0x7289DA))

	guild = ctx.guild
	avi = guild.icon_url
	poke = bot.get_user(448885364275281931)
	rules = bot.get_channel(447493465241026560)
	role = bot.get_channel(449199056154263552)
	announcement = bot.get_channel(447492742315114496)

	e.set_author(name = "Donations", icon_url = avi)
	e.add_field(name="Why would I donate?", value=f"Donating supports the server but also the developement of {poke.mention}. But you also get perks: 250 credits for each 25 cents donated! Also, you get a special role that only donators have and a custom role if you donate 1$ or more.\nㅤ", inline=False)
	e.add_field(name="Where can I donate?", value="You can donate through PayPal with the link provided by `p!donation`.", inline=False)

	e2.set_author(name = "Others Questions", icon_url = avi)
	e2.add_field(name="IVs and Pokemon Stats", value="IVs now can be seen with `p!detailed` and then `p!info`. IVs are individual values of each unique pokemon and they do not change through levels. They are used to calculate the final stats of each pokemon. They range from 0-31.\nㅤ", inline=False)
	e2.add_field(name="Can I be unmuted please?", value="If you're muted it's for a reason nah? If not, prove it. So... No.\nㅤ", inline=False)
	e2.add_field(name="Can I message Admins privately?", value="Yes. But please, only do when its absolutely important. You are not the only one who thought of messaging an admin/mod to joke around. We don't wanna get tons of messages as after some point it gets annoying.\nㅤ", inline=False)
	e2.add_field(name="This person is catching all the pokemon! They are using copy-pasting to catch! We can't catch pokemon when they are here.", value="What do you expect us to do? It's all fair game. Just do what they are doing if you are so desperate to catch pokemon.\nㅤ", inline=False)
	e2.add_field(name="Can you spawn a pokemon?", value="No we can't, sorry.. ^^'\nㅤ", inline=False)
	e2.add_field(name="Can you give me a pokemon?", value=f"Read the {rules.mention}, no begging.\nㅤ", inline=False)
	e2.add_field(name="When are you gonna do giveaways?", value="When the server hits major membercounts for example, hitting 100 players.\nㅤ", inline=False)
	e2.add_field(name="Where's the spam/NSFW channel?", value="Nowhere. Spamming and NSFW is not allowed in the server in any channel. If you wanna see NSFW things there are webpages for that.\nㅤ", inline=False)
	e2.add_field(name="How much is <pokemon> worth?", value="There are no set prices. The prices vary depending on how many people want the pokemon and how strong it is. You decide how much a pokemon is worth following market prices. Not admins.\nㅤ", inline=False)
	e2.add_field(name="How do I make my own team?", value=f"We are not accepting any new teams at the moment. Please join the already existing ones. You can find them in {role.mention}.\nㅤ", inline=False)
	e2.add_field(name="How can we be recruited?", value=f"When we need new staffs, we post a Google Document (to fill in) in {announcement.mention}, you must be active and fill this Document seriously with developed answers.", inline=False)
	e2.set_footer(text ="Any other questions? You can ask other members or contact the staff team.")

	await ctx.send(embed = e)
	await ctx.send(embed = e2)

###################################################################################
###################################################################################
###																				###
###																				###
###								   BOT/SERVER STATS  							###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['stats'])
async def about(self):
    stat1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
    servers = len(bot.guilds)
    members=0
    for guild in bot.guilds:
        members+=len(guild.members)
    total_online = len({m.id for m in self.bot.get_all_members() if m.status is not discord.Status.offline})
    total_unique = len(self.bot.users)
    total_bots = len([m.id for m in self.bot.get_all_members() if m.bot])
    categories=0
    for guild in bot.guilds:
        categories+=len(guild.categories)
    channels=0
    for guild in bot.guilds:
        channels+=len(guild.channels)
    texts=0
    for guild in bot.guilds:
        texts+=len(guild.text_channels)
    voices=0
    for guild in bot.guilds:
        voices+=len(guild.voice_channels)

    stat2 = bot.get_user(390478999828037632)

    stat1.set_author(name= stat2)
    stat1.add_field(name= "Members in serverㅤ", value=f"Total Users: **{members}** \nTotal Uniques: **{total_unique}** \nTotal Online: **{total_online}** \nTotal BOTS: **{total_bots}**", inline=True)
    stat1.add_field(name= "Channels in server", value=f"Total Categories: **{categories}** \nTotal Channels: **{channels}** \nText Channels: **{texts}** \nVoice Channels: **{voices}**", inline=True)
    stat1.add_field(name= "Program Informations", value=f"Program Language: **<:Python:453634265197051934> 3.6.3** \nDiscord Program: **Discord.py** \nProgram Version: **1.0.0a**", inline=True)
    stat1.add_field(name= "ㅤRun/Bot Informations", value=f"ㅤRunning on: **Heroku** <:Heroku:453634258041438210>\nㅤEdited with: **Sublime Text 3** <:Sublime:453634264248877056>\n\nㅤ*More with `p!helpme` command*", inline=True)
    await self.send(embed = stat1)

###################################################################################
###################################################################################
###																				###
###																				###
###								   SNOWBALL COMMAND  							###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['sb'])
async def snowball(ctx, *, member : discord.Member = None):

    number = random.randint(1, 5)

    if not member:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone!")
    elif member is ctx.author:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone else!")
    else:
        if number == 1:
            snowball_hit = [
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws an __iceball__ in **{member.name}**'s face! *ouchh... these ones hurt...*",
                ]

            choice_hit = random.choice(snowball_hit)
            hit = discord.Embed(colour = discord.Colour(0xE4D7FF))
            hit.description = f"{choice_hit}"
            await ctx.send(embed = hit)
        else:
            snowball_miss = [
                f":snowflake: **| {member.name}** dodged the snowball thrown by **{ctx.author.name}**!",
                f":snowflake: **| {ctx.author.name}**, tried to throw a snowball at **{member.name}** and missed!",
                f":snowflake: **| {ctx.author.name}**, missed and threw the snowball through a window! *Oops*",
                f":snowflake: **| {member.name}** laughed at **{ctx.author.name}**, how can you miss me?",
                f":snowflake: **| {ctx.author.name}** tries to use all their energy, and fell on the ground! *definitely a miss*",
                f":snowflake: **| {ctx.author.name}**, tried to throw an __iceball__ at **{member.name}** and missed! Lucky you, **{member.name}**!",
                ]

            choice_miss = random.choice(snowball_miss)
            miss = discord.Embed(colour = discord.Colour(0xE4D7FF))
            miss.description = f"{choice_miss}"
            await ctx.send(embed = miss)

###################################################################################

if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))

#https://discordapp.com/oauth2/authorize/?permissions=2138569983&scope=bot&client_id=448885364275281931
