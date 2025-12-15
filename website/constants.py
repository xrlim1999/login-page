"""
Validation policy for user account credentials.

Defines minimum and maximum length requirements for
usernames and passwords used during registration.
"""

# User's username length constraints
username_min_length = int(6)
username_max_length = int(25)

# User's password length constraints (plaintext input length, not hash length)
password_min_length = int(8)
password_max_length = int(225)