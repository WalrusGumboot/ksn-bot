import discord
client = discord.Client()

prefix = "/ksn "
helpMessage = '''KSN Bot, geprogrammeerd en ontworpen door WalrusGumboot.\nCommands:\n\n
*help*: Geeft dit bericht weer.
Gebruik: /ksn help
*prefix*: Verandert de commandoprefix. Standaard is dit /ksn maar dit kan aangepast worden.
Gebruik: /ksn prefix (de nieuwe prefix)
NB: een commandoprefix moet starten met een slash (/).
'''

prefixFile = open("prefixFile.txt", "r+")
prefix = prefixFile.readline(1)
print(prefix, " is de huidige prefix.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'help'):
        msg = helpMessage.format(message)
        print("Iemand heeft help opgeroepen!")
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'prefix '):
        setPrefixArray = message.content.split()
        setPrefix = setPrefixArray[setPrefixArray.length]
        print("Iemand heeft prefix opgeroepen!\nBericht was ", message.content, "\nsetPrefixArray was ", setPrefixArray)
        print("prefix is: ", setPrefix)
        if setPrefix.startswith("/"):
            prefixFile.write(setPrefix, "\n")
        else:
            await client.send_message(message.channel, "Prefix moet met een slash (/) beginnen!")

@client.event
async def on_ready():
    print('Ingelogd als ' + client.user.name)
    print('ID: ' + client.user.id)
    print('------')


