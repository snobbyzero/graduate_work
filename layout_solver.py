import random
from z3 import *

from classes.CardElement import CardElement
from classes.TextElement import TextElement
from classes.BaseElement import BaseElement
from classes.IconElement import IconElement
from classes.IconsListElement import IconsListElement
from classes.ListElement import ListElement
from classes.ModelRes import ModelRes
from classes.Table import Table
from classes.TextList import TextList

"""
==============================Functions============================
"""


def place_elem(x, y, col_count, row_count, label, arr):
    for i in range(y, row_count + y):
        for j in range(x, col_count + x):
            arr[i][j] = label


"""
================================OBJECTS==============================
"""


def create_body(width=1900, height=1000):
    body = BaseElement("body", width=width, height=height, min_width=width, min_height=height, label='body')
    body.table = Table(10, 10, width=width, height=height)

    return body


def create_content(parent, is_fullwidth=False, is_flexwidth=False, justify_left=False, justify_right=False, min_width=0,
                   min_height=0,
                   max_width=None, max_height=None, min_margin_right=0, min_margin_left=0, min_margin_top=0,
                   min_margin_bottom=0, max_margin_right=10, max_margin_left=10, max_margin_top=10,
                   max_margin_bottom=10):
    content = BaseElement("content", parent=parent, is_fullwidth=is_fullwidth, is_flexwidth=is_flexwidth,
                          justify_left=justify_left,
                          justify_right=justify_right, min_width=min_width, label="content",
                          min_height=min_height, max_width=max_width, max_height=max_height,
                          min_margin_right=min_margin_right,
                          min_margin_left=min_margin_left, min_margin_top=min_margin_top,
                          min_margin_bottom=min_margin_bottom,
                          max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                          max_margin_top=max_margin_top,
                          max_margin_bottom=max_margin_bottom)

    return content


def create_card(parent, number, size, min_margin_right=0, min_margin_left=0, center_horizontal=False,
                center_vertical=False,
                min_margin_top=0, min_margin_bottom=0, max_margin_right=10, max_margin_left=10, max_margin_top=10,
                max_margin_bottom=10):
    card = CardElement(f"card{number}", size, parent=parent, min_margin_right=min_margin_right,
                       min_margin_left=min_margin_left, center_horizontal=center_horizontal,
                       min_margin_top=min_margin_top, min_margin_bottom=min_margin_bottom,
                       max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                       max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom,
                       center_vertical=center_vertical)

    return card


def create_text(text, parent, label, min_width=0, min_height=0, max_width=None, max_height=None, min_margin_right=0,
                min_margin_left=0, is_fullwidth=False, is_flexwidth=False,
                min_margin_top=0, min_margin_bottom=0, max_margin_right=0, max_margin_left=0, max_margin_top=0,
                max_margin_bottom=0):
    text = TextElement(text, min_width=min_width, min_height=min_height, max_width=max_width, max_height=max_height,
                       parent=parent, is_fullwidth=is_fullwidth, is_flexwidth=is_flexwidth,
                       min_margin_right=min_margin_right, min_margin_left=min_margin_left,
                       min_margin_top=min_margin_top, min_margin_bottom=min_margin_bottom,
                       max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                       max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom, label=label)
    return text


def create_icons_list(parent, name, label, rules=None, center_horizontal=False, center_vertical=False,
                      min_margin_right=0, is_fullwidth=False, is_flexwidth=False, justify_left=False,
                      min_margin_left=0, min_margin_top=0, min_margin_bottom=0, max_margin_right=0,
                      max_margin_left=0, max_margin_top=0, max_margin_bottom=0, is_vertical=False):
    icons_list = IconsListElement(name, rules=rules, label=label, is_fullwidth=is_fullwidth,
                                  center_horizontal=center_horizontal, center_vertical=center_vertical, parent=parent,
                                  min_margin_right=min_margin_right, min_margin_left=min_margin_left,
                                  min_margin_top=min_margin_top, min_margin_bottom=min_margin_bottom,
                                  max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                                  max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom,
                                  is_vertical=is_vertical, is_flexwidth=is_flexwidth, justify_left=justify_left)

    return icons_list


