from thread.name_thread import NameThread
import time

thread1 = NameThread("Tu vieja en tanga")
thread1.start()
# time.sleep(1/100000)

thread2 = NameThread("Pampita")
thread2.start()

thread3 = NameThread("Maria Roe")
thread3.start()

print(f"Thread1 is Alive: {thread1.is_alive()}")
print(f"thread2 is Alive: {thread2.is_alive()}")
print(f"thread3 is Alive: {thread3.is_alive()}")