from src.nats_client import NatsClient

servers = "nats://127.0.0.0:4222"
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
nc.publish(subject, "Hello world")