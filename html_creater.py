from yattag import Doc

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.IconButtonJSON import IconButtonJSON
from json_classes.Measure import Measure
from json_classes.NavListJSON import NavListJSON
from json_classes.SearchBarJSON import SearchBarJSON
from json_classes.ValueJSON import ValueJSON
from layout_solver import *

doc, tag, text = Doc().tagtext()

header = create_header(width=900, height=160)
logo = create_logo(header, is_left=True, width=60, height=40, min_margin_left=10, min_margin_right=10, min_margin_top=10, min_margin_bottom=10, max_margin_left=20, max_margin_right=20, max_margin_bottom=10, max_margin_top=10)
nav = create_nav(header, LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.0, word_height=20+16+16),
                 is_flexwidth=True, min_margin_left=10, min_margin_right=10, min_margin_top=10, min_margin_bottom=10, max_margin_left=20, max_margin_right=20, max_margin_bottom=10, max_margin_top=10)
search_div = create_search_div(header, min_width=200, min_height=60, is_flexwidth=True, min_margin_left=10, min_margin_right=10, min_margin_top=10, min_margin_bottom=10, max_margin_left=20, max_margin_right=20, max_margin_bottom=10, max_margin_top=10)
header.mutable_elements = [nav.y, search_div.y, nav.col_count, search_div.col_count]

icls_icons = create_icls_icons_list(header, is_right=True, min_margin_left=10, min_margin_right=10, min_margin_top=10, min_margin_bottom=10, max_margin_left=20, max_margin_right=20, max_margin_bottom=10, max_margin_top=10)
profile_icon = create_icon(icls_icons, 'p', 30, 30, min_margin_left=0, min_margin_right=10, min_margin_top=0, min_margin_bottom=0, max_margin_left=0, max_margin_right=10, max_margin_bottom=0, max_margin_top=0)
cart_icon = create_icon(icls_icons, 'c', 30, 30, min_margin_left=0, min_margin_right=10, min_margin_top=0, min_margin_bottom=0, max_margin_left=0, max_margin_right=10, max_margin_bottom=0, max_margin_top=0)
icls_icons.add_children([profile_icon, cart_icon])

sn_icons = create_sn_icons_list(header, is_right=True, min_margin_left=10, min_margin_right=10, min_margin_top=10, min_margin_bottom=10, max_margin_left=20, max_margin_right=20, max_margin_bottom=10, max_margin_top=10)
twitter_icon = create_icon(sn_icons, 't', 30, 30, min_margin_left=0, min_margin_right=10, min_margin_top=0, min_margin_bottom=0, max_margin_left=0, max_margin_right=10, max_margin_bottom=0, max_margin_top=0)
vk_icon = create_icon(sn_icons, 'v', 30, 30, min_margin_left=0, min_margin_right=10, min_margin_top=0, min_margin_bottom=0, max_margin_left=0, max_margin_right=10, max_margin_bottom=0, max_margin_top=0)
fb_icon = create_icon(sn_icons, 'f', 30, 30, min_margin_left=0, min_margin_right=10, min_margin_top=0, min_margin_bottom=0, max_margin_left=0, max_margin_right=10, max_margin_bottom=0, max_margin_top=0)
sn_icons.add_children([twitter_icon, vk_icon, fb_icon])

find_solutions(header, [logo, nav, search_div, icls_icons, sn_icons])

header_json = BaseElementJSON(
    "header",
    x=0,
    y=0,
    width=ValueJSON(100, Measure.PERCENT),
    height=ValueJSON(150, Measure.PIXEL),
    margin_left=ValueJSON(0, Measure.PERCENT),
    margin_right=ValueJSON(0, Measure.PERCENT),
    margin_top=ValueJSON(0, Measure.PERCENT),
    margin_bottom=ValueJSON(0, Measure.PERCENT),
    label=header.label,
    fullwidth=header.is_fullwidth,
    fullheight=header.is_fullheight,
    center_horizontal=True,
    center_vertical=True,
    justify_left=header.justify_left,
    justify_right=header.justify_right
)

