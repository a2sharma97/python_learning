def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name = "Abhishek", course = "BCA")
print_kwargs(name = "Abhishek", course = "MCA")
print_kwargs(name = "khushi")