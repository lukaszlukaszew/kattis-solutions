"""Hidden Password"""

password, message = input().split()
result = 1

for i in message:
    if i in password:
        if i == password[0]:
            password = password[1:]
            if not password:
                print("PASS")
                break
        else:
            print("FAIL")
            break

else:
    if password:
        print("FAIL")
