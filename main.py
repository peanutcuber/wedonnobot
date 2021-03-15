import discord
from discord.ext import commands
import random
import keep_alive
import ses
import os
import ffmpeg
import youtube_dl
client = commands.Bot(command_prefix='!')

client.remove_command("help")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("maballs"))


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed=discord.Embed(
              title="Thank you for adding wedonnobot to your server!",
              description="Im a music+text bot, use !help to see a list of commands!\nTo add me to another server: https://bit.ly/wedonno",
              colour=discord.Colour.red()
            )
            embed.set_image(url="https://media.discordapp.net/attachments/787385063284932630/820979172511449118/kaki.png?width=676&height=676")
            await channel.send(embed=embed)

            
        break


@client.command()
async def ping(ctx):
    await ctx.send(
        f'Penis {round(client.latency * 1000)}ms. My developers ping is twice as much, damn hot.'
    )


@client.command()
async def mandarin(ctx):
    await ctx.send("""近前看其 詳上寫著 秦香蓮年三十 二歲那狀告當朝
駙馬郎, 欺君王瞞皇上, 那悔婚男兒招東床 this is a good song""")


@client.command()
async def amogus(ctx):
    await ctx.send("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠉⠉⠉⠉⠉⠉⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⣠⣶⠛⠛⠛⠛⠛⠛⠳⣦⡀⠀⠘⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⢹⣿⣦⣀⣀⣀⣀⣀⣠⣼⡇⠀⠀⠸⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠉⠛⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⣿⡄⣠
⠀⠀⢀⣀⣀⣀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀
⠿⠿⠟⠛⠛⠉⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣠⡶⠶⠿⠿⠿⠿⢷⣦⠀⠀⠀⠀⠀⠀⠀⣿⠀
⠀⠀⣀⣀⣀⠀⣸⡇⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⠀
⣠⡿⠛⠛⠛⠛⠻⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⣿⠀
⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⢀⣤⣤⣴⣿⠀⠀⠀⠀⠀⠀⠀⣿⠀
⠈⠙⢷⣶⣦⣤⣤⣤⣴⣶⣾⠿⠛⠁⢀⣶⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀
⢷⣶⣤⣀⠉⠉⠉⠉⠉⠄⠀⠀⠀⠀⠈⣿⣆⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡾⠃⠀
⠀⠈⠉⠛⠿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣾⣿⡿⠿⠟⠋⠁⠀⠀

              SUS⠀
              
              https://i.kym-cdn.com/entries/icons/original/000/036/482/cover5.jpg"""
                   )


#AUDIOCOMMANDS


@client.command(aliases=['p', 'playsong'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send(
            "Wait for the current playing music to end or use the 'stop' command"
        )
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    embed = discord.Embed(colour=discord.Colour.orange())
    x = file.find("-")
    fixed_name = file[:x]
    embed.set_author(name="Playing: " + fixed_name)
    await ctx.send(embed=embed)


@client.command(aliases=['l', 'kishta'])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
    await ctx.send("Bye!")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")
    await ctx.send("Paused the current track.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")
    await ctx.send("Resuming the paused track!")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Stopping track/queue.")


@client.command(aliases=['8ball', 'ball', '8b'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.send(f'You asked: {question}\nAnswer: {random.choice(responses)}'
                   )


@client.command(aliases=['delete', 'remove', 'rm'])
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
async def devs(ctx):

    embed = discord.Embed(title='Authors:',
                          description="This is my developers info",
                          colour=discord.Colour.blue())
    embed.set_footer(text="Omri Dvora, Roee Mor")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/787385063284932630/820979172511449118/kaki.png"
    )
    embed.set_image(
        url=
        "https://cdn.discordapp.com/attachments/787385063284932630/820962153066004491/Untitled_1.png"
    )
    embed.set_author(
        name="peanutcuber, Omridvo",
        icon_url=
        "https://cdn.discordapp.com/attachments/783348416482770947/820960636791554078/Untitled.png"
    )
    await ctx.send(embed=embed)


#help


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
      color=discord.Colour.orange(),
      description="My prefix here is ! so use it to send commands! Here is the list of the commands you can use on me"   
    )
    embed.set_author(name="Help")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/787385063284932630/820979172511449118/kaki.png"
    )
    embed.add_field(name="!ping", value="Returns your ping.", inline=False)
    embed.add_field(name="!mandarin",
                    value="Shows the lyrics of the best song to ever exist.",
                    inline=False)
    embed.add_field(name="!amogus", value="Test and see...", inline=False)
    embed.add_field(name="!play",
                    value="Plays a song from the url you entered.",
                    inline=False)
    embed.add_field(name="!pause",
                    value="Pauses the current track",
                    inline=False)
    embed.add_field(name="!leave",
                    value="Disconnects from the channel.",
                    inline=False)
    embed.add_field(name="!stop",
                    value="Stops the current track/queue",
                    inline=False)
    embed.add_field(name="!resume",
                    value="Resumes the paused track.",
                    inline=False)
    embed.add_field(name="!8ball",
                    value="Ask a question, and get an answer!",
                    inline=False)
    embed.add_field(name="!clear",
                    value="Deletes the last 5 messeges",
                    inline=False)
    embed.add_field(name="!devs",
                    value="Those people codedthe bot.",
                    inline=False)
    embed.add_field(name="!help",value="If you arrived here, i guess you know what it does.", inline=False)
    embed.add_field(name="Thank you for using wedonnobot!",
                    value="Python-Discord.py",
                    inline=False)
    

    await ctx.send(embed=embed)



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
