from typing import List

jsons = [
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Ракетка",
        "equipmentCount": 2
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Мяч",
        "equipmentCount": 3
    },
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Палатка",
        "equipmentCount": 6
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Удочка",
        "equipmentCount": 2
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Мангал",
        "equipmentCount": 1
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Спальник",
        "equipmentCount": 5
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Рюкзак",
        "equipmentCount": 10
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Дождевик",
        "equipmentCount": 10
    },
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Компас",
        "equipmentCount": 1
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Термос",
        "equipmentCount": 4
    }
]


def new_class(class_name: str) -> object:
    """ Creates new class based on new class name.
    Args:
        class_name : str
    Returns:
        new custom class based on class name and attributes.
    """

    def constructor(self, attrs: dict):
        """ Class constructor method, parses a dict of attrubutes and values.
        Args:
            attrs : dict
        """
        for key in attrs.keys():
            self.__dict__[key] = attrs[key]


    return type(class_name, (object, ), {"__init__": constructor,})


# 83-94 simple examples
# method 1
cn = 'Custom'
Custom_class = new_class(cn)
new_obj = Custom_class({'a': 1, 'b': 2})
print(type(new_obj))
print(new_obj.a)
print(new_obj.b)

# method 2
setattr(new_obj, 'c', 5)
setattr(new_obj, 'd', 6)
print(new_obj.c)
print(new_obj.d)


# just serializing from jsons to custom objects
objs_from_json = [new_class('Holder')(json) for json in jsons]
print(type(objs_from_json[0]))
print(objs_from_json[0])
print(objs_from_json[0].holderName)

def desearialize_manual(jsons):
    def add_item(item, items : list, key):    
        if len(items):
            for i in items:
                if i[key] == item[key]:
                    break 
            else:
                items.append(item)
        else: 
            items.append(item)
        return items            

    holders, equipments = [], []
    for json in jsons:
        holder, equipment = dict(), dict()
        for key in json.keys():
            if key.startswith('holder'):
                holder[key] = json[key]
            else:   
                equipment[key] = json[key]

        holders = add_item(holder, holders, 'holderPhone')
        equipments = add_item(equipment, equipments, 'equipmentTitle')

    holder_objs = [new_class('Holder')(json) for json in holders]
    equipment_objs = [new_class('Equipment')(json) for json in equipments]

    return holder_objs, equipment_objs

print(desearialize_manual(jsons))


# def deserialize(jsons: List[dict]) -> List[object]:
#     """ Deserializes list of jsons to list of custom objects. 
#     Attributes and values are given by json. Function depends on camelCase attribute names.
#     Args:
#         jsons : List[dict]
#     Returns:
#         List[object] : a list of custom objects

#     """
#     # check if not empty
#     if not len(jsons):
#         return []

#     # find future unique classes' names
#     custom_classes = set()
#     for key in jsons[0].keys():
#         for i in range(len(key)):
#             if key[i].isupper():
#                 custom_classes.add(key[:i])

#     # now map json and split each by class name
#     objs_by_class = dict()
#     for json in jsons:
#         new = {class_name: dict() for class_name in custom_classes}
#         for key in json.keys():
#             for cn in new.keys():
#                 if key.startswith(cn):
#                     new[cn][key] = json[key]
#         for class_name in new.keys():
#             if class_name in objs_by_class.keys():
#                 objs_by_class[class_name].append(new[class_name])
#             else:
#                 objs_by_class[class_name] = [new[class_name]]

#     # remove duplicates. we cant make a set of dicts, but can make set of tuples %)
#     for class_name in objs_by_class.keys():
#         objs_by_class[class_name] = [dict(t) for t in {tuple(
#             d.items()) for d in objs_by_class[class_name]}]

#     # make objects from dicts
#     objs = []
#     for class_name in objs_by_class.keys():
#         for obj in objs_by_class[class_name]:
#             objs.append(new_class(class_name)(obj))

#     return objs


# objs = deserialize(jsons)

# for obj in objs:
#     print('*** Object ***')
#     for key in obj.__dict__.keys():
#         print(key, obj.__dict__[key])