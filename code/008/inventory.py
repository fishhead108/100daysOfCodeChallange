class Room:
    """
    This class define room
    """
    number_of_rooms = 0

    def __init__(self, items: dict, name: str):
        self.items = items
        self.name = name
        Room.number_of_rooms += 1

    def __repr__(self):
        return f"This room has {', '.join(self.items.keys())} and it cost is {sum([x for x in self.items.values()])}"

    def inventory(self):
        print(f"{'ITEM':<8} {'COST':<8}")
        for item in self.items.items():
            print("{:<8} {:<8}".format(*item))
        print(f"\nTOTAL: {sum(self.items.values()):>4}")

    def add_item(self, new_item: dict):
        self.items.update(new_item)

    def delete_item(self, item_name):
        del self.items[item_name]

    def list_items(self):
        return len(self.items)

def list_rooms(rooms):
    for room in rooms:
        print(f"ROOM: {room.name}:^8")
        print(f"{'ITEM':<8} {'COST':<8}")
        for item in room.items.items():
            print("{:<8} {:<8}".format(*item))
    print(f"\nTOTAL: {sum(rooms.items.values()):>4}")