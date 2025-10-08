import json

def main():
    demon_slayer_data = {
        "name": "",
        "breathing_style": "",
        "role": "",
    }
    
    nombre = input("Coloque el nombre de su personaje: ")
    estilo_respiracion = input("Coloque su estilo de respiracion: ")
    rol = input("Coloque su rol(Demonio o Cazador de Demonios): ")

    demon_slayer_data["name"] = nombre
    demon_slayer_data["breathing_style"] = estilo_respiracion
    demon_slayer_data["role"] = rol

    guardar_datos(demon_slayer_data)

    leer_datos()

    print(convertir_string(demon_slayer_data))


def guardar_datos(kny_data:dict):
# Guardar en archivo
    with open('dataKNY.json', 'w') as f:
        json.dump(kny_data, f, indent=2)

def leer_datos():
    # Leer desde archivo
    with open('dataKNY.json', 'r') as f:
        datos_leidos = json.load(f)
    print("Datos leídos:", datos_leidos)

def convertir_string(kny_data: dict) -> str:
    # Convertir a string
    json_str = json.dumps(kny_data, ensure_ascii=False)
    return json_str

if __name__ == "__main__":
    main()