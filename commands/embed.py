import discord


embed = discord.Embed(title="Update logs", description="might be the last who knows", color=0x0F0FFF)

async def run(message: discord.Message, args: list, settings: dict):
    content = message.content.splitlines()
    content[0] = content[0][6 + len(settings["prefix"]):]

    embed = discord.Embed(title=content.pop(0), color=settings["color"])

    name = ""
    value = ""

    for line in content:
        if line == "": continue
        if line.startswith("#"):
            if name != "":
                embed.add_field(name=name, value=value, inline=False)
                name = line[1:]
                value = ""
            else:
                name = line[1:]
        else:
            value += f"\n{line}"

    embed.add_field(name=name, value=value, inline=False)

    await message.channel.send(embed=embed)
    await message.delete()