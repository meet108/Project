# function with arguments
# Types Of Arguments
# 1. Default
def add(a=4, b=3):
    c = a+b
    print(f"Sum is {c}")
add(2,4)

# 2. Positional
def gree(name,dept):
    print("Name: ",name)
    print("Department: ",dept)
gree("Meet","CS")

# 3. Keyword
def gree(name,dept):
    print("Name: ",name)
    print("Department: ",dept)
gree(dept="CS", name="Meet")

# 4. arbitary
