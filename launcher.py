import asyncio
import discord
import core



discord.utils.setup_logging(level=core.config["OPTIONS"]["logging"])


async def main() -> None:
    bot = core.Bot()
    await bot.start(core.config["TOKENS"]["discord"])

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass