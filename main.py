'''
Impersonator bot for Discord
'''
import re
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='')

urlregex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)' +
                    r'+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

@client.event
async def on_ready():
    '''
    Loading the thing.
    '''
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online,
        activity=discord.Game("github.com/ajlee2006/discord-impersonator"))


@client.command(aliases = ["impersonator"])
async def impersonate(ctx, *msg):
    '''
    Does the stuff.
    '''
    print(msg)
    webhooks = await ctx.channel.webhooks()
    print(len(webhooks))

    webhook = None
    for awebhook in webhooks:
        if awebhook.name == "impersonator":
            webhook = awebhook
    if webhook is None:
        webhook = await ctx.channel.create_webhook(name="impersonator")

    username = msg[0]
    avatar_url = None
    content = msg[1]
    embed = None

    contentis = 1

    if re.match('<@!?[0-9]+>',username):
        userid = int(re.search('<@!?([0-9]+)>',msg[0]).group(1))
        print(userid)
        userpinged = await ctx.guild.query_members(user_ids=[userid])
        userpinged = userpinged[0]
        print(userpinged)
        username = userpinged.nick
        print(userpinged.nick)
        if username is None:
            username = userpinged.name
            print(userpinged.name)
        avatar_url = userpinged.avatar_url

    if re.match(urlregex, content.strip()) is not None:
        avatar_url = content
        content = msg[2]
        contentis = 2

    if content == "embed":
        content = ""
        colour = discord.Colour.blurple()
        if (len(msg) > contentis+3 and
            msg[contentis+3].isdigit() and int(msg[contentis+3]) < 16777216):
            colour = discord.Colour(int(msg[contentis+3]))
        embed = discord.Embed(title=msg[contentis+1], description=msg[contentis+2], colour=colour)

    # attachments
    files = None
    if ctx.message.attachments is not None and len(ctx.message.attachments) > 0:
        files = [await i.to_file() for i in ctx.message.attachments]

    await webhook.send(content=content, username=username,
        avatar_url=avatar_url, embed=embed, files=files)

    if msg[-1] == "delete":
        await ctx.message.delete()

client.run(os.environ.get('BOT_TOKEN'))
