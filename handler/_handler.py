import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout, ErrNoServers

class Handler:
  __instance = None

  def __init__(self, servers, loop):
    self.nc = NATS()
    self.loop = loop
    self.servers = servers
    self.queue = asyncio.Queue()

    if servers is None:
      servers = ["nats://127.0.0.1:4222"]
  
  async def error_cb(self, e):
    print("Error:", e)

  async def closed_cb(self):
    print("Connection to NATS is closed.")

  async def reconnected_cb(self):
    print(f"Connected to NATS at {self.nc.connected_url.netloc}...")

  async def connect(self):
    if self.nc != None:
      # Options to the nats connection
      options = {
        "loop": self.loop,
        "error_cb": self.error_cb,
        "closed_cb": self.closed_cb,
        "reconnected_cb": self.reconnected_cb,
        "servers": self.servers
      }
      # connect to nats server
      await self.nc.connect(**options)
      print("Connected to: " + self.servers)

  async def disconnect(self):
    if self.loop != None:
      await self.nc.flush()
      await self.nc.close()
      self.loop.stop()
      print("Connection to NATS is closed.")

  async def subscribe(self, subject, cb):
    if self.nc != None:
      await self.nc.subscribe(subject, cb=cb)
      print("Subscribed to: " + subject)

  async def publish(self, subject, message):
    if self.nc != None:
      await nc.publish(subject, message)
      print("Message: " + message + "published to: " + subject)
