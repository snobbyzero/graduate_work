from yattag import Doc
from layout_solver import *


doc, tag, text = Doc().tagtext()

header = create_header(width=1900, height=200, is_fullwidth=False)
logo = create_logo(header, is_left=True)
nav = create_nav(header, LinksLists(['Home', 'About Us', 'Contacts', 'Profile'], font_size_factor=1.5, word_height=50), is_flexwidth=True)
search = create_search(header, min_width=200, min_height=100, is_flexwidth=True)
icls_icons = create_icls_icons_list(header, ['c', 'p'], is_right=True)
sn_icons = create_sn_icons_list(header, ['t', 'v', 'f'], is_right=True)

m_arr_header, res_arr_header = find_solutions_header(header, [logo, nav, search, icls_icons, sn_icons], [nav.y, nav.row_count])
m_arr_icls_icons, res_arr_icls_icons = None, None
m_arr_sn_icons, res_arr_sn_icons = None, None
for m in m_arr_header:
    icls_table = Table(10, 10, width=icls_icons.get_width_with_parent(m), height=icls_icons.get_height_with_parent(m))
    icls_icons.table = icls_table
    solve(icls_icons, [profile_x])

    sn_table = Table(10, 10, width=sn_icons.get_width_with_parent(m), height=sn_icons.get_height_with_parent(m))
    sn_icons.table = sn_table
    solve(sn_icons, [twitter_x])


def generate_html(m_arr, res_arr, elements):
    with tag('html'):
        with tag('body'):
            with tag('p'):
                text('test text')

    res = doc.getvalue()
    return res

print(generate_html([]))
