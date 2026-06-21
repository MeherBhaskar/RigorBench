# Prompt

Write a function `validate_schema(data, schema)` that verifies if a given Python data structure `data` conforms to the provided `schema`.

The schema supports the following types:
- `"string"`: must be a string
- `"number"`: must be an int or float
- `"object"`: must be a dictionary. May have `"properties"` (a dictionary of field names to schemas) and `"required"` (a list of field names that must be present).
- `"array"`: must be a list. May have `"items"` (a schema that all items in the list must conform to).

If the data conforms to the schema, return `True`. Otherwise, return `False`.