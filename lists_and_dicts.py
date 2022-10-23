def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"Firstname": "David", "Lastname": "Gracia"}

    super_list = [
        {"Firstname": "David", "Lastname": "Gracia"},
        {"Firstname": "David", "Lastname": "Velasquez"},
        {"Firstname": "Gabriel", "Lastname": "Gracia"},
        {"Firstname": "Dayana", "Lastname": "Velasquez"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floatig_nums": [1.1,4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == "__main__":
    run()