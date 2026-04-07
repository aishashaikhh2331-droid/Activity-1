name = "Tanu"
age = "20" # BUG 1: age should be a number (int), not text (string)
def greet(name):
print(f"Hello, {name}!") # BUG 2: this line is not indented — Python needs indentation
def check_age(age):
if age = 18: # BUG 3: = is assignment, should be == for comparison
print("You are 18")
def calculate(a, b):
result = a / 0 # BUG 4: cannot divide by zero, should be a / b
return result
def add(a, b):
return a + b
total = add(5) # BUG 5: add() needs 2 arguments, only 1 given
def count():
i = 0
while i < 5:
print(i) # BUG 6: i never changes — this loop runs forever!
def main():
greet(name)
check_age(age)
calculate(10, 2)
count()
if _name_ == "_main_":
main()
