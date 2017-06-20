"""
Create some sort of program shell with a menu system around this. ie, "Which room would you like to list out?"

If you're really game, allow users to create rooms and update information.


Have persistent storage of the data. sqlite3 = stdlib and light-weight, but feel free to use your preferred DB / module.
"""


from shutil import get_terminal_size


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


def main_menu():
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

def show_room_menu():
    print("""
    1). Show available rooms
    2). Exit
    """)


def add_room_menu():
    print("""
        1). Add new room.
        2). Exit
        """)

def add_item_to_room_menu():
    pass

def removeitem_from_room():
    pass

def main():
    house = House()
    loop = True
    while loop:
        main_menu()
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:
            menu1 = True
            while menu1:
                # TODO: clean STDOUT
                show_room_menu()
                choice = int(input("Enter your choice [1-2]: "))
                if choice == 1:
                    house.list_rooms()
                elif choice == 2:
                    menu1 = False
                else:
                    pass

        elif choice == 2:
            menu2 = True
            while menu2:
                # TODO: clean STDOUT
                add_room_menu()
                choice = int(input("Enter your choice [1-2]: "))
                if choice == 1:
                    room_name = input("Enter room name: ")
                    raw_items = input("Enter items with cost. Example - soap: 20, table: 30: ")
                    items = {}
                    for item in raw_items.split(','):
                        key, value = item.split(':')
                        items.update({key.strip(): int(value.strip())})
                    house.add_room(Room(name=room_name, items=items))
                    menu2 = False
                elif choice == 2:
                    menu2 = False
                else:
                    pass

        elif choice == 3:
            print("Menu 3 has been selected")
            break
            ## You can add your code or functions here
        elif choice == 4:
            print("Menu 4 has been selected")
            break
            ## You can add your code or functions here
        elif choice == 5:
            print("You choose to exit")
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")
        #
        # house.add_room(Room(name='bedroom', items={'cup': 3, 'bath': 200, 'soap': 1, 'item4': 12, 'item5': 33}))
        # house.add_room(Room(name='bathroom', items={'cup': 4, 'bath': 100, 'soap': 6, 'item4': 52, 'item5': 23}))
        # house.add_room(Room(name='kitchen', items={'cup': 5, 'bath': 20, 'soap': 5, 'item4': 4, 'item5': 53}))
        # house.add_room(Room(name='baby room', items={'cup': 6, 'bath': 500, 'soap': 2, 'item4': 32, 'item5': 63}))
        # house.add_room(Room(name='living room', items={'cup': 73, 'bath': 50, 'soap': 3, 'item4': 22, 'item5': 73}))
        #
        # house.list_rooms()


if __name__ == '__main__':
    main()
