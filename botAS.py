#=================================================================
#   Author:         Aaron Shingleton
#   Last Modified:  10/12/2023
#   Purpose:        Skeleton template of a discord bot
#=================================================================

import discord
import responsesAS
from responsesAS import handle_response

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
    TOKEN = 'MTE2MTM3NTcwMTg0NTQyMjExMQ.GScZho.chnwZv88-STZ5r897bTNA8ywMxBlrfaPoNrFG0'
    # TOKEN = os.getenv('TOKEN')
    client = discord.Client()

    # BOT STARTUP
    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')

    # BOT RESPONSES TO MESSAGES (COMMANDS, CUSTOM MESSAGES)
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in ({channel})")

    # EMOJI REACTION EVENT
    ### SEE https://www.youtube.com/watch?v=MgCJG8kkq50
    @client.event
    async def on_raw_reaction_add(payload):
            # payload variable contains properties that identify
            # individual messages
            if payload.message_id == -1: # placeholder
                # message ID should be copied from message in existing channel
                # i.e. when a user reacts to MESSAGE_ID message, then...
                guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)

                # Branches for specific emoji
                if payload.emoji.name == 'placeholder': # :placeholder:
                    role = discord.utils.get(guild.roles, name="ROLE") # Name of role | if role's name == emoji's name, then no need to check
                elif payload.emoji.name == 'otherPlaceholder':
                    role = discord.utils.get(guild.roles, name="otherROLE")
                # Catch-all statement for assigning role when role's nmame matches the emoji's name
                else:
                    role = discord.utils.get(guild.roles, name=payload.emoji.name)

                # ASSIGNING ROLE
                if role is not None:
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    if member is not None:
                        await member.add_roles(role)
                    else:
                        print(f"{member} not found.")
                else:
                    print(f"{role} not found.")
                    
    @client.event
    async def on_raw_reaction_remove(payload):
        # message ID above should be copied from message in existing channel
        # i.e. when a user reacts to MESSAGE_ID message, then...
        if payload.message_id == -1: # placeholder
                # guild = the guild that this bot is in where the payload is coming from
                guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)

                # Branches for specific emoji
                if payload.emoji.name == 'placeholder': # :placeholder: | Match emoji to conditional statement
                    role = discord.utils.get(guild.roles, name="ROLE") # Get name of role if name of role != name of emoji
                elif payload.emoji.name == 'otherPlaceholder':
                    role = discord.utils.get(guild.roles, name="otherROLE")
                # Catch-all statement for assigning role when role's name matches the emoji's name
                else:
                    role = discord.utils.get(guild.roles, name=payload.emoji.name)

                # ASSIGNING ROLE
                if role is not None:
                    # member = user that reacted to message in current guild
                    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                    # If found, add role to user
                    if member is not None:
                        await member.remove_roles(role)
                    else:
                        print(f"{member} not found.")
                else:
                    print(f"{role} not found.")

    # Logs in bot in Discord - green dot in Discord => bot is running
    client.run(TOKEN)
