import random
from z3 import *

from classes.BaseElement import BaseElement
from classes.ListElement import ListElement
from classes.Table import Table
from classes.LinksList import LinksLists

header = BaseElement(row_x=0, col_y=0, is_fullwidth=True, width=1900, height=300, label="h")
header_table = Table(50, 50, width=header.width, height=header.height)
header.table = header_table

logo = BaseElement(height=150, width=150, label="l")
nav_list = ListElement(is_flexwidth=True,
                       links_list=LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.5,
                                             word_height=50, min_height_c=50), label="n")
search_bar = BaseElement(is_flexwidth=True, min_height=150, min_width=500, label="s")
twitter_icon = BaseElement(width=100, height=100, label="t")
vk_icon = BaseElement(width=100, height=100, label="v")
profile_icon = BaseElement(width=100, height=100, label="p")

header.add_children(logo)
header.add_children(nav_list)
header.add_children(search_bar)
header.add_children(twitter_icon)
header.add_children(vk_icon)
header.add_children(profile_icon)

row_logo = Int('row_logo')
col_logo = Int('col_logo')
row_count_logo = Int('row_count_logo')
col_count_logo = Int('col_count_logo')

row_nav = Int('row_nav')
col_nav = Int('col_nav')
row_count_nav = Int('row_count_nav')
col_count_nav = Int('col_count_nav')

row_search = Int('row_search')
col_search = Int('col_search')
row_count_search = Int('row_count_search')
col_count_search = Int('col_count_search')

row_twitter = Int('row_twitter')
col_twitter = Int('col_twitter')
row_count_twitter = Int('row_count_twitter')
col_count_twitter = Int('col_count_twitter')

row_vk = Int('row_vk')
col_vk = Int('col_vk')
row_count_vk = Int('row_count_vk')
col_count_vk = Int('col_count_vk')

row_profile = Int('row_profile')
col_profile = Int('col_profile')
row_count_profile = Int('row_count_profile')
col_count_profile = Int('col_count_profile')



"""
X = [[Int("x_%s_%s" % (i, j)) for i in range(header.table.col_count)] for j in range(header.table.row_count)]
instance = [[0 for i in range(header.table.col_count)] for j in range(header.table.row_count)]

instance_c = [X[i][j] == instance[i][j] for i in range(header.table.row_count) for j in range(header.table.col_count)]

logo_x = Int('logo_x')
logo_y = Int('logo_y')

s.add(instance_c)

for i in range(len(instance)):
    print(instance[i])
print('------------------------------')

print(s.check())
if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(X[i][j]) for j in range(header.table.col_count)]
         for i in range(header.table.row_count)]
    for i in range(len(r)):
        print(r[i])
    print(f"logo_x: {m.evaluate(logo_x)}")
    print(f"logo_y: {m.evaluate(logo_y)}")
else:
    print("WTF")
    


def place_element(row_count, col_count, label):
    for i in range(header.table.row_count - row_count):
        for j in range(header.table.col_count - col_count):
            is_taken = False
            for x in range(i, i + row_count):
                for y in range(j, j + col_count):
                    if instance[x][y] != 0:
                        is_taken = True
            if not is_taken:
                for x in range(i, i + row_count):
                    for y in range(j, j + col_count):
                        s.add(X[x][y] == label)
                        instance[x][y] = label
                return
    
    for i in range(len(instance)):
    print(instance[i])
print('------------------------------')
"""

print("ROW:")
print(header.table.row_count)
print("COL:")
print(header.table.col_count)


s = Optimize()

s.add(
    row_count_logo == header.table.get_row_count_from_height(logo.height),
    col_count_logo == header.table.get_col_count_from_width(logo.width),
    row_count_nav >= header.table.get_row_count_from_height(nav_list.min_height),
    col_count_nav >= header.table.get_row_count_from_height(nav_list.min_width),
    row_count_search >= header.table.get_row_count_from_height(search_bar.min_height),
    col_count_search >= header.table.get_col_count_from_width(search_bar.min_width),
    row_count_twitter == header.table.get_row_count_from_height(twitter_icon.height),
    col_count_twitter == header.table.get_col_count_from_width(twitter_icon.width),
    row_count_vk == header.table.get_row_count_from_height(vk_icon.height),
    col_count_vk == header.table.get_col_count_from_width(vk_icon.width),
    row_count_profile == header.table.get_row_count_from_height(profile_icon.height),
    col_count_profile == header.table.get_col_count_from_width(profile_icon.width),
)

