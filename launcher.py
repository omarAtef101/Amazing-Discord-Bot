import asyncio

import discord

import core



bot = core.Bot()
bot.run(token=core.config["TOKENS"]["discord"])

