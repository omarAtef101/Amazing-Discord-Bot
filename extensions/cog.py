from discord import app_commands
from discord.ext import commands
import discord
import core

from core import config

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
                self.bot = bot
    
    @commands.command()
    async def sync(self, ctx):
        print("sync command")
        if ctx.author.id == config["IDES"]["owner_userid"]:
            await self.bot.tree.sync()
            await ctx.send('Command tree synced.')
        else:
            await ctx.send('You must be the owner to use this command!')
    
    @app_commands.command(name="hey", description="This is a command!")
    async def hey(self, interaction: discord.Interaction):
        await interaction.response.send_message("HEY!")

async def setup(bot: core.Bot) -> None:
    await bot.add_cog(MyCog(bot))