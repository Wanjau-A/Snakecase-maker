def main():
    camel_case = input("Enter Camelcase:  ").strip()
    snake_case = compute_function(camel_case)
    print(f"Snake case: {snake_case}")


def compute_function(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += ("_" + char.lower())
        else:
            snake_case += char
    return snake_case
if __name__ == "__main__":
    main()