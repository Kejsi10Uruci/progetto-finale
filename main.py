import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True         # INTENT PRIVILEGIATO
intents.presences = True       # INTENT PRIVILEGIATO
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command(name="comandi")
async def mostra_comandi(ctx):
    help_message = """
**– Comandi disponibili:**

`!trasporti` – Consiglio su mezzi sostenibili  
`!ridurreriusarericiclare` – Consiglio sul riciclo e riduzione rifiuti  
`!cibo` – Suggerimento per evitare lo spreco alimentare  
`!acqua` – Come risparmiare acqua  
`!casa` – Consigli per risparmiare energia e migliorare la casa  
`!consumo` – Scelte di consumo sostenibile  
`!sprecoalimenti` – Altro consiglio sullo spreco di cibo  
`!comandi` – Mostra questo elenco

💡 Digita uno di questi comandi nel server per ricevere un consiglio utile!
"""
    await ctx.send(help_message)

@bot.command()
async def trasporti(ctx):
    await ctx.send("Scegli trasporti sostenibili🌿: riduci l'uso dell'auto privata optando per mezzi pubblici, bicicletta o camminate. Se possibile, considera l'acquisto di un veicolo elettrico. Il settore dei trasporti è responsabile di circa il 30% delle emissioni di gas serra.")

@bot.command()
async def ridurreriusarericiclare(ctx):
    await ctx.send("Riduci, riusa e ricicla♻️: limita l'uso di plastica monouso, riutilizza gli oggetti quando possibile e segui le regole della raccolta differenziata per ridurre i rifiuti.")

@bot.command()
async def cibo(ctx):
    await ctx.send("Riduci lo spreco alimentare🍽️: compra solo ciò che ti serve, conserva bene il cibo e consuma gli avanzi. Lo spreco alimentare contribuisce alle emissioni di metano.")

@bot.command()
async def acqua(ctx):
    await ctx.send("Conserva l'acqua💧: chiudi il rubinetto mentre ti lavi i denti, utilizza lavatrici e lavastoviglie solo a pieno carico e considera l'installazione di dispositivi per il risparmio idrico.")

@bot.command()
async def casa(ctx):
    await ctx.send("- Risparmia energia in casa💡: adotta lampadine a LED, spegni gli apparecchi elettronici quando non li usi e regola la temperatura del riscaldamento e del condizionatore per evitare sprechi energetici.")
    await ctx.send("- Migliora l'efficienza energetica della tua abitazione🏠: isola termicamente la casa, installa pannelli solari e utilizza elettrodomestici a basso consumo energetico per ridurre l'impatto ambientale e risparmiare sulle bollette.")

@bot.command()
async def consumo(ctx):
    await ctx.send("Fai scelte di consumo consapevoli🛒: acquista prodotti locali e di stagione, preferisci aziende che adottano pratiche sostenibili e riduci il consumo di carne, poiché l'allevamento intensivo contribuisce significativamente alle emissioni di gas serra.")

@bot.command()
async def sprecoalimenti(ctx):
    await ctx.send("Riduci lo spreco alimentare🍽️: compra solo ciò che ti serve, conserva bene il cibo e consuma gli avanzi. Lo spreco alimentare contribuisce alle emissioni di metano ")

bot.run("TOKEN")
