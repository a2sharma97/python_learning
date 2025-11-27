# List comprehension
# [expression for item in iterable if condition]
heros = [
    "ironman",
    "superman",
    "spiderman",
    "aquaman",
    "batman"
]

my_fav_hero = [hero for hero in heros if "ironman" in hero]
print(f"my favourite hero is: {my_fav_hero}")

# set comprehension
# {expression for item in iterable if condition}

more_heros = ["ironman",
    "superman",
    "spiderman",
    "aquaman",
    "batman",
    "ironman",
    "spiderman",
    "hawkeye",
    "asur",
    "hulk"
    ]

unique_heros = {hero for hero in more_heros} # set always returns unique values. 
print(unique_heros)
unique_heros = {hero for hero in more_heros if len(hero) > 5} #with condition
print(unique_heros)

all_heros = {
    "marvel_heros": ["ironman", "spiderman","hawkeye"],
    "DC_heros": ["superman", "batman", "aquaman"],
    "heros": ["batman",
    "ironman",
    "spiderman",
    "hawkeye",
    "asur",
    "hulk"]
}

unique_heros = {hero for heros in all_heros.values() for hero in heros}
print("unique heros from all heros: ",unique_heros)

# dictionary comprehension
# {expression for item in iterable if condition}

books_price = {
    "HC verma" : 100,
    "let's us C": 120,
    "AI models": 200
}

books_price_usd = {book_name: price /80 for book_name, price in books_price.items()}
print(f"book name and price in usd ${books_price_usd.values}")

# generator comprehension
# used for memory optimization, it never stores in memory immedeately, it stores step by step or during the processing.
# (expression for in iterable if condition)

daily_sales = [4, 2, 5, 9, 1, 46, 23]

total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups) #<generator object <genexpr> at 0x000001D30164A5A0>

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)