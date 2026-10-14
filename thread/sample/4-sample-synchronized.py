from threading import Thread #, Lock
from thread.imprimir_frases_task import PrintPhrasesTask


t1 = Thread(target=PrintPhrasesTask("Hola", "Que Tal"))
t1.start()

t2 = Thread(target=PrintPhrasesTask("Quien Eres", "Tu"))
t2.start()

t3 = Thread(target=PrintPhrasesTask("Muchas Gracias", "Amigo"))
t3.start()

