
from os import environ, path
import discord
from json import load
from importlib import import_module
import shared
from settings import load_settings
from shared import settings as SETTINGS
from check_permissions import is_allowed
import constants
from rat import TOKEN


PREFIX = SETTINGS["prefix"]

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_message(message):
    if message.author.bot: return

    if not message.content.startswith(PREFIX): return
    if len(message.content) <= len(PREFIX): return

    msg = message.content.lower()[len(PREFIX):].split()

    command = msg[0]
    args = msg[1:] if len(msg) > 1 else []

    if message.author.id != constants.daddy:
        if path.exists(f'commands/{command}.py'):
            if not is_allowed(message.author.id, command):
                await message.reply(f"i only listen to daddy <@{daddy}>")
        return


    if path.exists(f'commands/{command}.py'):
        file = import_module(f'commands.{command}')
        await file.run(message, args, SETTINGS)


@bot.event
async def on_raw_reaction_add(payload):
    # Fetch the message and reaction from the payload
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji)

    main_server = await bot.fetch_guild(1230944124128067794)

    user = await main_server.fetch_member(int(payload.user_id))

    if user is None or user.bot:
        return

    # Check if the message has reaction roles assigned
    if message.id in shared.reaction_roles:
        # Check if the reaction emoji is in the reaction roles
        if payload.emoji.name in shared.reaction_roles[message.id]:
            # Get the role to assign
            role_id = shared.reaction_roles[message.id][payload.emoji.name]
            role = main_server.get_role(role_id)

            # Assign the role to the user
            if role:
                await user.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    # Fetch the message and reaction from the payload
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji)

    main_server = await bot.fetch_guild(1230944124128067794)

    user = await main_server.fetch_member(int(payload.user_id))

    if user is None or user.bot:
        return


    # Check if the message has reaction roles assigned
    if message.id in shared.reaction_roles:
        # Check if the reaction emoji is in the reaction roles
        if payload.emoji.name in shared.reaction_roles[message.id]:
            # Get the role to assign
            role_id = shared.reaction_roles[message.id][payload.emoji.name]
            role = main_server.get_role(role_id)

            # Assign the role to the user
            if role:
                await user.remove_roles(role)

bot.run(TOKEN)
