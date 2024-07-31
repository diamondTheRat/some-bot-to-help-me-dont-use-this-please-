import discord


async def run(message: discord.Message, args: list, settings: dict):
    if len(args) == 0 or args[0].isnumeric() == False:
        return

    number = int(args[0])

    await message.channel.purge(limit=number + 1)
    await message.channel.send(f"deleted {number} message{'s' if number > 1 else ''}", delete_after=5)