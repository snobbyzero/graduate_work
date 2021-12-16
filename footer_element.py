from layout_solver import *

# vert_lists = [(title, [subtitle, subtitle]), (title, []), ...]
# links = [link, link, link]
# subscribe_form = "Subscribe now"
def create_footer_element(body, min_width, min_height, is_fullwidth, is_logo, vert_lists: [], links: [], sn_icons_list: [], copyright_text, subscribe_form):
    footer = create_footer(body, min_width=min_width, min_height=min_height, is_fullwidth=is_fullwidth)

    div_footer = None
    fullwidth = random.choice([False, False])
    if fullwidth:
        div_footer = create_div(footer, "div_footer", "div_footer", min_width=footer.min_width, min_height=footer.min_height, is_flexheight=True, is_fullwidth=True)
    else:
        div_footer = create_div(footer, "div_footer", "div_footer", min_width=1000, min_height=footer.min_height, is_flexheight=True)

    div_footer.logo = None
    div_footer.vert_lists = None
    div_footer.links = None
    div_footer.copyright_text = None
    div_footer.sn_icons = None
    div_footer.subscribe_form = None

    footer.add_child(div_footer)
    footer.div_footer = div_footer

    if is_logo:
        logo = create_child(
            div_footer,
            "footer_logo",
            "fl",
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
        div_footer.add_child(logo)
        div_footer.logo = logo

    if len(links) > 0:
        links_text = [TextElement(links[i], label='footer_link_a', min_width=50, min_height=10) for i in range(len(links))]
        nav = create_text_list(
            div_footer,
            "footer_links",
            "fn",
            TextList(links_text),
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
        div_footer.add_child(nav)
        div_footer.links = nav

    if len(vert_lists) > 0:
        vert_lists_div = create_div(
            div_footer,
            "vert_lists_div",
            "vlds",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=10,
            max_margin_top=10,
            is_flexwidth=True,
            center_horizontal=True
        )
        arr = []
        for i in range(len(vert_lists)):
            vert_list = create_div(
                vert_lists_div,
                f"vert_list_div_{i}",
                "vld",
                min_margin_left=10,
                min_margin_right=10,
                min_margin_top=0,
                min_margin_bottom=10,
                max_margin_left=20,
                max_margin_right=20,
                max_margin_bottom=10,
                max_margin_top=0,
                center_vertical=True,
                center_horizontal=True,
            )
            title = create_text(
                vert_lists[i][0],
                vert_list,
                "vld_title",
                min_width=100,
                min_height=20,
                is_flexwidth=True,
                min_margin_bottom=10,
                max_margin_bottom=20
            )
            links_text = [TextElement(vert_lists[i][1][j], label='footer_vert_list_a', min_width=100, min_height=10) for j in range(len(vert_lists[i][1]))]
            list = create_text_list(
                vert_list,
                "vert_list",
                "vl",
                TextList(links_text, is_vertical=True)
            )
            vert_list.add_children([title, list])
            vert_list.title = title
            vert_list.list = list
            vert_list.min_width = max(title.min_width + title.min_margin_right + title.min_margin_left, list.min_width + list.min_margin_left, list.min_margin_right)
            vert_list.min_height = sum(ch.min_height + ch.min_margin_bottom + ch.min_margin_top for ch in [title, list])
            title.set_neighbours(bottom_elements=[list])
            arr.append(vert_list)
        vert_lists_div.add_children(arr)
        #vert_lists_div.min_width = sum(vert_list.min_width + vert_list.min_margin_right + vert_list.min_margin_left for vert_list in arr)
        vert_lists_div.min_width = 400
        #vert_lists_div.min_height = max(vert_list.min_height + vert_list.min_margin_bottom + vert_list.min_margin_top for vert_list in arr)
        vert_lists_div.min_height = 300
        [arr[i].set_neighbours(right_elements=arr[i:], left_elements=arr[i:]) for i in range(len(arr))]


        div_footer.add_child(vert_lists_div)
        div_footer.vert_lists = vert_lists_div

    if len(sn_icons_list) > 0:
        sn_icons = create_icons_list(
            div_footer,
            "footer_sn_icons",
            "footer_sn_icons",
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
                icon_label='footer_sn_icon',
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

        div_footer.add_child(sn_icons)
        div_footer.sn_icons = sn_icons



    if div_footer.vert_lists:
        div_footer.vert_lists.set_neighbours(bottom_elements=[div_footer.links, div_footer.sn_icons], right_elements=[div_footer.sn_icons], left_elements=[div_footer.sn_icons])
    if div_footer.logo:
        div_footer.logo.set_neighbours(bottom_elements=[div_footer.links, div_footer.vert_lists, div_footer.sn_icons], right_elements=[div_footer.vert_lists], left_elements=[div_footer.vert_lists])
    if div_footer.sn_icons:
        div_footer.sn_icons.set_neighbours(bottom_elements=[div_footer.links], right_elements=[div_footer.links])
    div_footer.rules = []

    return footer
