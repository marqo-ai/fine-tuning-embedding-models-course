import marqo

# Create a Marqo client
mq = marqo.Client(url="http://localhost:8882")

# Delete the index if it already exists to ensure a fresh start.
# Comment this out when you first run the script. 
mq.index("movies-index").delete()

# Create an index
mq.create_index("movies-index", model="hf/e5-base-v2")

# Add documents (movie descriptions) to the index
mq.index("movies-index").add_documents(
    [
        {
            "Title": "Inception",
            "Description": "A mind-bending thriller about dream invasion and manipulation.",
        },
        {
            "Title": "Shrek",
            "Description": "An ogre's peaceful life is disrupted by a horde of fairy tale characters who need his help.",
        },
        {
            "Title": "Interstellar",
            "Description": "A team of explorers travel through a wormhole in space to ensure humanity's survival.",
        },
        {
            "Title": "The Martian",
            "Description": "An astronaut becomes stranded on Mars and must find a way to survive.",
        },
    ],
    tensor_fields=["Description"],
)

# Perform a search query on the index
results = mq.index("movies-index").search(
    q="Which movie is about space exploration?"
)

# Print the search results
for result in results['hits']:
    print(f"Title: {result['Title']}, Description: {result['Description']}. Score: {result['_score']}")