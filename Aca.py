import os
import random
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

Aca = commands.Bot(command_prefix="°", intents=intents)

@Aca.event
async def on_ready():
    print("El bot se ha iniciado correctamente")

@Aca.command()
async def hola(ctx):
    await ctx.send("Hola, ¿cómo estás?")

@Aca.command()
async def bien(ctx):
    await ctx.send("¡Qué bacano! ¿Qué deseas hacer?")

@Aca.command()
async def suma(ctx, num1: int, num2: int):
    suma = num1 + num2
    await ctx.send(f"La suma de {num1} + {num2} = {suma}")

@Aca.command()
async def emojii(ctx):
    emojis = ["😀", "😂", "🥳", "😎", "😍", "😢", "😡"] 
    random_emoji = random.choice(emojis)
    await ctx.send(random_emoji)
 
@Aca.command()
async def meme(ctx):
    Carp = 'Bot1/images'
    Imgs = os.listdir(Carp)
    Img_Random = random.choice(Imgs)
    ruta = os.path.join(Carp, Img_Random)

    with open(ruta, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@Aca.command()
async def memanimales(ctx):
    Carp = 'Bot1/images/animales'
    Imgs = os.listdir(Carp)
    Img_Random = random.choice(Imgs)
    ruta = os.path.join(Carp, Img_Random)

    with open(ruta, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


Aca.run("ACA TU TOKEN")
