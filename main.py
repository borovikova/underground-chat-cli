import asyncio
import aiofiles
import datetime

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        'minechat.dvmn.org', 5000)

    # print(f'Send: {message!r}')
    # writer.write(message.encode())
    data = await reader.read(1000)
    while data:
        async with aiofiles.open("messages.txt", "a") as f:
            await f.write(f'[{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}] {data.decode()}')
            print(f'[{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}] {data.decode()}')
        data = await reader.read(1000)

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client('Hello World!'))
