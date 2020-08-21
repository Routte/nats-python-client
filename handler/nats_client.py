import asyncio
from handler._handler import Handler

class NatsClient:
  __instance = None

  def __init__(self, servers):
    self.loop = asyncio.get_event_loop()
    self.nats_handler = Handler(loop=self.loop, servers=servers)

  def connect(self):
    self.loop.run_until_complete(self.nats_handler.connect())

  def disconnect(self):
    self.loop.run_until_complete(self.nats_handler.nats.disconnect())

  def subscribe(self, subject, cb):
    self.loop.run_until_complete(self.nats_handler.subscribe(subject=subject, cb=cb))
    try:
      self.loop.run_forever()
    finally:
      self.loop.close()

  def publish(self, subject, msg):
    self.loop.run_until_complete(self.nats_handler.publish(subject=subject, msg=msg))

