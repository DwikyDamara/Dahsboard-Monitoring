import requests
from bs4 import BeautifulSoup


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

    try:
        content = requests.get("https://bmkg.go.id/")
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")

        date = soup.find("span", {"class": "waktu"})  # =>alternate code=date.text.split(", ")
        waktu = date.string.split(", ")[1]           # waktu=date[1] and same way with tanggal
        tanggal = date.string.split(", ")[0]

        other_data = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        other_data = other_data.findChildren('li')
        magnitudo = other_data[1].text
        kedalaman = other_data[2].text
        koordinat = other_data[3].text.split(" - ")
        ls = koordinat[0]
        bt = koordinat[1]
        lokasi = other_data[4].text
        dirasakan = other_data[5].text

        # i = 0
        # magnitudo = None
        # kedalaman = None
        # ls = None
        # bt = None
        # lokasi = None
        # dirasakan = None
        #
        # for data in other_data:
        #     print(data)
        #     if i == 1:
        #         magnitudo = data.text
        #     elif i == 2:
        #         kedalaman = data.text
        #     elif i == 3:
        #         koordinat = data.text.split(" - ")
        #         ls = koordinat[0]
        #         bt = koordinat[1]
        #     elif i == 4:
        #         lokasi = data.text
        #     elif i == 5:
        #         dirasakan = data.text
        #     i = i + 1
        hasil = dict()
        hasil["Tanggal"] = tanggal
        hasil["Waktu"] = waktu
        hasil["Magnitudo"] = magnitudo
        hasil["Kedalaman"] = kedalaman
        hasil["Koordinat"] = {"ls": ls, "bt": bt}
        hasil["Lokasi"] = lokasi
        hasil["Dirasakan"] = dirasakan
        return hasil
    else:
        return None


def data_displaying(result):
    if result is None:
        print("Gagal menampilkan data")
        return
    print("Deteksi Gempa Terkini")
    print(f'Tanggal : {result["Tanggal"]}')
    print(f'Waktu : {result["Waktu"]}')
    print(f'Magnitudo : {result["Magnitudo"]}')
    print(f'Kedalaman : {result["Kedalaman"]}')
    print(f'Koordinat : LS = {result["Koordinat"]["ls"]} BT = {result["Koordinat"]["bt"]}')
    print(f'Lokasi : {result["Lokasi"]}')
    print(f'Dirasakan : {result["Dirasakan"]}')
