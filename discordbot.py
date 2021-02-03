from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import os
import traceback
import discord

# 接続に必要なオブジェクトを生成
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
targetChannnel = os.environ['TEST_CHANNEL']

# 指定時間に走る処理
async def sendMessage():
    channel = client.get_channel(targetChannnel)
    await channel.send('やっほー！おはよー騎士くん！')

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    await sendMessage()
    #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
#     await asyncio.sleep(30)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '困ったときは':
        await message.channel.send('お互いさまさま')
    if message.content == 'メンバー取得':
        await message.channel.send('メンバー一覧だよー')
        
#ループ処理
time_check.start()
#botの起動
client.run(token)
