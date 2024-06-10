import marqo

# Create a Marqo client with the specified URL
mq = marqo.Client(url="http://localhost:8882")

# Delete the index if it already exists to ensure a fresh start.
# Comment this out when you first run the script. 
mq.index("my-multimodal-index").delete()

# Settings for the index creation, enabling image indexing and specifying the model to use.
settings = {
    "treat_urls_and_pointers_as_images": True,  # allows us to treat URLs as images and index them
    "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",  # model used for indexing
}

# Create the index with the specified settings
response = mq.create_index("my-multimodal-index", **settings)

# Add documents to the created index, including an image and its description
response = mq.index("my-multimodal-index").add_documents(
    [
        {
            "My_Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg/640px-Hipop%C3%B3tamo_%28Hippopotamus_amphibius%29%2C_parque_nacional_de_Chobe%2C_Botsuana%2C_2018-07-28%2C_DD_82.jpg",
            "Description": "The hippopotamus, also called the common hippopotamus or river hippopotamus, is a large semiaquatic mammal native to sub-Saharan Africa",
            "_id": "hippo-facts",  # unique identifier for the document
        }
    ],
    tensor_fields=["My_Image"],  # specify that "My_Image" should be treated as a tensor field
)

# Search the index for the term "animal"
results = mq.index("my-multimodal-index").search("animal")

# Print the search results
import pprint
pprint.pprint(results)