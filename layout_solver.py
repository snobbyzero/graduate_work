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
header_margin_right = Int('header_margin_right')
header_margin_left = Int('header_margin_left')
header_margin_top = Int('header_margin_top')
header_margin_bottom = Int('header_margin_bottom')

logo_x = Int('logo_x')
logo_y = Int('logo_y')
logo_row_count = Int('logo_row_count')
logo_col_count = Int('logo_col_count')
logo_margin_right = Int('logo_margin_right')
logo_margin_left = Int('logo_margin_left')
logo_margin_top = Int('logo_margin_top')
logo_margin_bottom = Int('logo_margin_bottom')

nav_x = Int('nav_x')
nav_y = Int('nav_y')
nav_row_count = Int('nav_row_count')
nav_col_count = Int('nav_col_count')
nav_margin_right = Int('nav_margin_right')
nav_margin_left = Int('nav_margin_left')
nav_margin_top = Int('nav_margin_top')
nav_margin_bottom = Int('nav_margin_bottom')

search_div_x = Int('search_div_x')
search_div_y = Int('search_div_y')
search_div_row_count = Int('search_div_row_count')
search_div_col_count = Int('search_div_col_count')
search_div_margin_right = Int('search_div_margin_right')
search_div_margin_left = Int('search_div_margin_left')
search_div_margin_top = Int('search_div_margin_top')
search_div_margin_bottom = Int('search_div_margin_bottom')

search_x = Int('search_x')
search_y = Int('search_y')
search_col_count = Int('search_col_count')
search_row_count = Int('search_row_count')
search_margin_right = Int('search_margin_right')
search_margin_left = Int('search_margin_left')
search_margin_top = Int('search_margin_top')
search_margin_bottom = Int('search_margin_bottom')

sn_x = Int('sn_x')
sn_y = Int('sn_y')
sn_row_count = Int('sn_row_count')
sn_col_count = Int('sn_col_count')
sn_margin_right = Int('sn_margin_right')
sn_margin_left = Int('sn_margin_left')
sn_margin_top = Int('sn_margin_top')
sn_margin_bottom = Int('sn_margin_bottom')

vk_x = Int('vk_x')
vk_y = Int('vk_y')
vk_row_count = Int('vk_row_count')
vk_col_count = Int('vk_col_count')
vk_margin_right = Int('vk_margin_right')
vk_margin_left = Int('vk_margin_left')
vk_margin_top = Int('vk_margin_top')
vk_margin_bottom = Int('vk_margin_bottom')

twitter_x = Int('twitter_x')
twitter_y = Int('twitter_y')
twitter_row_count = Int('twitter_row_count')
twitter_col_count = Int('twitter_col_count')
twitter_margin_right = Int('twitter_margin_right')
twitter_margin_left = Int('twitter_margin_left')
twitter_margin_top = Int('twitter_margin_top')
twitter_margin_bottom = Int('twitter_margin_bottom')

fb_x = Int('fb_x')
fb_y = Int('fb_y')
fb_row_count = Int('fb_row_count')
fb_col_count = Int('fb_col_count')
fb_margin_right = Int('fb_margin_right')
fb_margin_left = Int('fb_margin_left')
fb_margin_top = Int('fb_margin_top')
fb_margin_bottom = Int('fb_margin_bottom')

icls_x = Int('icls_x')
icls_y = Int('icls_y')
icls_row_count = Int('icls_row_count')
icls_col_count = Int('icls_col_count')
icls_margin_right = Int('icls_margin_right')
icls_margin_left = Int('icls_margin_left')
icls_margin_top = Int('icls_margin_top')
icls_margin_bottom = Int('icls_margin_bottom')

profile_x = Int('profile_x')
profile_y = Int('profile_y')
profile_row_count = Int('profile_row_count')
profile_col_count = Int('profile_col_count')
profile_margin_right = Int('profile_margin_right')
profile_margin_left = Int('profile_margin_left')
profile_margin_top = Int('profile_margin_top')
profile_margin_bottom = Int('profile_margin_bottom')

