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
async def bien(ctx):
    await ctx.send("¡Qué bacano! ¿Qué deseas hacer?")

@bot.command()
async def suma(ctx, num1: int, num2: int):
    resultado = num1 + num2
    await ctx.send(f"La suma de {num1} + {num2} = {resultado}")

@bot.command()
async def emoji(ctx):
    emojis = ["😀", "😂", "🥳", "😎", "😍", "😢", "😡"]
    random_emoji = random.choice(emojis)
    await ctx.send(random_emoji)

@bot.command()
async def contaminacion(ctx):
    mensaje = """
    🌍 **¿Qué es la contaminación?**
    La contaminación es la introducción de sustancias o energías dañinas en el medio ambiente que afectan la salud de los seres vivos y el equilibrio ecológico.
    
    **Tipos de contaminación:**
    - Aire: Emisiones de vehículos e industrias.
    - Agua: Desechos industriales y plásticos.
    - Suelo: Pesticidas y basura.
    - Ruido: Tráfico y construcciones.

    ¡Cada acción cuenta para combatirla! Usa `°reducir_impacto` para obtener consejos prácticos. 💪
    """
    await ctx.send(mensaje)

@bot.command()
async def impacto(ctx):
    mensaje = """
    **Impacto de la contaminación:**
    - **Salud humana:** Causas de enfermedades respiratorias, cardiovasculares y cáncer.
    - **Ecosistemas:** Pérdida de biodiversidad, contaminación de suelos y agua.
    - **Cambio climático:** Emisiones de gases de efecto invernadero provocan el calentamiento global.
    """
    await ctx.send(mensaje)

@bot.command()
async def reducir_impacto(ctx):
    mensaje = """
    **Consejos para reducir tu impacto ambiental:**
    1. **Recicla**: Separa tus desechos y recicla materiales como papel, vidrio y plástico.
    2. **Usa transporte sostenible**: Camina, usa la bicicleta o el transporte público.
    3. **Ahorra energía**: Apaga las luces y dispositivos electrónicos cuando no los uses.
    4. **Consume responsablemente**: Evita productos con excesivos empaques plásticos.
    5. **Planta árboles**: Los árboles ayudan a reducir el CO2 y mejoran la calidad del aire.
    """
    await ctx.send(mensaje)

@bot.command()
async def ahorro_energia(ctx):
    mensaje = """
    **Consejos para ahorrar energía en casa:**
    1. Apaga las luces cuando no las necesites.
    2. Usa bombillas de bajo consumo (LED).
    3. Desenchufa los aparatos electrónicos que no uses.
    4. Usa electrodomésticos eficientes.
    5. Aprovecha la luz natural durante el día.
    """
    await ctx.send(mensaje)

@bot.command()
async def movilidad_sostenible(ctx):
    mensaje = """
    **Consejos de movilidad sostenible:**
    1. Camina o usa la bicicleta para distancias cortas.
    2. Opta por transporte público o comparte el coche (carpooling).
    3. Si puedes, elige un vehículo eléctrico o híbrido.
    4. Planifica tus viajes para evitar trayectos innecesarios.
    """
    await ctx.send(mensaje)

@bot.command()
async def quiz(ctx):
    preguntas = [
        {"pregunta": "¿Cuál de estos gases es el principal causante del cambio climático?", "respuestas": ["CO2", "O2", "N2"], "correcta": "CO2"},
        {"pregunta": "¿Qué es reciclable?", "respuestas": ["Plástico", "Comida", "Ropa"], "correcta": "Plástico"},
        {"pregunta": "¿Cuál de estos es un contaminante del aire?", "respuestas": ["CO2", "O2", "H2O"], "correcta": "CO2"},
    ]
    pregunta = random.choice(preguntas)
    await ctx.send(pregunta["pregunta"])
    await ctx.send("\n".join([f"{i+1}. {respuesta}" for i, respuesta in enumerate(pregunta["respuestas"])]))
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        respuesta = await bot.wait_for("message", check=check, timeout=30.0)
        if respuesta.content.lower() == pregunta["correcta"].lower():
            await ctx.send("¡Correcto! 🎉")
        else:
            await ctx.send(f"Incorrecto. La respuesta correcta era: {pregunta['correcta']}")
    except TimeoutError:
        await ctx.send("El tiempo se ha agotado. ¡Inténtalo de nuevo!")

