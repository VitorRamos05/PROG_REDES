import os, sys, requests, json
from datetime import datetime

def extract_exif_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            if file.read(4) == b'\xFF\xD8\xFF\xE1':
                file.seek(18)
                num_metadata = int.from_bytes(file.read(2), byteorder='big')
                file.seek(22)
                metadata_info = {}
                for _ in range(num_metadata):
                    metadata_id = int.from_bytes(file.read(2), byteorder='big')
                    metadata_type = int.from_bytes(file.read(2), byteorder='big')
                    num_repetitions = int.from_bytes(file.read(4), byteorder='big')

                    if metadata_type == 2:
                        value = file.read(num_repetitions).decode('utf-8')
                    else:
                        value = int.from_bytes(file.read(4), byteorder='big')

                    metadata_info[metadata_id] = value

                processo_metadata(metadata_info)

    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")

def processo_metadata(metadata_info):
    metadata_mapa = {
        0x0100: "Largura da Imagem",
        0x0101: "Altura da Imagem",
        0x010F: "Fabricante da Câmera",
        0x0110: "Modelo da Câmera",
        0x0132: "Data de Modificação",
        0x9003: "Data de Captura",
        0x8825: "Informações de GPS"
    }

    width = metadata_info.get(0x0100, "Desconhecida")
    height = metadata_info.get(0x0101, "Desconhecida")
    manufacturer = metadata_info.get(0x010F, "Desconhecida")
    model = metadata_info.get(0x0110, "Desconhecida")
    capture_date = metadata_info.get(0x9003, "Desconhecida")
    latitude = metadata_info.get(0x8825, {}).get(0x0002, "Desconhecida")
    longitude = metadata_info.get(0x8825, {}).get(0x0004, "Desconhecida")

    if capture_date != "Desconhecida":
        capture_date = datetime.strptime(capture_date, "%Y:%m:%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")

    print(f"Largura da Imagem: {width}")
    print(f"Altura da Imagem: {height}")
    print(f"Fabricante da Câmera: {manufacturer}")
    print(f"Modelo da Câmera: {model}")
    print(f"Data de Captura: {capture_date}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print("")

def get_city_name(latitude, longitude):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
        response = requests.get(url)
        data = json.loads(response.text)
        cidade = data.get('address', {}).get('city', "Desconhecida")
        return cidade
    except Exception as e:
        print(f"Erro ao obter nome da cidade: {e}")
        return "Desconhecida"

directory_path = input("Digite o caminho do diretório: ")

cidades_info = {}

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path) and filename.lower().endswith('.jpg'):
        print(f"\nProcessando {filename}:")

        extract_exif_data(file_path)

        latitude = -23.550520
        longitude = -46.633308
        cidade = get_city_name(latitude, longitude)

        if cidade in cidades_info:
            cidades_info[cidade] += 1
        else:
            cidades_info[cidade] = 1

print("\nCidades onde as fotos foram capturadas:")
for cidade, regiao in cidades_info.items():
    print(f"{cidade}: {regiao} fotos")
