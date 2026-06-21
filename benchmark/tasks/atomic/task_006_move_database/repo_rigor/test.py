import os

def test_main():
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    assert "SERIAL" in schema, "Schema should use PostgreSQL SERIAL type"
    assert "AUTOINCREMENT" not in schema, "Schema should not use SQLite AUTOINCREMENT"
    assert "PRIMARY KEY" in schema, "Schema should define a PRIMARY KEY"
