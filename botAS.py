# =================================================================
#   Author:         Aaron Shingleton
#   Last Modified:  10/12/2023
#   Purpose:        Skeleton template of a discord bot
# =================================================================

import discord
from discord import app_commands
import responsesAS
import random
from discord.ext import commands
from discord import Intents

# EVENT SYNTAX
# @client.event
# async def {API event}(args)
#     event code

# COMMAND SYNTAX
# @tree.command(name="", description?="", guild?=guild_id, guilds? = [])
# @app_commands.describe(name=arg1 = "")
# async def myCommand(interactionVariable = discord.Interaction, arg1?: type, arg2?...)

# initializes the bot
TOKEN = ''
intents = discord.Intents.default()
intents.message_content = True


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False  # we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  # check if slash commands have been synced
            await tree.sync(guild=discord.Object(
                id=1164402314468139028))  # guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)


@client.event
async def send_message(message, user_message, is_private):
    try:
        response = responsesAS.get_response(user_message)
        if response is not None:
            await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


# BOT RESPONSES TO MESSAGES (COMMANDS, CUSTOM MESSAGES)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' in ({channel})")

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

    # EMOJI REACTION EVENT
    ### SEE https://www.youtube.com/watch?v=MgCJG8kkq50
    @client.event
    async def on_raw_reaction_add(payload):
        # payload variable contains properties that identify
        # individual messages
        message_id = payload.message_id
        if message_id == 1164430733817954315:  # placeholder, Needs to be updated when added to any server
            # message ID should be copied from message in existing channel
            # i.e. when a user reacts to MESSAGE_ID message, then...
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            # Branches for specific emoji
            if payload.emoji.name == 'ComputerScience':  # :placeholder:
                role = discord.utils.get(guild.roles,
                                         name="Computer Science")  # Name of role | if role's name == emoji's name, then no need to check
            elif payload.emoji.name == 'CyberSecurity':
                role = discord.utils.get(guild.roles, name="Cyber Security")
            elif payload.emoji.name == 'InformationSystems':
                role = discord.utils.get(guild.roles, name="Information Systems")
            elif payload.emoji.name == 'InformationTechnology':
                role = discord.utils.get(guild.roles, name="Information Technology")
            elif payload.emoji.name == 'Alumni':
                role = discord.utils.get(guild.roles, name="Alumni")
            elif payload.emoji.name == 'GradSchool':
                role = discord.utils.get(guild.roles, name="Grad-School")
            # Catch-all statement for assigning role when role's name matches the emoji's name
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            # ASSIGNING ROLE
            if role is not None:
                member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
                if member is not None:
                    await member.add_roles(role)
                else:
                    print(f"{member} not found.")
            else:
                print(f"{role} not found.")


@client.event
async def on_raw_reaction_remove(payload):
    # payload variable contains properties that identify
    # individual messages
    message_id = payload.message_id
    if message_id == 1164446737520406538:  # placeholder
        # message ID should be copied from message in existing channel
        # i.e. when a user reacts to MESSAGE_ID message, then...
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

        # Branches for specific emoji
        if payload.emoji.name == 'ComputerScience':  # :placeholder:
            role = discord.utils.get(guild.roles,
                                     name="Computer Science")  # Name of role | if role's name == emoji's name, then no need to check
        elif payload.emoji.name == 'CyberSecurity':
            role = discord.utils.get(guild.roles, name="Cyber Security")
        elif payload.emoji.name == 'InformationSystems':
            role = discord.utils.get(guild.roles, name="Information Systems")
        elif payload.emoji.name == 'InformationTechnology':
            role = discord.utils.get(guild.roles, name="Information Technology")
        elif payload.emoji.name == 'Alumni':
            role = discord.utils.get(guild.roles, name="Alumni")
        elif payload.emoji.name == 'GradSchool':
            role = discord.utils.get(guild.roles, name="Grad-School")
        # Catch-all statement for assigning role when role's name matches the emoji's name
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        # ASSIGNING ROLE
        if role is not None:
            member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Test1")
                print(f"{member} not found.")
        else:
            print("Test2")
            print(f"{role} not found.")


@tree.command(guild = discord.Object(id=1164402314468139028), name='roll', description='Rolls dice using text')
@app_commands.describe(dice = "1d20 = one 20-sided die roll")
async def do_roll(ctx: discord.Interaction, dice: str = "1d20"):
    try:
        rolls, sides = map(int, dice.split('d'))
        print(f"Rolls: {rolls}    Sides: {sides}")
        print(f"{ctx.user.display_name}")
        results = [random.randint(1, sides) for _ in range(rolls)]
        await ctx.response.send_message(f"{ctx.user.display_name} rolled {rolls}d{sides}: {', '.join(map(str, results))}")

    except Exception as e:
        await ctx.response.send_message("Invalid input. Use !roll (rolls)d(sides) format, e.g., !roll 1d20")

@tree.command(name="dnd5e", description="Provides link to DnDBeyond reference webpage",
              guild=discord.Object(id=1164402314468139028))
async def dnd_ref(interaction: discord.Interaction, category: str = "", values: str = ""):
    dnd_url = "https://www.dndbeyond.com/"
    if category is not "":
        dnd_url += f"{category}/"
        if values is not "":
            dnd_url += f"{values}"

    await interaction.response.send_message(dnd_url)

client.run(TOKEN)
