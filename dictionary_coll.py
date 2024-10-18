players = {"Name": "Virat", "Age": "35", "Team": "India", "Role": "Captain"}
print(players)
print(type(players))

print("Iteration Through Keys")
for i in players:
    print(i)

print("Iteration Through Values")
for i in players.values():
    print(i)

print("Iteration Through Keys & Values")
for key, value in players.items():
    print(key, value)
