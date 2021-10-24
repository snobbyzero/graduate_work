import random
from z3 import *

from classes.BaseElement import BaseElement
from classes.IconElement import IconElement
from classes.IconsListElement import IconsListElement
from classes.ListElement import ListElement
from classes.Table import Table
from classes.LinksList import LinksLists

"""
==============================Functions============================
"""


def place_elem(x, y, col_count, row_count, label, arr):
    for i in range(y, row_count + y):
        for j in range(x, col_count + x):
            arr[i][j] = label


"""
==============================VARIABLES=============================
"""
header_x = Int('header_x')
header_y = Int('header_y')
header_row_count = Int('header_row_count')
header_col_count = Int('header_col_count')

logo_x = Int('logo_x')
logo_y = Int('logo_y')
logo_row_count = Int('logo_row_count')
logo_col_count = Int('logo_col_count')

nav_x = Int('nav_x')
nav_y = Int('nav_y')
nav_row_count = Int('nav_row_count')
nav_col_count = Int('nav_col_count')

search_x = Int('search_x')
search_y = Int('search_y')
search_row_count = Int('search_row_count')
search_col_count = Int('search_col_count')

sn_x = Int('sn_x')
sn_y = Int('sn_y')
sn_row_count = Int('sn_row_count')
sn_col_count = Int('sn_col_count')

vk_x = Int('vk_x')
vk_y = Int('vk_y')
vk_row_count = Int('vk_row_count')
vk_col_count = Int('vk_col_count')

twitter_x = Int('twitter_x')
twitter_y = Int('twitter_y')
twitter_row_count = Int('twitter_row_count')
twitter_col_count = Int('twitter_col_count')

fb_x = Int('fb_x')
fb_y = Int('fb_y')
fb_row_count = Int('fb_row_count')
fb_col_count = Int('fb_col_count')

icls_x = Int('icls_x')
icls_y = Int('icls_y')
icls_row_count = Int('icls_row_count')
icls_col_count = Int('icls_col_count')

profile_x = Int('profile_x')
profile_y = Int('profile_y')
profile_row_count = Int('profile_row_count')
profile_col_count = Int('profile_col_count')

cart_x = Int('cart_x')
cart_y = Int('cart_y')
cart_row_count = Int('cart_row_count')
cart_col_count = Int('cart_col_count')
"""
================================OBJECTS==============================
"""

"""
h - header
l - logo
n - nav
s - search
i - social network icons
I - other icons (e.g. profile, cart)
t - twitter icon
v - vk icon
f - facebook icon
"""


def create_header(width=1900, height=200, center_horizontal=False, center_vertical=False, is_fullwidth=False,
                  justify_left=False, justify_right=False, justify_center=False, min_width=0, min_height=0,
                  max_width=None, max_height=None):
    header = BaseElement(header_x, header_y, header_col_count, header_row_count, order=0, width=width, height=height,
                         center_horizontal=center_horizontal, center_vertical=center_vertical, label="h",
                         is_fullwidth=is_fullwidth, justify_left=justify_left, justify_right=justify_right,
                         justify_center=justify_center, min_width=min_width, min_height=min_height, max_width=max_width,
                         max_height=max_height)
    header_table = Table(50, 50, width=header.width, height=header.height)
    header.table = header_table

    return header


def find_solutions_header(header, children, mutable_elements):
    arr = []
    for child in children:
        if child is not None:
            arr.append(child)
    header.add_children(arr)

    print("ROW:")
    print(header.table.row_count)
    print("COL:")
    print(header.table.col_count)

    return solve(header, mutable_elements)


def create_logo(parent, is_left=False, is_right=False, is_top=False, is_bottom=False, width=100, height=100,
                min_width=100, min_height=100, max_width=200, max_height=200, order=0):
    logo = BaseElement(logo_x, logo_y, logo_col_count, logo_row_count, order=order, is_left=is_left, is_right=is_right,
                       is_top=is_top, is_bottom=is_bottom, height=height, width=width, min_width=min_width,
                       min_height=min_height, max_width=max_width, max_height=max_height,
                       label="l", parent=parent)

    return logo


