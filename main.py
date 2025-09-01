import kagglehub
from kagglehub import KaggleDatasetAdapter
from transformers import pipeline

#df = kagglehub.load_dataset(
#  KaggleDatasetAdapter.HUGGING_FACE,
#  "denizbilginn/google-maps-restaurant-reviews",
#  "reviews.csv"
#)
#df = df.select_columns(["text"])

pl = pipeline("text-generation", model="openai-community/gpt2")

print(pl('You are a review sorter trying to filter out unnecessary. You are given 5 policies, their description, and an example of them. 1. No advertisements, Reviews should not contain promotional content or links, "Best pizza! Visit www.pizzapromo.com for discounts!" 2. No Irrelevant content, Reviews must be about the location and not about unrelated topics, “I love my new phone, but this place is too noisy.” 3. No reviews that are 1 word, Reviews must contain more than 1 word, "Bad" 4. No rants without actually visiting the place, Rants/complaints must come from actual visitors inferred via content of the review., “Never been here, but I heard it’s terrible.” 5. No vulgarities, Reviews must not contain any offensive slangs, "I fucking hate this restaurant". By following these policies, could you come to a conclusion if the following review is legitimate or not giving a single answer in either 1 or 0 where 1 represents yes and 0 represents no.'))
