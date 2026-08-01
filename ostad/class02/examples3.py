name = input("Enter your name: ")
age_text = input("Enter your age: ")  # this is a STRING, e.g. "25"
salary_text = input("Enter your monthly salary: ")

age = int(age_text)  # string -> integer
salary = float(salary_text)  # string -> float (supports decimals)

age_after_10_years = age + 10
yearly_salary = salary * 12

# "+" on two strings means concatenation, NOT addition.
wrong_result = age_text + age_text  # "25" + "25" -> "2525"
right_result = age + age  # 25 + 25 -> 50

print("\n----- Summary -----")
print(f"Name              : {name}")
print(f"Type of age_text  : {type(age_text)}")  # <class 'str'>
print(f"Type of age       : {type(age)}")  # <class 'int'>
print(f"Age after 10 years: {age_after_10_years}")
print(f"Yearly salary     : {yearly_salary}")
print(f"String '+'  (concatenation): {wrong_result}")
print(f"Integer '+' (addition)     : {right_result}")