logo_x = Int('logo_x')
logo_y = Int('logo_y')

nav_x = Int('nav_x')
nav_y = Int('nav_y')

search_x = Int('search_x')
search_y = Int('search_y')

vk_x = Int('vk_x')
vk_y = Int('vk_y')

twitter_x = Int('twitter_x')
twitter_y = Int('twitter_y')

profile_x = Int('profile_x')
profile_y = Int('profile_y')

logo_c = And(logo_x >= 0, logo_x + col_count_logo <= header.table.col_count, logo_y >= 0,
             logo_y + row_count_logo <= header.table.row_count)
nav_c = And(And(nav_x >= 0, nav_x + col_count_nav <= header.table.col_count, nav_y >= 0,
                nav_y + row_count_nav <= header.table.row_count),
            Or(nav_x >= logo_x + col_count_logo, nav_y >= logo_y + row_count_logo))
search_c = And(And(search_x >= 0, search_x + col_count_search <= header.table.col_count, search_y >= 0,
                   search_y + row_count_search <= header.table.row_count),
               Or(search_x >= nav_x + col_count_nav,
                  And(search_y >= nav_y + row_count_nav, search_y >= logo_y + row_count_logo), And(search_y + row_count_search <= nav_y, search_y + row_count_search <= logo_y)))
vk_c = And(And(vk_x >= 0, vk_x + col_count_vk <= header.table.col_count, vk_y >= 0, vk_y + row_count_vk <= header.table.row_count),
           Or(And(vk_x >= search_x + col_count_search, vk_y + row_count_vk <= nav_y), And(vk_x >= nav_x + col_count_nav, vk_y + col_count_vk <= search_y)))
# twitter_c = And(And(twitter_x >= 0, twitter_x + col_count_twitter <= header.table.col_count, twitter_y >= 0, twitter_y + row_count_twitter <= header.table.row_count),
#                Or(twitter_x > vk_x + col_count_vk, And(twitter_x + col_count_twitter < vk_x, twitter_x > search_x + col_count_search)))
# profile_c = And(And(profile_x >= 0, profile_x + col_count_profile <= header.table.col_count, profile_y >= 0, profile_y + row_count_profile <= header.table.row_count),
#                Or(profile_x > twitter_x + col_count_twitter))

s.add(
    logo_c,
    nav_c,
    search_c,
    vk_c
)

arr = [['0' for i in range(header.table.col_count)] for j in range(header.table.row_count)]


def place_elem(x, y, col_count, row_count, label):
    for i in range(y, row_count + y):
        for j in range(x, col_count + x):
            arr[i][j] = label


s.maximize(col_count_search)
s.maximize(col_count_nav)
res = s.check()
if res == sat:
    m = s.model()
    print(m)

    place_elem(m[logo_x].as_long(), m[logo_y].as_long(), m[col_count_logo].as_long(), m[row_count_logo].as_long(), 'l')
    place_elem(m[nav_x].as_long(), m[nav_y].as_long(), m[col_count_nav].as_long(), m[row_count_nav].as_long(), 'n')
    place_elem(m[search_x].as_long(), m[search_y].as_long(), m[col_count_search].as_long(),
               m[row_count_search].as_long(), 's')
    place_elem(m[vk_x].as_long(), m[vk_y].as_long(), m[col_count_vk].as_long(), m[row_count_vk].as_long(), 'v')
    # place_elem(m[twitter_x].as_long(), m[twitter_y].as_long(), m[col_count_twitter].as_long(), m[row_count_twitter].as_long(), 't')
    # place_elem(m[profile_x].as_long(), m[profile_y].as_long(), m[col_count_profile].as_long(), m[row_count_profile].as_long(), 'p')

    for i in range(len(arr)):
        print(arr[i])
else:
    print(res)