def create_div(parent, name, label, min_margin_right=0, min_margin_left=0, min_margin_top=0, min_margin_bottom=0,
               is_flexheight=False, is_flexwidth=False,
               max_margin_right=0, max_margin_left=0, max_margin_top=0, max_margin_bottom=0, min_width=0, min_height=0,
               is_fullwidth=False,
               width=None, height=None, center_horizontal=False, center_vertical=False, ):
    div = BaseElement(name, min_width=min_width, min_height=min_height, label=label, min_margin_right=min_margin_right,
                      min_margin_left=min_margin_left,
                      min_margin_top=min_margin_top, min_margin_bottom=min_margin_bottom, is_fullwidth=is_fullwidth,
                      is_flexwidth=is_flexwidth,
                      max_margin_right=max_margin_right, max_margin_left=max_margin_left, is_flexheight=is_flexheight,
                      max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom, parent=parent, width=width,
                      height=height,
                      center_vertical=center_vertical, center_horizontal=center_horizontal)

    return div


def create_header(parent, width=None, height=None, rules=None, is_fullwidth=False,
                  justify_left=False, justify_right=False, min_width=0, min_height=0,
                  max_width=None, max_height=None, min_margin_right=0, min_margin_left=0, min_margin_top=0,
                  min_margin_bottom=0, max_margin_right=0, max_margin_left=0, max_margin_top=0, max_margin_bottom=0):
    header = BaseElement("header", rules=rules, width=width,
                         height=height, parent=parent, label="header", is_fullwidth=is_fullwidth,
                         justify_left=justify_left, max_margin_left=0, max_margin_right=0, min_margin_left=0, min_margin_right=0,
                         justify_right=justify_right, min_width=min_width,
                         min_height=min_height, max_width=max_width, max_height=max_height)

    return header


def create_footer(parent, width=None, height=None, rules=None, is_fullwidth=False,
                  justify_left=False, justify_right=False, min_width=0, min_height=0,
                  max_width=None, max_height=None):
    footer = BaseElement("footer", rules=rules, width=width,
                         height=height, parent=parent, label="footer", is_fullwidth=is_fullwidth,
                         justify_left=justify_left, max_margin_left=0, max_margin_right=0, min_margin_left=0, min_margin_right=0,
                         justify_right=justify_right, min_width=min_width,
                         min_height=min_height, max_width=max_width, max_height=max_height)

    return footer


def create_child(parent, name, label, width=50, height=50, min_width=0, min_height=0, max_width=None, max_height=None,
                 min_margin_right=0, min_margin_left=0, min_margin_top=0, min_margin_bottom=0,
                 max_margin_right=0, max_margin_left=0, max_margin_top=0, max_margin_bottom=0):
    el = BaseElement(name, height=height, width=width,
                     min_width=min_width, min_height=min_height, max_width=max_width, max_height=max_height,
                     label=label, parent=parent,
                     min_margin_right=min_margin_right, min_margin_left=min_margin_left,
                     min_margin_top=min_margin_top, min_margin_bottom=min_margin_bottom,
                     max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                     max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom)
    return el


def create_text_list(parent, name, label, text_list, is_fullwidth=False,
                     is_fullheight=False, is_flexwidth=False, is_flexheight=False, min_margin_right=0,
                     min_margin_left=0,
                     min_margin_top=0, min_margin_bottom=0, max_margin_right=10, max_margin_left=10, max_margin_top=10,
                     max_margin_bottom=10):
    text_list = ListElement(name, is_flexwidth=is_flexwidth,
                            is_flexheight=is_flexheight, is_fullwidth=is_fullwidth, is_fullheight=is_fullheight,
                            text_list=text_list, label=label, parent=parent, min_margin_right=min_margin_right,
                            min_margin_left=min_margin_left, min_margin_top=min_margin_top,
                            min_margin_bottom=min_margin_bottom, max_margin_right=max_margin_right,
                            max_margin_left=max_margin_left, max_margin_top=max_margin_top,
                            max_margin_bottom=max_margin_bottom)

    return text_list


def create_input(parent, name, label, is_fullwidth=False, is_flexwidth=False, max_width=None, max_height=None,
                      min_width=0, min_height=0, min_margin_right=0, min_margin_left=0, min_margin_top=0, min_margin_bottom=0,
                      max_margin_right=10, max_margin_left=10, max_margin_top=10, max_margin_bottom=10):
    input = BaseElement(name, min_height=min_height, min_width=min_width, label=label, max_width=max_width,
                        max_height=max_height, parent=parent, is_fullwidth=is_fullwidth, is_flexwidth=is_flexwidth,
                        min_margin_right=min_margin_right, min_margin_left=min_margin_left, min_margin_top=min_margin_top,
                        min_margin_bottom=min_margin_bottom, max_margin_right=max_margin_right, max_margin_left=max_margin_left,
                        max_margin_top=max_margin_top, max_margin_bottom=max_margin_bottom)
    return input