def create_nav(parent, links_list, is_left=False, is_right=False, is_top=False, is_bottom=False, is_fullwidth=False,
               is_fullheight=False, is_flexwidth=False, is_flexheight=False, order=1):
    #    nav = ListElement(nav_x, nav_y, nav_col_count, nav_row_count, order=1, is_flexwidth=True,
    #                      links_list=LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.5,
    #                                            word_height=50), label="n", parent=parent)
    nav = ListElement(nav_x, nav_y, nav_col_count, nav_row_count, order=order, is_flexwidth=is_flexwidth,
                      is_flexheight=is_flexheight, is_left=is_left, is_right=is_right, is_top=is_top,
                      is_bottom=is_bottom, is_fullwidth=is_fullwidth, is_fullheight=is_fullheight,
                      links_list=links_list, label="n", parent=parent)

    return nav


def create_search(parent, is_left=False, is_right=False, is_top=False, is_bottom=False, is_fullwidth=False,
                  is_flexwidth=False, is_flexheight=False, min_width=0, min_height=0, max_width=None, max_height=None, order=1):
    search = BaseElement(search_x, search_y, search_col_count, search_row_count, order=order, is_flexwidth=is_flexwidth,
                         is_flexheight=is_flexheight, is_left=is_left, is_right=is_right, is_top=is_top,
                         is_bottom=is_bottom, is_fullwidth=is_fullwidth,
                         min_height=min_height, min_width=min_width, max_width=max_width, max_height=max_height,
                         label="s", parent=parent)

    return search


def create_sn_icons_list(parent, icons, icon_width=50, icon_height=50, is_left=False, is_right=False, is_top=False,
                         is_bottom=False, center_horizontal=False, center_vertical=False, order=2):
    sn_icons = IconsListElement(sn_x, sn_y, sn_col_count, sn_row_count, is_left=is_left, is_right=is_right,
                                is_top=is_top, is_bottom=is_bottom, order=order,
                                center_horizontal=center_horizontal, center_vertical=center_vertical, parent=parent)
    arr = []
    for icon in icons:
        if icon == 't':
            arr.append(IconElement(twitter_x, twitter_y, twitter_col_count, twitter_row_count, width=icon_width,
                                   height=icon_height, order=1, label="t",
                                   parent=sn_icons))
        elif icon == 'v':
            arr.append(
                IconElement(vk_x, vk_y, vk_col_count, vk_row_count, width=icon_width, height=icon_height, order=1,
                            label="v", parent=sn_icons))
        elif icon == 'f':
            arr.append(
                IconElement(fb_x, fb_y, fb_col_count, fb_row_count, width=icon_width, height=icon_height, order=1,
                            label="f", parent=sn_icons))
    sn_icons.add_children(arr)

    return sn_icons


def create_icls_icons_list(parent, icons, icon_width=50, icon_height=50, is_left=False, is_right=False, is_top=False,
                           is_bottom=False, center_horizontal=False, center_vertical=False, order=2):
    icls_icons = IconsListElement(icls_x, icls_y, icls_col_count, icls_row_count, is_left=is_left, is_right=is_right,
                                  is_top=is_top, is_bottom=is_bottom, order=order,
                                  center_horizontal=center_horizontal, center_vertical=center_vertical, parent=parent,
                                  label='I')
    arr = []
    for icon in icons:
        if icon == 'p':
            arr.append(IconElement(profile_x, profile_y, profile_col_count, profile_row_count, width=icon_width,
                                   height=icon_height, order=1, label="p",
                                   parent=icls_icons))
        elif icon == 'c':
            arr.append(IconElement(cart_x, cart_y, cart_col_count, cart_row_count, width=icon_width, height=icon_height,
                                   order=1, label="c", parent=icls_icons))
    icls_icons.add_children(arr)

    return icls_icons


