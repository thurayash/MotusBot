import discord

client = discord.Client()

@client.event
async def on_ready():
    print("I'm ready to play!")

@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    
    if (message.content.startswith("ping")):
        await message.channel.send("pong!")
    
    if (message.content == "blue"):
        await message.add_reaction("\U0001F499")


client.run('OTY2OTk2NTE1ODE2MDc5NDMw.YmJ3rw.ucwzVoE0mYLKQesNIvJ2UeAgZgA')
