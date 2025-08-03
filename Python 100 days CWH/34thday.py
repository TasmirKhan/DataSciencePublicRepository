print("Dictionary Methods")
Memory = {256:8, 128:4,64:2,32:1,16:1,512:16,1024:32}
battery = {"18w":4000,"60w":6000, "32w":5000}
print(Memory, " and ",battery)

Memory.update(battery)
print(Memory)
# battery.clear()
Memory.pop(16)
print(Memory)
print(battery.popitem())
print(battery)
del Memory["60w"]
print(Memory)
# # ep1.update(ep2)
# # ep1.clear()
# # ep1.pop(122)
# ep1.popitem()
# del ep1[122]
# print(ep1) 
