import os
import asyncio
import aiofiles
import datetime
import argparse
from dotenv import load_dotenv

def get_args():
    load_dotenv()
    host = os.getenv("HOST")
    outgoing_port = os.getenv("SEND_PORT")

    parser = argparse.ArgumentParser(
        description='Chat untility')
    parser.add_argument('--host',
                        default=host,
                        type=str,
                        help='Connection host')
    parser.add_argument('--outgoing_port',
                        default=outgoing_port,
                        type=int,
                        help='Outgoing connections port')
    return parser.parse_args()

async def tcp_echo_client(host, outgoing_port):
    reader, writer = await asyncio.open_connection(
        host, outgoing_port)

    token = '80d5bd9e-f92a-11eb-8c47-0242ac110002\n'.encode()
    message = 'Hello!\n\n'.encode()
    info_message = await reader.readline()
    print(info_message)
    writer.write(token)

    info_message = await reader.readline()
    print(info_message)
    writer.write(message)


    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    args = get_args()
    asyncio.run(tcp_echo_client(args.host, args.outgoing_port))
