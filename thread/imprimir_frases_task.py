from dataclasses import dataclass
import time
from threading import Lock
from thread.functions import print_phrases

_lock = Lock()
@dataclass
class PrintPhrasesTask:
    phrase1: str
    phrase2: str

    # def run(self)-> None:
    #     with _lock:
    #         print(self.phrase1, end=" ")#, flush=True)
    #         #El flush sirve para que se muestre inmediatamente el print, sin esperar a que termine la ejecucion del hilo
    #         time.sleep(0.5)
    #         print(self.phrase2)#, flush=True)

    def __call__(self)-> None:
        print_phrases(text=self.phrase1, text2=self.phrase2)
