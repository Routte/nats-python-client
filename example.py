from src.nats_client import NatsClient

servers = "nats://45.32.192.50:8080"
subject = "events.*"

nc = NatsClient(servers)
nc.connect()

async def message_handler(msg):
  subject = msg.subject
  reply = msg.reply
  data = msg.data.decode()
  print("Received a message on '{subject} {reply}': {data}".format(
      subject=subject, reply=reply, data=data))

nc.subscribe(subject, cb=message_handler)