from operator import index
from os import stat
from tabnanny import check
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="visit poopfartnuts.com"))
    print("BOT IS ON")


@bot.event
async def on_message(msg):
    print(msg.author.id)
    if msg.author.id != "500037296054075432":
        return False
    #idk just for trolling ig
    if msg.content == "%how":
        await msg.channel.send("idk")


    #checkbox for rules
    if msg.content == "%%RULES":
        rules_string = open("rules.txt").read()
        rules_embed=discord.Embed(title="RULES",description=rules_string,color=0x31c438)
        rules_msg = await msg.channel.send(embed=rules_embed)

        #detects when someone reacts
        while True:
            reaction = await bot.wait_for("reaction_add")

            if reaction[0].emoji == "✅":
                verified_role_to_add = discord.utils.get(msg.guild.roles, name="Verified")
                roles_role_to_add = discord.utils.get(msg.guild.roles, name="---- SELF ROLES ----")
                await reaction[1].add_roles(verified_role_to_add,roles_role_to_add)



    #adds roles
    if msg.content != "%%ROLES":
        return False


    
    embed=discord.Embed(title="SELF ROLES", 
    description='PRONOUNS: \n \n 🔵=He/Him \n 🔴=She/Her \n 🟣=They/Them \n 🟠=It/Its \n ⚪=Neopronouns \n 🟤=Just Ask \n \n ORIENTATIONS \n \n ♥️=Lesbian \n 💙=Gay \n 💞=Bisexual \n 💗=Demisexual \n 💚=Asexual \n ❤️=Omnisexual \n 💕=Polysexual \n 🤍=Straight \n 🧡=Abrosexual \n 💛=Pansexual \n ❔=Questioning \n 🖤=Other Orientation',
    color=0x5f1994)
    embed_msg = await msg.channel.send(embed=embed)
    
    #adds reactions for people to tick off
    data_from_file = json.loads(open("roles.json").read())
    for i in data_from_file:
        await embed_msg.add_reaction(i)

    #detects when someone reacts
    while True:
        reaction = await bot.wait_for("reaction_add")
        print(str(reaction[0].emoji) + " " + str(reaction[1].id))

        await reaction[1].add_roles(add_role(msg.guild, reaction[0].emoji))



def add_role(guild,emoji):
    data_from_file = json.loads(open("roles.json").read())
    role_string = "none"
    for i in data_from_file:
        if i != emoji:
            continue
        role_string = data_from_file[i]
        break

    if role_string == "none":
        return "not an emoji"

    role_to_add = discord.utils.get(guild.roles, name=role_string)
    return role_to_add

bot.run("NjkxNzExNzEwNDkwMjYzNjYz.GDQ2pZ.bqZStWXQqfXWTtuJ0FrY0yj0n5jpdVNVZUwCLc")