import discord
import json
import shared


async def run(message: discord.Message, args: list, settings: dict):
    if len(args) < 2:
        await message.channel.send(f"syntax is `{settings['prefix']}reaction <emoji> role_id`")
        return


    reference: discord.MessageReference = message.reference
    if reference is None:
        await message.channel.send("reply to the message")
        return

    reference: discord.Message = await message.channel.fetch_message(reference.message_id)

    if args[0] == "remove":
        if reference.id in shared.reaction_roles:
            if args[1] in shared.reaction_roles[reference.id]:
                del shared.reaction_roles[reference.id][args[1]]

            if len(shared.reaction_roles[reference.id]) == 0:
                del shared.reaction_roles[reference.id]
        try:
            await reference.clear_reaction(args[1])
        except Exception:
            pass

    await message.channel.send("removed it i think")
    return

    args[0] = args[0].split(":")[2]
    try:
        emoji = await message.channel.guild.fetch_emoji(int(args[0]))
        args[0] = emoji.name
    except Exception:
        pass

    if not args[1].isnumeric():
        await message.channel.send("role_id must be an integer")
        return

    try:
        await reference.add_reaction(args[0])
    except discord.NotFound:
        await message.channel.send("invalid emoji")

    if reference.id not in shared.reaction_roles:
        shared.reaction_roles[reference.id] = {}


    shared.reaction_roles[reference.id][args[0]] = int(args[1])
    with open("reaction_roles.json", "w") as f:
        json.dump(shared.reaction_roles, f, indent=2)

