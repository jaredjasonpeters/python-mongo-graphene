import graphene

# ********************ENUM************************

# Episode = graphene.Enum('Episode', [(a, b), (c, d)])

# class Episode(graphene.Enum):
# a = b
# c = d

# value description
# @property
# def description(self):
#     if self == Episode.a:
#         return 'this is episode a'
#     return 'this is anything else'


# class Color(graphene.Enum):
#     RED = 0
#     GREEN = 1
#     BLUE = 2


# assert Color.get(1) == Color.GREEN


class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return f'Hello, {argument}'


schema = graphene.Schema(query=Query)


result = schema.execute('{ hello }')
print(result.data['hello'])


result = schema.execute('{ hello(argument: "Will")}')
print(result.data['hello'])


name = 'Phil'

f_result = 'True' if name else 'False'  # ternary

print(f_result)
