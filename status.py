import discord
from discord.ext import commands
from discord.ui import View, Button

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Status Cog carregado!")

    async def send_status_menu(self, interaction_or_ctx):
        """Gera e envia o menu de status."""

        nome = "Jogador Desconhecido"
        motivacao = "Motivação não definida"
        idade = "Idade não definida"
        estrelas = 0
        forca = "Ogro"
        velocidade = "Ogro"
        resistencia = "Ogro"
        classe = "Ainda não definida"
        raca = "Ainda não definida"
        social = "Ainda não definido"
        prodigio = "Ainda não definido"

        embed = discord.Embed(
            title="Sistema - Status",
            description=(
                "‧˚₊꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒦꒷‧₊˚⊹\n\n"
                f"🎭 **Jogador**: {nome}\n"
                f"✨ **Motivação**: {motivacao}\n"
                f"📅 **Idade**: {idade}\n"
                f"⚔️ **Classe**: {classe}\n"
                f"👑 **Social**: {social}\n"
                f"🧠 **Prodígio**: {prodigio}\n"
                f"🧬 **Raça**: {raca}\n\n"
                "Status Atuais:\n\n"
                f"➤ **Força**: {forca}\n"
                f"➤ **Velocidade**: {velocidade}\n"
                f"➤ **Resistência mental**: {resistencia}\n"
                f"➤ **Mana**: 10%\n\n"
                f":dizzy: **Estrelas**: {estrelas}\n\n"
                "‧˚₊꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒷꒦︶︶︶︶︶︶︶︶︶︶︶꒦꒷‧₊˚⊹"
            ),
            color=discord.Color.green()
        )
        embed.set_image(url="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaF2MbX2f6m1184lVOlUEI0bnpZi_16w2nLNv8a1cyi8qxWsgpbs0kdSz-5biTdKta00ZWUSICFGJC0oSbMsvfWOYNVuOR9uMtth3IP07yzmKGrzD3pT2wstTyqubKJMf7HtWyEFC8JQk7n1dHF-OoSjnmTr_1wFbeBjAICcJBQYSNi7n0Z88-J3qxoB9o/w640-h362/Captura%20de%20tela%202024-01-21%20134611.png")

        if isinstance(interaction_or_ctx, discord.Interaction):
            await interaction_or_ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction_or_ctx.send(embed=embed)

    @commands.command(name="status")
    async def show_status(self, ctx):
        """Mostra os status do jogador através do comando."""
        await self.send_status_menu(ctx)

    async def status_button_callback(self, interaction):
        """Callback do botão de status no menu principal."""
        await self.send_status_menu(interaction)

async def setup(bot):
    await bot.add_cog(Status(bot))
