from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def 困ったときは(ctx):
    await ctx.send('お互いさまさま')
    
@bot.command()
async def メンバー(ctx):
    await ctx.send('メンバー一覧だよー！')

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    await channel.send('やっほー！おはよー騎士くん！')  
#ループ処理実行
loop.start()

bot.run(token)
