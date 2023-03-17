"""
This is main module
"""


def data_extraction():
    """
        Tanggal : 16 Maret 2023
        Waktu : 12:22:39 WIB
        Magnitudo : 5.7
        Kedalaman : 10 km
        Location : 10.90 LS - 113.30 BT
        Pusat Gempa : 302 km BaratDaya JEMBER-JATIM
        Keterangan : tidak berpotensi TSUNAMI
    """
    hasil = dict()
    hasil["Tanggal"] = "16 Maret 2023"
    hasil["Waktu"] = "12:22:39 WIB"
    hasil["Magnitudo"] = 5.7
    hasil["Kedalaman"] = "10 km"
    hasil["Lokasi"] = {"ls": 10.90, "bt": 113.30}
    hasil["Pusat Gempa"] = "302 km BaratDaya JEMBER-JATIM"
    hasil["Keterangan"] = "tidak berpotensi TSUNAMI"
    return hasil


def data_displaying(result):
    print(f'Tanggal {result["Tanggal"]}')
    print(f'Waktu {result["Waktu"]}')
    print(f'Magnitudo {result["Magnitudo"]}')
    print(f'Kedalaman {result["Kedalaman"]}')
    print(f'Lokasi : LS = {result["Lokasi"]["ls"]} BT = {result["Lokasi"]["bt"]}')
    print(f'Pusat Gempa {result["Pusat Gempa"]}')
    print(f'Keterangan {result["Keterangan"]}')


if __name__ == "__main__":
    print("Main Application")
    result = data_extraction()
    data_displaying(result)