import discord
from discord.ext import commands
import requests
import my_secrets
from datetime import datetime
import asyncio


def get_csgo_hours(steam_id):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={my_secrets.STEAM_API_KEY}&steamid={steam_id}&format=json"
    response = requests.get(url)
    data = response.json()
    for game in data['response']['games']:
        if game['appid'] == 730:  # 730 es el AppID de CS:GO
            return game['playtime_forever'] / 60  # Convertir minutos a horas
    return

def get_fivem_hours(steam_id):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={my_secrets.STEAM_API_KEY}&steamid={steam_id}&format=json"
    response = requests.get(url)
    data = response.json()
    for game in data['response']['games']:
        if game['appid'] == 218:  
            return game['playtime_forever'] / 60  # Convertir minutos a horas
    return None

def get_reinbow_hours(steam_id):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={my_secrets.STEAM_API_KEY}&steamid={steam_id}&format=json"
    response = requests.get(url)
    data = response.json()
    for game in data['response']['games']:
        if game['appid'] == 359550 :  # 730 es el AppID de CS:GO
            return game['playtime_forever'] / 60  # Convertir minutos a horas
    return

def get_rust_hours(steam_id):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={my_secrets.STEAM_API_KEY}&steamid={steam_id}&format=json"
    response = requests.get(url)
    data = response.json()
    for game in data['response']['games']:
        if game['appid'] == 252490 :  # 730 es el AppID de CS:GO
            return game['playtime_forever'] / 60  # Convertir minutos a horas
    return

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)





@bot.event
async def on_ready():
    global mensaje_id_global
    print(f"{bot.user.name} ha iniciado sesión en Discord!")
    await bot.change_presence(activity=discord.Game(name="¡Eitr!"))


@bot.command()
async def test(ctx):
    await ctx.send('¡Hola! 👋')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def horas_csgo(ctx, *,steam_id):
    
    hours = get_csgo_hours(steam_id)
    if hours is not None:
        await ctx.send(f'Has jugado {hours:.2f} horas de CS:GO.')
    else:
        await ctx.send('No se encontraron horas jugadas para CS:GO.')


@bot.command()
async def horas_fivem(ctx, *,steam_id):
    hours = get_fivem_hours(steam_id)
    if hours is not None:
        await ctx.send(f'Has jugado {hours:.2f} horas de FiveM.')
    else:
        await ctx.send('No se encontraron horas jugadas para FiveM.')

@bot.command()
async def horas_rs6(ctx,*,steam_id):
    
    hours = get_reinbow_hours(steam_id)
    if hours is not None:
        await ctx.send(f'Has jugado {hours:.2f} horas de RS6.')
    else:
        await ctx.send('No se encontraron horas jugadas para RS6.')

@bot.command()
async def horas_rust(ctx, *,steam_id):
    hours = get_rust_hours(steam_id)
    if hours is not None:
        await ctx.send(f'Has jugado {hours:.2f} horas de rust.')
    else:
        await ctx.send('No se encontraron horas jugadas para rust.')

@bot.command()
async def sexo_anal(ctx):
    await ctx.send('Eso le gusta a tu mamá 😏')

# Que muestre la hora exacta sin milisegundos ni fehca en la que se ejecutó el comando
@bot.command()
async def hora(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'La hora: {current_time} es perfecto para hacerse una turbopaja')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "oinc oinc" in message.content.lower():
        await message.channel.send('https://media.discordapp.net/attachments/832209775625240586/834001284536991754/bypassing_discord_be_like.gif?ex=67d0ae79&is=67cf5cf9&hm=e44758c61fe5edb08ee67bd88b5a95a6a4ab7e7c2e1bce475b9388a7afd34165&')

    if "saluden al generalisimo" in message.content.lower():
        user = await bot.fetch_user(610522653161160744) # ID de usuario
        saluden = (f"Saluden a {user.mention}\n"
                   "¡Por una, grande y libre!\n"
                   "Viva, viva, la revolución\n"
                   "viva, viva Falange de las JONS\n"
                   "muera, muera, muera el capital\n"
                   "viva, viva el Estado Sindical\n"
                   "que no queremos reyes idiotas\n"
                   "que no nos dejan gobernar\n")
        await message.channel.send('https://phantom-elmundo.unidadeditorial.es/5fd01e4cd7f813917be72b3362a233aa/crop/56x0/918x575/resize/414/f/jpg/assets/multimedia/imagenes/2019/10/29/15723652525948.jpg')
        await message.channel.send(f"{saluden}")

    if "viva españa" in message.content.lower():
        españa = ("Por españa \n"
                  "y el que quiera defenderla, \n"
                  "honrado muera, \n"
                  "y el traidor que la abandone, \n"
                  "no tenga quien le perdone, \n"
                  "ni en tierra santa cobijo, \n"
                  "ni una cruz en sus despojos, \n"
                  "ni las manos de un buen hijo, \n"
                  "para cerrarle los ojos.\n "
                  "¡Por una grande y libre!\n"
                  "¡Viva España! \n"
                  "¡Viva el Rey! \n"
                  "¡Viva el orden y la ley! \n")
        await message.channel.send(españa)

    if "oviedo rojo" in message.content.lower():
        rojo =("Unión inalterable de repúblicas libres \n"
               "que unificó para siempre la gran Rusia. \n"
               "¡Viva la única y poderosa Unión Soviética, \n"
               "Creada por la voluntad de los pueblos! \n\n"
               "¡Gloria a nuestra patria libre, \n"
               "baluarte firme de la amistad de los pueblos! \n"
               "El partido de Lenin, la fuerza del pueblo, \n"
               "nos conducirá al trinfuo del comunismo")
        user = await bot.fetch_user(610522653161160744)  # ID de usuario
        await message.channel.send(f"{rojo} {user.mention}")
    await bot.process_commands(message)


@bot.command()
async def recordar(ctx, tiempo: int, *, mensaje: str):
    rol = ctx.guild.get_role(1022262278046887987 )
    
    await ctx.send(f"Recordatorio establecido: {mensaje} en {tiempo} segundos.")
    await asyncio.sleep(tiempo)
    
    # Mencionar al rol especificado
    await ctx.send(f"Recordatorio: {mensaje}, <@&{rol.id}>")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, cantidad: int):
    if cantidad > 100:
        await ctx.send("No puedes eliminar más de 100 mensajes a la vez.")
        return

    deleted = await ctx.channel.purge(limit=cantidad)
    await ctx.send(f"Se han eliminado {len(deleted)} mensajes.", delete_after=5)



bot.run(my_secrets.TOKEN)
