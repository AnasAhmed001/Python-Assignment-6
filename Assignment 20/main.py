class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    return "Age is valid"

# Test the function with try-except
try:
    result = check_age(15)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    result = check_age(20)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")