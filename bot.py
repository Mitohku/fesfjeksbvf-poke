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


command_prefix = "p." #CHANGE IT TO WHAT YOU WANT
description = "Pokéberry🍓" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()

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

	bot.gym = [385419569558323202, 307219837648764928, 220231135949619200]
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

	bot.pewter2 = []
	bot.cerulean2 = []
	bot.vermilion2 = []
	bot.celadon2 = []
	bot.fuschia2 = []
	bot.saffron2 = []
	bot.cinnabar2 = []
	bot.viridian2 = []
	bot.violet2 = []
	bot.azalea2 = []
	bot.goldenrod2 = []
	bot.ecruteak2 = []
	bot.cianwood2 = []
	bot.olivine2 = []
	bot.mahogany2 = []
	bot.blackthorn2 = []
	bot.laverre2 = []

	bot.elite = [220231135949619200, 247166156467732482]
	bot.elitelead = [385419569558323202] 

	if not member:
		await ctx.send(f"Please **mention** the person who **reached/finished** your gym !")

	else:
		if author2.id in gym:
			if author2.id in pewter:
				await bot.pewter2.append(member.id)
			elif author2.id in cerulean:
				await bot.cerulean2.append(member.id)
			elif author2.id in vermilion:
				await bot.vermilion2.append(member.id)
			elif author2.id in celadon:
				await bot.celadon2.append(member.id)
			elif author2.id in fuschia:
				await bot.uschia2.append(member.id)
			elif author2.id in saffron:
				await bot.saffron2.append(member.id)
			elif author2.id in cinnabar:
				await bot.cinnabar2.append(member.id)
			elif author2.id in viridian:
				await bot.viridian2.append(member.id)
			elif author2.id in violet:
				await bot.violet2.append(member.id)
			elif author2.id in azalea:
				await bot.azalea2.append(member.id)
			elif author2.id in goldenrod:
				await bot.goldenrod2.append(member.id)
			elif author2.id in ecruteak:
				await bot.ecruteak2.append(member.id)
			elif author2.id in cianwood:
				await bot.cianwood2.append(member.id)
			elif author2.id in olivine:
				await bot.olivine2.append(member.id)
			elif author2.id in mahogany:
				await bot.mahogany2.append(member.id)
			elif author2.id in blackthorn:
				await bot.blackthorn2.append(member.id)
			elif author2.id in laverre:
				await bot.laverre2.append(member.id)
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
###								   BADGES COMMAND  								###
###																				###
###																				###
###################################################################################
###################################################################################

@bot.command(aliases = ['badge', 'profile'])
async def badges(ctx, *, member: discord.Member = None):

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
		
	if member.id in bot.pewter2:
		if member.id in bot.cerulean2:
			features1 = ":one:"
		elif member.id in bot.vermilion2:
			features2 = ":two:"
		elif member.id in bot.celadon2:
			features3 = ":three:"
		elif member.id in bot.fuschia2:
			features4 = ":four:"
		elif member.id in bot.saffron2:
			features5 = ":five:"
		elif member.id in bot.cinnabar2:
			features6 = ":six:"
		elif member.id in bot.viridian2:
			features7 = ":seven:"
		elif member.id in bot.violet2:
			features8 = ":eight:"
		elif member.id in bot.azalea2:
			features9 = ":nine:"
		elif member.id in bot.goldenrod2:
			features10 = ":one::zero:"
		elif member.id in bot.ecruteak2:
			features11 = ":one::one:"
		elif member.id in bot.cianwood2:
			features12 = ":one::two:"
		elif member.id in bot.olivine2:
			features13 = ":one::three:"
		elif member.id in bot.mahogany2:
			features14 = ":one::four:"
		elif member.id in bot.blackthorn2:
			features15 = ":one::five:"
		elif member.id in bot.laverre2:
			features16 = ":one::six:"
		else:
			features = ":one:"
	else:
		features = "ㅤ"
		features1 = "ㅤ"
		features2 = "ㅤ"
		features3 = "ㅤ"
		features4 = "ㅤ"
		features5 = "ㅤ"
		features6 = "ㅤ"
		features7 = "ㅤ"
		features8 = "ㅤ"
		features9 = "ㅤ"
		features10 = "ㅤ"
		features11 = "ㅤ"
		features12 = "ㅤ"
		features13 = "ㅤ"
		features14 = "ㅤ"
		features15 = "ㅤ"
		features16 = "ㅤ"
		features17 = "ㅤ"

	e = discord.Embed(colour = discord.Colour(0xA522B3))
	e.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y at %H:%M:%S')}")#.timestamp = member.joined_at
	e.add_field(name = 'User ID', value = member.id)
	e.add_field(name = 'Client Status', value = status_name)
	e.add_field(name = 'Account created at', value = member.created_at.__format__('Date: **%d %b %Y**\nTime: **%H:%M:%S**'))
	e.add_field(name = 'Pokébadges', value = f"{features}ㅤ**|**ㅤ{features1}ㅤ**|**ㅤ{features2}\n{features3}ㅤ**|**ㅤ{features4}ㅤ**|**ㅤ{features5}\n{features6}ㅤ**|**ㅤ{features7}ㅤ**|**ㅤ{features8}\n{features9}ㅤ**|**ㅤ{features10}ㅤ**|**ㅤ{features11}\n{features12}ㅤ**|**ㅤ{features13}ㅤ**|**ㅤ{features14}\nㅤㅤ{features15}ㅤ**|**ㅤ{features16}\nㅤㅤㅤㅤㅤ{features17}")

	await ctx.send(embed=e)

###################################################################################

if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
