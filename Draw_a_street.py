"""
Task: Draw a street
Given an array of tuples (int, int) indicating one or more buildings height and width,
draw them consecutively one after another as in a street. ("■" for walls)
- The minimum size of a building is (4, 5)
- A buildings width is always going to be odd.
- The sizes of buildings are random.
- Some buildings are going to be smaller than others, leaving some space overhead " ".
- Every building has a door, which looks the same regardless of the buildings height and width
___ <-- The door
| |
| |
- Between every building there are 2 spaces "  ". However if there is only 1 building there isn't any extra space.
- The street has a sidewalk made with the character / from the
beginning of the first building to the end of the last building.
- The street has street lights:
   - Streetlights are set every 10 spaces
   - They are closer forward to the viewer, which is why they will block other objects like building walls, doors,
    and sidewalks. Streetlights look like this:
         #
         |
         |
/////////|//////////

■■■■■■■
■     ■             <---Street
■     ■  ■■■■■
■     ■  ■   ■
■ ___ ■  #___■
■ | | ■  || |■
■ | | ■  || |■
/////////|////
"""


class Street:
    def __init__(self, buildings):
        self.buildings = buildings
        self.street_height = max(buildings)[0] + 1
        self.street_width = sum(buildings_width[1] for buildings_width in buildings) + 2 * (len(buildings) - 1)
        self.build_list = [[" "] * self.street_width for x in range(self.street_height)]
        self.x = self.street_height - 2
        self.y = 0

    def wall(self, height):
        for point in range(self.x, self.x - height, -1):
            self.build_list[point][self.y] = "■"

    def roof(self, height,  width):
        for point in range(self.y, self.y + width):
            self.build_list[self.street_height - height - 1][point] = "■"

    def door(self, height, width):
        dist_to_door = width // 2 - 1
        for point in range(self.x, self.x - 2, -1):
            self.build_list[point][self.y + dist_to_door] = "|"
            self.build_list[point][self.y + dist_to_door + 2] = "|"
        for count in range(0, 3):
            self.build_list[-4][self.y + dist_to_door + count] = "_"

    def houses(self, height, width):
        self.roof(height, width)
        self.door(height, width)
        # left wall
        self.wall(height)
        # right wall
        self.y += width - 1
        self.wall(height)
        self.y += 3

    def sidewalk(self):
        self.build_list[-1] = ["/" for char in self.build_list[-1]]

    def light(self):
        for point in range(9, self.street_width, 10):
            self.build_list[-1][point] = "|"
            self.build_list[-2][point] = "|"
            self.build_list[-3][point] = "|"
            self.build_list[-4][point] = "#"

    def build_street_lst(self):
        for height, width in self.buildings:
            self.houses(height, width)
        self.sidewalk()
        self.light()

    def get_str(self):
        res_str = ""
        for stg in self.build_list:
            if stg == self.build_list[-1]:
                res_str += "".join(stg)
            else:
                res_str += "".join(stg) + "\n"
        return res_str


# test
street = Street([(5, 5), (7, 5), (5, 7)])
street.build_street_lst()
print(street.get_str())


