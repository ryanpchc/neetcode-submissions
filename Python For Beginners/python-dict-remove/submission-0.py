from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    new_dict = {}

    for key, value in my_dict.items():
        if key not in keys:
            new_dict[key] = value
    return new_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