def create_search_div(parent, is_fullwidth=False, is_flexwidth=False, is_flexheight=False,
                      search_min_width=0, search_min_height=0, max_width=None, max_height=None,
                      min_margin_right=0, min_margin_left=0, min_margin_top=0, min_margin_bottom=0,
                      max_margin_right=10, max_margin_left=10, max_margin_top=10, max_margin_bottom=10):
    search = BaseElement("search", min_width=search_min_width, min_height=search_min_height, min_margin_left=10,
                         min_margin_right=10,
                         min_margin_bottom=0, min_margin_top=0, label="search")
    search_div = BaseElement("search", is_flexwidth=is_flexwidth, is_flexheight=is_flexheight,
                             is_fullwidth=is_fullwidth,
                             min_height=search.min_height + search.min_margin_bottom + search.min_margin_top,
                             min_width=search.min_width + search.min_margin_right + search.min_margin_left,
                             max_width=max_width, max_height=max_height,
                             label="s", parent=parent, min_margin_right=min_margin_right,
                             min_margin_left=min_margin_left, min_margin_top=min_margin_top,
                             min_margin_bottom=min_margin_bottom, max_margin_right=max_margin_right,
                             max_margin_left=max_margin_left, max_margin_top=max_margin_top,
                             max_margin_bottom=max_margin_bottom, center_vertical=True)
    search.parent = search_div
    search_div.add_child(search)

    return search_div


def create_icon(parent, name, icon_label, icon_width=20, icon_height=20, min_margin_right=0, min_margin_left=0,
                min_margin_top=0, min_margin_bottom=0, max_margin_right=10, max_margin_left=10, max_margin_top=10,
                max_margin_bottom=10, link=""):
    icon = IconElement(name, width=icon_width, height=icon_height,
                       label=icon_label, parent=parent, min_margin_right=min_margin_right,
                       min_margin_left=min_margin_left, min_margin_top=min_margin_top,
                       min_margin_bottom=min_margin_bottom, max_margin_right=max_margin_right,
                       max_margin_left=max_margin_left, max_margin_top=max_margin_top,
                       max_margin_bottom=max_margin_bottom, link=link)

    return icon


"""
==============================RULES=========================
"""


