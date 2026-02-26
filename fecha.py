from datetime import datetime, timedelta

fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")

fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

nueva_fecha = fecha + timedelta(days=1)

print("La nueva fecha es:", nueva_fecha.strftime("%Y-%m-%d"))