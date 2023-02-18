# import spacy and load nlp
import spacy
nlp = spacy.load('en_core_web_md')

# create a function to get the similar movies
# taking the description of the movie as a parameter
def find_similar_movie(description):
    movies = [
        "Movie A",
        "Movie B",
        "Movie C",
        "Movie D",
        "Movie E",
        "Movie F",
        "Movie G",
        "Movie H",
        "Movie I",
        "Movie J"
    ]

    # then process the description
    doc = nlp(description)

    # check similarity scores between description and each of the movies
    scores = [nlp(movie).similarity(doc) for movie in movies]

    # then it returns the title of the most similar movie
    return movies[scores.index(max(scores))]

# prompt user input description
desc = input("Enter the movie description: ")
# call the function
print(find_similar_movie(desc))


