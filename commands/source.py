import discord


async def run(message: discord.Message, args: list, settings: dict):
    reference: discord.MessageReference = message.reference
    if reference is None:
        await message.channel.send("reply to the message you want the source of")
        return

    reference: discord.Message = await message.channel.fetch_message(reference.message_id)
    if len(reference.embeds) == 0:
        await message.channel.send("message has no embed")
        return

    for embed in reference.embeds:
        msg = f"```\n{settings['prefix']}embed {embed.title}"

        for field in embed.fields:
            msg += f"\n# {field.name}\n{field.value}"
        msg += "\n```"
        await message.channel.send(msg)