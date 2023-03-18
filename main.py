"""
This is main module
"""
from EathquakeDetection import data_extraction, data_displaying
from PopularNews import data_extraction1,data_displaying1


if __name__ == "__main__":
    print("Earthquake Detection Dahsboard!")
    result = data_extraction()
    data_displaying(result)


    print("\nPopular News Dashboard!")
    result = data_extraction1()
    data_displaying1(result)