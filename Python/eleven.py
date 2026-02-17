

world={"afganistan":30.5 ,"india":19.2,"china":20.8} #dictionary

print(world["india"])#19.2
print(world)


print(world.keys())#dict_keys(['afganistan', 'india', 'china'])

print(world.values())#dict_values([30.5, 19.2, 20.8])

print('italy' in world)#False
#keys are immutable and values are mutable
world={["afganistan","india","china"]:["nation"]} #TypeError: unhashable type: 'list'
print(world)


