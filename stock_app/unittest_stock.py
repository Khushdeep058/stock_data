import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
import pandas as pd
from main import app  

client = TestClient(app) 


def calculate_moving_average(data, window_size):
    if not isinstance(window_size, int) or window_size <= 0:
        raise ValueError("Window size must be a positive integer")

    return data.rolling(window=window_size).mean().dropna().tolist()


class TestStockAPI(unittest.TestCase):

    @patch("routes.routes.fetch_all_stocks")  
    def test_get_stock_data(self, mock_fetch):
        mock_fetch.return_value = [
            {"datetime": "2024-03-27 10:00:00", "close": 100.5, "high": 105.0, "low": 98.5, "open": 99.0, "volume": 5000}
        ]
        response = client.get("/data")  
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertIn("datetime", response.json()[0])

   
    def test_moving_average_valid(self):
        data = pd.Series([10, 20, 30, 40, 50])
        window_size = 3
        expected_result = [20.0, 30.0, 40.0]
        self.assertEqual(calculate_moving_average(data, window_size), expected_result)

    def test_moving_average_large_window(self):
        data = pd.Series([1, 2, 3])
        window_size = 5
        expected_result = []
        self.assertEqual(calculate_moving_average(data, window_size), expected_result)

    def test_moving_average_negative_window_size(self):
        data = pd.Series([1, 2, 3, 4, 5])
        window_size = -2
        with self.assertRaises(ValueError):
            calculate_moving_average(data, window_size)

if __name__ == "__main__":
    unittest.main()
