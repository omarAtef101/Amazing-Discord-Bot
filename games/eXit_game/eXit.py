from __future__ import annotations

import discord



class eXit_Game(discord.ui.View):
    async def send(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=self.create_embade(), view=self)
    
    def create_embade(slef):
        embed = discord.Embed(
            title="Test",
            description="this is an embed",
        )
        embed.set_image(url="https://cdn.mos.cms.futurecdn.net/A2zZsEd4niP9KVPJFpMyfH-925-80.jpg.webp")
        return embed
    
    @discord.ui.button(label="Test", style=discord.ButtonStyle.primary)
    async def test(self, interaction: discord.Integration, button: discord.Button):
        await interaction.response.defer()
        