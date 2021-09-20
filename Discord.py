import discord
import os
from time import sleep
from discord.ext import commands

client = discord.Client()
uang = []
player = []
level = []
autoMine = []

@client.event
async def on_ready(): # When the bot starts
    print(f"Bot online and logged in as {client.user}")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  pesan = message.content.lower()

  if pesan == "!tes":
    await message.channel.send("Hello")

  elif pesan == "!game":
    await message.channel.send("Yoi")
    player.append(message.author)
    uang.append(0)
    level.append(1)
    autoMine.append(False)

  elif pesan == "!farm":
    i = 0
    while i < len(player):
      if player[i] == message.author:
        break
      elif i >= (len(player) - 1):
        await message.channel.send("ketik \"!game\" untuk menambahkan player")
        return
      i+=1

    uang[i]+=5
    await message.channel.send("uang kamu = "+str(uang[i]))
  
  elif pesan == "!levelup":
    i = 0
    while i < len(player):
      if player[i] == message.author:
        break
      elif i >= (len(player) - 1):
        await message.channel.send("ketik \"!game\" untuk menambahkan player")
        return
      i+=1
    
    if uang[i] >= 100:
      level[i] += 1
      uang[i] -= 100

  elif pesan == "!profil":
    i = 0
    while i < len(player):
      if player[i] == message.author:
        break
      elif i >= (len(player) - 1):
        await message.channel.send("ketik \"!game\" untuk menambahkan player")
        return
      i+=1
    
    await message.channel.send("Nama Kamu = "+str(player[i])+" Uang = "+str(uang))

  elif pesan == "!automine":
    i = 0
    while i < len(player):
      if player[i] == message.author:
        break
      elif i >= (len(player) - 1):
        await message.channel.send("ketik \"!game\" untuk menambahkan player")
        return
      i+=1

    if level[i] < 5:
      await message.channel.send("Level kamu belum cukup :(")
      return

    if autoMine[i] == True:
      await message.channel.send("Automine Sudah Nyala :v")
      return
    
    await message.channel.send("Siap Bos")
    autoMine[i] = True
    while True:
      uang[i]+=5
      sleep(5)

client.run(os.getenv('token'))
