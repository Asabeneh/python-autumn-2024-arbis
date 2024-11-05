# What is function, module, package

def add_two_nums (a, b):
    return a + b 

def make_square(x):
    return x ** 2 

def change_list_upper(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.upper())
    return new_lst

def filter_country_by_starting_letter(substring, lst):
    new_lst = []
    for country in lst:
        if country.startswith(substring):
            new_lst.append(country)
    return new_lst, len(new_lst)
