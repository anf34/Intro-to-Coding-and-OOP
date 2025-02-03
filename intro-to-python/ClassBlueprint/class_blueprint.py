from helper import *
import os




class ClassBlueprint:

    def __init__(self, name, attributes, methods):
        self.validate_input(name, attributes, methods)
        self.name = name
        self.attributes = attributes
        self.methods = methods
        self.camelname = camel_to_snake(name);

    def validate_input(self, name, attributes, methods):
        self.name_check(name)
        self.attribute_check(attributes)
        self.method_check(methods)

    def list_attributes_input(self, file_content):
        file_content.write("")
        for i, (attribute, attr_type) in enumerate(self.attributes):
            snake_attr = str_to_snake_case(attribute)
            if i == len(self.attributes) - 1:
                file_content.write(snake_attr)
            else:
                file_content.write(snake_attr + ", ")
        file_content.write(")")

    def name_check(self, name):
        if not (isinstance(name, str) and name):
            raise TypeError("Name must be a non-empty string.")

    def attribute_check(self, attributes):
        if not (isinstance(attributes, list) and attributes and valid_string_tuples(attributes)):
            raise TypeError("Attributes must be a non empty list of tuples.")

    def method_check(self, methods):
        if not (isinstance(methods, list) and methods and valid_string_list(methods)):
            raise TypeError("Methods must be a non empty list of strings.")

    def write_to_file(self):
        # Open a file in write mode
        with open(self.camelname + ".py", "w") as file_content:
            self.write_constructor(file_content)
            self.write_class(file_content)# Pass the file object to write_constructor

    def write_constructor(self, file_content):
        # The file object is passed and can be used here
        file_content.write(f"class {self.name}:\n")  # Corrected to properly format the class
        file_content.write("\tdef __init__(self, ")  # Add the constructor header
        # Loop through the attributes and format the last one without a comma

        self.insert_attributes_in_declaration(file_content)
        file_content.write("):\n")
        self.group_tests(file_content)

        self.list_attributes_in_constructor(file_content)

    def write_class(self, file_content):
        self.validate_function(file_content)
        self.getter_methods(file_content)
        self.setter_methods(file_content)
        self.write_tests(file_content)
        self.additional_methods(file_content)

    def validate_file(self, file_path):
        if not file_path:
            raise ValueError(f"Not a valid file.")
        return

    def group_tests(self, file_content):
        file_content.write("\t\tself.validate_input(")
        self.list_attributes_input(file_content)
        file_content.write("\n")

    def insert_attributes_in_declaration(self, file_content):
        for i, (attribute, attr_type) in enumerate(self.attributes):
            snake_attr = str_to_snake_case(attribute)  # Unpacking the tuple
            if i == len(self.attributes) - 1:  # Check if it's the last attribute
                file_content.write(snake_attr)  # No comma after the last attribute
            else:
                file_content.write(snake_attr + ", ")

    def insert_test_methods(self, file_content):
        for (attribute, attr_type) in self.attributes:
            snake_attr = str_to_snake_case(attribute)
            file_content.write("\t\tself.validate_" + snake_attr + "(" + attribute + ")\n")
        file_content.write("\n")

    def list_attributes_in_constructor(self, file_content):
        for (attribute, attr_type) in self.attributes:
            file_content.write("\t\tself." + attribute + " = " + attribute + "\n")
        file_content.write("\n")

    def validate_function(self, file_content):
        file_content.write("\tdef validate_input(self, ")
        self.list_attributes_input(file_content)
        file_content.write(":\n")
        self.insert_test_methods(file_content)

    def write_tests(self, file_content):
        for (attribute, attr_type) in self.attributes:
            snake_attr = str_to_snake_case(attribute)
            file_content.write("\tdef validate_" + snake_attr + "(self, " + snake_attr + "):\n")
            if attr_type == "int":
                file_content.write("\t\tif not isinstance(" + snake_attr + ", " + attr_type + ")):\n")
            else:
                file_content.write("\t\tif not (" + snake_attr +" and isinstance(" + snake_attr + ", " + attr_type + ")):\n")
            file_content.write("\t\t\traise TypeError('" + attribute.capitalize() + " must be of type " + attr_type + " and non empty.')\n\n")

    def getter_methods(self, file_content):
        for (attribute, attr_type) in self.attributes:
            snake_attr = str_to_snake_case(attribute)
            file_content.write("\tdef get_" + snake_attr + "(self):\n")
            file_content.write("\t\treturn self." + snake_attr + "\n\n")

    def setter_methods(self, file_content):
        for (attribute, attr_type) in self.attributes:
            snake_attr = str_to_snake_case(attribute)
            file_content.write("\tdef set_" + snake_attr + "(self, " + snake_attr + "):\n")
            file_content.write("\t\tself.validate_"+ snake_attr + "(" + snake_attr + ")\n")
            file_content.write("\t\tself." + snake_attr + " = " + snake_attr + "\n\n")

    def additional_methods(self, file_content):
        for method in self.methods:
            file_content.write("\tdef " + str_to_snake_case(method) + "(self" + "):\n\t\tpass\n\n")

    #Also at the end of the file have an example of an instantiation of the class object
