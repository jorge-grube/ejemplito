import pytest
from unittest import mock
from Database import DatabaseManager  # Asegúrate de tener dos líneas en blanco antes de esta línea

@mock.patch('Database.DatabaseManager.connect_to_database')
@mock.patch('Database.DatabaseManager.execute_query_on_database')
def test_database_operations(mock_execute_query, mock_connect):
    resultado_esperado = "Resultado esperado"

    mock_connect.return_value = True
    mock_execute_query.return_value = resultado_esperado

    assert DatabaseManager.connect_to_database() == True, "Error: Conexión fallida"
    resultado = DatabaseManager.execute_query_on_database("SELECT * FROM tabla")
    assert resultado == resultado_esperado, "Error: Resultado inesperado"
