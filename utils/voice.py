import discord

async def play_audio(ctx_or_message, path):
    voice = getattr(ctx_or_message.author, "voice", None)
    if not voice:
        return

    channel = voice.channel
    vc = channel.guild.voice_client
    if not vc:
        vc = await channel.connect()

    source = discord.FFmpegPCMAudio(path)
    source = discord.PCMVolumeTransformer(source, volume=0.5)
    vc.play(source)