movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# User input for additional movies
add_movies = input("Do you want to add more movies? (yes/no): ").lower()
if add_movies == "yes":
    num_movies = int(input("How many movies do you want to add? "))
    
    count = 0
    while count < num_movies:
        name = input(f"Enter movie name {count + 1}: ")
        budget = int(input(f"Enter budget for {name}: $"))
        movies.append((name, budget))
        count += 1

# Calculate statistics
total = 0
for film in movies:
    total += film[1]

average = total / len(movies)

high_budget_films = 0
print(f"\nAverage Budget: ${average:,.2f}")
print("\nHigh Budget Movies:")
for title, cost in movies:
    if cost > average:
        excess = cost - average
        print(f"  {title}: ${excess:,.2f} above average")
        high_budget_films += 1

print(f"\n{high_budget_films} movies exceeded the average budget")