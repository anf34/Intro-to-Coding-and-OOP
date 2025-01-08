from class_blueprint import ClassBlueprint

person = ClassBlueprint("Person", [("age", "int") ,("height", "float"),("hair colour", "str")], ["grow", "change person hair colour"])

person.write_to_file()

box = ClassBlueprint("Box",[("items", "int") ],["add_item", "get weight"])

item = ClassBlueprint("Item",[("name", "str"), ("weight", "float")], ["is pretty item"])

#box.write_to_file()
#item.write_to_file()