cart_x = Int('cart_x')
cart_y = Int('cart_y')
cart_row_count = Int('cart_row_count')
cart_col_count = Int('cart_col_count')
cart_margin_right = Int('cart_margin_right')
cart_margin_left = Int('cart_margin_left')
cart_margin_top = Int('cart_margin_top')
cart_margin_bottom = Int('cart_margin_bottom')
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


def create_header(width=1900, height=300, center_horizontal=False, center_vertical=False, is_fullwidth=False,
                  justify_left=False, justify_right=False, justify_center=False, min_width=0, min_height=0,
                  max_width=None, max_height=None):
    header = BaseElement(header_x, header_y, header_col_count, header_row_count, header_margin_right,
                         header_margin_left, header_margin_bottom, header_margin_top, order=0, width=width,
                         height=height,
                         center_horizontal=center_horizontal, center_vertical=center_vertical, label="h",
                         is_fullwidth=is_fullwidth, justify_left=justify_left, justify_right=justify_right,
                         justify_center=justify_center, min_width=min_width, min_height=min_height, max_width=max_width,
                         max_height=max_height)
    header_table = Table(10, 10, width=header.width, height=header.height)
    header.table = header_table

    return header


def find_solutions(el, children, mutable_elements):
    arr = []
    for child in children:
        if child is not None:
            arr.append(child)
    el.add_children(arr)

    print("ROW:")
    print(el.table.row_count)
    print("COL:")
    print(el.table.col_count)

    return solve(el, mutable_elements)


def create_logo(parent, is_left=False, is_right=False, is_top=False, is_bottom=False, width=50, height=50,
                min_width=100, min_height=100, max_width=200, max_height=200, order=0):
    logo = BaseElement(logo_x, logo_y, logo_col_count, logo_row_count, logo_margin_right, logo_margin_left,
                       logo_margin_bottom, logo_margin_top, order=order, is_left=is_left, is_right=is_right,
                       is_top=is_top, is_bottom=is_bottom, height=height, width=width, min_width=min_width,
                       min_height=min_height, max_width=max_width, max_height=max_height,
                       label="l", parent=parent)

    return logo


def create_nav(parent, links_list, is_left=False, is_right=False, is_top=False, is_bottom=False, is_fullwidth=False,
               is_fullheight=False, is_flexwidth=False, is_flexheight=False, order=1):
    #    nav = ListElement(nav_x, nav_y, nav_col_count, nav_row_count, order=1, is_flexwidth=True,
    #                      links_list=LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.5,
    #                                            word_height=50), label="n", parent=parent)
    nav = ListElement(nav_x, nav_y, nav_col_count, nav_row_count, nav_margin_right, nav_margin_left, nav_margin_bottom,
                      nav_margin_top, order=order, is_flexwidth=is_flexwidth,
                      is_flexheight=is_flexheight, is_left=is_left, is_right=is_right, is_top=is_top,
                      is_bottom=is_bottom, is_fullwidth=is_fullwidth, is_fullheight=is_fullheight,
                      links_list=links_list, label="n", parent=parent)

    return nav


def create_search(parent, is_left=False, is_right=False, is_top=False, is_bottom=False, is_fullwidth=False,
                  is_flexwidth=False, is_flexheight=False, min_width=0, min_height=0, max_width=None, max_height=None,
                  order=1):
    search_div = BaseElement(search_div_x, search_div_y, search_div_col_count, search_div_row_count,
                             search_div_margin_right, search_margin_left, search_div_margin_bottom,
                             search_div_margin_top, order=order,
                             is_flexwidth=is_flexwidth,
                             is_flexheight=is_flexheight, is_left=is_left, is_right=is_right, is_top=is_top,
                             is_bottom=is_bottom, is_fullwidth=is_fullwidth,
                             min_height=min_height, min_width=min_width, max_width=max_width, max_height=max_height,
                             label="s", parent=parent)

    # search_div.add_children([BaseElement(search_x, search_y, search_col_count, search_row_count, )])
    return search_div


