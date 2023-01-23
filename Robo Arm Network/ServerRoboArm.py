import serial
import os, time
import asyncio
import json
import subprocess
import threading

class Server:

    def __init__(self):
        file = open('config.json')
        config = json.load(file)
        self.host = config['host_device']
        self.port = config['port_device']
        self.queue = config['queue_size']
        self.device = serial.Serial(config['device'], config['baudrate'])   

    async def listen_and_accept(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        rdata = None
        addr, port = writer.get_extra_info("peername")
        print("Device [" + addr + ":" + str(port) + "] connected")
        while rdata != "<quit>":
            try:
                rdata = await reader.read(self.queue)
                data = json.loads(rdata.decode())
                print("Received data " + rdata.decode())
                data = data['axis'] + str(data['angle'])
                self.device.write(f'{data}'.encode())
            except Exception as ex:
                print(ex)
                pass

    async def run_server(self) -> None:
        print("Server started")
        server = await asyncio.start_server(self.listen_and_accept, self.host, self.port)

        async with server:
            await server.serve_forever()

if __name__ == '__main__':
    server = Server()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(server.run_server())
