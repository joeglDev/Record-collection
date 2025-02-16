from typing import List

from polars import read_csv, DataFrame
from schemas.input_csv_schema import input_csv_schema
from utils.create_columns import create_columns


class GenerateRecordsStatistics:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.input_df: DataFrame | None = None

    def import_data(self):
        print(f"Importing raw data from {self.input_path}")
        input_df = read_csv("data/discogs.csv", schema=input_csv_schema)
        self.input_df = input_df.sort(by="Released", descending=True)

        print("Input data:")
        input_df.glimpse(max_items_per_column=50)

    def split_df_by_column(self, column: str) -> List[DataFrame]:
        print(f"Splitting dataframe by {column}")
        dfs_by_genre = self.input_df.partition_by(column)
        return dfs_by_genre

    def _write_to_csv(self, name: str, statistics: dict[str, int], df: DataFrame):
        file_name = f"{self.output_path}/{name}.csv"
        print(f"Writing dataframe to {file_name}")

        result_df = df.with_columns(create_columns(statistics))
        result_df.write_csv(file=file_name)

    def save_summary_statistics(self, dfs: List[DataFrame], column: str):
        print(f"Generating summary statistics for dataframes split by {column}")
        for df in dfs:
            # year published statistics
            genre = df.item(row=0, column=column)
            years_published = df.get_column("Released")
            mean = years_published.mean()
            median = years_published.median()
            mode = years_published.mode()[0]

            statistics = {
                "mean_year_released": mean,
                "median_year_released": median,
                "mode_year_released": mode,
            }

            output_text = f"""
            For Records in the {genre} genre.
            The mean release year is {mean}.
            The median release year is {median}.
            The mode release year is {mode}."
            """
            print(output_text)

            self._write_to_csv(name=genre, statistics=statistics, df=df)

    def run(self):
        self.import_data()
        split_dfs = self.split_df_by_column(column="Collection Genre")
        self.save_summary_statistics(dfs=split_dfs, column="Collection Genre")


service = GenerateRecordsStatistics(
    input_path="data/discogs.csv", output_path="output_data"
)
service.run()
