# Functions with Parameters
def name(stname):
    print("Hello ",stname)

name("Eagle")

# Default Parameters
def hello(name="Eagle"):
    print("Hellow",name)
hello()    

# Returning values
def hello(name="Eagle"):
    return "Hellow "+name

greeting = hello()
print(greeting)

# Returning Multiple Values
def hello(name="Eagle"):
    return ("Hellow",name)

(greeting, person)=hello()
print(greeting,"to",person)

# Documenting Functions
def build(name="CGV"):
     '''Build a greeting in the format  Hello plus a given name'''
     return ("Hello", name)
