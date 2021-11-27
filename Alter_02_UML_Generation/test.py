# cleaned_doc = [token for token in doc if not token.is_stop and not token.is_punct]
# sentence = "WarehouseOperator should be able to make adjustments to the order."
# d = sentence.split("should be able to ")
# print(d[1])

from graphviz import Digraph

dot = Digraph(format='png')

dot.node('a', 'User', image='stick1.jpeg')
dot.node('1', 'Sign In')
dot.node('2', 'Sign Up')
dot.edges(['a1', 'a2'])
# dot.format = 'png'

# print(dot.source)
dot.render('./outputs/generated_use_case_diagrams/test.png', view=True)

# dot.node('b', 'Admin',  shapefile='./data/sources/stick-user.png')
#
#
# dot.node('c', 'WarehouseOperator',  shapefile='./data/sources/stick-user.png')
#
#
# dot.node('d', 'WarehouseIncharge',  shapefile='./data/sources/stick-user.png')
