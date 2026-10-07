def validate_email():
    while True:
        email = input("SENDER EMAIL: ")

        if "@" not in email or "." not in email:
            print("Please enter a valid email address")
        else:
            return email

def validate_receiver_email():
    while True:
        receiver_email = input("RECEIVER EMAIL: ")

        if "@" not in receiver_email or "." not in receiver_email:
            print("Please enter a valid email address")
        else:
            return receiver_email