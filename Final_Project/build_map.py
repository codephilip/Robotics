#Created By: Michael Roduin
#Date: 5/1/22

import random

class node:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.action = "None"

    def set_border(self, node):
        if node.x > self.x:
            self.east = node
            node.west = self
        elif node.x < self.x:
            self.west = node
            node.east = self
        elif node.y > self.y:
            self.south = node
            node.north = self
        elif node.y < self.y:
            self.north = node
            node.south = self
        else:
            print("Error During Border Processing")

    def get_bordering(self):
        return (self.north, self.east, self.south, self.west)

    def get_north(self):
        return self.north

    def get_east(self):
        return self.east

    def get_south(self):
        return self.south

    def get_west(self):
        return self.west

    def get_action(self):
        return self.action

def generate_level_2():
    #Generate map and connections
    game_map = [[node(x,y) for y in range(0,3)] for x in range(0,3)]
    game_map[0][0].set_border(game_map[1][0])
    game_map[1][0].set_border(game_map[2][0])
    game_map[2][0].set_border(game_map[2][1])
    game_map[1][0].set_border(game_map[1][1])
    game_map[1][1].set_border(game_map[0][1])
    game_map[1][1].set_border(game_map[1][2])
    game_map[0][1].set_border(game_map[0][2])
    game_map[1][2].set_border(game_map[2][2])
    
    #Add Actions
    corner_options = [(0,0),(0,2),(2,0),(2,2)]
    start = random.choice(corner_options)
    corner_options.remove(start)
    end = random.choice(corner_options)
    game_map[start[0]][start[1]].action = "Start"
    game_map[end[0]][end[1]].action = "End"
    map_options = [(x,y) for x in range(0,3) for y in range(0,3)]
    map_options.remove(start)
    map_options.remove(end)
    action_tiles = ["Recharge", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Medium_Enemy_With_Key", "Medium_Enemy"]
    random.shuffle(map_options)
    for item in action_tiles:
        tile = map_options.pop()
        game_map[tile[0]][tile[1]].action = item
    return game_map

def generate_level_3():
    #Generate map and connections
    game_map = [[node(x,y) for y in range(0,5)] for x in range(0,5)]
    game_map[0][0].set_border(game_map[1][0])
    game_map[1][0].set_border(game_map[2][0])
    game_map[1][0].set_border(game_map[1][1])
    game_map[2][0].set_border(game_map[2][1])
    game_map[3][0].set_border(game_map[4][0])
    game_map[4][0].set_border(game_map[4][1])
    game_map[0][1].set_border(game_map[1][1])
    game_map[0][1].set_border(game_map[0][2])
    game_map[1][1].set_border(game_map[1][2])
    game_map[3][1].set_border(game_map[4][1])
    game_map[3][1].set_border(game_map[3][2])
    game_map[4][1].set_border(game_map[4][2])
    game_map[0][2].set_border(game_map[0][3])
    game_map[1][2].set_border(game_map[2][2])
    game_map[2][2].set_border(game_map[3][2])
    game_map[3][2].set_border(game_map[3][3])
    game_map[4][2].set_border(game_map[4][3])
    game_map[0][3].set_border(game_map[1][3])
    game_map[1][3].set_border(game_map[1][4])
    game_map[2][3].set_border(game_map[2][4])
    game_map[3][3].set_border(game_map[4][3])
    game_map[3][3].set_border(game_map[3][4])
    game_map[0][4].set_border(game_map[1][4])
    game_map[1][4].set_border(game_map[2][4])
    game_map[3][4].set_border(game_map[4][4])

    #Add Actions
    corner_options = [(0,x) for x in range(0,5)] + [(x,0) for x in range(0,5)] + [(4,x) for x in range(0,5)] + [(x,4) for x in range(0,5)]
    start = random.choice(corner_options)
    corner_options.remove(start)
    end = random.choice(corner_options)
    game_map[start[0]][start[1]].action = "Start"
    game_map[end[0]][end[1]].action = "End"
    map_options = [(x,y) for x in range(0,5) for y in range(0,5)]
    map_options.remove(start)
    map_options.remove(end)
    action_tiles = ["Recharge", "Recharge", "Recharge", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Weak_Enemy", "Medium Enemy", "Medium Enemy", "Medium Enemy", "Medium Enemy", "Medium Enemy", "Hard Enemy", "Hard Enemy",  "Coffee Shop", "Coffee Shop", "Fun Node", "Fun Node", "Riddle"]
    random.shuffle(map_options)
    for item in action_tiles:
        tile = map_options.pop()
        game_map[tile[0]][tile[1]].action = item
    return game_map

def get_start_direction(game_map):
    for x in game_map:
        for node in x:
            if node.action == "Start":
                options = []
                if node.north:
                    options.append("North")
                if node.south:
                    options.append("South")
                if node.east:
                    options.append("East")
                if node.west:
                    options.append("West")
                if len(options) == 0:
                    print("Error: Unaccessible Node")
                return random.choice(options)

def get_start_position(game_map):
    for x in game_map:
        for node in x:
            if node.action == "Start":
                return (node.x, node.y)

"""
game_map = generate_level_2()
for x in range(0,3):
    for y in range(0,3):
        print(x,y,game_map[x][y].action)
"""
"""
game_map = generate_level_3()
for x in range(0,5):
    for y in range(0,5):
        print(x,y,game_map[x][y].action)

print(get_start_direction(game_map))
"""