@bot.command()
async def reto(ctx):
    retos = [
        "No uses plásticos de un solo uso durante 24 horas.",
        "Camina o usa la bicicleta para tus próximos 5 viajes.",
        "Recicla todo el material posible hoy.",
        "Planta un árbol o una planta en tu jardín o balcón.",
    ]
    reto = random.choice(retos)
    await ctx.send(f"¡Te reto a hacer esto! {reto}")

@bot.command()
async def mi_huella(ctx):
    mensaje = """
    **Calcula tu huella de carbono:**
    Responde las siguientes preguntas para obtener una estimación de tu huella de carbono.
    
    1. ¿Cuántos kilómetros recorres al mes en coche? (por ejemplo: 500)
    """
    await ctx.send(mensaje)
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        km = await bot.wait_for("message", check=check, timeout=30.0)
        km = int(km.content) if km.content.isdigit() else 0
        

        huella = km * 0.21
        await ctx.send(f"Tu huella de carbono estimada por el coche es de {huella} kg de CO2 al mes.")
    except TimeoutError:
        await ctx.send("Tiempo agotado. ¡Inténtalo de nuevo!")

@bot.command()
async def frase(ctx):
    frases = [
        "La Tierra no es una herencia de nuestros padres, es un préstamo de nuestros hijos. - Proverbio indígena",
        "No hay un planeta B. - Anónimo",
        "La naturaleza nunca se apura, pero todo se logra. - Lao Tzu",
        "Cada acción cuenta. - Anónimo",
    ]
    await ctx.send(random.choice(frases))

@bot.command()
async def progreso(ctx):
    mensaje = """
    **¡Sigue tu progreso!**
    Realiza las acciones ecológicas y lleva un registro:
    1. Apaga las luces cuando no las necesites.
    2. Usa transporte público o bicicleta.
    3. Recicla todos los materiales posibles.
    4. Planta un árbol.
    5. Usa menos plástico.
    ¡Tu compromiso hace la diferencia! 🌱
    """
    await ctx.send(mensaje)

@bot.command()
async def elegir(ctx, *opciones):
    if opciones:
        eleccion = random.choice(opciones)
        await ctx.send(f"He elegido: {eleccion}")
    else:
        await ctx.send("Por favor, proporciona opciones para elegir.")

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
    °contaminacion - Explica qué es la contaminación.
    °impacto - Muestra el impacto de la contaminación en la salud y el ambiente.
    °reducir_impacto - Consejos prácticos para reducir tu impacto ambiental.
    °ahorro_energia - Consejos para ahorrar energía en tu hogar.
    °movilidad_sostenible - Sugerencias para usar transporte más ecológico.
    °quiz - Realiza un cuestionario sobre el medio ambiente.
    °reto - Reta al usuario a realizar una acción ecológica.
    °mi_huella - Calcula tu huella de carbono.
    °frase - Envía una frase motivacional sobre la sostenibilidad.
    °progreso - Proporciona ideas para seguir tu progreso ecológico.
    °hola - Saluda al bot.
    °bien - Responde a 'bien'.
    °suma <num1> <num2> - Suma dos números.
    °emoji - Envía un emoji al azar.
    °elegir <opción1> <opción2> ... - Elige una opción al azar.
    °hola - Saluda al bot.
    °contra <longitud> - Genera una contraseña segura y pregunta para qué servicio es, luego la guarda.
    °ver_contras - Muestra todas las contraseñas guardadas.
    °borrar_contras - Borra todas las contraseñas guardadas.
    """
    await ctx.send(comandos)

bot.run("ACA TU TOKEN")
