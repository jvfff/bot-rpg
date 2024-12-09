import discord
from discord.ext import commands
from discord.ui import Button, View
from status import Status
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

class RoleplayBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def menu(self, ctx):
        """Comando que abre o menu interativo."""
        embed = discord.Embed(
            title="Sistema - Menu",
            description=(
                "‧˚₊꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒦꒷‧₊˚⊹\n\n"
                "˚。. ✦「✧」๑︵˚ ꒰ Elder World - RP :dizzy: ┋〃・魅\n\n"
                "➤ :fire: **Status** - Veja suas habilidades e atributos pessoais.\n\n"
                "➤ :school_satchel: **Inventário** - Confira os itens que conquistou ao longo do caminho.\n\n"
                "➤ :convenience_store: **Loja** - Adquira novos equipamentos e poções mágicas.\n\n"
                "➤ :crossed_swords: **Comandos** - Explore todos os nossos comandos personalizados!\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "Um caçador de Deuses, armado com aço e determinação, desafia o impossível, caminhando entre sombras e "
                "luzes antigas em busca de divindades que ousaram brincar com o destino dos mortais.\n\n"
                "‧˚₊꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒦꒷‧₊˚⊹"
            ),
            color=discord.Color.gold()
        )
        embed.set_image(url="https://zumaki.co.in/wp-content/uploads/2024/01/System.webp")

        status_button = Button(label="Status", style=discord.ButtonStyle.primary, emoji="🔥")
        inventory_button = Button(label="Inventário", style=discord.ButtonStyle.secondary, emoji="🎒")
        shop_button = Button(label="Loja", style=discord.ButtonStyle.success, emoji="🏪")
        commands_button = Button(label="Comandos", style=discord.ButtonStyle.danger, emoji="⚔️")

        async def status_callback(interaction):
            status_cog = bot.get_cog("Status")
            if status_cog:
                await status_cog.status_button_callback(interaction)
            else:
                await interaction.response.send_message("Erro: Cog de Status não está carregado.", ephemeral=True)

        async def inventory_callback(interaction):
            await interaction.response.send_message("Abrindo inventário...", ephemeral=True)

        async def shop_callback(interaction):
            await interaction.response.send_message("Abrindo loja...", ephemeral=True)

        async def commands_callback(interaction):
            await interaction.response.send_message("Abrindo comandos...", ephemeral=True)

        status_button.callback = status_callback
        inventory_button.callback = inventory_callback
        shop_button.callback = shop_callback
        commands_button.callback = commands_callback

        view = View()
        view.add_item(status_button)
        view.add_item(inventory_button)
        view.add_item(shop_button)
        view.add_item(commands_button)

        await ctx.send(embed=embed, view=view)

async def main():
    async with bot:
        await bot.add_cog(RoleplayBot(bot))
        await bot.load_extension("status")
        await bot.start(os.environ['TOKEN'])

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())