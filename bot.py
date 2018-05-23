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
	mention = member.mention

	gym = [385419569558323202, 307219837648764928, 220231135949619200]
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

	pewter2 = [385419569558323202]
	cerulean2 = [385419569558323202]
	vermilion2 = [385419569558323202]
	celadon2 = [385419569558323202]
	fuschia2 = [385419569558323202]
	saffron2 = [385419569558323202]
	cinnabar2 = [385419569558323202]
	viridian2 = [385419569558323202]
	violet2 = [385419569558323202]
	azalea2 = [385419569558323202]
	goldenrod2 = [385419569558323202]
	ecruteak2 = [385419569558323202]
	cianwood2 = [385419569558323202]
	olivine2 = [385419569558323202]
	mahogany2 = [385419569558323202]
	blackthorn2 = [385419569558323202]
	laverre2 = [385419569558323202]

	elite = [220231135949619200, 247166156467732482]
	elite.lead = [385419569558323202] 

	if not member:
		await ctx.send(f"Please **mention** the person who **reached/finished** your gym !")

	else:
		if author in gym:
			if author in pewter:
				await pewter2.append(member.id)
			elif author in cerulean:
				await cerulean2.append(member.id)
			elif author in vermilion:
				await vermilion2.append(member.id)
			elif author in celadon:
				await celadon2.append(member.id)
			elif author in fuschia:
				await fuschia2.append(member.id)
			elif author in saffron:
				await saffron2.append(member.id)
			elif author in cinnabar:
				await cinnabar2.append(member.id)
			elif author in viridian:
				await viridian2.append(member.id)
			elif author in violet:
				await violet2.append(member.id)
			elif author in azalea:
				await azalea2.append(member.id)
			elif author in goldenrod:
				await goldenrod2.append(member.id)
			elif author in ecruteak:
				await ecruteak2.append(member.id)
			elif author in cianwood:
				await cianwood2.append(member.id)
			elif author in olivine:
				await olivine2.append(member.id)
			elif author in mahogany:
				await mahogany2.append(member.id)
			elif author in blackthorn:
				await blackthorn2.append(member.id)
			elif author in laverre:
				await laverre2.append(member.id)
			else:
				return

			embed = discord.Embed(colour = discord.Colour(0xA522B3))
			embed.description = f"{memtion} now have your **gym badge** for reaching/finishing your gym!"
			await ctx.send(embed = embed)

		else:
			await ctx.send(f"You aren't a **Gym Leader**, {author} !")

if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
