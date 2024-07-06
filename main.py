from discord.ext import commands
from keep_alive import keep_alive
import os
#import secret
client = commands.Bot(command_prefix="okay neb ", self_bot=True)

# Declare Bot Variables here

monitor_guild_id = 664509279251726363
monitor_channel_id = 1249091913189949470
notification_channel_id = 1168865189366595735

@client.event
async def on_message(message):
    if message.channel.id == monitor_channel_id:
        if message.embeds:
            embed = message.embeds[0].to_dict()
            description = embed.get("description", "")
            author = embed.get("author", {}).get("name", "")

            if all(word in author for word in ("World", "Boss", "appeared!")):
                worldboss = description.split("\n")[0].split()[-1]
                if "Shiny" in description:
                    worldboss = "Shiny " + worldboss
                
                channel = client.get_channel(notification_channel_id)
                await channel.send(f"### WorldBoss: {worldboss}")

    elif message.guild.id == 799192078222753832:
        if client.user.mentioned_in(message):
            await message.add_reaction('👍')
    
@client.event
async def on_ready():
    print('Ready to Notify: ', client.user)

keep_alive()
client.run(os.environ["TOKEN"])