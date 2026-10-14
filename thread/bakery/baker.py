from threading import Thread
from thread.bakery.bakery import Bakery
import random
import time

class Baker(Thread):
    def __init__(self, bakery: Bakery):
        super().__init__()
        self.bakery = bakery

    def run(self):
        for i in range(10):
            self.bakery.bake(f"Pan num: {i}")
            time.sleep(random.uniform(0.5, 2))
            