from threading import Thread, current_thread
import time
from random import random

def travel_task()-> None:
        for i in range(10):
            print(f"{i}-{current_thread().name}")
            time.sleep(random())
        print(f"Finalmente voy a viajar a : {current_thread().name}")

travel = lambda: travel_task()

thread1 = Thread(target=travel, name="Isla de Pascua")#.start()
thread1.start()

# task = TravelTask(name="Isla de Pascua")
thread2 = Thread(target=travel, name="Malargue")
thread2.start()
thread3 = Thread(target=travel, name="El nihuil")
thread3.start()
thread4 = Thread(target=travel, name="Villa Atuel")
thread4.start()
thread5 = Thread(target=travel, name="La llave vieja")
thread5.start()
thread6 = Thread(target=travel, name="Jaime Prats")
thread6.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()

# time.sleep(7)
print("Continuando con la ejecucion del thread principal")