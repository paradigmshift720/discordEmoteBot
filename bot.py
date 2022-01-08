import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
import config
 
bot = commands.Bot(command_prefix = 'prefix')
 
@bot.event
async def on_ready():
    print ("welcome_msg")
 
async def react(message):
    custom_emojis = [
    "<:grog:929288598430285824>"                                     # emoji ids need the quotations ie. "" keep them                                          
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
        # print(emoji, guild_emoji_names)                # debugging your shite remove the "#" if you wanna see print in cmd console
        # print(emoji in guild_emoji_names)
        if emoji in guild_emoji_names:
            await message.add_reaction(emoji)
 
@bot.event                                             
async def on_message(message):
    if message.channel.id == config.channelId:                # remove this line == the bot reacts to everyone in the channel                 
            await react(message)                        # channelid and authorid do not need quotations ie. "" remove them
 
bot.run(config.server)
 



