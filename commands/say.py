import discord


async def run(message: discord.Message, args: list, settings: dict):
    await message.channel.send(" ".join(args))
