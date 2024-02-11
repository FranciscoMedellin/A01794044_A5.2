import pytest
import compute_sales


# Path file 
PATH = "C:/Users/v-fzertuche/Documents/Actividad_5_2"
TCFILES = {
    "TC1": {
        "price_catalogue": PATH + "/TC1/TC1.ProductList.json",
        "sales_record": PATH + "/TC1/TC1.Sales.json",
    },
    "TC2": {
        "price_catalogue": PATH + "/TC2/TC2.ProductList.json",
        "sales_record": PATH + "/TC2/TC2.Sales.json",
    },
    "TC3": {
        "price_catalogue": PATH + "/TC3/TC3.ProductList.json",
        "sales_record": PATH + "/TC3/TC3.Sales.json",
    }
}
RESULTS = {
    "TC1" : 2481.86,
    "TC2" : 166568.23,
    "TC3" : 165235.37
}


@pytest.mark.parametrize(
    "filename",
    [
        (TCFILES["TC1"]["price_catalogue"]) ,
        (TCFILES["TC2"]["price_catalogue"]) ,
        (TCFILES["TC3"]["price_catalogue"])  
    ]
)
def test_load_json_file_existing(filename):
    """
    Prueba para verificar la carga de un archivo JSON existente
    """
    data = compute_sales.load_json_file(filename)
    assert data is not None


def test_load_json_file_invalid_format():
    """Prueba para verificar el manejo de un archivo JSON con formato incorrecto"""
    data = compute_sales.load_json_file("invalid_format.json")
    assert data is None

@pytest.mark.parametrize(
    "price_catalogue,sales_record,result",
    [
        (TCFILES["TC1"]["price_catalogue"],TCFILES["TC1"]["sales_record"], RESULTS["TC1"]) ,
        (TCFILES["TC2"]["price_catalogue"],TCFILES["TC2"]["sales_record"], RESULTS["TC2"]) ,
        (TCFILES["TC3"]["price_catalogue"],TCFILES["TC3"]["sales_record"], RESULTS["TC3"])  
    ]
)
def test_calculate_toal_cost_multi(price_catalogue, sales_record, result):
    price_catalogue = compute_sales.load_json_file(price_catalogue)
    sales_record = compute_sales.load_json_file(sales_record)
    total_cost = compute_sales.calculate_total_cost(price_catalogue, sales_record)
    assert total_cost == pytest.approx(result, abs=0.01)


if __name__ == "__main__":
    pytest.main()
