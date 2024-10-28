# try:
#     number = int(input("Please enter an integer: "))
#     result = 2024 / number
#     print(result)
# except ValueError as e:
#     print("You should enter an integer!")
#     print(e)
# except ZeroDivisionError as e:
#     print('You should not enter 0.')
#     print(e)
# finally:
#     print('No matter what happens, we will get here!')

# print("\nNext section of the app.")
# print("Hello world!")


names = ["Youssef", "Felipe", 2024, "Zhi", "Aisha", ""]
# for name in names:
#     if isinstance(name, str) and len(name) > 0:
#         print(name[0])

for name in names:
    try:
        print(name[0])
    except TypeError as e:
        print(f"{name} is not a string!")
    except Exception as e:
        print(e)

print("\nNext section of the app.")
print("Hello world!")
