from polars import DataFrame
from polars.testing import assert_frame_equal

from schemas.input_csv_schema import input_csv_schema
from utils.create_columns import create_columns
from utils.test.test_data import mock_initial_data, mock_result_schema, mock_result_data


class TestCreateColumns:
    def test_no_columns_appended(self):
        new_columns = {}
        initial_df = DataFrame(data=mock_initial_data, schema=input_csv_schema)
        result_df = initial_df.with_columns(create_columns(new_columns))

        assert_frame_equal(initial_df, result_df)

    def test_columns_appended(self):
        new_columns = {"key1": "test", "key2": 2}
        initial_df = DataFrame(data=mock_initial_data, schema=input_csv_schema)
        result_df = initial_df.with_columns(create_columns(new_columns))

        assert_frame_equal(
            result_df, DataFrame(data=mock_result_data, schema=mock_result_schema)
        )
