def pdto(dct):
    def _class_factory(name, argnames, base_class=object):
        return type(name, (base_class,), {"__set_attr__": lambda self, key, value: setattr(self, key, value)})

    def _hash_sugar(hsh):
        return f"n{hsh * -1 if hsh < 0 else hsh}".format(hsh * -1) if hsh < 0 else hsh

    cls_name = f"cls{_hash_sugar(hash(''.join(dct.keys())))}"

    obj = _class_factory(cls_name, ())()

    for key, value in dct.items():
        if isinstance(value, dict):
            value = pdto(value)
        try:
            _ = int(key)
            key = f"s{key}"
        except ValueError:
            pass
        obj.__set_attr__(key, value)

    return obj
