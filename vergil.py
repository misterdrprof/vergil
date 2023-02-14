import discord, random, asyncio, json, time, string, re
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Emoji
from discord.utils import get
from datetime import datetime
from functions import *
import functions as RL
from discord.ext import commands
from discord import File
import discord
import os
from discord.ext.commands import CommandNotFound

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)
bot.remove_command('help')
roles = ['Burnt Sienna King', 'developer', 'Middleman']
roleMessage = 840660607921553448

@bot.event
async def on_ready():
    global roleMessage
    global msg

    await bot.change_presence(status=discord.Status.online)
    print('-' * 30)
    print('Logged in as: ')
    print(bot.user)
    print('-' * 30)
        
@bot.event
async def on_raw_reaction_add(payload):
    global roleMessage
    if payload.message_id == roleMessage:
        await handle_reaction(payload, True)

@bot.event
async def on_raw_reaction_remove(payload):
    global roleMessage
    if payload.message_id == roleMessage:
        await handle_reaction(payload, False)


async def handle_reaction(payload, action):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)
    if action:
        if str(payload.emoji.name) == 'crimson':
            crimsonRole = "Crimson Collector"
            crimRole = get(guild.roles, name=crimsonRole)
            await user.add_roles(crimRole)
        if str(payload.emoji.name) == 'crimson':
            orangeRole = "Orange Collector"
            oranRole = get(guild.roles, name=orangeRole)
            await user.add_roles(oranRole)
        if str(payload.emoji.name) == 'bs':
            siennaRole = "Burnt Sienna Collector"
            bsRole = get(guild.roles, name=siennaRole)
            await user.add_roles(bsRole)
        if str(payload.emoji.name) == 'saffron':
            saffronRole = "Saffron Collector"
            saffRole = get(guild.roles, name=saffronRole)
            await user.add_roles(saffRole)
        if str(payload.emoji.name) == 'lime':
            LimeRole = "Lime Collector"
            limeRole = get(guild.roles, name=LimeRole)
            await user.add_roles(limeRole)
        if str(payload.emoji.name) == 'fg':
            FgRole = "Forest Green Collector"
            fgRole = get(guild.roles, name=FgRole)
            await user.add_roles(fgRole)
        if str(payload.emoji.name) == 'sb':
            SbRole = "Sky Blue Collector"
            sbRole = get(guild.roles, name=SbRole)
            await user.add_roles(sbRole)
        if str(payload.emoji.name) == 'cobalt':
            cobaltRole = "Cobalt Collector"
            cobRole = get(guild.roles, name=cobaltRole)
            await user.add_roles(cobRole)
        if str(payload.emoji.name) == 'purple':
            purpleRole = "Purple Collector"
            purpRole = get(guild.roles, name=purpleRole)
            await user.add_roles(purpRole)
        if str(payload.emoji.name) == 'pink':
            PinkRole = "Pink Collector"
            pinkRole = get(guild.roles, name=PinkRole)
            await user.add_roles(pinkRole)
        if str(payload.emoji.name) == 'tw':
            TwRole = "Titanium White Collector"
            twRole = get(guild.roles, name=TwRole)
            await user.add_roles(twRole)
        if str(payload.emoji.name) == 'grey':
            GreyRole = "Grey Collector"
            greyRole = get(guild.roles, name=GreyRole)
            await user.add_roles(greyRole)
        if str(payload.emoji.name) == 'black':
            BlackRole = "Black Collector"
            blackRole = get(guild.roles, name=BlackRole)
            await user.add_roles(blackRole)
        if str(payload.emoji.name) == 'Prof':
            tradeRole = "Trader"
            traderRole = get(guild.roles, name=tradeRole)
            await user.add_roles(traderRole)
        if str(payload.emoji.name) == 'PC':
            pcRole = "PC"
            PcRole = get(guild.roles, name=pcRole)
            await user.add_roles(PcRole)
        if str(payload.emoji.name) == 'xbox':
            xboxRole = "Xbox"
            XboxRole = get(guild.roles, name=xboxRole)
            await user.add_roles(XboxRole)
        if str(payload.emoji.name) == 'PS4':
            ps4Role = "PS4"
            Ps4Role = get(guild.roles, name=ps4Role)
            await user.add_roles(Ps4Role)
        if str(payload.emoji.name) == 'switch':
            switchRole = "Switch"
            SwitchRole = get(guild.roles, name=switchRole)
            await user.add_roles(SwitchRole)
    else:
        if str(payload.emoji.name) == 'crimson':
            crimsonRole = "Crimson Collector"
            crimRole = get(guild.roles, name=crimsonRole)
            await user.remove_roles(crimRole)
        if str(payload.emoji.name) == 'crimson':
            orangeRole = "Orange Collector"
            oranRole = get(guild.roles, name=orangeRole)
            await user.remove_roles(oranRole)
        if str(payload.emoji.name) == 'bs':
            siennaRole = "Burnt Sienna Collector"
            bsRole = get(guild.roles, name=siennaRole)
            await user.remove_roles(bsRole)
        if str(payload.emoji.name) == 'saffron':
            saffronRole = "Saffron Collector"
            saffRole = get(guild.roles, name=saffronRole)
            await user.remove_roles(saffRole)
        if str(payload.emoji.name) == 'lime':
            LimeRole = "Lime Collector"
            limeRole = get(guild.roles, name=LimeRole)
            await user.remove_roles(limeRole)
        if str(payload.emoji.name) == 'fg':
            FgRole = "Forest Green Collector"
            fgRole = get(guild.roles, name=FgRole)
            await user.remove_roles(fgRole)
        if str(payload.emoji.name) == 'sb':
            SbRole = "Sky Blue Collector"
            sbRole = get(guild.roles, name=SbRole)
            await user.remove_roles(sbRole)
        if str(payload.emoji.name) == 'cobalt':
            cobaltRole = "Cobalt Collector"
            cobRole = get(guild.roles, name=cobaltRole)
            await user.remove_roles(cobRole)
        if str(payload.emoji.name) == 'purple':
            purpleRole = "Purple Collector"
            purpRole = get(guild.roles, name=purpleRole)
            await user.remove_roles(purpRole)
        if str(payload.emoji.name) == 'pink':
            PinkRole = "Pink Collector"
            pinkRole = get(guild.roles, name=PinkRole)
            await user.remove_roles(pinkRole)
        if str(payload.emoji.name) == 'tw':
            TwRole = "Titanium White Collector"
            twRole = get(guild.roles, name=TwRole)
            await user.remove_roles(twRole)
        if str(payload.emoji.name) == 'grey':
            GreyRole = "Grey Collector"
            greyRole = get(guild.roles, name=GreyRole)
            await user.remove_roles(greyRole)
        if str(payload.emoji.name) == 'black':
            BlackRole = "Black Collector"
            blackRole = get(guild.roles, name=BlackRole)
            await user.remove_roles(blackRole)
        if str(payload.emoji.name) == 'Prof':
            tradeRole = "Trader"
            traderRole = get(guild.roles, name=tradeRole)
            await user.remove_roles(traderRole)
        if str(payload.emoji.name) == 'PC':
            pcRole = "PC"
            PcRole = get(guild.roles, name=pcRole)
            await user.remove_roles(PcRole)
        if str(payload.emoji.name) == 'xbox':
            xboxRole = "Xbox"
            XboxRole = get(guild.roles, name=xboxRole)
            await user.remove_roles(XboxRole)
        if str(payload.emoji.name) == 'PS4':
            ps4Role = "PS4"
            Ps4Role = get(guild.roles, name=ps4Role)
            await user.remove_roles(Ps4Role)
        if str(payload.emoji.name) == 'switch':
            switchRole = "Switch"
            SwitchRole = get(guild.roles, name=switchRole)
            await user.remove_roles(SwitchRole)

