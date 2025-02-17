class Adventurer:
    def __init__(self):

        #All attributes initialised to default as required
        self.inventory = []
        self.skill = 5
        self.will = 5

    def get_inv(self):
        return self.inventory

    def get_skill(self):
        # """TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.skill

    def get_will(self):
        # """TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.will

    def take(self, item):
        """TODO: Adds an item to the adventurer's inventory."""
        #Make sure it adds an item object!
        #!!Validate item
        if not item.get_obtained():
            item.set_obtained(True)
            self.skill += item.get_skill_bonus()
            self.will += item.get_will_bonus()
            self.inventory.append(item)
        else:
            print("You've already picked up this item")

    def check_self(self):
        print("You are an adventurer, with a SKILL of 5 and a WILL of 5.")
        print("You are carrying: \n")

        if len(self.inventory) != 0:
            for item_ in self.inventory:
                print(item_.get_name())
                print("Grants a bonus of " + item_.get_skill_bonus() + " to SKILL.")
                print("Grants a bonus of " + item_.get_will_bonus() + " to WILL.")

        else:
            print("Nothing.")
        print("With your items you have a SKILL level of " + self.skill + " and a WILL power of " + self.will)
        #"""TODO: Shows adventurer stats and all item stats."""
        pass

    def set_inventory(self, inventory):
        self.validate_inventory(inventory)
        self.inventory = inventory

    def set_will(self, will):
        self.validate_will(will)
        self.will = will

    def set_skill(self, skill):
        self.validate_skill(skill)
        self.skill = skill

    def validate_input(self, inventory, skill, will):
        if not (inventory and isinstance(inventory, list)):
            raise TypeError("inventory must be of type list and non-empty.")
        if not isinstance(skill, int):
            raise TypeError("skill must be of type int and non-empty.")
        if not isinstance(will, int):
            raise TypeError("will must be of type int and non-empty.")
