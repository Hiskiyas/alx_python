#!/usr/bin/env python3
validate_password=__import__('6-password').validate_password
password = input("Enter Password:")
print(validate_password(password))