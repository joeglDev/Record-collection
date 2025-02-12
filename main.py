from polars import Schema, String, Int32, read_csv, col

csv_schema = Schema(
    {
        "Catalog#": String(),
        "Artist": String(),
        "Title": String(),
        "Label": String(),
        "Format": String(),
        "Rating": String(),
        "Released": Int32(),
        "release_id": Int32(),
        "CollectionFolder": String(),
        "Date Added": String(),
        "Collection Media Condition": String(),
        "Collection Sleeve Condition": String(),
        "Collection Notes": String(),
        "Collection Year Published": Int32(),
    }
)

# Read the CSV file
df = read_csv("data/discogs.csv", schema=csv_schema)
df = df.with_columns(col("Collection Year Published"))
df = df.sort(by="Collection Year Published", descending=True)

# Display the entire DataFrame
# print(df.schema)
print(df)

# year published statistics
years_published = df.get_column("Collection Year Published")
mean = years_published.mean()
median = years_published.median()
mode = years_published.mode()[0]

print(f"The mean publication year is {mean}.")
print(f"The median publication year is {median}.")
print(f"The mode publication year is {mode}.")

