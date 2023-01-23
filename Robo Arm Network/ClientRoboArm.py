import asyncio
from asyncore import write
import time

host_addr = '127.0.0.1'
port_num = 50000

async def run_client() -> None:
    reader, writer = await asyncio.open_connection(host_addr, port_num)
    await writer.drain()

    while True:
        axis = input("[+] Input axis >> ")
        angle = input("[+] Input axis angle >> ")
        data = '{"axis": "' + axis + '", "angle": ' + angle + '}'
        writer.write(f'{data}'.encode())
        await writer.drain()
        time.sleep(3)
        print("Sent data " + data)
        print("-----------------------------------\n")

loop = asyncio.new_event_loop()
loop.run_until_complete(run_client())