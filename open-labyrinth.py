#Your code here
#You can import some modules or create additional functions


def checkio(maze_map):
    #replace this for solution
    #This is just example for first maze
    return "SSSSSEENNNEEEEEEESSWWWWSSSEEEESS"
    
    queue = [((1, 1), "")] # we will use list for simplicity
    
    visited = set()
    
    while queue:
        position, path = queue.pop(0)
        if position == (10, 10):
            return path
        if position in visited:
            continue
    
    for neigh_position, direction in get_neighbours(maze, positions):
        if neigh_position in visited:
            continue
        queue.append(neigh_position, path + direction)