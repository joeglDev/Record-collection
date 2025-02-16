from typing import List

from polars import read_csv, DataFrame
from schemas.input_csv_schema import input_csv_schema

class GenerateRecordsStatistics:
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.input_df: DataFrame | None = None

    def import_data(self):
        print(f"Importing raw data from {self.input_path}")
        input_df = read_csv("data/discogs.csv", schema=input_csv_schema)
        self.input_df = input_df
        # df = df.sort(by="Released", descending=True)

        print("Input data:")
        input_df.glimpse()

    def split_df_by_column(self, column: str) -> List[DataFrame]:
        print(f"Splitting dataframe by {column}")
        dfs_by_genre = self.input_df.partition_by(column)
        return dfs_by_genre

    def save_summary_statistics(self, dfs: List[DataFrame], column: str):
        print(f"Generating summary statistics for dataframes split by {column}")
        for df in dfs:
            # year published statistics
            genre = df.item(row=0, column=column)
            years_published = df.get_column("Released")
            mean = years_published.mean()
            median = years_published.median()
            mode = years_published.mode()[0]

            output_text = f"""
            For Records in the {genre} genre.
            The mean publication year is {mean}.
            The median publication year is {median}.
            The mode publication year is {mode}."
            """
            print(output_text)

    def run(self):
        self.import_data()
        split_dfs = self.split_df_by_column(column="Collection Genre")
        self.save_summary_statistics(dfs=split_dfs, column="Collection Genre")


service = GenerateRecordsStatistics(input_path="data/discogs.csv")
service.run()



