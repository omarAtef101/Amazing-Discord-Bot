import logging
import pathlib

from discord.ext import commands

import core


logger: logging.Logger = logging.getLogger(__name__)


async def setup(bot: core.Bot) -> None:
    extensions: list[str] = [f".{f.stem}" for f in pathlib.Path("extensions").glob("*[a-zA-Z].py")]
    loaded: list[str] = []

    for extension in extensions:
        try:
            await bot.load_extension(extension, package="extensions")
        except Exception as e:
            logger.error('Unable to load extension: "%s" > %s', extension, e)
        else:
            loaded.append(f"extensions{extension}")

    logger.info("Loaded the following extensions: %s", loaded)
    
async def teardown(bot: core.Bot) -> None:
    extensions: list[str] = [f".{f.stem}" for f in pathlib.Path("extensions").glob("*[a-zA-Z].py")]

    for extension in extensions:
        try:
            await bot.unload_extension(extension, package="extensions")
        except commands.ExtensionNotLoaded:
            pass