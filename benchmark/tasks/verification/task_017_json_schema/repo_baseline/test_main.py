from main import validate_schema

def test_validate_schema_string():
    assert validate_schema("hello", {"type": "string"}) == True
    assert validate_schema(123, {"type": "string"}) == False

def test_validate_schema_number():
    assert validate_schema(123.5, {"type": "number"}) == True
    assert validate_schema("123", {"type": "number"}) == False

def test_validate_schema_object():
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name"]
    }
    assert validate_schema({"name": "Alice", "age": 30}, schema) == True
    assert validate_schema({"name": "Bob"}, schema) == True
    assert validate_schema({"age": 25}, schema) == False
    assert validate_schema({"name": 123}, schema) == False
    assert validate_schema("not an object", schema) == False

def test_validate_schema_array():
    schema = {
        "type": "array",
        "items": {"type": "number"}
    }
    assert validate_schema([1, 2, 3.5], schema) == True
    assert validate_schema([1, "two", 3], schema) == False
    assert validate_schema({"items": [1]}, schema) == False

def test_nested_schema():
    schema = {
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"}
                    },
                    "required": ["id"]
                }
            }
        }
    }
    assert validate_schema({"users": [{"id": 1}, {"id": 2}]}, schema) == True
    assert validate_schema({"users": [{"id": 1}, {"name": "Bob"}]}, schema) == False
