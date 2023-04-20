class Map:
    def __init__(self, rooms):
        self.rooms = rooms
        self.map = {}

    def build_map(self):
        for room in self.rooms:
            self.map[room] = {}
            for direction, connected_room in room.exits.items():
                self.map[room][direction] = connected_room

    def draw_map(self, current_room):
        print("Building map...")
        print("=====================================")
        self.build_map()

        positions = {}
        current_pos = (0, 0)
        stack = [(current_pos, self.rooms[0])]
        while stack:
            pos, room = stack.pop()
            if room not in positions:
                positions[room] = pos
                for direction, connected_room in self.map[room].items():
                    if direction == "right":
                        new_pos = (pos[0], pos[1] + 1)
                    elif direction == "left":
                        new_pos = (pos[0], pos[1] - 1)
                    elif direction == "up":
                        new_pos = (pos[0] - 1, pos[1])
                    elif direction == "down":
                        new_pos = (pos[0] + 1, pos[1])
                    stack.append((new_pos, connected_room))

        min_x = min(pos[1] for pos in positions.values())
        max_x = max(pos[1] for pos in positions.values())
        min_y = min(pos[0] for pos in positions.values())
        max_y = max(pos[0] for pos in positions.values())

        for y in range(min_y, max_y + 1):
            row = ''
            for x in range(min_x, max_x + 1):
                room = None
                for r, pos in positions.items():
                    if pos == (y, x):
                        room = r
                        break
                if room is not None:
                    room_number = self.rooms.index(room) + 1
                    room_marker = "[R{}{}]".format(room_number, "*" if room == current_room else "")
                    row += room_marker
                else:
                    row += "    "
            print(row)
        print("=====================================")
