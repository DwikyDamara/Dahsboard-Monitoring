"""
This is main module
"""
from EathquakeDetection import data_extraction, data_displaying
import PopularNews


if __name__ == "__main__":
    print("Earthquake Detection Dahsboard!")
    result = data_extraction()
    data_displaying(result)

    print("\nPopular News Dashboard!")
    result = PopularNews.data_extraction1()
    PopularNews.data_displaying1(result)
