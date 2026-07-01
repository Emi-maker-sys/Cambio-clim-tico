import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
import pyttsx3
load_dotenv()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("vulume", 1.0)

bot = commands.Bot(command_prefix="!", intents=intents)

datos = [
    "Los oceanos absorben más del 90% del calor generado en la Tierra.",
    "Las capas de hielo de Groenlandia y la Antártida pierden cientos de miles de millones de toneladas de hielo al año.",
    "El rendimiento agrícola mundial podría disminuir hasta un 30% para 2050 si no se toman medidas.",
    "El agua marina se ha vuelto un 30% más ácida desde la Revolución Industrial, afectando corales y vida marina.",
    "El clima extremo propicia la expansión de enfermedades transmitidas por vectores, como el paludismo y el dengue.",
    "Los niveles actuales de dióxido de carbono (CO₂) en la atmósfera son los más altos registrados en los últimos 800,000 años.",
    "El Polo Norte se está calentando a un ritmo dos veces más rápido que el promedio mundial, acelerando la pérdida de hielo marino y el hábitat de especies endémicas.",
    "El aumento sostenido de las temperaturas está provocando cambios drásticos en la duración de las estaciones, ocasionando que los inviernos sean más cortos y los veranos más largos.",
    "Las últimas décadas han sido el periodo más cálido del planeta en los últimos 125,000 años.",
    "El sapo dorado (nativo de Costa Rica) es considerado una de las primeras especies extintas oficialmente a causa del calentamiento global, al no poder adaptarse a la alteración de su hábitat húmedo en 1989.",
    "Las sequías, inundaciones y tormentas extremas amenazan con empujar a la pobreza extrema a más de 130 millones de personas, obligándolas a abandonar sus hogares.",
    "Los científicos alertan de que una de cada seis especies animales y vegetales de la Tierra podría enfrentarse a la extinción si los ecosistemas continúan alterándose al ritmo actual.",
    "La capacidad de energía eléctrica que generan los huracanes se estima que equivale a la mitad de toda la energía utilizada en el mundo, siendo más destructivos cuando las aguas superficiales del océano son más cálidas.",
    "La generación de electricidad, el calor y el uso de carbón, petróleo y gas representan la gran mayoría de las emisiones causantes del efecto invernadero.",
    "Los científicos calculan que para el año 2100, la temperatura media de la Tierra podría aumentar entre 1.1°C y hasta 6.7°C.",
]

def speak (text):
    engine.say(text)
    engine.runAndWait()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def dato(ctx):
    """Envía un dato curioso aleatorio."""

    text = random.choice(datos)
    await ctx.send(text)
    speak(text)

bot.run(TOKEN)