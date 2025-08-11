from class_blueprint import ClassBlueprint

#person = ClassBlueprint("Person", [("age", "int") ,("height", "float"),("hair colour", "str")], ["grow", "change person hair colour"])

#person.write_to_file()

#box = ClassBlueprint("Box",[("items", "int") ],["add_item", "get weight"])

#item = ClassBlueprint("Item",[("name", "str"), ("weight", "float")], ["is pretty item"])

#box.write_to_file()
#item.write_to_file()


#worldPoint = ClassBlueprint("WorldPoint", [("place", "string"), ("latitude", "float"), ("longitude", "float")], ["grow"])

#foo = ClassBlueprint("*class name*", [("*attribute1*", "*attribute1type*"), ...], ["method1", ...])
#foo = ClassBlueprint("", [("", ""), ("", ""), ("", "")], [""])
#spell = ClassBlueprint("Spell", [("name", "str"), ("school", "str"), ("level", "int"), ("cast_limit", "int"), ("effect", "str"), ("casts", "int")], ["cast", "recharge"])
#spell.write_to_file()

#cd /Users/anthonyvolpe/Documents/UNI_DEFINITIVE/sum24-25/info1110/labs/9/ClassBlueprint
#
# spellbook = ClassBlueprint("Spellbook",[("material", "str"), ("capacity", "int")], ["add_spell", "cast_spell", "cast_strongest", "cast_all", "recharge_all"])
#
# spellbook.write_to_file()


#song = ClassBlueprint("Song",[("artist", "str"), ("album", "str"), ("name", "str"), ("dat", "str")], ["dummy", "dummy2"])
song = ClassBlueprint("Song", [("artist", "str"), ("album", "str"), ("name", "str"), ("dat", "str")], ["dummy", "dummy2"])

song.write_to_file()
