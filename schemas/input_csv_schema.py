from polars import Schema, String, Int32

input_csv_schema = Schema(
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
        "Collection Owner": String(),
        "Collection Genre": String()
    }
)