@bot.event
async def on_member_join(member):
    welcomeChannel = bot.get_channel(int(831171637171716136))
    assignChannel = bot.get_channel(830377069769916448)
    rulesChannel = bot.get_channel(830376368776282112)
    await welcomeChannel.send(f'{member.mention}, Welcome to colorful traders - assign your roles {assignChannel.mention} then view our {rulesChannel.mention}')

@commands.has_any_role(*roles)
@bot.command(aliases=['c', 'clears', 'clea', 'clearr'])
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author.mention}, cleared {amount} messages.')
    await asyncio.sleep(15)
    await ctx.channel.purge(limit=1)

@commands.has_any_role(*roles)
@bot.command(name="ban")
async def ban_command(ctx, user : discord.Member, *reason):
    timestamp = time.strftime('%H:%M:%S')
    if reason:
        await user.ban(reason=reason)
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been banned**", value=f"{user.mention} has been banned.\nReason: **{reason[0]}**\nBy: {ctx.author.mention}", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(3)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)
    if not reason:
        await user.ban()
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been banned**", value=f"{user.mention} has been banned.", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(3)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)

@commands.has_any_role(*roles)
@bot.command(name="unban")
async def unban_command(ctx, *, member):
    timestamp = time.strftime('%H:%M:%S')
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
    embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
    embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name=f"**{member_name}#{member_discriminator} has been unbanned**", value=f"{member_name}#{member_discriminator} has been unbanned.", inline=False)
    mess = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(3)
    await mess.delete()
    logChan = bot.get_channel(840598868269072404)
    await logChan.send(embed=embed)

