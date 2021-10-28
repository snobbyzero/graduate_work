from yattag import Doc

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.IconButtonJSON import IconButtonJSON
from json_classes.Measure import Measure
from json_classes.SearchBarJSON import SearchBarJSON
from json_classes.ValueJSON import ValueJSON
from layout_solver import *

doc, tag, text = Doc().tagtext()

header = create_header(width=1500, height=150, is_fullwidth=False)
logo = create_logo(header, is_left=True, width=40, height=40)
nav = create_nav(header, LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.0, word_height=20), is_flexwidth=True)
search = create_search(header, min_width=200, min_height=30, is_flexwidth=True)
icls_icons = create_icls_icons_list(header, ['c', 'p'], is_right=True, icon_width=30, icon_height=30)
sn_icons = create_sn_icons_list(header, ['t', 'v', 'f'], is_right=True, icon_width=30, icon_height=30)

m_arr_header, res_arr_header = find_solutions(header, [logo, nav, search, icls_icons, sn_icons],
                                              [search.y])
m_arr_icls_icons, res_arr_icls_icons = None, None
m_arr_sn_icons, res_arr_sn_icons = None, None
for m in m_arr_header:
    icls_table = Table(10, 10, width=icls_icons.get_width_with_parent(m), height=icls_icons.get_height_with_parent(m))
    icls_icons.table = icls_table
    m_arr_icls_icons, res_arr_icls_icons = solve(icls_icons, [profile_x])

    sn_table = Table(10, 10, width=sn_icons.get_width_with_parent(m), height=sn_icons.get_height_with_parent(m))
    sn_icons.table = sn_table
    m_arr_sn_icons, res_arr_sn_icons = solve(sn_icons, [twitter_x])

m_header = m_arr_header[0]
header_json = BaseElementJSON(
    "header",
    x=ValueJSON(0, Measure.PERCENT),
    y=ValueJSON(0, Measure.PERCENT),
    width=ValueJSON(header.table.col_count * header.table.cell_width, Measure.PERCENT),
    height=ValueJSON(header.table.row_count * header.table.cell_height, Measure.PERCENT),
    fullwidth=header.is_fullwidth,
    fullheight=header.is_fullheight,
    center_horizontal=header.center_horizontal,
    center_vertical=header.center_vertical,
    justify_left=header.justify_left,
    justify_right=header.justify_right
)

logo_json = IconButtonJSON(
    parent=header_json,
    icon_name="profile",
    x=ValueJSON(m_header[logo.x] * header.table.cell_width, Measure.PERCENT),
    y=ValueJSON(m_header[logo.y] * header.table.cell_height, Measure.PERCENT),
    width=ValueJSON(m_header[logo.col_count] * header.table.cell_width, Measure.PERCENT),
    height=ValueJSON(m_header[logo.row_count] * header.table.cell_height, Measure.PERCENT),
)

search_bar_json = SearchBarJSON(
    parent=header_json,
    x=ValueJSON(m_header[search.x] * header.table.cell_width, Measure.PERCENT),
    y=ValueJSON(m_header[search.y] * header.table.cell_height, Measure.PERCENT),
    width=ValueJSON(m_header[search.col_count] * header.table.cell_width, Measure.PERCENT),
    height=ValueJSON(m_header[search.row_count] * header.table.cell_height, Measure.PERCENT),
    fullwidth=search.is_fullwidth,
    fullheight=search.is_fullheight,
    flexgrow=1,
)

m_icls_icons = m_arr_icls_icons[0]
icls_icons_json = BaseElementJSON(
    "div",
    parent=header_json,
    x=ValueJSON(m_header[icls_icons.x] * header.table.cell_width, Measure.PERCENT),
    y=ValueJSON(m_header[icls_icons.y] * header.table.cell_height, Measure.PERCENT),
    width=ValueJSON(m_header[icls_icons.col_count] * header.table.cell_width, Measure.PERCENT),
    height=ValueJSON(m_header[icls_icons.row_count] * header.table.cell_height, Measure.PERCENT),
    fullwidth=icls_icons.is_fullwidth,
    fullheight=icls_icons.is_fullheight,
    center_horizontal=icls_icons.center_horizontal,
    center_vertical=icls_icons.center_vertical,
    justify_left=icls_icons.justify_left,
    justify_right=icls_icons.justify_right,
)

for i in range(len(icls_icons.children)):
    icon_name = ""
    if icls_icons.children[i].label == 'p':
        icon_name = 'profile'
    elif icls_icons.children[i].label == 'c':
        icon_name = 'cart'
    icls_icons_json.children.append(
        IconButtonJSON(
            parent=icls_icons_json,
            icon_name=icon_name,
            x=ValueJSON(m_icls_icons[icls_icons.children[i].x] * header.table.cell_width, Measure.PERCENT),
            y=ValueJSON(m_icls_icons[icls_icons.children[i].y] * header.table.cell_height, Measure.PERCENT),
            width=ValueJSON(m_icls_icons[icls_icons.children[i].col_count] * header.table.cell_width, Measure.PERCENT),
            height=ValueJSON(m_icls_icons[icls_icons.children[i].row_count] * header.table.cell_height, Measure.PERCENT),
        )
    )

m_sn_icons = m_arr_sn_icons[0]
sn_icons_json = BaseElementJSON(
    "div",
    parent=header_json,
    x=ValueJSON(m_header[sn_icons.x] * header.table.cell_width, Measure.PERCENT),
    y=ValueJSON(m_header[sn_icons.y] * header.table.cell_height, Measure.PERCENT),
    width=ValueJSON(m_header[sn_icons.col_count] * header.table.cell_width, Measure.PERCENT),
    height=ValueJSON(m_header[sn_icons.row_count] * header.table.cell_height, Measure.PERCENT),
    fullwidth=sn_icons.is_fullwidth,
    fullheight=sn_icons.is_fullheight,
    center_horizontal=sn_icons.center_horizontal,
    center_vertical=sn_icons.center_vertical,
    justify_left=sn_icons.justify_left,
    justify_right=sn_icons.justify_right,
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
            x=ValueJSON(m_sn_icons[sn_icons.children[i].x] * header.table.cell_width, Measure.PERCENT),
            y=ValueJSON(m_sn_icons[sn_icons.children[i].y] * header.table.cell_height, Measure.PERCENT),
            width=ValueJSON(m_sn_icons[sn_icons.children[i].col_count] * header.table.cell_width, Measure.PERCENT),
            height=ValueJSON(m_sn_icons[sn_icons.children[i].row_count] * header.table.cell_height, Measure.PERCENT),
        )
    )

header_json.children.append(logo_json)
header_json.children.append(search_bar_json)
header_json.children.append(icls_icons_json)
header_json.children.append(sn_icons_json)

print(len(header_json.children))


def generate_html(arr, elements, m_header, m_icls_icons=None, m_sn_icons=None):
    with tag('html'):
        with tag('body'):
            with tag('p'):
                text('test text')

    res = doc.getvalue()
    return res


print(generate_html())
