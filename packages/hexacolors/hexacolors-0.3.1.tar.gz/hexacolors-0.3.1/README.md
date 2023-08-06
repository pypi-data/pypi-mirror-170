# hexacolors

A simple library that converts string to hexadecimal understandable by python

## Usage:
### install with pip

```shell
pip install hexacolors
```

### Import on your code:

```python
import hexacolors
from hexacolors import hexacolor, stringcolor
```
### Run it
```python
hexacolors.stringcolor("Blue")
or
hexacolors.hexacolor('#711A89')
```

convert this string for hexadecimal understandable by python

### Using in py-cord

```python

import  discord

from discord.ext import commands
from hexacolors import hexacolor, stringcolor

intents = discord.Intents.all()

client = commands.Bot(
command_prefix = '!',
help_command = None,
case_insensitive = True,
intents = intents
)

@client.event
async def on_ready():
    print("i'm logged with {}".format(client.user))

@client.event
async def on_message(msg):
    if msg.author == client.user: return

    if msg.author.bot: return

    await client.process_commands(msg)

@client.command()
async def ping(ctx):

    ping = client.latency * 1000

    e = discord.Embed(
    title ='Ping',
    description = 'My ping is {}'.format(int(ping)),
    color = hexacolor('#2f005c')
    )

    await ctx.send(embed = e)

#or

@client.command()
async def ping(ctx):

    ping = client.latency * 1000

    e = discord.Embed(
    title ='Ping',
    description = 'My ping is {}'.format(int(ping)),
    color = stringcolor('Blue')
    )

    await ctx.send(embed = e)

client.run('Token bot here')

```