import requests
import time

def obtener_posicion():
    url = "http://api.open-notify.org/iss-now.json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    lat = float(datos["iss_position"]["latitude"])
    lon = float(datos["iss_position"]["longitude"])
    return lat, lon

print("🌍 Monitoreando la posición de la Estación Espacial Internacional cada 1 minuto...\n")

lat_anterior, lon_anterior = obtener_posicion()
repeticiones = 0

while True:
    time.sleep(60)  # Espera 1 minuto

    lat_actual, lon_actual = obtener_posicion()

    print("===========================================")
    print(f"📍 Posición actual:")
    print(f"   Latitud: {lat_actual:.6f}")
    print(f"   Longitud: {lon_actual:.6f}")

    # Calcular cambio de coordenadas por hora
    cambio_lat = abs(lat_actual - lat_anterior) * 60
    cambio_lon = abs(lon_actual - lon_anterior) * 60

    print(f"\n📊 Cambios estimados por hora:")
    print(f"   Cambio de latitud por hora: {cambio_lat:.4f}°")
    print(f"   Cambio de longitud por hora: {cambio_lon:.4f}°\n")

    # Actualizar posición anterior
    lat_anterior, lon_anterior = lat_actual, lon_actual

    repeticiones += 1

    if repeticiones % 5 == 0:
        respuesta = input("¿Deseas continuar con otras 5 repeticiones? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n👋 Consulta finalizada. ¡Hasta luego!")
            break
