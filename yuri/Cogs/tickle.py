import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Tickle(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.guild_only()
    async def tickle(self,ctx):
        if ctx.guild.id not in conf.act2:
            laughs1 = ["Oh! Hehehe!", "P-Please! Stop it! Ehehe!", "Hey, that tickles! Hahaha!", "HAHAHAHAHAHA! *snort*", "H-Hey! That's my ticklish spot!! :laughing:"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(laughs1))

        elif ctx.guild.id in conf.act2:
            laughs2 = ["Ahahaha! Yes, just like that!", "HEHEHEHEHEHEHE!!!", "Hahahahahaha!!!", "AHAHAHAHAHAHAHAHAHA!!!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(laughs2))

def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Tickle(bot))
