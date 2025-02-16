from polars import read_csv, DataFrame
from schemas.input_csv_schema import input_csv_schema

class GenerateRecordsStatistics:
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.input_df: DataFrame | None = None

    def import_data(self):# Read the CSV file
        input_df = read_csv("data/discogs.csv", schema=input_csv_schema)
        self.input_df = input_df
        # df = df.sort(by="Released", descending=True)

        print("Input data:")
        input_df.glimpse()

    def split_df_by_column(self):
        pass

    def run(self):
        self.import_data()

        # year published statistics
        years_published = self.input_df.get_column("Released")
        mean = years_published.mean()
        median = years_published.median()
        mode = years_published.mode()[0]

        print(f"The mean publication year is {mean}.")
        print(f"The median publication year is {median}.")
        print(f"The mode publication year is {mode}.")

        self.split_df_by_column()



service = GenerateRecordsStatistics(input_path="data/discogs.csv")
service.run()



