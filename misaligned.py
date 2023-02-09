
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
for pair_number in result:
    num,minor,major=pair_number.split('|')
    assert(pair_number[0:2]==map_number)
    assert(int(num)==map_number)
    map_number+=1

    
print("All is well (maybe!)\n")
