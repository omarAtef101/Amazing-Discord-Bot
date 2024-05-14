from __future__ import annotations

from .config import config

from discord.ext import commands
import discord
import logging

logger: logging.Logger = logging.getLogger(__name__)

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            intents=intents, 
            command_prefix=config['OPTIONS']['prefixes']
            )
    
    async def setup_hook(self) -> None:
        await self.load_extension("extensions")
    
    async def on_ready(self) -> None:
        logger.info("Logged in as %s | %d", self.user, self.user.id)