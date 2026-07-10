#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Harry Potter and the Chamber of Secrets"

print("My favorite movie is "+ favMovie)


#Part 3 Investigate the data
#print(movieData.head())
print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
scienceFictionFantasyMovieBooleanList = movieData["genres"].str.contains("Science Fiction & Fantasy")

scienceFictionFantasyMovieData = movieData.loc[scienceFictionFantasyMovieBooleanList]

numOfMovies = scienceFictionFantasyMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Science Fiction & Fantasy in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Science Fiction & Fantasy.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = scienceFictionFantasyMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 72 points higher than the lowest rated movie.")
print()

#find max
max = scienceFictionFantasyMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 20 points lower than the highest rated movie.")
print()

#find mean
mean = scienceFictionFantasyMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = scienceFictionFantasyMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(scienceFictionFantasyMovieData["audience_rating"], range = (0,100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Science Fiction & Fantasy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction & Fantasy Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most movies have medium to high ratings"
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data = scienceFictionFantasyMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between the Audience Rating and Critic Rating. The points follow an upward trend with a few outliers."
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