def solve(parent, rule=None, parent_model=None):
    s = Optimize()
    #if rule is not None:
    #    s.add(rule)
    for r in rule:
        s.add_soft(r)

    if parent.width:
        s.add(parent.col_count == parent.table.get_col_count_from_width(parent.width))
    if parent.height:
        s.add(parent.row_count == parent.table.get_row_count_from_height(parent.height))
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
            s.add(child.margin_right <= parent.table.get_col_count_from_width(child.max_margin_right))
        if child.max_margin_left:
            s.add(child.margin_left <= parent.table.get_col_count_from_width(child.max_margin_left))
        if child.max_margin_top:
            s.add(child.margin_top <= parent.table.get_row_count_from_height(child.max_margin_top))
        if child.max_margin_bottom:
            s.add(child.margin_bottom <= parent.table.get_row_count_from_height(child.max_margin_bottom))

        if child.width:
            s.add(child.col_count == parent.table.get_col_count_from_width(child.width))
        else:
            s.add(child.col_count >= parent.table.get_col_count_from_width(child.min_width))
            if child.max_width:
                s.add(child.col_count <= parent.table.get_col_count_from_width(child.max_width))

        if child.height:
            s.add(child.row_count == parent.table.get_row_count_from_height(child.height))
        else:
            s.add(child.row_count >= parent.table.get_row_count_from_height(child.min_height))
            if child.max_height:
                s.add(child.row_count <= parent.table.get_row_count_from_height(child.max_height))

        for another_child in parent.children:
            if child != another_child:
                s.add(Or(
                    And(another_child in child.right_elements,
                        another_child.x - another_child.margin_left >= child.x + child.col_count + another_child.margin_right,
                        ),
                    And(another_child in child.left_elements,
                        child.x - child.margin_left >= another_child.x + another_child.col_count + another_child.margin_right,
                        ),
                    And(another_child in child.top_elements,
                        child.y - child.margin_top >= another_child.y + another_child.row_count + another_child.margin_bottom),
                    And(another_child in child.bottom_elements,
                        another_child.y - another_child.margin_top >= child.y + child.row_count + child.margin_bottom),
                    And(another_child not in child.right_elements, another_child not in child.left_elements,
                        another_child not in child.bottom_elements, another_child not in child.top_elements)
                ))
        if len(child.right_elements) > 0:
            if child.right_elements[0] is not None:
                s.add_soft(child.right_elements[0].y - child.right_elements[0].margin_top == child.y - child.margin_top)
        if len(child.left_elements) > 0:
            if child.left_elements[0] is not None:
                s.add_soft(child.left_elements[0].y - child.left_elements[0].margin_top == child.y - child.margin_top)

        if parent.center_vertical:
            pass
        else:
            if parent.justify_left:
                s.minimize(child.x)
            elif parent.justify_right:
                s.maximize(child.x)
        if child.is_fullwidth:
            #print("fullwidth:")
            #(child.name)
            #print(parent.name)
            s.add(child.col_count + child.margin_left + child.margin_right == parent.table.col_count)
        if child.is_flexwidth:
            s.maximize(child.col_count)
        if child.is_flexheight:
            s.maximize(child.row_count)

    # res_arr = []
    # m_arr = []
    res = s.check()
    if res == sat:
        m = s.model()

        arr = [['0' for i in range(parent.table.col_count)] for j in range(parent.table.row_count)]

        model = ModelRes(m, arr, parent_model)
        parent.add_model(model)

        for child in parent.children:

            #print(m[parent.col_count])
            #print(f"{child.x} : {m[child.x]}")
            #print(f"{child.y} : {m[child.y]}")
            #print(f"{child.col_count} : {m[child.col_count]}")
            #print(f"{child.row_count} : {m[child.row_count]}")
            #print(f"{child.margin_right} : {m[child.margin_right]}")
            #print(f"{child.margin_left} : {m[child.margin_left]}")
            #print(f"{child.margin_bottom} : {m[child.margin_bottom]}")
            #print(f"{child.margin_top} : {m[child.margin_top]}")
            place_elem(m[child.x].as_long(), m[child.y].as_long(), m[child.col_count].as_long(),
                       m[child.row_count].as_long(), child.label, arr)

            if len(child.children) > 0:
                child.table = Table(5, 5, width=child.get_width_with_parent(m),
                                    height=child.get_height_with_parent(m))
                find_solutions(child, model)
        #if parent.name == 'div_header' or parent.name == 'card0' or parent.name == 'top_div' and parent.name != 'body' and parent.name != 'content' and parent.name != 'cards':
            #for i in range(len(arr)):
                #print(arr[i])
        #print("----------------------------------------------------")

    #else:
        #print(res)


def find_solutions(parent, model=None):
    soft_rules = []
    # Составляем список всевозможных софт правил
    # Ширина и высота с шагом 10
    # Если макс значение отсутствует, то макс = мин + 100

    for child in parent.children:
        if child.width is None and child.is_flexwidth == False and child.is_fullwidth == False:
            if child.max_width:
                for i in range(0, (child.max_width - child.min_width) // 10):
                    soft_rules.append(And(child.col_count >= parent.table.get_col_count_from_width(child.min_width + i * 10)))
            else:
                for i in range(0, 10):
                    soft_rules.append(And(child.col_count >= parent.table.get_col_count_from_width(child.min_width + i * 10)))
        if child.height is None:
            if child.max_height:
                for i in range(0, (child.max_height - child.min_height) // 10):
                    soft_rules.append(And(child.row_count >= parent.table.get_row_count_from_height(child.min_height + i * 10)))
            else:
                for i in range(0, 20):
                    soft_rules.append(And(child.row_count >= parent.table.get_row_count_from_height(child.min_height + i * 10)))
        for another_child in child.right_elements:
            if another_child is not None:
                soft_rules.append(And(child.x <= another_child.x))
        for another_child in child.left_elements:
            if another_child is not None:
                soft_rules.append(And(child.x >= another_child.x))
        for another_child in child.top_elements:
            if another_child is not None:
                soft_rules.append(And(child.y <= another_child.y))
        for another_child in child.bottom_elements:
            if another_child is not None:
                soft_rules.append(And(child.y >= another_child.y))
    # выбираем n рандомных софт правил
    #print(len(soft_rules))
    k = len(soft_rules) // 3

    arr = random.choices(soft_rules, k=k)
    if model is not None:
        solve(parent, arr, parent_model=model)
    else:
        solve(parent, arr)
    #if len(parent.rules) > 0:
    #    for rule in parent.rules:
    #        solve(parent, rule, model)
    #elif model is not None:
    #    solve(parent, parent_model=model)
    #else:
    #    solve(parent)

