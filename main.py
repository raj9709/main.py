import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix = "!")

client.remove_command('help')


@client.event

async def on_ready():

    print("Bot is currently online!")



    #help command

    @client.command(pass_context=True)

    async def help(ctx):

        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Colour.orange()

        )


        embed.set_author(name="Help")

        embed.add_field(name="!help",value="Help command",inline=False)

        channel = await author.create_dm()

        await channel.send(author,embed=embed)

        await ctx.message.channel.send("Message sent to your DMs")




TOKEN = os.environ.get("OTIzNzk0OTE0MzI2NzQxMDYz.YcVNDg.8t6MvHqZnzbtidxqS7B_YpPRmnw")

client.run("OTIzNzk0OTE0MzI2NzQxMDYz.YcVNDg.8t6MvHqZnzbtidxqS7B_YpPRmnw")