import discord
from discord.ext import commands
import asyncio
from generate import generate
from datetime import datetime

client=discord.Client()
# client=commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    sum=0
    for x in client.guilds:
        # print(x)
        sum+=x.member_count
    activity = discord.Game(name=f"{sum} members, {len(client.guilds)} servers", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("logged in as {0.user}".format(client))

d={}
@client.event
async def on_message(message):
    if message.content.startswith("!"):
        if message.author in d.keys():
            a = datetime.now()
            c=a-d[message.author]
            if c.total_seconds()<15:
                await message.channel.send(f"wait for a few seconds {message.author}")
                return
            d[message.author]=a
        else:
            a = datetime.now()
            d[message.author]=a
        mess=message.content[1:]
        lis1=generate(mess)
        if len(lis1)==1:
            await message.channel.send("No such coin in the db")
        else:
            embed=discord.Embed(title=f"{lis1[0]}",description="May fluctuate",color=discord.Color(0xf1c40f))
            embed.add_field(name="price($)",value=lis1[1],inline=False)
            embed.add_field(name="Change in 24 hrs(%)",value=lis1[2],inline=False)
            embed.add_field(name="Change in a week (%)",value=lis1[3],inline=False)
            await message.channel.send(embed=embed)



client.run(token)
