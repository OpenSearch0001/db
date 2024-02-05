import discord
import os

from discord.ext import commands
from discord.embeds import Embed
from discord.ext.commands import Bot
from discord_webhook import DiscordWebhook

intents = discord.Intents.default()
intents.message_content = True
PATH = os.getcwd()


def folder_file_checking():
    if not os.path.isfile(f"{PATH}/wl.txt"):
        with open('wl.txt', 'w') as fichier:
            fichier.write("")
    if not os.path.isfile(f"{PATH}/owners.txt"):
        with open('owners.txt', 'w') as fichier:
            fichier.write("")
    if not os.path.exists(f"{PATH}/db/")
        os.makedirs(f"{PATH}/db/")

folder_file_checking()


allowed_user_ids = [int(id) for id in open('wl.txt').read().split()]
ownerlist = [int(id) for id in open('owners.txt').read().split()]



bot = Bot("x", intents=intents)

bot.remove_command("help")



@bot.command()
async def help(ctx):
    embed = Embed(
        title="Command List",
        color=0x2c2d30 
    )
    embed.add_field(name="xlookup ID", value="Lookup l'ID d'une personne pour obtenir plus d'informations sur la personne.", inline=False)
    embed.add_field(name="xcredits", value="Informations sur le createur du bot.", inline=False)
    embed.add_field(name="xwl ID", value="Ajouter des gens qui pourront avoir access au bot.", inline=False)
    embed.add_field(name="xwllist", value="Voir les gens qui ont access au bot", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def lookup(ctx, arg1):
    if ctx.author.id not in allowed_user_ids:
        embed = Embed(
            title=":x:",
            description="Veuillez acheter ce bot en contactant <@725075907538190397>",
            color=0x2c2d30 
        )
        await ctx.send(embed=embed)
        return

    # auto add file name
    file_paths = [
        'scrapped\\db.txt',
        'scrapped\\db1.txt',
        'scrapped\\db2.txt',
        'scrapped\\Discord.com_2023.txt',
        'scrapped\\discord.ggUser2023.txt',
        'scrapped\\discord.ggUser2023scraped.txt',
        'scrapped\\discord1_2023.com.txt',
        'scrapped\\discord1.txt',
        'scrapped\\discord2.csv',
        'scrapped\\discord3.txt',
        'scrapped\\discord4.csv',
        'scrapped\\discord5.csv',
        'scrapped\\discord6.txt',
        'scrapped\\discord7.txt',
        'scrapped\\discord8.csv',
        'scrapped\\Discords.com53.67k.csv',
        'scrapped\\Discords.com64.84k.csv',
    ]

    found_messages = []

    for file_path in file_paths:
        found = False
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if arg1 in line:
                    found_messages.append(f"{line.strip()}")
                    found = True

        if not found:
            found_messages.append(f"Rien trouvé de cette DB: {file_path}")

    embed = Embed(
        title="Résultats",
        color=0x2c2d30  
    )

    for msg in found_messages:
        embed.add_field(name='\u200b', value=msg, inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def credits(ctx):
    embed = Embed(
        title="Crédits",
        description="Codé par sq slav (725075907538190397)\nCe n'est pas un bot officiel par Discord, veuillez utiliser ce bot légalement.",
        color=0x2c2d30 
    )
    await ctx.send(embed=embed)

@bot.command()
async def wl(ctx, arg1):
    if ctx.author.id not in ownerlist:
        embed = Embed(
            title=":x:",
            description="Vous ne pouvez pas faire cette commande.",
            color=0x2c2d30 
        )
        await ctx.send(embed=embed)
        return
    user_id = int(arg1[2:-1])

    allowed_user_ids.append(user_id)
    await ctx.send(f"**<@{arg1}> est maintenant WL!**")

@bot.command()
async def wllist(ctx):
    if ctx.author.id not in ownerlist:
        embed = Embed(
            title=":x:",
            description="Vous ne pouvez pas faire cette commande.",
            color=0x2c2d30 
        )
        await ctx.send(embed=embed)
        return
    embed = Embed(
        title="Liste de personne WL",
        color=0x2c2d30  
    )
    embed.add_field(name='\u200b', value=allowed_user_ids, inline=False)
    await ctx.send(embed=embed)


bot.run("")
