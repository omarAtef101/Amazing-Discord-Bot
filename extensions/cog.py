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
    
    @commands.command()
    async def clear(self, ctx):
        print("clear command")
        if ctx.author.id == config["IDES"]["owner_userid"]:
            global_commands = await self.bot.http.get_global_commands(self.bot.application_id)
            for command in global_commands:
                await self.bot.http.delete_global_command(self.bot.application_id, command['id'])

            async for guild in self.bot.fetch_guilds():
                guild_commands = await self.bot.http.get_guild_commands(self.bot.application_id, guild.id)
                for command in guild_commands:
                    await self.bot.http.delete_guild_command(self.bot.application_id, guild.id, command['id'])
        await ctx.send('All tree app commands are cleared.\nSync Now!')
            
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
    
    @app_commands.command(name="play", description="Choose a funny game!")
    async def play(self, interaction: discord.Interaction, game: Game):
        if game.value == 0:
            game = eXit_Game()
            await game.send(interaction)

async def setup(bot: core.Bot) -> None:
    await bot.add_cog(MyCog(bot))