mytitle = "ALIEN SOFTWARE SERVER CLONE VI"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Sizin ID niz'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from clay1000 import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}                                                                                          
ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE 
ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE 
ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE 
ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE 
ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE ALIEN SOFTWARE 
{Style.RESET_ALL}
{Fore.MAGENTA}Developed by: clay#1000{Style.RESET_ALL}
        """)
token = input(f'Token Girin:\n >')
guild_s = input('Kopyalanacak Sunucu ID:\n >')
guild = input('Yapıştırılacak Sunucu ID:\n >')
input_guild_id = guild_s  
output_guild_id = guild  
token = token  


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Şu Hesaba Giriş Yaptım: {client.user}")
    print("Server Klonlanıyor!")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}

ЗАКРЫТЫЙ ЗАКРЫТЫЙ ЗАКРЫТЫЙ
ЗАКРЫТЫЙ ЗАКРЫТЫЙ ЗАКРЫТЫЙ
ЗАКРЫТЫЙ ЗАКРЫТЫЙ ЗАКРЫТЫЙ 
ЗАКРЫТЫЙ ЗАКРЫТЫЙ ЗАКРЫТЫЙ
ЗАКРЫТЫЙ ЗАКРЫТЫЙ ЗАКРЫТЫЙ

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)


client.run(token, bot=False)
