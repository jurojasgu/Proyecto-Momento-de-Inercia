import pandas as pd
import io

def analizar_datos_csv(nombre_archivo):
    """
    Lee un archivo CSV existente, filtra los datos activos (Frecuencia > 0) y 
    calcula el promedio del Periodo y la Frecuencia para esas lecturas válidas.
    
    Su entrada es un archivo Csv en este caso
    """
    # Lectura
    try:
        # Leer el archivo CSV en pandas
        df = pd.read_csv(nombre_archivo)
        
        #Mostrar número de filas leídas
        print(f"Total de filas leídas: {len(df)}")
        print(df.head())
        print("-" * 40)

        # Filtración
        # Filtrar las filas donde la frecuencia es mayor que cero para obtener solo las lecturas válidas del sensor
        df_activos = df[df['Frecuencia_Hz'] > 0]
        
        # Si hay datos distintos de cero, calcular sus promedios
        if not df_activos.empty:
            promedio_periodo_activo = df_activos['Periodo_ms'].mean()
            promedio_frecuencia_activa = df_activos['Frecuencia_Hz'].mean()
        else:
            # Para caso de todo 0
            promedio_periodo_activo = 0.0
            promedio_frecuencia_activa = 0.0
            
        # Impresión
        print("\nResultados de promedio")
        print("\n Promedios de Datos útiles (Frecuencia > 0)")
        # Cuantas filas habia en el CSV con archivos no nulos
        print(f"Filas con datos activos utilizadas en el promedio: {len(df_activos)}")
        
        if len(df_activos) > 0:
            print(f"Promedio del Periodo: {promedio_periodo_activo:.3f} ms")
            print(f"Promedio de la Frecuencia: {promedio_frecuencia_activa:.3f} Hz")
        else:
            print("No se encontraron lecturas activas (Frecuencia > 0) para calcular el promedio.")

        print("==============================")
        
    except FileNotFoundError:
        # Mensaje de error por si no se encuentra el archivo
        print(f"\nError: El archivo '{nombre_archivo}' no fue encontrado.")
        print(f"Revisar '{nombre_archivo}' y que esté en esta carpeta.")
        
# Ejecutar la función principal
if __name__ == "__main__":
    # Se llama al archivo al que se le vayan a hacer los promedios
    analizar_datos_csv("Prueba 6.csv")