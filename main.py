import os
import asyncio
import aiofiles
import datetime
import argparse
from dotenv import load_dotenv

def get_args():
    load_dotenv()
    history_file_path = os.getenv("MESSAGE_HISTORY_FILE_PATH")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    parser = argparse.ArgumentParser(
        description='Parser for an online library tululu.org')
    parser.add_argument('--host',
                        default=host,
                        type=str,
                        help='Connection host')
    parser.add_argument('--port',
                        default=port,
                        type=int,
                        help='Connection port')
    parser.add_argument('--history',
                        default=history_file_path,
                        type=str,
                        help='Message history file path')
    return parser.parse_args()

async def tcp_echo_client(file_path, host, port):
    reader, writer = await asyncio.open_connection(
        host, port)

    # print(f'Send: {message!r}')
    # writer.write(message.encode())
    data = await reader.read(1000)
    while data:
        async with aiofiles.open(file_path, "a") as f:
            await f.write(f'[{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}] {data.decode()}')
            print(f'[{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}] {data.decode()}')
        data = await reader.read(1000)

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    args = get_args()
    asyncio.run(tcp_echo_client(args.history, args.host, args.port))
