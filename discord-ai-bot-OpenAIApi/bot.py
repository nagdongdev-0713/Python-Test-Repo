import discord # 디스코드 봇 모듈
import openai # openai(챗gpt) 모듈
from discord import discord.ext

intents = discord.Intents.all() # Intents 선언 (22년 후반부부터 intents 필요함)
client = discord.Client(intents=intents) #클라이언트 정보

# OpenAI API 인증 정보 설정
openai.api_key = "OPENAI GPT-3 모듈 API 키"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # OpenAI API를 사용하여 챗봇 기능 작동!
    response = openai.Completion.create(
        engine="davinci",
        prompt=message.content,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 결과를 디스코드채널에 보낸다(send)
    await message.channel.send(response.choices[0].text)
    # 주의!!!! 너무 많이 요청하면 Too many Requests때문에 API키가 정지될수 있으니 주의하자

client.run('your_token_here')