def create_sn_icons_list(parent, icons, icon_width=50, icon_height=50, is_left=False, is_right=False, is_top=False,
                         is_bottom=False, center_horizontal=False, center_vertical=False, order=2):
    sn_icons = IconsListElement(sn_x, sn_y, sn_col_count, sn_row_count, sn_margin_right, sn_margin_left,
                                sn_margin_bottom, sn_margin_top, is_left=is_left, is_right=is_right,
                                is_top=is_top, is_bottom=is_bottom, order=order,
                                center_horizontal=center_horizontal, center_vertical=center_vertical, parent=parent)
    arr = []
    for icon in icons:
        if icon == 't':
            arr.append(IconElement(twitter_x, twitter_y, twitter_col_count, twitter_row_count, twitter_margin_right,
                                   twitter_margin_left, twitter_margin_bottom, twitter_margin_top, width=icon_width,
                                   height=icon_height, order=1, label="t",
                                   parent=sn_icons))
        elif icon == 'v':
            arr.append(
                IconElement(vk_x, vk_y, vk_col_count, vk_row_count, vk_margin_right, vk_margin_left, vk_margin_bottom,
                            vk_margin_top, width=icon_width, height=icon_height, order=1,
                            label="v", parent=sn_icons))
        elif icon == 'f':
            arr.append(
                IconElement(fb_x, fb_y, fb_col_count, fb_row_count, fb_margin_right, fb_margin_left, fb_margin_bottom,
                            fb_margin_top, width=icon_width, height=icon_height, order=1,
                            label="f", parent=sn_icons))
    sn_icons.add_children(arr)

    return sn_icons


def create_icls_icons_list(parent, icons, icon_width=50, icon_height=50, is_left=False, is_right=False, is_top=False,
                           is_bottom=False, center_horizontal=False, center_vertical=False, order=2):
    icls_icons = IconsListElement(icls_x, icls_y, icls_col_count, icls_row_count, icls_margin_right, icls_margin_left,
                                  icls_margin_bottom, icls_margin_top, is_left=is_left, is_right=is_right,
                                  is_top=is_top, is_bottom=is_bottom, order=order,
                                  center_horizontal=center_horizontal, center_vertical=center_vertical, parent=parent,
                                  label='I')
    arr = []
    for icon in icons:
        if icon == 'p':
            arr.append(IconElement(profile_x, profile_y, profile_col_count, profile_row_count, profile_margin_right,
                                   profile_margin_left, profile_margin_bottom, profile_margin_top, width=icon_width,
                                   height=icon_height, order=1, label="p",
                                   parent=icls_icons))
        elif icon == 'c':
            arr.append(IconElement(cart_x, cart_y, cart_col_count, cart_row_count, cart_margin_right, cart_margin_left,
                                   cart_margin_bottom, cart_margin_top, width=icon_width, height=icon_height,
                                   order=1, label="c", parent=icls_icons))
    icls_icons.add_children(arr)

    return icls_icons


"""
==============================RULES=========================
"""


