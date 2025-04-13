components = ["Resistor", "Capacitor", "Inductor", "Diode"]

# Loop through components and print index and component
for index, component in enumerate(components):
    print(f"Index {index} : {component}")

print("\nAccessing the Components by Index:- ")

# Access the components by index and print them
for i in range(len(components)):
    print(f"Component at index {i} : {components[i]}")

# Adding a new component ("L.E.D")
new_component = "L.E.D"
new_length = len(components) + 1
new_array = [None] * new_length

# Copy existing components to the new array
for i in range(len(components)):
    new_array[i] = components[i]

# Add the new component at the end
new_array[-1] = new_component

# Update the components list
components = new_array

# Print the updated list of components
print("\nUpdated List of the Components:- ")
for index, component in enumerate(components):
    print(f"Index {index}: {component}")
