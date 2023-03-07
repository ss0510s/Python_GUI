import pandas as pd

# df = pd.DataFrame(
#     {"a" : [4, 5 , 6],
#      "b" : [7, 8, 9],
#      "c" : [10, 11, 12]},
#     index = [1, 2, 3])
#
# print(df)

df = pd.DataFrame(
    [[4, 7, 10],
     [5, -8, 11],
     [6, 9, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c'])

print(df)

# print(pd.melt(df)
#       .rename( columns= {'variable': 'val',
#                         'value':'val'})
#       .query('val >= 8')
#       .tail(2)
#       )

# print(df.describe())

# def square(n) :
#     return n*n
#
# df_square = df.apply(square)

df_square = df.apply(lambda n : n * n)

print(df_square)

df_sort = df.sort_values('b', ascending=False)
print(df_sort)
