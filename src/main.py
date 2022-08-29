import discord
from discord.ext import commands
import asyncio
from generate import generate
from datetime import datetime
from plot import Plot
import os
client=discord.Client()
# client=commands.Bot(command_prefix="!")
# def name(mem='u'):
@client.event
async def on_ready():
    sum=0
    for x in client.guilds:
        print(x)
        sum+=x.member_count
        # for y in x.members:
            # print(y)

    print(sum)
    print(len(client.guilds))
    activity = discord.Game(name=f"Loneliness", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("logged in as {0.user}".format(client))

d={}
# name()
@client.event
async def on_message(message):
    if message.content.startswith("!"):
        print('hi bb')
        idk=str(message.author)
        idk=idk[0:len(idk)-5]
        activity = discord.Game(name=f"Big Bren {idk}", type=3)
        await client.change_presence(status=discord.Status.idle, activity=activity)

        if message.author in d.keys():
            a = datetime.now()
            c=a-d[message.author]
            if c.total_seconds()<15:
                await message.channel.send(f"wait for {int(c.total_seconds())} seconds {message.author}")
                return
            d[message.author]=a
        else:
            a = datetime.now()
            d[message.author]=a
        mess=message.content[1:]
        mess=mess.lstrip()
        # lis=mess.split()
        # lis1=generate(lis[0])
        lis1=generate(mess)
        if len(lis1)==1:
            await message.channel.send("No such coin in the db")
        else:
            embed=discord.Embed(title=f"{lis1[0]}",description="May fluctuate",color=discord.Color(0xf1c40f))
            embed.add_field(name="price($)",value=lis1[1],inline=False)
            embed.add_field(name="Change in 24 hrs(%)",value=lis1[2],inline=False)
            embed.add_field(name="Change in a week (%)",value=lis1[3],inline=False)
            await message.channel.send(embed=embed)
    
    if message.content.startswith("plot!"):
        idk=str(message.author)
        idk=idk[0:len(idk)-5]
        activity = discord.Game(name=f"Big Bren {idk}", type=3)
        await client.change_presence(status=discord.Status.idle, activity=activity)
        if message.author in d.keys():
            a = datetime.now()
            c=a-d[message.author]
            if c.total_seconds()<15:
                await message.channel.send(f"wait for {int(c.total_seconds())} seconds {message.author}")
                return
            d[message.author]=a
        else:
            a = datetime.now()
            d[message.author]=a
        mess=message.content[5:]
        mess=mess.lstrip()
        lis1=generate(mess)
        # print(lis1[4])
        
        # print(img)
        if len(lis1)==1:
            await message.channel.send("No such coin in the db")
        else:
            ok=lis1[4][1:len(lis1[4])-1]
            # print(ok)
            # idk='BTC'
            Plot(ok)
            embed=discord.Embed()
            # data_stream.seek(0)
            chart = discord.File("images/fig1.png",filename="fig1.png")
            embed.set_image(url="attachment://fig1.png")
            await message.channel.send(embed=embed,file=chart)
            path="images/fig1.png"
            os.remove(path)



client.run(bot_token)
