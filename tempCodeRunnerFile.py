import pandas as pd

# 1. Membaca data dari file Excel
file_path = "data_sampah_jabar.xlsx"  # Ganti dengan path file Anda
data = pd.read_excel(file_path)

# Tampilkan data awal
print("Data Awal:")
print(data)

# 2. Menghitung total produksi sampah berdasarkan tahun
total_per_tahun = {}
for index, row in data.iterrows():
    tahun = row['Tahun Pencatatan']
    jumlah = row['Jumlah Produksi Sampah (Ton)']
    if tahun in total_per_tahun:
        total_per_tahun[tahun] += jumlah
    else:
        total_per_tahun[tahun] = jumlah

print("\nTotal Produksi Sampah per Tahun:")
print(total_per_tahun)

# 3. Menghitung produksi sampah per Kabupaten/Kota per tahun
total_per_kota_tahun = {}
for index, row in data.iterrows():
    kota = row['Nama Kabupaten/Kota']
    tahun = row['Tahun Pencatatan']
    jumlah = row['Jumlah Produksi Sampah (Ton)']
    key = (kota, tahun)
    if key in total_per_kota_tahun:
        total_per_kota_tahun[key] += jumlah
    else:
        total_per_kota_tahun[key] = jumlah

# Konversi hasil ke DataFrame
df_kota_tahun = pd.DataFrame(
    [(k[0], k[1], v) for k, v in total_per_kota_tahun.items()],
    columns=['Nama Kabupaten/Kota', 'Tahun Pencatatan', 'Jumlah Produksi Sampah (Ton)']
)

print("\nProduksi Sampah per Kabupaten/Kota per Tahun:")
print(df_kota_tahun)

# 4. Ekspor ke CSV dan Excel
output_csv = "hasil_sampah_jabar.csv"
output_excel = "hasil_sampah_jabar.xlsx"

df_kota_tahun.to_csv(output_csv, index=False)
df_kota_tahun.to_excel(output_excel, index=False)

print("\nHasil ekspor telah disimpan ke CSV dan Excel.")

# 5. Dokumentasi Video dan Upload ke GitHub
# Rekam langkah-langkah Anda dan upload ke platform GitHub.
