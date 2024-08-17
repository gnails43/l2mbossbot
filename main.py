import discord
from discord.ext import commands, tasks

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

###Login section
# # discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#Message queues
# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Loops
# botが起動したときの処理
@client.event
async def on_ready():
    print("Botが立ち上がったよ！")
    loops.start()

@tasks.loop(seconds=10)
async def loops():
    channel = client.get_channel(1270744099275804742)  # 送信したいチャンネルのIDを入れてください
    if channel:
        table = """```
ボスリストだよ！:panda_face:
出現率100%のボスには下線がついてるよ！
英雄以上ドロップありは:fleur_de_lis:、
インターボスには:earth_asia:がついてるよ！

01:01→エンクラ
01:01→ブレカ
01:02→テンペスト :fleur_de_lis:
01:04→クイーンアント :fleur_de_lis:
01:04→コルーン :fleur_de_lis:
01:04→ヒシルローメ :fleur_de_lis:
01:04→ブラックリリー :fleur_de_lis:
01:05→サミュエル :fleur_de_lis:
01:05→ランドール :fleur_de_lis:
02:04→ガレス :fleur_de_lis:
03:02→バシラ
03:04→フェリス
03:05→忘却の鏡 :fleur_de_lis:
03:06→グラーキ :fleur_de_lis:
03:06→コアサセプタ :fleur_de_lis:
04:01→ベヒモス :fleur_de_lis:
04:04→アンドラス :fleur_de_lis:
04:04→ナイアス :fleur_de_lis:
04:04→フリント :fleur_de_lis:
04:04→レピロ :fleur_de_lis:
05:04→ケルソス
05:04→セル :fleur_de_lis:
05:04→タルキン
05:04→チェルトゥバ
05:04→バルボ :fleur_de_lis:
05:04→パンナロード
05:04→マトゥラ
05:05→ミュータントクルマ :fleur_de_lis:
06:04→スタン :fleur_de_lis:
06:05→トロンバ
07:01→サルカ
07:02→サヴァン :fleur_de_lis:
07:02→タラキン :fleur_de_lis:
07:02→ティミトリス :fleur_de_lis:
07:02→パンドライド :fleur_de_lis:
07:02→メデューサ :fleur_de_lis:
07:03→カタン :fleur_de_lis:
07:03→ティミニエル :fleur_de_lis:
07:04→ドラゴンビースト :fleur_de_lis:
07:04→シーラー風 :fleur_de_lis: :earth_asia:
07:04→ムーフ闇 :fleur_de_lis: :earth_asia:
07:04→ノルムス地 :fleur_de_lis: :earth_asia:
07:04→ウカンバ水 :fleur_de_lis: :earth_asia:
07:05→汚染したクルマ :fleur_de_lis:
07:07→カブリオ :fleur_de_lis:
13:04→サイラックス :fleur_de_lis:
13:04→バラック :fleur_de_lis:
19:00→ラムダル :fleur_de_lis: :earth_asia:
19:00→カーノン :fleur_de_lis: :earth_asia:
19:00→ハラト :fleur_de_lis: :earth_asia:
19:00→シュリエル :fleur_de_lis: :earth_asia:
19:00→ベリタス :fleur_de_lis: :earth_asia:
19:04→オルクス :fleur_de_lis:
19:04→オルフェン :fleur_de_lis:
19:04→ハーフ :fleur_de_lis:
19:04→バロン :fleur_de_lis:
19:04→フェニックス :fleur_de_lis:
19:05→モデウス :fleur_de_lis:
20:00→マルディル :fleur_de_lis: :earth_asia:
20:00→タリム :fleur_de_lis: :earth_asia:
20:00→ベラ :fleur_de_lis: :earth_asia:
20:00→ガラッシア :fleur_de_lis: :earth_asia:
20:00→リリス :fleur_de_lis: :earth_asia:
00:05→タナトス :fleur_de_lis:
07:04→ラーハ :fleur_de_lis:
```"""
        await channel.send(table)


# クライアントの実行
client.run(ディスコードのシークレット)
