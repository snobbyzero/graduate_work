from layout_solver import *


def create_header_element(body, min_width, min_height, is_fullwidth, is_logo, nav_list: [], is_search, icls_icons_list: [], sn_icons_list: []):
    header = create_header(body, min_width=min_width, min_height=min_height, is_fullwidth=is_fullwidth)
    logo = None
    nav = None
    search_div = None
    icls_icons = None
    sn_icons = None

    div_header = None
    fullwidth = random.choice([True, False])
    if fullwidth:
        div_header = create_div(header, "div_header", "div_header", min_width=header.min_width, min_height=header.min_height, center_vertical=True)
    else:
        div_header = create_div(header, "div_header", "div_header", min_width=1000, min_height=header.min_height, center_vertical=True)

    header.add_child(div_header)
    header.div_header = div_header

    if is_logo:
        logo = create_child(
            div_header,
            "logo",
            "l",
            width=60,
            height=40,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10
        )
        div_header.add_child(logo)
        div_header.logo = logo

    if len(nav_list) > 0:
        links = [TextElement(nav_list[i], label='nav_a', min_width=100, min_height=10, min_margin_right=0, max_margin_right=20) for i in range(len(nav_list))]
        nav = create_text_list(
            div_header,
            "nav",
            "n",
            TextList(links),
            is_flexwidth=True,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10
        )
        div_header.add_child(nav)
        div_header.nav = nav

    if is_search:
        search_div = create_search_div(
            div_header,
            search_min_width=200,
            search_min_height=40,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10,
            is_flexwidth=True,
        )
        div_header.add_child(search_div)
        div_header.search_div = search_div


    if len(icls_icons_list) > 0:
        icls_icons = create_icons_list(
            div_header,
            "icls_icons",
            "icls_icons",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10
        )
        icons = []
        for icon in icls_icons_list:
            ic = create_icon(
                icls_icons,
                icon,
                icon_label='icls_icon',
                icon_width=25,
                icon_height=25,
                min_margin_left=0,
                min_margin_right=10,
                min_margin_top=0,
                min_margin_bottom=0,
                max_margin_left=0,
                max_margin_right=10,
                max_margin_bottom=0,
                max_margin_top=0
            )
            icons.append(ic)
        [icons[i].set_neighbours(right_elements=icons[i:], left_elements=icons[i:]) for i in range(len(icons))]
        icls_icons.add_children(icons)

        div_header.add_child(icls_icons)
        div_header.icls_icons = icls_icons

    if len(sn_icons_list) > 0:
        sn_icons = create_icons_list(
            div_header,
            "header_sn_icons",
            "header_sn_icons",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10
        )
        icons = []
        for icon in sn_icons_list:
            ic = create_icon(
                sn_icons,
                icon,
                icon_label='header_sn_icon',
                icon_width=25,
                icon_height=25,
                min_margin_left=0,
                min_margin_right=10,
                min_margin_top=0,
                min_margin_bottom=0,
                max_margin_left=0,
                max_margin_right=10,
                max_margin_bottom=0,
                max_margin_top=0
            )
            icons.append(ic)
        [icons[i].set_neighbours(right_elements=icons[i:], left_elements=icons[i:]) for i in range(len(icons))]
        sn_icons.add_children(icons)

        div_header.add_child(sn_icons)
        div_header.sn_icons = sn_icons

    logo.set_neighbours(
        right_elements=[nav, search_div, icls_icons, sn_icons],
        bottom_elements=[nav, search_div]
    )
    nav.set_neighbours(
        left_elements=[logo, search_div],
        top_elements=[search_div, icls_icons, sn_icons, logo],
        bottom_elements=[search_div],
        right_elements=[search_div, icls_icons, sn_icons])
    search_div.set_neighbours(
        left_elements=[logo, nav],
        top_elements=[nav, icls_icons, sn_icons, logo],
        bottom_elements=[nav],
        right_elements=[nav, icls_icons, sn_icons]
    )
    icls_icons.set_neighbours(
        left_elements=[logo, sn_icons, search_div, nav],
        top_elements=[search_div, nav],
        bottom_elements=[search_div, nav],
        right_elements=[sn_icons]
    )
    sn_icons.set_neighbours(
        right_elements=[icls_icons],
        left_elements=[logo, search_div, nav, icls_icons],
        top_elements=[search_div, nav],
        bottom_elements=[search_div, nav]
    )

    div_header.rules = [And(nav.y == logo.y, logo.y == search_div.y),
                    And(nav.y == logo.y, search_div.y >= nav.y + nav.row_count),
                    And(search_div.y == logo.y, nav.y >= search_div.y + search_div.row_count)]



    return header