def solve(parent, mutable_elements):
    s = Optimize()

    for child in parent.children:
        s.add(And(
            child.x - child.margin_left >= 0,
            child.x + child.col_count + child.margin_right <= parent.table.col_count,
            child.y - child.margin_top >= 0,
            child.y + child.row_count + child.margin_bottom <= parent.table.row_count
        ))

        s.add(child.margin_right >= parent.table.get_col_count_from_width(child.min_margin_right))
        s.add(child.margin_left >= parent.table.get_col_count_from_width(child.min_margin_left))
        s.add(child.margin_top >= parent.table.get_row_count_from_height(child.min_margin_top))
        s.add(child.margin_bottom >= parent.table.get_row_count_from_height(child.min_margin_bottom))

        if child.max_margin_right:
            s.add(child.margin_right <= child.max_margin_right)
        if child.max_margin_left:
            s.add(child.margin_left <= child.max_margin_left)
        if child.max_margin_top:
            s.add(child.margin_top <= child.max_margin_top)
        if child.max_margin_bottom:
            s.add(child.margin_bottom <= child.max_margin_bottom)

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
                    And(another_child.x - another_child.margin_left >= child.x + child.col_count + another_child.margin_right,
                        # another_child.y - another_child.margin_top == child.y - child.margin_top,
                        # another_child.y + another_child.row_count + another_child.margin_bottom == child.y + child.row_count + child.margin_bottom
                        another_child.row_count + another_child.margin_top + another_child.margin_bottom == child.row_count + child.margin_top + child.margin_bottom,
                        If(child.row_count > another_child.row_count,
                           another_child.y == (child.row_count - another_child.row_count) / 2 + child.y,
                           child.y == (another_child.row_count - child.row_count) / 2 + another_child.y)
                        ),
                    And(child.x - child.margin_left >= another_child.x + another_child.col_count + another_child.margin_right,
                        # another_child.y - another_child.margin_top == child.y - child.margin_top,
                        # another_child.y + another_child.row_count + another_child.margin_bottom == child.y + child.row_count + child.margin_bottom
                        another_child.row_count + another_child.margin_top + another_child.margin_bottom == child.row_count + child.margin_top + child.margin_bottom,
                        If(child.row_count > another_child.row_count,
                           another_child.y == (child.row_count - another_child.row_count) / 2 + child.y,
                           child.y == (another_child.row_count - child.row_count) / 2 + another_child.y)

                        ),
                    another_child.y - another_child.margin_top >= child.y + child.row_count + child.margin_bottom,
                    child.y - child.margin_top >= another_child.y + another_child.row_count + another_child.margin_bottom
                ))
            if child.order == 0:
                if another_child.order == 1 or another_child.order == 2:
                    s.add(Or(And(
                        another_child.x - another_child.margin_left >= child.x + child.col_count + child.margin_right,
                        # another_child.y - another_child.margin_top == child.y - child.margin_top,
                        # another_child.y + another_child.row_count + another_child.margin_bottom == child.y + child.row_count + child.margin_bottom
                        another_child.row_count + another_child.margin_top + another_child.margin_bottom == child.row_count + child.margin_top + child.margin_bottom,
                        If(child.row_count > another_child.row_count,
                           another_child.y == (child.row_count - another_child.row_count) / 2 + child.y,
                           child.y == (another_child.row_count - child.row_count) / 2 + another_child.y)

                    ),
                        another_child.y - another_child.margin_top >= child.y + child.row_count + child.margin_bottom
                    ))
            elif child.order == 2:
                if another_child.order == 1:
                    s.add(Or(And(
                        child.x - child.margin_left >= another_child.x + another_child.col_count + another_child.margin_right,
                        # another_child.y - another_child.margin_top == child.y - child.margin_top,
                        # another_child.y + another_child.row_count + another_child.margin_bottom == child.y + child.row_count + child.margin_bottom
                        another_child.row_count + another_child.margin_top + another_child.margin_bottom == child.row_count + child.margin_top + child.margin_bottom,
                        If(child.row_count > another_child.row_count,
                           another_child.y == (child.row_count - another_child.row_count) / 2 + child.y,
                           child.y == (another_child.row_count - child.row_count) / 2 + another_child.y)

                    ),
                        another_child.y >= child.y + child.row_count + child.margin_bottom
                    ))

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
            pass
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
            print(f"{child.x} : {m[child.x]}")
            print(f"{child.y} : {m[child.y]}")
            print(f"{child.col_count} : {m[child.col_count]}")
            print(f"{child.row_count} : {m[child.row_count]}")
            print(f"{child.margin_right} : {m[child.margin_right]}")
            print(f"{child.margin_left} : {m[child.margin_left]}")
            print(f"{child.margin_bottom} : {m[child.margin_bottom]}")
            print(f"{child.margin_top} : {m[child.margin_top]}")
            place_elem(m[child.x].as_long(), m[child.y].as_long(), m[child.col_count].as_long(),
                       m[child.row_count].as_long(), child.label, arr)

        res_arr.append(arr)
        # for i in range(len(arr)):
        #    print(arr[i])

        for t in mutable_elements:
            s.add(t != m[t])
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
