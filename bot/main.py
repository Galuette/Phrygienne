import discord as ds
import wikipedia
import os

wikipedia.set_lang('fr')

client = ds.Client()
token = os.getenv("DISCORD_BOT_TOKEN")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	m = message.content.lower()

	if m.startswith ("?info"):
		if wikipedia.suggest(m[5:len(m)]) != None :
			await message.channel.send(wikipedia.summary(wikipedia.suggest(m[5:len(m)])))
		elif len(wikipedia.search(m[5:len(m)])) != 0 :
			await message.channel.send(wikipedia.summary(wikipedia.search(m[5:len(m)])[0]))
		else :
			await message.channel.send(wikipedia.summary(m[5:len(m)]))
		
	if m.startswith("?iind degré") | m.startswith("?second degré") | m.startswith("?évangile selon saint franck") | m.startswith("?évangile selon st franck") | m.startswith(".deuxième degré") :
		await message.channel.send("IInd degré chiffré 6 : on double la basse si possible au ténor, et ça descend !")

client.run(token)
