from mirai import Mirai, Plain, MessageChain, Group, Member, At, Source, Image
# from mirai.face import QQFaces
# from mirai import Face
# import asyncio
import requests
from ostest import picbase, randompic

num = randompic()
dir = "./PixivImage/" + num
url1 = "https://nmsl.shadiao.app/api.php?from=sunbelife"
url2 = "https://chp.shadiao.app/api.php?from=sunbelife"
qq = 3207033875  # 字段 qq 的值
authKey = '1234567890'  # 字段 authKey 的值
mirai_api_http_locate = 'localhost:8080/'
# httpapi所在主机的地址端口,如果 setting.yml 文件里字段 "enableWebsocket" 的值为 "true" 则需要将 "/" 换成 "/ws", 否则将接收不到消息.

app = Mirai(f"mirai://{mirai_api_http_locate}?authKey={authKey}&qq={qq}")


@app.receiver("GroupMessage")
async def quote(app: Mirai, group: Group, message: MessageChain,
                member: Member, source: Source):
    if message.toString().find("骂我") != -1:
        txt1 = requests.get(url1)
        await app.sendGroupMessage(
            group, [At(member.id), Plain(text=txt1.text)], quoteSource=source)
        return True
    if message.toString().find("夸我") != -1:
        txt2 = requests.get(url2)
        await app.sendGroupMessage(
            group, [At(member.id), Plain(text=txt2.text)], quoteSource=source)
        return True
    if message.toString().find("tu") != -1:
        pic = picbase()
        print(pic)
        await app.sendGroupMessage(group, [Image.fromBase64(pic)])
        return True


if __name__ == "__main__":
    app.run()
