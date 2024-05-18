from discord import app_commands
from discord.ext import commands
import discord
import core

from core import config
from .options_ import Game

from games.eXit_game.eXit import eXit_Game

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
                self.bot = bot
    
    
    async def cog_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.NotOwner):
            await ctx.send('You must be the owner to use this command!')
        else:
            print(error)
    
    @commands.is_owner()
    @commands.command()
    async def clear(self, ctx):
        self.bot.tree.clear_commands(guild=None)
        await self.bot.tree.sync(guild=None)
        await ctx.send('All tree app commands are cleared.')

    @commands.is_owner()         
    @commands.command()
    async def sync(self, ctx):
        await self.bot.reload_extension("extensions")
        await self.bot.tree.sync(guild=None)
        await ctx.send('Command tree synced.')
    
    @app_commands.command(name="hey", description="This is a command!")
    async def hey(self, interaction: discord.Interaction):
        await interaction.response.send_message("HEY!")
    
    @app_commands.command(name="play", description="Choose a funny game!")
    async def play(self, interaction: discord.Interaction, game: Game):
        if game.value == 0:
            game = eXit_Game()
            await game.send(interaction)

async def setup(bot: core.Bot) -> None:
    await bot.add_cog(MyCog(bot))