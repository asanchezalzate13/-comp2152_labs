
class Person:
    def __init__(self, name, age, height):
        print("Constructing the person object.")
        self.name = name
        self.age = age
        self.height = height
        self.public_prop = "Im public"

        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self, new_name):
            self.__name = new_name

        def __del__(self):
            print("The person has been deleted.")


    person1 = Person("Joe", 30, 178)
    print("The name of the person is: "+str(person1.name))
    print("The age of the person is: "+str(person1.age))

