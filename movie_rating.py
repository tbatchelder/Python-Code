myMovie = ""
myRating = 0
yourRating = 0

myMovie = input("What is your favorite movie? ")
myRating = eval(input(f"On a scale of 1 - 5, how would you rate {myMovie}? "))

yourRating = eval(input(f"How would you rate the movie {myMovie}? "))

print("The difference between your rate and the user's is", myRating - yourRating)
