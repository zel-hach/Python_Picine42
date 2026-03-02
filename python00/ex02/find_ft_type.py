def all_thing_is_obj(obj: any) -> int:
    match type(obj).__name__:
        case "list":
            print(f"List : {type(obj)}")
        case "tuple":
            print(f"Tuple : {type(obj)}")
        case "set":
            print(f"Set : {type(obj)}")
        case "dict":
            print(f"Dict : {type(obj)}")
        case "str":
            print(f"{obj} is in the kitchen : {type(obj)}")
        case _:
            print("Type not found")
    return 42