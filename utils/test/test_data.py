from polars import Schema, String, Int32

mock_initial_data = {
    "Catalog#": ["ABC123", "DEF456", "GHI789"],
    "Artist": ["The Beatles", "Pink Floyd", "Led Zeppelin"],
    "Title": ["Abbey Road", "Dark Side of the Moon", "IV"],
    "Label": ["Apple", "Harvest", "Atlantic"],
    "Format": ["LP", "CD", "Cassette"],
    "Rating": ["5", "4", "5"],
    "Released": [1969, 1973, 1971],
    "release_id": [1001, 1002, 1003],
    "CollectionFolder": ["Rock", "Rock", "Rock"],
    "Date Added": ["2023-01-15", "2023-02-20", "2023-03-10"],
    "Collection Media Condition": [
        "Very Good Plus (VG+)",
        "Near Mint (NM)",
        "Excellent (EX)",
    ],
    "Collection Sleeve Condition": [
        "Very Good (VG)",
        "Excellent (EX)",
        "Very Good Plus (VG+)",
    ],
    "Collection Owner": ["John", "Jane", "Bob"],
    "Collection Genre": ["Rock", "Progressive Rock", "Hard Rock"],
}

mock_result_data = {
    "Catalog#": ["ABC123", "DEF456", "GHI789"],
    "Artist": ["The Beatles", "Pink Floyd", "Led Zeppelin"],
    "Title": ["Abbey Road", "Dark Side of the Moon", "IV"],
    "Label": ["Apple", "Harvest", "Atlantic"],
    "Format": ["LP", "CD", "Cassette"],
    "Rating": ["5", "4", "5"],
    "Released": [1969, 1973, 1971],
    "release_id": [1001, 1002, 1003],
    "CollectionFolder": ["Rock", "Rock", "Rock"],
    "Date Added": ["2023-01-15", "2023-02-20", "2023-03-10"],
    "Collection Media Condition": [
        "Very Good Plus (VG+)",
        "Near Mint (NM)",
        "Excellent (EX)",
    ],
    "Collection Sleeve Condition": [
        "Very Good (VG)",
        "Excellent (EX)",
        "Very Good Plus (VG+)",
    ],
    "Collection Owner": ["John", "Jane", "Bob"],
    "Collection Genre": ["Rock", "Progressive Rock", "Hard Rock"],
    "key1": ["test", "test", "test"],
    "key2": [2, 2, 2],
}

mock_result_schema = Schema(
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
        "Collection Genre": String(),
        "key1": String(),
        "key2": Int32(),
    }
)
