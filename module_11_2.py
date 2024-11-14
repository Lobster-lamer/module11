import inspect


def introspection_info(obj):
    info = {}
    info.update({"type": type(obj).__name__})
    if hasattr(obj, __name__):
        pass
    else:
        obj = type(obj)
    _attributes = []
    _methods = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name, attr_name)
        if callable(attr):
            _methods.append(attr.__name__)
        else:
            _attributes.append(attr_name)
    info.update({"attributes": _attributes})
    info.update({"methods": _methods})
    info.update({"module": inspect.getmodule(obj).__name__})
    return info


if __name__ == "__main__":
    print(introspection_info("54"))
    print(introspection_info(print))
    print(introspection_info(list))