@commands.has_any_role(*roles)
@bot.command(name="kick")
async def kick_command(ctx, user : discord.Member, *reason):
    timestamp = time.strftime('%H:%M:%S')
    if reason:
        await user.kick(reason=reason)
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been kicked**", value=f"{user.mention} has been kicked.\nReason: **{reason[0]}**", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(3)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)
    if not reason:
        await user.kick()
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been kicked**", value=f"{user.mention} has been kicked. | Invoked by: {ctx.author.name}", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(3)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)

@commands.has_any_role(*roles)
@bot.command(name="mute")
async def mute_command(ctx, user : discord.Member, *reason):
    timestamp = time.strftime('%H:%M:%S')
    role = get(ctx.guild.roles, name="Muted")
    await user.add_roles(role)
    if reason:
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been muted**", value=f"{user.mention} has been muted.\nReason: **{reason[0]}**", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(5)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)
    if not reason:
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"**{user.name}#{user.discriminator} has been muted**", value=f"{user.mention} has been muted.", inline=False)
        mess = await ctx.send(embed=embed)
        await ctx.message.delete()
        await asyncio.sleep(3)
        await mess.delete()
        logChan = bot.get_channel(840598868269072404)
        await logChan.send(embed=embed)

@commands.has_any_role(*roles)
@bot.command(name="unmute")
async def unmute_command(ctx, user : discord.Member):
    timestamp = time.strftime('%H:%M:%S')
    role = get(ctx.guild.roles, name="Muted")
    await user.remove_roles(role)
    embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
    embed.set_footer(text=f"e:) | {timestamp} | Invoked by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name=f"**{user.name}#{user.discriminator} has been unmuted**", value=f"{user.mention} has been unmuted.", inline=False)
    mess = await ctx.send(embed=embed)
    await ctx.message.delete()
    await asyncio.sleep(3)
    await mess.delete()
    logChan = bot.get_channel(840598868269072404)
    await logChan.send(embed=embed)

@bot.listen()
async def on_message(message):
    
    with open('files/custom_commands.json', 'r') as json_file:
        all_commands = json.load(json_file)

    if all_commands and (message.content[1:] in all_commands['normal']):
        await message.channel.send(all_commands['normal'][message.content[1:]])
    if all_commands and (message.content[1:] in all_commands['embed']):
        embed = discord.Embed(title="Vergil", description=f"**{all_commands['embed'][message.content[1:]]}**", color=0x1406EF)
        await message.channel.send(embed=embed)
    if all_commands and (message.content[1:] in all_commands['embedurls']):
        embed = discord.Embed(title="Vergil", color=0x1406EF)
        embed.set_image(url=all_commands['embedurls'][message.content[1:]])
        await message.channel.send(embed=embed)


    mess = message.content.lower()
    bad_words = ["nigger", "nigga", "rape", "rapist", "pedo", "pedophile"]

    devRole = "developer"
    devRole = get(message.guild.roles, name=devRole)
    bsKingRole = "Burnt Sienna King"
    bsKingRole = get(message.guild.roles, name=bsKingRole)
    middlemanRole = "Middleman"
    middlemanRole = get(message.guild.roles, name=middlemanRole)
    communityFigureRole = "Community Figure"
    communityFigureRole = get(message.guild.roles, name=communityFigureRole)
    crimsonRole = "Crimson Collector"
    crimRole = get(message.guild.roles, name=crimsonRole)
    orangeRole = "Orange Collector"
    oranRole = get(message.guild.roles, name=orangeRole)
    siennaRole = "Burnt Sienna Collector"
    bsRole = get(message.guild.roles, name=siennaRole)
    saffronRole = "Saffron Collector"
    saffRole = get(message.guild.roles, name=saffronRole)
    LimeRole = "Lime Collector"
    limeRole = get(message.guild.roles, name=LimeRole)
    FgRole = "Forest Green Collector"
    fgRole = get(message.guild.roles, name=FgRole)
    SbRole = "Sky Blue Collector"
    sbRole = get(message.guild.roles, name=SbRole)
    cobaltRole = "Cobalt Collector"
    cobRole = get(message.guild.roles, name=cobaltRole)
    purpleRole = "Purple Collector"
    purpRole = get(message.guild.roles, name=purpleRole)
    PinkRole = "Pink Collector"
    pinkRole = get(message.guild.roles, name=PinkRole)
    TwRole = "Titanium White Collector"
    twRole = get(message.guild.roles, name=TwRole)
    GreyRole = "Grey Collector"
    greyRole = get(message.guild.roles, name=GreyRole)
    BlackRole = "Black Collector"
    blackRole = get(message.guild.roles, name=BlackRole)
    tradeRole = "Trader"
    traderRole = get(message.guild.roles, name=tradeRole)
    pcRole = "PC"
    PcRole = get(message.guild.roles, name=pcRole)
    xboxRole = "Xbox"
    XboxRole = get(message.guild.roles, name=xboxRole)
    ps4Role = "PS4"
    Ps4Role = get(message.guild.roles, name=ps4Role)
    everyoneRole = get(message.guild.roles, name="@everyone")
    switchRole = "Switch"
    SwitchRole = get(message.guild.roles, name=switchRole)
    mess = remove(mess)

    if bsKingRole:
        pass
    if devRole:
        pass
    if middlemanRole:
        pass
    if communityFigureRole:
        pass
    if crimRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if everyoneRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if oranRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if bsRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if limeRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if saffRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if fgRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if sbRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if cobRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if purpRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if pinkRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if twRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if greyRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if blackRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if traderRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if PcRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if XboxRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if Ps4Role:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    if SwitchRole:
        for word in bad_words:
            if word in mess:
                timestamp = time.strftime('%H:%M:%S')
                await message.delete()
                embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
                embed.set_footer(text=f"e:) | {timestamp}", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Vergil Moderation**", value=f"{message.author.mention}, you cannot say that.", inline=False)
                messChan = bot.get_channel(message.channel.id)
                modMess = await messChan.send(embed=embed)
                await asyncio.sleep(5)
                await modMess.delete()
    
@bot.event
async def on_message_delete(message):
    if message.author != bot.user:
        async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
            deleter = entry.user
        timestamp = time.strftime('%H:%M:%S')
        embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:)")
        embed.add_field(name=f"**{message.author.name}#{message.author.discriminator} has deleted a message**", value=f"{message.author.id}", inline=False)
        embed.add_field(name=f"**Deleted At**", value=f"{timestamp}", inline=False)
        embed.add_field(name=f"**Content**", value=f"{message.content}", inline=False)
        embed.add_field(name=f"**Timestamp**", value=f"{message.created_at}", inline=False)
        logChan = bot.get_channel(840648088619974686)
        await logChan.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author != bot.user or after.author != bot.user:
        timestamp = time.strftime('%H:%M:%S')
        embed = discord.Embed(title="Vergil Log", colour=discord.Colour(0x1406EF))
        embed.set_footer(text=f"e:)")
        embed.add_field(name=f"**{before.author.name}#{before.author.discriminator} has edited a message**", value=f"{before.author.id}", inline=False)
        embed.add_field(name=f"**Edited at At**", value=f"{timestamp}", inline=False)
        embed.add_field(name=f"**Before Edit**", value=f"{before.content}", inline=False)
        embed.add_field(name=f"**After Edit**", value=f"{after.content}", inline=False)
        embed.add_field(name=f"**Timestamp**", value=f"{before.created_at}", inline=False)
        logChan = bot.get_channel(840648119544184882)
        await logChan.send(embed=embed)

def remove(string):
    return string.replace(" ", "")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Vergil Help", colour=discord.Colour(0x1406EF))
    embed.set_footer(text="e:)")
    embed.add_field(name="**!Rank** (Check all ranks)", value="Rank Steam {ID}\nRank Epic {ID}\nRank PSN {PSN}\nRank XBL {gamertag}\n\n", inline=False)
    embed.add_field(name="**!Duel** (Check 1v1 rank)", value="Duel Steam {ID}\nDuel Epic {ID}\nDuel PSN {PSN}\nDuel XBL {gamertag}\n\n", inline=False)
    embed.add_field(name="**!Doubles** (Check 2v2 rank)", value="Doubles Steam {ID}\nDoubles Epic {ID}\nDoubles PSN {PSN}\nDoubles XBL {gamertag}\n\n", inline=False)
    embed.add_field(name="**!Standard** (Check 3v3 rank)", value="Standard Steam {ID}\nStandard Epic {ID}\nStandard PSN {PSN}\nStandard XBL {gamertag}\n\n", inline=False)
    embed.add_field(name="**!Price** (Check price of item)", value="Price Platform White Octane { e.g.Price Xbox Black Dieci -exotic}\n\n", inline=False)
    embed.add_field(name="**Moderation", value="!ban @user *reason\n!unban user#1234\n!kick @user *reason\n!mute @user reason*\n!unmute @user\n\n", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['ranks', 'ran', 'rankk'])
async def rank(ctx, platform, player):
    if "xbox" in platform:
        platform = 'xbl'
    if "ps4" in platform:
        platform = 'psn'
    if "pc" in platform:
        platform = 'steam'
    searchPlayer(platform, player)
    embed=discord.Embed(title=f"{RL.playerName} Ranks\n(Views: {RL.profileViews})", color=0x021ff7)
    embed.set_author(name="Vergil")
    if RL.avatar == 'None':
        embed.set_thumbnail(url='https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png')
    else:
        embed.set_thumbnail(url=RL.avatar)
    embed.add_field(name="**Season Reward**", value=f"{RL.seasonRewards}", inline=False)
    embed.add_field(name="**Duel**", value=f"{RL.duel}", inline=False)
    embed.add_field(name="**Doubles**", value=f"{RL.doubles}", inline=False)
    embed.add_field(name="**Standard**", value=f"{RL.standard}", inline=False)
    embed.add_field(name="**Hoops**", value=f"{RL.hoops}", inline=False)
    embed.add_field(name="**Rumble**", value=f"{RL.rumble}", inline=False)
    embed.add_field(name="**Dropshot**", value=f"{RL.dropshot}", inline=False)
    embed.add_field(name="**Snowday**", value=f"{RL.snowday}", inline=False)
    embed.set_footer(text="e:)")
    await ctx.send(embed=embed)

@bot.command(aliases=['ones', '1s', '1'])
async def duell(ctx, platform, player):
    searchPlayer(platform, player)
    embed=discord.Embed(title=f"{RL.playerName} Ranks\n(Views: {RL.profileViews})", color=0x021ff7)
    embed.set_author(name="Vergil")
    if RL.avatar == 'None':
        embed.set_thumbnail(url='https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png')
    else:
        embed.set_thumbnail(url=RL.avatar)
    embed.add_field(name="**Season Reward**", value=f"{RL.seasonRewards}", inline=False)
    embed.add_field(name="**Duel**", value=f"{RL.duel}", inline=False)
    embed.set_footer(text="e:)")
    await ctx.send(embed=embed)

@bot.command(aliases=['twos', '2s', '2'])
async def doubless(ctx, platform, player):
    searchPlayer(platform, player)
    embed=discord.Embed(title=f"{RL.playerName} Ranks\n(Views: {RL.profileViews})", color=0x021ff7)
    embed.set_author(name="Vergil")
    if RL.avatar == 'None':
        embed.set_thumbnail(url='https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png')
    else:
        embed.set_thumbnail(url=RL.avatar)
    embed.add_field(name="**Season Reward**", value=f"{RL.seasonRewards}", inline=False)
    embed.add_field(name="**Doubles**", value=f"{RL.doubles}", inline=False)
    embed.set_footer(text="e:)")
    await ctx.send(embed=embed)

@bot.command(aliases=['threes', '3s', '3'])
async def standardd(ctx, platform, player):
    searchPlayer(platform, player)
    embed=discord.Embed(title=f"{RL.playerName} Ranks\n(Views: {RL.profileViews})", color=0x021ff7)
    embed.set_author(name="Vergil")
    if RL.avatar == 'None':
        embed.set_thumbnail(url='https://trackercdn.com/cdn/tracker.gg/rocket-league/ranks/s4-0.png')
    else:
        embed.set_thumbnail(url=RL.avatar)
    embed.add_field(name="**Season Reward**", value=f"{RL.seasonRewards}", inline=False)
    embed.add_field(name="**Standard**", value=f"{RL.standard}", inline=False)
    embed.set_footer(text="e:)")
    await ctx.send(embed=embed)

@bot.command(aliases=['prices', 'pric', 'check'])
async def price(ctx, platform, *, item):
    platform = platform.lower()
    if platform == 'ps4':
        platform = 'psn'
    item = item.lower()
    itemInfo = grabItem(platform, item)
    if itemInfo[0] == 'options':
        embed=discord.Embed(title=f"Multiple options for {item}", color=0x021ff7)
        embed.set_author(name="Vergil")
        embed.add_field(name="**Options**", value=f"!price platform item -itemType (e.g. -exotic -uncommon -trail -goal -boost)", inline=False)
        embed.set_footer(text="e:)")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"{itemInfo[2]}", color=0x021ff7, url=itemInfo[0])
        embed.set_author(name="Vergil")
        embed.set_thumbnail(url=itemInfo[1])
        embed.add_field(name=f"**{itemInfo[2]} Price**", value=f"{itemInfo[3]} Credits", inline=False)
        embed.set_footer(text="e:)")
        await ctx.send(embed=embed)

