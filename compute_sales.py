"""
Compute Sales Program
"""
import json
import sys
import time


def load_json_file(filename):
    """
    Función para cargar datos desde un archivo JSON
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return None


def calculate_total_cost(price_catalogue, sales_record):
    """
    Función para calcular el costo total de las ventas
    """
    total_cost = 0
    try:
        for sale in sales_record:
            product = sale.get("Product")
            quantity = sale.get("Quantity")
            for item in price_catalogue:
                if item.get("title") == product:
                    price = item.get("price")
                    total_cost += price * quantity
                    break
        return total_cost
    except ValueError:
        print("Error processing json files")
        return None


def main():
    """
    Funcion Main para ejecutar el programa
    """
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Please use next comands:"
              "python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    # Obtener tiempo inicial de ejecucion
    start_time = time.time()

    # Obtener los nombres de los archivos
    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    # Cargar datos de los archivos JSON
    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    # Verificar si los datos se cargaron correctamente
    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    # Calcular el costo total de las ventas
    total_cost = calculate_total_cost(price_catalogue, sales_record)
    end_time = time.time()
    execution_time = end_time - start_time

    # Mostrar el costo total en la pantalla
    print(f"Total cost of all sales: ${total_cost:.2f}")

    # Guardar el resultado en un archivo SalesResults.txt
    with open("SalesResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write(f"Total cost of all sales: ${total_cost:.2f}\n")
        result_file.write(f"Execution time: {execution_time:.4f} seconds\n")

    # Mostrar el tiempo de ejecución en la pantalla
    print(f"Execution time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()
