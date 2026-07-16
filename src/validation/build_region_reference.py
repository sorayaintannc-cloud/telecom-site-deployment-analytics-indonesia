from pathlib import Path
import csv

REFERENCE_YEAR = 2025

# Root folder project
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Folder penyimpanan data reference
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"

# File input
POPULATION_FILE = REFERENCE_DIR / "west_java_population_raw.csv"
DENSITY_FILE = REFERENCE_DIR / "west_java_population_density_raw.csv"
REGION_FILE = REFERENCE_DIR / "west_java_region_codes_raw.csv"

# File output
OUTPUT_FILE = REFERENCE_DIR / "west_java_region_reference.csv"


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def normalize_region_name(name):
    return " ".join(name.strip().title().split())


def derive_region_type(name):
    upper_name = name.upper()

    if upper_name.startswith("KABUPATEN "):
        return "Regency"

    if upper_name.startswith("KOTA "):
        return "City"

    raise ValueError(f"Unknown region type: {name}")


def derive_density_class(density):
    if density < 1000:
        return "Low"

    if density < 3000:
        return "Medium"

    if density < 8000:
        return "High"

    return "Very High"


# Membaca seluruh file sumber.
population_rows = read_csv(POPULATION_FILE)
density_rows = read_csv(DENSITY_FILE)
region_rows = read_csv(REGION_FILE)


# Mengambil data jumlah penduduk untuk tahun referensi.
population_2025 = {}

for row in population_rows:
    if int(row["tahun"]) != REFERENCE_YEAR:
        continue

    region_code = row["kode_kabupaten_kota"].strip()

    population_2025[region_code] = {
        "region_name": normalize_region_name(
            row["nama_kabupaten_kota"]
        ),
        # Satuan sumber adalah ribu orang.
        "population": round(
            float(row["jumlah_penduduk"]) * 1000
        ),
    }


# Mengambil data kepadatan penduduk untuk tahun referensi.
density_2025 = {}

for row in density_rows:
    if int(row["tahun"]) != REFERENCE_YEAR:
        continue

    region_code = row["kode_kabupaten_kota"].strip()

    density_2025[region_code] = int(
        float(row["kepadatan_penduduk"])
    )


# Membuat referensi kode dan nama wilayah.
region_lookup = {}

for row in region_rows:
    region_code = row["bps_kota_kode"].strip()
    region_name = normalize_region_name(
        row["bps_kota_nama"]
    )

    if not region_code:
        continue

    if (
        region_code in region_lookup
        and region_lookup[region_code] != region_name
    ):
        raise ValueError(
            f"Inconsistent region name for {region_code}: "
            f"{region_lookup[region_code]} vs {region_name}"
        )

    region_lookup[region_code] = region_name


# Mengambil kumpulan kode wilayah dari setiap sumber.
population_codes = set(population_2025)
density_codes = set(density_2025)
region_codes = set(region_lookup)


# Memastikan kode wilayah pada data populasi dan kepadatan sama.
if population_codes != density_codes:
    raise ValueError(
        "Population and density region codes do not match. "
        f"Population only: "
        f"{sorted(population_codes - density_codes)}; "
        f"Density only: "
        f"{sorted(density_codes - population_codes)}"
    )


# Memastikan seluruh kode wilayah tersedia pada referensi wilayah.
missing_region_codes = population_codes - region_codes

if missing_region_codes:
    raise ValueError(
        "Region codes missing from region reference: "
        f"{sorted(missing_region_codes)}"
    )


# Menggabungkan seluruh data menjadi satu reference table.
records = []

for region_code in sorted(population_codes):
    population_name = population_2025[
        region_code
    ]["region_name"]

    region_name = region_lookup[region_code]

    if population_name != region_name:
        raise ValueError(
            f"Region name mismatch for {region_code}: "
            f"{population_name} vs {region_name}"
        )

    density = density_2025[region_code]

    records.append(
        {
            "region_code": region_code,
            "regency_city_name": region_name,
            "region_type": derive_region_type(
                region_name
            ),
            "population": population_2025[
                region_code
            ]["population"],
            "population_density": density,
            "density_class": derive_density_class(
                density
            ),
            "reference_year": REFERENCE_YEAR,
        }
    )


# Memastikan hasil akhir berisi 27 kabupaten/kota.
if len(records) != 27:
    raise ValueError(
        f"Expected 27 West Java regions, "
        f"found {len(records)}"
    )


# Menentukan urutan kolom pada file output.
fieldnames = [
    "region_code",
    "regency_city_name",
    "region_type",
    "population",
    "population_density",
    "density_class",
    "reference_year",
]


# Menulis hasil akhir ke file CSV.
with OUTPUT_FILE.open(
    "w",
    encoding="utf-8",
    newline="",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
    )

    writer.writeheader()
    writer.writerows(records)


# Menampilkan pesan keberhasilan.
print(
    f"Created {OUTPUT_FILE.name} "
    f"with {len(records)} rows."
)