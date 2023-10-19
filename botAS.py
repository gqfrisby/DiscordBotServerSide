#=================================================================
#   Author:         Aaron Shingleton
#   Last Modified:  10/12/2023
#   Purpose:        Skeleton template of a discord bot
#=================================================================

import discord
import responsesAS

# TODO: Use .env file to pull in TOKEN, other environment variables instead of hardcoding into source
# import os
# from dotenv import load_dotenv
# load_dotenv()

# async def send_message(message, user_message, isDM):
#     try:
#         response = handle_response(user_message)
#         await message.author.send(response) if (is_private) else await message.channel.send(response)
#     except Exception as e:
#         print(e)

### EVENT SYNTAX
### @client.event
### async def {API event}(args)
###     event code


# RUNNING THE BOT
def run_discord_bot():
    # Establish bot instance using token; get client
    TOKEN = 'MTE2MTM3NTcwMTg0NTQyMjExMQ.GnVplh.S5N60SV8uDNOZA3osmJouzkxU6r1aT3B-yuejY'
    # TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # BOT STARTUP
    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')

    @client.event
    async def send_message(message, user_message, is_private):
        try:
            response = responsesAS.get_response(user_message)
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
        if message_id == 1164430733817954315: # placeholder, Needs to be updated when added to any server
            # message ID should be copied from message in existing channel
            # i.e. when a user reacts to MESSAGE_ID message, then...
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            # Branches for specific emoji
            if payload.emoji.name == 'ComputerScience': # :placeholder:
                role = discord.utils.get(guild.roles, name="Computer Science") # Name of role | if role's name == emoji's name, then no need to check
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
        if message_id == 1164446737520406538: # placeholder
            # message ID should be copied from message in existing channel
            # i.e. when a user reacts to MESSAGE_ID message, then...
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            # Branches for specific emoji
            if payload.emoji.name == 'ComputerScience': # :placeholder:
                role = discord.utils.get(guild.roles, name="Computer Science") # Name of role | if role's name == emoji's name, then no need to check
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

    # Logs in bot in Discord - green dot in Discord => bot is running
    client.run(TOKEN)
