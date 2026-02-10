def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    type_map = {
        "int": int,
        "float": float,
        "str": str,
    }

    results = []

    for idx, record in enumerate(records):
        errors = []

        for col_def in schema:
            col = col_def["column"]
            expected_type_name = col_def["type"]
            nullable = col_def["nullable"]
            expected_type = type_map[expected_type_name]

            # missing column error
            if col not in record:
                errors.append(f"{col}: missing")
                continue

            value = record[col]

            if value is None:
                if not nullable:
                    errors.append(f"{col}: null")
                # if nullable and null, skip chec
                continue

            actual_type = type(value)

            type_ok = False
            if expected_type_name == "float":
                # float accepts int or float
                if actual_type in (int, float):
                    type_ok = True
            else:
                if actual_type is expected_type:
                    type_ok = True

            if not type_ok:
                errors.append(f"{col}: expected {expected_type_name}, got {actual_type.__name__}")
                continue  

            if expected_type_name in ("int", "float"):
                min_v = col_def.get("min")
                max_v = col_def.get("max")

                if min_v is not None and value < min_v:
                    errors.append(f"{col}: out of range")
                    continue

                if max_v is not None and value > max_v:
                    errors.append(f"{col}: out of range")
                    continue

        results.append((idx, len(errors) == 0, errors))

    return results
