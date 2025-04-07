import discord
from discord.ext import commands
import os

TOKEN = 'BOT_TOKENINIZ'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
 await ctx.send("he" * count_heh)
@bot.command()
async def gorsel_kaydet(ctx):
    """Kullanıcının gönderdiği görselleri kaydeder."""
    if ctx.message.attachments:
        
        for attachment in ctx.message.attachments:
            if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                
                if not os.path.exists('gorseller'):
                    os.makedirs('gorseller')
 
            
                await attachment.save(f'gorseller/{attachment.filename}')
                await ctx.send(f'{attachment.filename} kaydedildi!')
            else:
                await ctx.send('Eklenen dosya bir görsel değil!')
    else:
        await ctx.send('Lütfen bir görsel ekleyin!')

bot.run(TOKEN)