"""
==============================RULES=========================
"""


def solve(parent, mutable_elements):
    s = Optimize()

    for child in parent.children:
        s.add(And(child.x >= 0, child.x + child.col_count <= parent.table.col_count, child.y >= 0,
                  child.y + child.row_count <= parent.table.row_count))

        if child.width:
            s.add(child.col_count == parent.table.get_col_count_from_width(child.width))
        else:
            s.add(And(
                child.col_count >= parent.table.get_col_count_from_width(child.min_width),
                child.col_count <= parent.table.get_col_count_from_width(child.max_width)
            ))
        if child.height:
            s.add(child.row_count == parent.table.get_row_count_from_height(child.height))
        else:
            s.add(And(
                child.row_count >= parent.table.get_row_count_from_height(child.min_height),
                child.row_count <= parent.table.get_row_count_from_height(child.max_height)
            ))

        if child.is_flexwidth:
            s.maximize(child.col_count)
        if child.is_flexheight:
            s.maximize(child.row_count)

        for another_child in parent.children:
            if child != another_child and child.order == another_child.order:
                s.add(Or(
                    And(another_child.x >= child.x + child.col_count, another_child.y == child.y),
                    And(child.x >= another_child.x + another_child.col_count, another_child.y == child.y),
                    another_child.y >= child.y + child.row_count,
                    child.y >= another_child.y + another_child.row_count
                ))
            if child.order == 0:
                if another_child.order == 1 or another_child.order == 2:
                    s.add(Or(And(another_child.x >= child.x + child.col_count, another_child.y == child.y),
                             another_child.y >= child.y + child.row_count))
            elif child.order == 2:
                if another_child.order == 1:
                    s.add(Or(And(child.x >= another_child.x + another_child.col_count, another_child.y == child.y),
                             another_child.y >= child.y + child.row_count))

        if parent.center_vertical:
            pass
        else:
            if parent.justify_left:
                s.minimize(child.x)
            elif parent.justify_right:
                s.maximize(child.x)
            else:
                if child.is_left:
                    s.minimize(child.x)
                elif child.is_right:
                    s.maximize(child.x)

        if parent.center_horizontal:
            for another_child in parent.children:
                if child != another_child:
                    s.add(If(And((another_child.y + another_child.row_count) >= child.y + child.row_count,
                                 child.y >= another_child.y),
                             child.y == another_child.y + another_child.row_count / 2 - child.row_count / 2, True))
        else:
            if child.is_top:
                s.minimize(child.y)
            elif child.is_bottom:
                s.maximize(child.y)

    res_arr = []
    m_arr = []
    res = s.check()
    while res == sat:
        m = s.model()
        m_arr.append(m)

        arr = [['0' for i in range(parent.table.col_count)] for j in range(parent.table.row_count)]

        for child in parent.children:
            #    print(f"{child.x} : {m[child.x]}")
            #    print(f"{child.y} : {m[child.y]}")
            #    print(f"{child.col_count} : {m[child.col_count]}")
            #    print(f"{child.row_count} : {m[child.row_count]}")
            place_elem(m[child.x].as_long(), m[child.y].as_long(), m[child.col_count].as_long(),
                       m[child.row_count].as_long(), child.label, arr)

        res_arr.append(arr)
        # for i in range(len(arr)):
        #    print(arr[i])

        for t in mutable_elements:
            s.add(Or(t != m[t]))
        res = s.check()
    else:
        print(res)

    # SORT RESULT BY 0 COUNT
    sorter = lambda x: sum(x[i] != 0 for i in range(len(x)))
    sorted_res_arr = sorted(res_arr, key=sorter)
    for arr in sorted_res_arr:
        for i in range(len(arr)):
            print(arr[i])
        print("----------------------------------------------------")

    return m_arr, res_arr


