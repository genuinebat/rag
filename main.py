import kagglehub
from kagglehub import KaggleDatasetAdapter

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.HUGGING_FACE,
  "denizbilginn/google-maps-restaurant-reviews",
  "reviews.csv"
)
df = df.select_columns(["text"])

print(df[0])
