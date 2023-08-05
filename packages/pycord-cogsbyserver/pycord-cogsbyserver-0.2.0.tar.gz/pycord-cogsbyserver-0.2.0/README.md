# Pycord Cogs by Server
A simple addon to the pycord library that allows you to make cogs that exist as different objects between different servers. This is better explained by an example, so say you're making a simple music bot. Your cog might look something like this without the library...
```python
import discord
from discord.ext import commands
class CogThing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}
        self.volumes = {}
    
    @discord.slash_command()
    async def add_to_queue(self, ctx, *, song_title):
        if ctx.guild not in self.queues:
            self.queues[ctx.guild] = []
        self.queues[ctx.guild].append(song_title)
        await ctx.respond("Song added")
    
    @discord.slash_command()
    async def change_volume(self, ctx, *, volume: int):
        self.volumes[ctx.guild] = volume
        await ctx.respond(f"Volume set to {volume}")
    
    async def play_song(self, vc):
        if vc.guild not in self.queues or len(self.queues[vc.guild])==0:
            return
        
        song = self.queues[vc.guild].pop(0)
        volume = 100 if vc.guild not in self.volumes else self.volumes[vc.guild]
        do_some_things_play_some_music(vc, song, volume)
```
...but with the library it can look like this!
```python
import discord
from pycord_cogsbyserver import ServerCog
class CogThing(ServerCog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.volume = 100
    
    @ServerCog.slash_command()
    async def add_to_queue(self, ctx, *, song_title):
        self.queue.append(song_title)
        await ctx.respond("Song added")
    
    @ServerCog.slash_command()
    async def change_volume(self, ctx, *, volume:int):
        self.volume = volume
        await ctx.respond(f"Volume set to {volume}")
    
    async def play_song(self, vc):
        if len(self.queue) == 0:
            return
        song = self.queue.pop(0)
        do_some_things_play_some_music(vc, song, self.volume)
```
You can imagine how that would reduce complexity as the bot's functionality increases.