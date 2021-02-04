from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import os
import traceback
import discord

# 接続に必要なオブジェクトを生成
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
channel_id = int(os.environ['TEST_CHANNEL'])


# 起動時の処理
@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    await channel.send('ヒヨリぼっと起動したよ。おはよう騎士くん！')
    #ループ処理
    loop.start()

# 指定時間に走る処理
async def sendMessage():
    await channel.send('騎士くん、今は ' + datetime.now().strftime('%H:%M') + '時だよ')

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%M')
    if now == '00':
        await sendMessage()


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
        
#botの起動
client.run(token)
