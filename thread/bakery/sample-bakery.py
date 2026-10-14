from thread.bakery.baker import Baker
from thread.bakery.bakery import Bakery
from thread.consumer import Consumer


bakery = Bakery()

baker = Baker(bakery)
consumer = Consumer(bakery)

consumer.start()
baker.start()
