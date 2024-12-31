import os
import random
import string
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="°", intents=intents)

PASSWORD_FILE = "passwords.txt"

async def on_ready():
    print(f"El bot {bot.user.name} se ha iniciado correctamente.")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, ¿cómo estás?")


@bot.command()
async def contra(ctx, longitud: int = 12):
    if longitud < 6:
        await ctx.send("La longitud mínima de la contraseña debe ser 6 caracteres.")
        return

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

    await ctx.send("¿Para qué servicio es esta contraseña?")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        respuesta = await bot.wait_for("message", check=check, timeout=30.0)
        servicio = respuesta.content

        with open(PASSWORD_FILE, "a") as file:
            file.write(f"Servicio: {servicio} | Contraseña: {contrasena}\n")

        await ctx.send(f"Tu contraseña para el servicio `{servicio}` es: `{contrasena}`\n¡Ha sido guardada con éxito!")

    except TimeoutError:
        await ctx.send("No respondiste a tiempo. Por favor, intenta de nuevo.")

@bot.command()
async def ver_contra(ctx):
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            contenido = file.read()
        if contenido:
            await ctx.send(f"**Contraseñas guardadas:**\n```\n{contenido}\n```")
        else:
            await ctx.send("No hay contraseñas guardadas.")
    else:
        await ctx.send("Aún no se ha guardado ninguna contraseña.")

@bot.command()
async def borrar_contra(ctx):
    if os.path.exists(PASSWORD_FILE):
        os.remove(PASSWORD_FILE)
        await ctx.send("¡Todas las contraseñas han sido borradas!")
    else:
        await ctx.send("No hay contraseñas guardadas para borrar.")

@bot.command()
async def ayuda(ctx):
    comandos = """
    **Lista de comandos disponibles:**
    °hola - Saluda al bot.
    °contra <longitud> - Genera una contraseña segura y pregunta para qué servicio es, luego la guarda.
    °ver_contras - Muestra todas las contraseñas guardadas.
    °borrar_contras - Borra todas las contraseñas guardadas.
    """
    await ctx.send(comandos)

bot.run("ACA TU TOKEN")

