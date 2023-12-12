from collections import Iterable

def flatten_dict(d, parent_key=()):
    res = []
    for k, v in d.items():
        new_key = (*parent_key, k) if parent_key else (k,)
        if isinstance(v, dict):
            res.extend(flatten_dict(v, parent_key=new_key).items())
        else:
            res.append((new_key, v))
    return dict(res)