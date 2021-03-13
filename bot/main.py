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
		if suggest(m[5:-1]) != None :
			await message.channel.send(wikipedia.summary(suggest(m[5:-1])))
		elif len(search(m[5:-1])) != 0 :
			await message.channel.send(wikipedia.summary(search(m[5:-1])[0]))
		else :
			await message.channel.send(wikipedia.summary(m[5:-1])[0])

	if m.startswith("?iind degré") | m.startswith("?second degré") | m.startswith("?évangile selon saint franck") | m.startswith("?évangile selon st franck") | m.startswith(".deuxième degré") :
		await message.channel.send("IInd degré chiffré 6 : on double la basse si possible au ténor, et ça descend !")

client.run(token)
