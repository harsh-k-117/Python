components=["Resistor", "Capacitor", "Inductor", "Diode"] # type: ignore

for index, component in enumerate(components):
    print("Index", {index}, " : ", {component})

print("\nAccessing the Components by Index:- ")
for i in range(len(components)):
    print("Component at index {" +str(i)+ "} : "+str({components[i]}))

new_component="L.E.D"
new_length=len(components)+1
new_array=[None]*new_length

for i in range(len(components)):
    new_array[i]=components[i]
new_array[-1]=new_component
components=new_array

print("\nUpdated List of the Components:- ")
for index, component in enumerate(components):
    print("Index", {index},{component})