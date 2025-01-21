import inspect


class Dir_print:
    def __init__(self, obj):
        self.obj = obj

    def out_put(self):
        for attr_name in dir(self.obj):
            att = getattr(self.obj, attr_name)
            print(attr_name, type(att))

def introspection_info(obj):
    object_data = dict()
    object_data['type'] = type(obj).__name__
    object_data['attributes'] = []
    object_data['methods'] = []
    for attr_name in dir(obj):
        att = getattr(obj, attr_name)
        object_data['attributes'].append(attr_name)
        if 'method' in type(att).__name__:
            object_data['methods'].append(attr_name)
    if inspect.getmodule(obj).__str__() == 'None':
        object_data['module'] = inspect.getmodule(obj).__str__()
    else:
        object_data['module'] = inspect.getmodule(obj).__str__().split("'")[1]
    return object_data

# oDir_print = Dir_print(inspect)
# print(introspection_info(oDir_print))

number_info = introspection_info(42)
print(number_info)