def randomDigits():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(10))

@bot.command(aliases=['cal', 'calll', 'caal'])
async def call(ctx, *, details):
    member = ctx.author
    guild = bot.get_guild(830366087866351646)


    bsKingRole = get(guild.roles, name="Burnt Sienna King")
    everyoneRole = get(guild.roles, name="@everyone")
    devRole = get(guild.roles, name="developer")
    mmRole = get(guild.roles, name="Middleman")
    pigeonRole = get(guild.roles, name='The Pigeon Man')
    mercRole = get(guild.roles, name='Merc Item Collector')
    communityFigureRole = get(guild.roles, name='Community Figure')
    crimRole = get(guild.roles, name='Crimson Collector')
    orangeRole = get(guild.roles, name='Orange Collector')
    bsRole = get(guild.roles, name='Burnt Sienna Collector')
    saffRole = get(guild.roles, name='Saffron Collector')
    limeRole = get(guild.roles, name='Lime Collector')
    fgRole = get(guild.roles, name='Forest Green Collector')
    sbRole = get(guild.roles, name='Sky Blue Collector')
    cobaltRole = get(guild.roles, name='Cobalt Collector')
    purpleRole = get(guild.roles, name='Purple Collector')
    pinkRole = get(guild.roles, name='Pink Collector')
    twRole = get(guild.roles, name='Titanium White Collector')
    greyRole = get(guild.roles, name='Grey Collector')
    blackRole = get(guild.roles, name='Black Collector')
    traderRole = get(guild.roles, name='Trader')
    pcRole = get(guild.roles, name='PC')
    ps4Role = get(guild.roles, name='PS4')
    xboxRole = get(guild.roles, name='Xbox')

    overwrites = {
        everyoneRole: discord.PermissionOverwrite(read_messages=False),
        pigeonRole: discord.PermissionOverwrite(read_messages=False),
        mercRole: discord.PermissionOverwrite(read_messages=False),
        communityFigureRole: discord.PermissionOverwrite(read_messages=False),
        crimRole: discord.PermissionOverwrite(read_messages=False),
        orangeRole: discord.PermissionOverwrite(read_messages=False),
        bsRole: discord.PermissionOverwrite(read_messages=False),
        saffRole: discord.PermissionOverwrite(read_messages=False),
        limeRole: discord.PermissionOverwrite(read_messages=False),
        fgRole: discord.PermissionOverwrite(read_messages=False),
        sbRole: discord.PermissionOverwrite(read_messages=False),
        cobaltRole: discord.PermissionOverwrite(read_messages=False),
        purpleRole: discord.PermissionOverwrite(read_messages=False),
        pinkRole: discord.PermissionOverwrite(read_messages=False),
        twRole: discord.PermissionOverwrite(read_messages=False),
        greyRole: discord.PermissionOverwrite(read_messages=False),
        blackRole: discord.PermissionOverwrite(read_messages=False),
        traderRole: discord.PermissionOverwrite(read_messages=False),
        pcRole: discord.PermissionOverwrite(read_messages=False),
        ps4Role: discord.PermissionOverwrite(read_messages=False),
        xboxRole: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        bsKingRole: discord.PermissionOverwrite(read_messages=True),
        devRole: discord.PermissionOverwrite(read_messages=True),
        mmRole: discord.PermissionOverwrite(read_messages=True)
    }
    digits = randomDigits()
    await ctx.channel.purge(limit=1)
    name = 'middleman-calls'
    category = discord.utils.get(ctx.guild.categories, name=name)
    buyerChannel = f'{ctx.message.author.name}-{digits}'
    channell = await guild.create_text_channel(buyerChannel, overwrites=overwrites, category=category)
    newChannel = bot.get_channel(int(channell.id))
    user1 = re.findall('<@!(\d{16,24})>', details)
    if user1:
        details = details.split('> ')
        user0 = user1[0]
        user1 = user1[0]
        user1 = user1.replace('<@!', '').replace('>', '') 
        user2 = get(bot.get_all_members(), id=int(user1))
        await newChannel.set_permissions(member, read_messages=True)
        await newChannel.set_permissions(user2, read_messages=True)
        await newChannel.send(f'**Details**:\nTrade: {details[1]}\n\nUser 1: {ctx.author.mention}\nDiscord Id: {ctx.author.id}\n\nUser 2: {user2.mention}\nDiscord Id: {user2.id}')
        await newChannel.send(f'\n{ctx.author.mention}, Please wait for a middleman.')
    if not user1:
        await newChannel.set_permissions(member, read_messages=True)
        await newChannel.send(f'**Details**:\nTrade: {details}\n\nUser: {ctx.author.mention}\nDiscord Id: {ctx.author.id}')
        await newChannel.send(f'\n{ctx.author.mention}, Please wait for a middleman.')

