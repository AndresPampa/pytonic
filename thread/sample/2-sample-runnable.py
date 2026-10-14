from threading import Thread
from thread.sample.travel_task import TravelTask


# task = TravelTask(name="Isla de Pascua")
Thread(target=TravelTask(name="Isla de Pascua").run).start()
Thread(target=TravelTask(name="El nihuil").run).start()
Thread(target=TravelTask(name="Villa Atuel").run).start()
Thread(target=TravelTask(name="La llave vieja").run).start()
Thread(target=TravelTask(name="Jaime Prats").run).start()