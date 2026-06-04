movies = {
    "action": ["Avengers", "Batman", "Spider-Man"],
    "comedy": ["3 Idiots", "Golmaal", "Hera Pheri"],
    "horror": ["Conjuring", "Insidious", "Annabelle"],
    "romance": ["Titanic", "The Notebook", "DDLJ"]
}

print("Movie Recommendation System")
print("Available categories:")
print("action, comedy, horror, romance")

choice = input("Enter your favorite category: ").lower()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Category not found.")