@commands.has_any_role(*roles)
@bot.command(aliases=['close', 'closee', 'clos', 'finish', 'finished'])
async def done(ctx):
    await ctx.channel.delete()

@bot.command()
async def invite(ctx):
    invite_link = await ctx.channel.create_invite()
    embed = discord.Embed(title='Server invite', description='send this link to invite people to this server')
    embed.add_field(name='link:', value=invite_link, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    msg = await ctx.send(f"**pinging...**")
    await msg.edit(content=f"**:stopwatch:  _{round(bot.latency * 1000)}_ ms**")

@commands.has_any_role(*roles)
@bot.command(aliases=['new-command', 'add-command'])
async def add_command(ctx, command_name, *, command_reply):
    if (command_name is None) or (not command_reply):
        await ctx.send('Missing Arguments')
    
    with open('files/custom_commands.json', 'r') as json_file:
        all_commands = json.load(json_file)

    if "-embed" in command_reply:
        command_reply = command_reply.split(' -embed')

        all_commands['embed'][command_name] = command_reply[0]
    
        with open('files/custom_commands.json', 'w') as json_file:
            json.dump(all_commands, json_file)

    elif "-url" in command_reply:
        command_reply = command_reply.split(' -url')

        all_commands['embedurls'][command_name] = command_reply[0]
    
        with open('files/custom_commands.json', 'w') as json_file:
            json.dump(all_commands, json_file)
    else:
        all_commands[command_name] = command_reply
        
        with open('files/custom_commands.json', 'w') as json_file:
            json.dump(all_commands, json_file)

    timestamp = time.strftime('%H:%M:%S')
    embed = discord.Embed(title="Vergil", colour=discord.Colour(0x1406EF))
    embed.set_footer(text=f"e:) | {timestamp}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name=f"**{command_name} has been added**", value=f"**By {ctx.author.name}**", inline=False)
    mess = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await mess.delete()
    await ctx.message.delete()
    logChan = bot.get_channel(840598868269072404)
    await logChan.send(embed=embed)

@commands.has_any_role(*roles)
@bot.command(aliases=['delete-command', 'del-command'])
async def delete_command(ctx, command_name):

    with open('files/custom_commands.json', 'r') as json_file:
        all_commands = json.load(json_file)
    
    if command_name in all_commands['embed']:
        all_commands['embed'].pop(command_name)

    elif command_name in all_commands['embedurls']:
        all_commands['embedurls'].pop(command_name)
    
    elif command_name in all_commands['normal']:
        all_commands['normal'].pop(command_name)
    
    else:
        await ctx.send(f'**{command_name} not found**')
        return


    with open('files/custom_commands.json', 'w') as json_file:
        json.dump(all_commands, json_file)
    
    await ctx.send(f'**{command_name} has been deleted successfully**')

@bot.command(aliases=['custom-commands'])
async def custom_commands(ctx):

    with open('files/custom_commands.json', 'r') as json_file:
        all_servers = json.load(json_file)


    if all_servers:
        embed = discord.Embed(title="Custom Commands", description="here are the server's custom commands: ")
        for command in all_servers['normal'].keys():
            embed.add_field(name=f'{command} [normal]', value=all_servers['normal'][command], inline=False)
            
        for command in all_servers['embed'].keys():
            embed.add_field(name=f'{command} [embedded]', value=all_servers['embed'][command], inline=False)
        for command in all_servers['embedurls'].keys():
            embed.add_field(name=f'{command} [embedded picture]', value=all_servers['embedurls'][command], inline=False)
    else:
        embed = discord.Embed(title="No custom commands have been found",
                                description=f"type `add-command` to add first command")

    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
            return
            
    error = getattr(error, 'original', error)

    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send('This command has been disabled.')
        return

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
        return

    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.UserInputError):
        await ctx.send("Invalid input.")
        await ctx.send("!help")
        return

    if isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send('This command cannot be used in direct messages.')
        except discord.Forbidden:
            pass
        return

    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")
        return




bot.run(TOKEN)
