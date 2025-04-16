from itertools import combinations
l = ["alice", "bob", "carey", "derek", "edward"]
for c in enumerate(combinations(l, 3), 1):
    print(f"{c[0]}: {c[1][0]}, {c[1][1]}, and {c[1][2]}")

from itertools import permutations
books = ["Harry Potter", 
         "The Hobbit", 
         "The Great Gatsby", 
         "The Catcher in the Rye"]

for p in enumerate(permutations(books, 2), 1):
    print(f"{p[0]}: {p[1][0]} and {p[1][1]}")