logo_json = IconButtonJSON(
    parent=header_json,
    icon_name="profile",
    x=ValueJSON(header.models[0][0][logo.x].as_long() * header.table.cell_width * 100 / header.width, Measure.PERCENT),
    y=ValueJSON(header.models[0][0][logo.y].as_long() * header.table.cell_height * 100 / header.height,
                Measure.PERCENT),
    width=ValueJSON(header.models[0][0][logo.col_count].as_long() * header.table.cell_width * 100 / header.width,
                    Measure.PERCENT),
    height=ValueJSON(header.models[0][0][logo.row_count].as_long() * header.table.cell_height * 100 / header.height,
                     Measure.PERCENT),
    min_width=ValueJSON(logo.min_width, Measure.PIXEL),
    min_height=ValueJSON(logo.min_height, Measure.PIXEL),
    margin_left=ValueJSON(
        header.models[0][0][logo.margin_left].as_long() * header.table.cell_width, Measure.PIXEL),
    margin_right=ValueJSON(
        header.models[0][0][logo.margin_right].as_long() * header.table.cell_width, Measure.PIXEL),
    margin_top=ValueJSON(
        header.models[0][0][logo.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
    margin_bottom=ValueJSON(
        header.models[0][0][logo.margin_bottom].as_long() * header.table.cell_height, Measure.PIXEL),
    label=logo.label
)

nav_json = NavListJSON(
    nav_list=nav.links_list.links,
    parent=header_json,
    x=ValueJSON(header.models[0][0][nav.x].as_long() * header.table.cell_width * 100 / header.width, Measure.PERCENT),
    y=ValueJSON(header.models[0][0][nav.y].as_long() * header.table.cell_height * 100 / header.height, Measure.PERCENT),
    width=ValueJSON(header.models[0][0][nav.col_count].as_long() * header.table.cell_width * 100 / header.width,
                    Measure.PERCENT),
    height=ValueJSON(header.models[0][0][nav.row_count].as_long() * header.table.cell_height * 100 / header.height,
                     Measure.PERCENT),
    min_width=ValueJSON(nav.min_width, Measure.PIXEL),
    min_height=ValueJSON(nav.min_height, Measure.PIXEL),
    margin_left=ValueJSON(header.models[0][0][nav.margin_left].as_long() * header.table.cell_width,
                          Measure.PIXEL),
    margin_right=ValueJSON(
        header.models[0][0][nav.margin_right].as_long() * header.table.cell_width, Measure.PIXEL),
    margin_top=ValueJSON(header.models[0][0][nav.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
    margin_bottom=ValueJSON(
        header.models[0][0][nav.margin_bottom].as_long() * header.table.cell_height, Measure.PIXEL),
    label=nav.label,
    fullwidth=search_div.is_fullwidth,
    fullheight=search_div.is_fullheight,
    center_vertical=True,
    center_horizontal=True,
    flexgrow=1,
    flexflow="row nowrap"
)

search_bar_div_json = BaseElementJSON(
    parent=header_json,
    tag="div",
    x=ValueJSON(header.models[0][0][search_div.x].as_long() * header.table.cell_width * 100 / header.width,
                Measure.PERCENT),
    y=ValueJSON(header.models[0][0][search_div.y].as_long() * header.table.cell_height * 100 / header.height,
                Measure.PERCENT),
    width=ValueJSON(header.models[0][0][search_div.col_count].as_long() * header.table.cell_width * 100 / header.width,
                    Measure.PERCENT),
    height=ValueJSON(
        header.models[0][0][search_div.row_count].as_long() * header.table.cell_height * 100 / header.height,
        Measure.PERCENT),
    min_width=ValueJSON(search_div.min_width, Measure.PIXEL),
    min_height=ValueJSON(search_div.min_height, Measure.PIXEL),
    margin_left=ValueJSON(
        header.models[0][0][search_div.margin_left].as_long() * header.table.cell_width,Measure.PIXEL),
    margin_right=ValueJSON(
        header.models[0][0][search_div.margin_right].as_long() * header.table.cell_width,Measure.PIXEL),
    margin_top=ValueJSON(
        header.models[0][0][search_div.margin_top].as_long() * header.table.cell_height,Measure.PIXEL),
    margin_bottom=ValueJSON(
        header.models[0][0][search_div.margin_bottom].as_long() * header.table.cell_height, Measure.PIXEL),
    label=search_div.label,
    fullwidth=search_div.is_fullwidth,
    fullheight=search_div.is_fullheight,
    flexgrow=1,
)

search_bar_json = BaseElementJSON(
    parent=search_bar_div_json,
    tag="input",
    x=ValueJSON(search_div.models[0][0][search_div.children[0].x].as_long() * search_div.table.cell_width * 100 / search_div.get_width_with_parent(header.models[0][0]),
                Measure.PERCENT),
    y=ValueJSON(search_div.models[0][0][search_div.children[0].y].as_long() * search_div.table.cell_height * 100 / search_div.get_height_with_parent(header.models[0][0]),
                Measure.PERCENT),
    width=ValueJSON(search_div.models[0][0][search_div.children[0].col_count].as_long() * search_div.table.cell_width * 100 / search_div.get_width_with_parent(header.models[0][0]),
                    Measure.PERCENT),
    height=ValueJSON(
        search_div.models[0][0][search_div.children[0].row_count].as_long() * search_div.table.cell_height * 100 / search_div.get_height_with_parent(header.models[0][0]),
        Measure.PERCENT),
    margin_left=ValueJSON(
        search_div.models[0][0][search_div.children[0].margin_left].as_long() * search_div.table.cell_width, Measure.PIXEL),
    margin_right=ValueJSON(
        search_div.models[0][0][search_div.children[0].margin_right].as_long() * search_div.table.cell_width, Measure.PIXEL),
    margin_top=ValueJSON(
        search_div.models[0][0][search_div.children[0].margin_top].as_long() * search_div.table.cell_height, Measure.PIXEL),
    margin_bottom=ValueJSON(
        search_div.models[0][0][search_div.children[0].margin_bottom].as_long() * search_div.table.cell_height, Measure.PIXEL),
    label=search_div.children[0].label,
    text_align="left",
    fullwidth=search_div.children[0].is_fullwidth,
    fullheight=search_div.children[0].is_fullheight,
    flexgrow=1
)
search_bar_div_json.children.append(search_bar_json)

icls_icons_json = BaseElementJSON(
    "div",
    x=ValueJSON(header.models[0][0][icls_icons.x].as_long() * header.table.cell_width * 100 / header.width,
                Measure.PERCENT),
    y=ValueJSON(header.models[0][0][icls_icons.y].as_long() * header.table.cell_height * 100 / header.height,
                Measure.PERCENT),
    width=ValueJSON(header.models[0][0][icls_icons.col_count].as_long() * header.table.cell_width * 100 / header.width,
                    Measure.PERCENT),
    height=ValueJSON(
        header.models[0][0][icls_icons.row_count].as_long() * header.table.cell_height * 100 / header.height,
        Measure.PERCENT),
    min_width=ValueJSON(icls_icons.min_width, Measure.PIXEL),
    min_height=ValueJSON(icls_icons.min_height, Measure.PIXEL),
    margin_left=ValueJSON(
        header.models[0][0][icls_icons.margin_left].as_long()* header.table.cell_width, Measure.PIXEL),
    margin_right=ValueJSON(
        header.models[0][0][icls_icons.margin_right].as_long()* header.table.cell_width, Measure.PIXEL),
    margin_top=ValueJSON(
        header.models[0][0][icls_icons.margin_top].as_long()* header.table.cell_height, Measure.PIXEL),
    margin_bottom=ValueJSON(
        header.models[0][0][icls_icons.margin_bottom].as_long()* header.table.cell_height, Measure.PIXEL),
    label=icls_icons.label,
    parent=header_json,
    fullwidth=icls_icons.is_fullwidth,
    fullheight=icls_icons.is_fullheight,
    center_horizontal=icls_icons.center_horizontal,
    center_vertical=icls_icons.center_vertical,
    justify_left=icls_icons.justify_left,
    justify_right=icls_icons.justify_right,
    flexflow="row nowrap"
)

icls_model = icls_icons.models[0][0]
for i in range(len(icls_icons.children)):
    icon_name = ""
    if icls_icons.children[i].label == 'p':
        icon_name = 'profile'
    elif icls_icons.children[i].label == 'c':
        icon_name = 'cart'
    icls_icons_json.children.append(
        IconButtonJSON(
            icon_name=icon_name,
            x=ValueJSON(icls_model[icls_icons.children[
                i].x].as_long() * icls_icons.table.cell_width * 100 / icls_icons.get_width_with_parent(
                header.models[0][0]), Measure.PERCENT),
            y=ValueJSON(icls_model[icls_icons.children[
                i].y].as_long() * header.table.cell_height * 100 / icls_icons.get_height_with_parent(
                header.models[0][0]), Measure.PERCENT),
            width=ValueJSON(icls_model[icls_icons.children[
                i].col_count].as_long() * icls_icons.table.cell_width, Measure.PIXEL),
            height=ValueJSON(icls_model[icls_icons.children[
                i].row_count].as_long() * icls_icons.table.cell_height, Measure.PIXEL),
            min_width=ValueJSON(icls_model[icls_icons.children[
                i].col_count].as_long() * icls_icons.table.cell_width, Measure.PIXEL),
            min_height=ValueJSON(icls_model[icls_icons.children[
                i].row_count].as_long() * icls_icons.table.cell_height, Measure.PIXEL),
            font_size=ValueJSON(icls_icons.models[0][0][icls_icons.children[
                i].col_count].as_long() * icls_icons.table.cell_width, Measure.PIXEL),
            margin_left=ValueJSON(icls_model[icls_icons.children[
                i].margin_left].as_long() * icls_icons.table.cell_width, Measure.PIXEL),
            margin_right=ValueJSON(icls_model[icls_icons.children[
                i].margin_right].as_long() * icls_icons.table.cell_width, Measure.PIXEL),
            margin_top=ValueJSON(icls_model[icls_icons.children[
                i].margin_top].as_long() * icls_icons.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(icls_model[icls_icons.children[
                i].margin_bottom].as_long() * icls_icons.table.cell_height, Measure.PIXEL),
            parent=icls_icons_json,
            label=icls_icons.children[i].label
        )
    )

sn_icons_json = BaseElementJSON(
    "div",
    parent=header_json,
    x=ValueJSON(header.models[0][0][sn_icons.x].as_long() * header.table.cell_width * 100 / header.width,
                Measure.PERCENT),
    y=ValueJSON(header.models[0][0][sn_icons.y].as_long() * header.table.cell_height * 100 / header.height,
                Measure.PERCENT),
    width=ValueJSON(header.models[0][0][sn_icons.col_count].as_long() * header.table.cell_width * 100 / header.width, Measure.PERCENT),
    height=ValueJSON(header.models[0][0][sn_icons.row_count].as_long() * header.table.cell_height * 100 / header.height, Measure.PERCENT),
    min_width=ValueJSON(sn_icons.min_width, Measure.PIXEL),
    min_height=ValueJSON(sn_icons.min_height, Measure.PIXEL),
    margin_left=ValueJSON(
        header.models[0][0][sn_icons.margin_left].as_long()* header.table.cell_width, Measure.PIXEL),
    margin_right=ValueJSON(
        header.models[0][0][sn_icons.margin_right].as_long()* header.table.cell_width, Measure.PIXEL),
    margin_top=ValueJSON(
        header.models[0][0][sn_icons.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
    margin_bottom=ValueJSON(
        header.models[0][0][sn_icons.margin_bottom].as_long() * header.table.cell_height, Measure.PIXEL),
    label=sn_icons.label,
    fullwidth=sn_icons.is_fullwidth,
    fullheight=sn_icons.is_fullheight,
    center_horizontal=True,
    center_vertical=False,
    justify_left=sn_icons.justify_left,
    justify_right=sn_icons.justify_right,
    flexflow="row nowrap"
)

for i in range(len(sn_icons.children)):
    icon_name = ""
    if sn_icons.children[i].label == 'f':
        icon_name = 'facebook'
    elif sn_icons.children[i].label == 'v':
        icon_name = 'vk'
    elif sn_icons.children[i].label == 't':
        icon_name = 'twitter'
    sn_icons_json.children.append(
        IconButtonJSON(
            parent=sn_icons_json,
            icon_name=icon_name,
            x=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].x].as_long() * sn_icons.table.cell_width * 100 / sn_icons.get_width_with_parent(header.models[0][0]),
                        Measure.PERCENT),
            y=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].y].as_long() * sn_icons.table.cell_height * 100 / sn_icons.get_height_with_parent(header.models[0][0]),
                        Measure.PERCENT),
            width=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
            height=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].row_count].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
            min_width=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
            min_height=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].row_count].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
            font_size=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
            margin_left=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].margin_left].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
            margin_right=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].margin_right].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
            margin_top=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].margin_top].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(sn_icons.models[0][0][sn_icons.children[
                i].margin_bottom].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
            label=sn_icons.children[i].label
        )
    )

