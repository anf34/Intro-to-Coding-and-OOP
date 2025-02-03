As is, this script took a while to make and is already saving me a lot of time in the long run. I will use it as a prototype for a while so I can discover the programs flaws before making any major changes to it.

Class maker program (Written in python, will soon write IN P5 INSTEAD, to generate python or p5 classes)
Input: Specify the class name, attributes, each of the attribute types and any extra methods
Class maker will then:
- make a class with given name
- perform a check to see if all provided types are the same as their attribute types
- all extra methods will pass (beta version)
- if x attribute is of type list the class will add a has_x(input) method which returns true if the list contains the input (in progress)
- automatically make setter and getter methods for each attribute
- the setters will check the input value is valid
- it will also check that input strings are not empty

Notes: Make sure input is CamelCase cause I don't how to do word recognition.
must put underscore for attributes
The extra methods list must contain a method or the program crashes*

For example

person = ClassBlueprint("Person", [("age", "int"), ("height", "float"), ("hair colour", "str")], ["grow", "change person hair colour"])

Future improvements:
FIXED? 0 evaluates to false in python so this code currently doesn't let you use 0 as an int...
Change the order of the functions so they show up in this file as they show up in write_constructor.
Change the order of the functions so they show up in this file as they show up in write_constructor.
str_to_snake_case and camel_to_snake are very similar functions in the helper file.
The helper file is a liability. Currently must ensure it is always in the same directory as this file.
Make (self, attribute0, attribute1, ...) a string and simply write the string whenever that is needed, instead of calling a function that writes it for you.
More compartmentalisation needed
Add comments
Extra feature: if one of the attributes is a list, automatically add a function to the file called "has_attribute_name", eg an attribute for a list of nicknames, the has function has_nickname(str) will return true if str is one of the nicknames.
Come up with a better system to keep track of number of tabs
Do a test to make sure none of attributes or method are the empty string.
*The program fails if the user does not specify any extra methods, which it shouldn't, because sometimes extra methods are not necessary.
Additionally the program might fail if the user tries to put their own class in as an attribute.
Future future: make the program more "blocky", eg instead of them having type "str" in every time they want an attribute with a str, have them click buttons to select their class attributes, like in scratch. This will also remove the chances of the user thinking "string" is the name of the string type in python, it isn't, "str" is.
At the end of the file have the program generate an example class and then have the program try to break the class by putting incorrect tests in
have the program add comments too
