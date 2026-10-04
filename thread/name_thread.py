from threading import Thread
import time

#por convencion las clases theard siempre terminan con thread
class NameThread(Thread):

    def __init__(self, name: str):
        super().__init__(name=name)


    def run(self):
        print(f"Se inicia el metodo run del hilo {self.name}")

        for i in range(10):
            time.sleep(10/1000)
            print(f"{i}-{self.name}")

        print(f"Finaliza el Hilo: {self.name}")