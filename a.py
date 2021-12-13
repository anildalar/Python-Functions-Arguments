from string import Template
#print("Hello Anil")

#1. FUnction defination
def greeting(n1,n2,n3,n4,n5): # n1,n2...,n5 are formal argument/Parameter

    # There are 4 Techniques for string substitution/Interpolation

    #
    print("Hello "+n5+", How are you?")

    print(f"Hello {n1}, How are you?")
    # 2. Str.format()
    print("Hello {}, How are you?".format(n2))

    # 3. %-formatting
    print("Hello %s, How are you?"%(n3))

    # 4. Template Strings
    new = Template("Hello $name, How are you?")
    print(new.substitute(name= n4))

#2. FUnction calling

greeting("Manish","Avadhi","Deepak","Ritik","Avinash") # "Manish" is string and  is a actual argument/parameter




# Arbitrary argument *
print(" \n Arbitrary argument \n ")

def hello(*n):
    print(f"Hello {n[2]}, How are you")
    print(f"Hello {n[1]}, How are you")


hello("Anil","Avadhi","Manish")


#Keyword Arguments
print(" \n Keyword Arguments \n ")

# Number of Actual Arguments must be equal to number of formal arguments

def hello2(student1,friend1):
    print("Hello {}, How are you. You are my Friend".format(friend1))
    print("Hello {}, How are you. You are my Student".format(student1))


hello2(student1="Avadhi",friend1="Manish")# key=value


print(" \n Arbitrary Keyword Arguments, **kwargs \n ")
# Arbitrary Arguments, *args +  Keyword Arguments = Arbitrary Keyword Arguments, **kwargs

def hello3(**n):
    print("Hello %s, How are you ? You are my Student."%(n["student1"]))
    print("Hello %s, How are you ? You are my Friend."%(n["friend1"]))

hello3(student1="Avadhi",friend1="Manish")