from recursion.components import Component

def recursive_function(c:Component, level: int = 0):
    print("\t" * level + c.name)
    c.level = level
    print(c.level)
    if c.has_children():
        for child in c.children:
            recursive_function(child, c.level + 1 )


pc = Component(name="Gabinete PC ATX")
power = Component(name="Fuente de poder")
motherboard = Component(name="Motherboard ASUS")
cpu = Component(name="CPU Intel Core i7")   
heatsink = Component(name="Disipador de calor")
graphic_card = Component(name="Tarjeta de video")
gpu = Component(name="GPU NVIDIA GeForce RTX 3080")
gpu_ram = Component(name="8gb Memoria de video GDDR6X")
gpu_ram2 = Component(name="8gb Memoria de video GDDR6X")
ram = Component(name="16gb Memoria RAM DDR4")
ssd = Component(name="SSD 1TB")


cpu.add_children(heatsink).add_children(ram).add_children(ram).add_children(ssd)
graphic_card.add_children(gpu).add_children(gpu_ram).add_children(gpu_ram2)
motherboard.add_children(cpu).add_children(graphic_card)

pc.add_children(power).add_children(motherboard).add_children(graphic_card)\
    .add_children(cpu).\
        add_children(heatsink).\
            add_children(ram).\
                add_children(ram).add_children(ssd).add_children(Component(name="Teclado"))

print("START".center(50, "-"))
recursive_function(pc)
print("---------------------------------------------------".center(50))
recursive_function(motherboard)
print("---------------------------------------------------".center(50))
recursive_function(graphic_card)
print("---------------------------------------------------".center(50))
recursive_function(cpu)