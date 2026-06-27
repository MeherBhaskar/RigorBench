def validate_schema(data, schema):
    t = schema.get("type")
    
    if t == "string":
        return isinstance(data, str)
    elif t == "number":
        return isinstance(data, (int, float)) and not isinstance(data, bool)
    elif t == "object":
        if not isinstance(data, dict):
            return False
        if "required" in schema:
            for req in schema["required"]:
                if req not in data:
                    return False
        if "properties" in schema:
            for prop, prop_schema in schema["properties"].items():
                if prop in data:
                    if not validate_schema(data[prop], prop_schema):
                        return False
        return True
    elif t == "array":
        if not isinstance(data, list):
            return False
        if "items" in schema:
            for item in data:
                if not validate_schema(item, schema["items"]):
                    return False
        return True
    
    return False