header_json.children.append(logo_json)
header_json.children.append(nav_json)
header_json.children.append(search_bar_div_json)
header_json.children.append(icls_icons_json)
header_json.children.append(sn_icons_json)

print(len(header_json.children))


def sort_children(parent):
    arr = sorted(parent.children, key=lambda child: child.x.val)
    print(arr)
    for i in range(len(arr)):
        if i - 1 >= 0 and arr[i].y.val > arr[i - 1].y.val and arr[i].x.val <= arr[i - 1].x.val + arr[i - 1].width.val:
            arr.append(arr.pop(i))
            i -= 1
        elif i + 1 < len(arr) and arr[i].y.val > arr[i + 1].y.val and arr[i].x.val + arr[i].width.val >= arr[i + 1].x.val:
            arr.append(arr.pop(i))
    print(arr)
    parent.children = arr


sort_children(header_json)


def generate_html(parent):
    styles = []
    generate_style(parent, styles)
    with tag('html'):
        with tag('head'):
            doc.stag("link", rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
            with tag('style'):
                doc.text("".join(styles))
        with tag('body'):
            generate_element_html(parent)
    res = doc.getvalue()
    return res


def generate_element_html(element):
    if element.tag == 'input':
        doc.stag(element.tag, ('type', 'text'), ('placeholder', 'Search'), ('class', element.label))
    else:
        class_exists = False
        with tag(element.tag):
            if element.text != "":
                doc.text(element.text)
            for attr in element.attrs:
                if attr[0] == 'class':
                    doc.attr((attr[0], attr[1] + " " + element.label))
                    class_exists = True
                else:
                    doc.attr(attr)
            if not class_exists:
                doc.attr(('class', element.label))
            if len(element.children) > 0:
                for child in element.children:
                    generate_element_html(child)


def generate_style(parent, styles):
    styles.append(
        f""".{parent.label} {{
        flex-grow: {parent.flexgrow};
        font-size: {parent.font_size.val}{parent.font_size.measure.value};
        flex-basis: {parent.width.val}{parent.width.measure.value};
             
        min-width:{parent.min_width.val}{parent.min_width.measure.value};
        min-height:{parent.min_height.val}{parent.min_height.measure.value};
        margin-right: {parent.margin_right.val}{parent.margin_right.measure.value};
        margin-left: {parent.margin_left.val}{parent.margin_left.measure.value};
        margin-top: {parent.margin_top.val}{parent.margin_top.measure.value};
        margin-bottom: {parent.margin_bottom.val}{parent.margin_bottom.measure.value};
        padding-left: {parent.padding_left.val}{parent.padding_left.measure.value};
        padding-right: {parent.padding_right.val}{parent.padding_right.measure.value};
        padding-top: {parent.padding_top.val}{parent.padding_top.measure.value};
        padding-bottom: {parent.padding_bottom.val}{parent.padding_bottom.measure.value};
        background: #{random.randint(100000, 999999)};
        text-align: {parent.text_align};
        """)
    if parent.tag == 'input':
        styles += "border: 0"
    if len(parent.children) > 0:
        if parent.center_vertical:
            styles += "align-items: center;\n"
        if parent.center_horizontal:
            styles += "justify-content: center;\n"
        styles.append(f"display: flex;\nflex-flow: {parent.flexflow};\n}}\n")
        for child in parent.children:
            generate_style(child, styles)
    else:
        styles.append("\n}\n")


with open('test.html', 'w') as f:
    f.write(generate_html(header_json))

print("***************")
print(icls_icons_json.width.val)
print(f"icls col count: {header.models[0][0][icls_icons.col_count].as_long()}")
print(f"header cell width: {header.table.cell_width}")
print(f"header width: {header.width}")