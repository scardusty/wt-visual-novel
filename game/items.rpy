init python:
    class InventoryItem:
        def __init__(self, name, description, cost = 0):
            self.name = name
            self.description = description
            self.cost = cost


    class Inventory:

        def __init__(self, items):
            self.items = items

        def __str__(self):
            return f"{self.items[0]}"
        
        def list_items(self):
            output = ""
            if self.items.__len__() < 1:
                output = f"I ain't got nothing :P "
                return output

            elif self.items.__len__() > 0:
                output = ""
                for i in self.items:
                    output += f"{i.name}. {i.description}. total items: {self.items.__len__()}\n"
                    #{len(self.items.__len__())}\n"
                return output
            else:
                return output
            pass
            

        def add_item(self, item):
            self.items.append(item)
            pass

        def remove_item(self, item):
            self.items.remove(item)
            pass

        def clear(self):
            self.items = []
            pass
        #def buy_item(self, item):
        #    if money >= item.cost:
        #        money -= item.cost
        
        #        self.add_item(item)
        #    else:
        #        print(f"I can't afford this.")

        #def earn(self, amount):
            #money += amount
#
        # def has_item(self, item):
        #       if item in self.items:
        #           return True
        #        else:
        #            return False
    


    potatoes = InventoryItem("Potatoes", "yummy", 0)
    olives = InventoryItem("Olives", "ok", 0)
    chocolate = InventoryItem("Chocolate", "delicioso", 0)


 
define inventory = Inventory([potatoes])

screen inventory_screen():
    tag menu
    use game_menu(_("Stuff"), scroll="viewport"):          
        has hbox
        hbox:
            spacing 10
            xalign 0.5
            yalign 1.0
            xfill True
            
            frame:
                xalign 0.5
                yalign 0.5
                ypadding 30
                xpadding 30
                xoffset -40
                has vbox
                text "Hello?"
                text inventory.list_items()
                textbutton "add potatoes" action ToggleSetMembership(inventory.items, potatoes)
                textbutton "add olives" action ToggleSetMembership(inventory.items, olives)
                textbutton "clear inventory" action Function(inventory.clear)

#screen list_inventory:
    # text inventory.list_items()



