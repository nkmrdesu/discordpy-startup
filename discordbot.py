from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channnel = os.environ['TEST_CHANNEL']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def 困ったときは(ctx):
    await ctx.send('お互いさまさま')
    
@bot.command()
async def メンバー(ctx):
    await ctx.send('メンバー一覧だよー！')

@tasks.loop(seconds=60)
async def loop():
    # 発言部
    targetChannel = bot.get_channel(CHANNEL_ID)
    await targetChannel.send('やっほー！おはよー騎士くん！')  

#ループ処理実行
loop.start()
#botの起動
bot.run(token)
