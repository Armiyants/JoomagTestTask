from src.driver import start_driver
from src.helpers import url_validator

user_input = input()

# Checking the validation of user input URL
is_valid = url_validator(user_input)
if is_valid:
    # setting default protocol to http if not provided
    if not user_input.startswith(("http", "https")):
        user_input = "http://" + user_input
else:
    print("invalid url")
    exit(1)

start_driver(user_input)
