import discord
import requests
import json
from discord.ext import commands 
import asyncio

client = commands.Bot(command_prefix= '!')

IDR = open("ID", "r")


@client.command()
async def ID (ctx, identifiant):
    print('connexion')
    
    for ligne in IDR:
        if identifiant in ligne:
            await ctx.send(f"Bonjour {identifiant}")
            print("réussi")
            break
    await ctx.send("Inscrit-toi")

@client.command()
async def delete(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    print("Il y a ", amount, "messages qui ont été supprimer.")
    




    



