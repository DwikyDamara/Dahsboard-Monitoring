"""
This is main module
"""
from EathquakeDetection import data_extraction, data_displaying

if __name__ == "__main__":
    print("Main Application")
    result = data_extraction()
    data_displaying(result)
    