from pycordia import models
import pycordia
import dotenv
import os

dotenv.load_dotenv()

client = pycordia.Client(intents=pycordia.Intents.all())

@client.event
async def on_message_create(message: models.Message):
    if message.author.bot or not message.content:
        return

    if message.content.startswith(".ping"):
        await models.Message.send(message.channel_id, embeds=[
            models.Embed.create(
                title="Pong",
                description=":ping_pong: Ping pong!"
            )
        ])
    elif message.content.startswith(".gullds"):
        guilds = await client.guilds

        embed = models.Embed.create(
            title="Guilds I'm in",
            description="\n".join(guild.name for guild in guilds),
            color=0xFF2A3C
        )
        embed.add_field(name="Guild Count", value=str(len(guilds)))

        await models.Message.send(message.channel_id, embeds=[embed])
    elif message.content.startswith(".info"):
        embed = models.Embed.create(
            title="PyBot",
            description=f"Running on **Pycordia v{pycordia.__version__}**"
        )
        embed.add_field(name="Github Repository", value="[Click here](https://github.com/angelCarias/pybot)")

        await models.Message.send(message.channel_id, embeds=[embed])


client.run(os.environ.get("DISCORD_TOKEN", ""))