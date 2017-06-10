"""
Create some sort of program shell with a menu system around this. ie, "Which room would you like to list out?"

If you're really game, allow users to create rooms and update information.

You could even make an API with Flask or your preferred framework

Have persistent storage of the data. sqlite3 = stdlib and light-weight, but feel free to use your preferred DB / module.
"""


class House:
    rooms = []

    def __init__(self):
        pass

    @staticmethod
    def add_room(room):
        House.rooms.append(room)

    @staticmethod
    def list_rooms():
        for room in House.rooms:
            print(f"\n{room.name.upper():<8}")
            print(f"{'ITEM':<8} {'COST':<8}")
            for item in room.items.items():
                print("{:<8} {:<8}".format(*item))

        money = [list(room.items.values()) for room in House.rooms]
        print(f"\nTOTAL: {sum([y for x in money for y in x]):>5}")


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


def menu():
    print("""
    1). Show available rooms          +--+
    2). Add new room                  |  |
    3). Add item to the room          |  |
    4). Remove item from the room     |  |  XXXXXXXXXXXXX
    5). Exit                          |  |XXX           XXX
                                      |  |X               XXX
                                      +--+                  XX
                                     XXX                     XXX
                                    XX------------------------XXX
                                    +                           |
                                    |                           |
                                    |  +------+      +------+   +-----+
                                    |  |___|__|      |___|__|   |     |
                                    |  |   |  |      |   |  |   |     |
                                    |  +------+      +------+   |    ++
                                    |                           |    ++
                                    |                           |     |
                                    |                           |     |
                                    +---------------------------+-----+
    """)

def main():
    house = House()
    house.add_room(Room(name='bedroom', items={'cup': 3, 'bath': 200, 'soap': 1, 'item4': 12, 'item5': 33}))
    house.add_room(Room(name='bathroom', items={'cup': 4, 'bath': 100, 'soap': 6, 'item4': 52, 'item5': 23}))
    house.add_room(Room(name='kitchen', items={'cup': 5, 'bath': 20, 'soap': 5, 'item4': 4, 'item5': 53}))
    house.add_room(Room(name='baby room', items={'cup': 6, 'bath': 500, 'soap': 2, 'item4': 32, 'item5': 63}))
    house.add_room(Room(name='living room', items={'cup': 73, 'bath': 50, 'soap': 3, 'item4': 22, 'item5': 73}))

    house.list_rooms()


if __name__ == '__main__':
    main()
