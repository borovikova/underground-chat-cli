import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        'minechat.dvmn.org', 5000)

    # print(f'Send: {message!r}')
    # writer.write(message.encode())
    data = await reader.read(1000)
    print(f'Received: {data.decode()!r}')
    while data:
        data = await reader.read(1000)
        print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client('Hello World!'))
