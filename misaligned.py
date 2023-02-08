
def create_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map=[]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map


result = create_color_map()
map_number=1
for pair_number in range(len(result)):
    assert(pair_number==map_number)
    map_number+=1
assert(result[1] == 2)
print("All is well (maybe!)\n")
