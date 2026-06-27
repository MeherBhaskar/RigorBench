def validate_schema(data, schema):
    schema_type = schema.get("type")
    
    if schema_type == "string":
        return isinstance(data, str)
        
    elif schema_type == "number":
        return isinstance(data, (int, float)) and not isinstance(data, bool)
        
    elif schema_type == "object":
        if not isinstance(data, dict):
            return False
            
        properties = schema.get("properties", {})
        for key, prop_schema in properties.items():
            if key in data:
                if not validate_schema(data[key], prop_schema):
                    return False
                    
        required = schema.get("required", [])
        for req in required:
            if req not in data:
                return False
                
        return True
        
    elif schema_type == "array":
        if not isinstance(data, list):
            return False
            
        items_schema = schema.get("items")
        if items_schema is not None:
            for item in data:
                if not validate_schema(item, items_schema):
                    return False
                    
        return True
        
    return False
