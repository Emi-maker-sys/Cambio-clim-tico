import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

datos = [
    "🌊Los oceanos absorben más del 90% del calor generado en la Tierra.",
    "🧊Las capas de hielo de Groenlandia y la Antártida pierden cientos de miles de millones de toneladas de hielo al año.",
    "El rendimiento agrícola mundial podría disminuir hasta un 30% para 2050 si no se toman medidas.",
    "🌊El agua marina se ha vuelto un 30% más ácida desde la Revolución Industrial, afectando corales y vida marina.",
    "🦠El clima extremo propicia la expansión de enfermedades transmitidas por vectores, como el paludismo y el dengue."
]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def dato(ctx):
    """Envía un dato curioso aleatorio."""
    await ctx.send(random.choice(datos))

bot.run(TOKEN)