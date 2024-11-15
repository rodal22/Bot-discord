import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

Aca = commands.Bot(command_prefix="°",intents=intents)

@Aca.event 
async def on_ready():
    print("se inicio el bot")

@Aca.command()
async def hola(ctx):
    await ctx.send("Hola, como estas")

@Aca.command()
async def Bien(ctx):
    await ctx.send("O q bacano q deceas")

@Aca.command()
async def suma(ctx,num1:int,num2:int):
    suma=num1+num2 
    await ctx.send(f"la suma de {num1} + {num2} = {suma}")

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

Aca.run("TOKEN ACA =)")
