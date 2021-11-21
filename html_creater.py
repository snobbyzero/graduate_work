from yattag import Doc

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.IconButtonJSON import IconButtonJSON
from json_classes.Measure import Measure
from json_classes.NavListJSON import NavListJSON
from json_classes.SearchBarJSON import SearchBarJSON
from json_classes.ValueJSON import ValueJSON
from layout_solver import *

body = create_body(1900, 1000)

content = create_content(body, min_width=1000, min_height=1000, is_fullwidth=True)
cards = []
for i in range(10):
    card = create_card(content, i, 'sm')

    title = create_text('Title', card, label='title')
    description = create_text('Blablabla blablal blsdadlas dsadsa', card, 'description')

    icons = create_icons_list(card, 'card_icons', 'card_icons')
    add_to_wishlist_icon = create_icon(
        icons,
        "wishlist_icon",
        icon_label='w',
        icon_width=40,
        icon_height=40,
        min_margin_left=0,
        min_margin_right=10,
        min_margin_top=0,
        min_margin_bottom=0,
        max_margin_left=0,
        max_margin_right=10,
        max_margin_bottom=0,
        max_margin_top=0
    )

    compare_icon = create_icon(
        icons,
        "compare_icon",
        icon_label='c',
        icon_width=40,
        icon_height=40,
        min_margin_left=0,
        min_margin_right=10,
        min_margin_top=0,
        min_margin_bottom=0,
        max_margin_left=0,
        max_margin_right=10,
        max_margin_bottom=0,
        max_margin_top=0
    )
    add_to_wishlist_icon.set_neighbours(right_elements=[compare_icon], left_elements=[compare_icon])
    icons.add_children([add_to_wishlist_icon, compare_icon])

    add_to_cart_button = create_text("Add to cart", card, 'ab')

    additional_text = create_text_list(card, "additional_text", "at", TextList([TextElement("Price: 200$"), TextElement("In stock: yes")], is_vertical=True))

    rating = create_icon(
        card,
        "rating",
        "r",
        icon_width=40,
        icon_height=40,
        min_margin_left=0,
        min_margin_right=10,
        min_margin_top=0,
        min_margin_bottom=0,
        max_margin_left=0,
        max_margin_right=10,
        max_margin_bottom=0,
        max_margin_top=0
    )
    rating_text = create_text("4.5", card, "rt")

    reviews = create_icon(
        card,
        "reviews",
        "re",
        icon_width=40,
        icon_height=40,
        min_margin_left=0,
        min_margin_right=10,
        min_margin_top=0,
        min_margin_bottom=0,
        max_margin_left=0,
        max_margin_right=10,
        max_margin_bottom=0,
        max_margin_top=0
    )
    reviews_text = create_text("455 reviews", card, "rc")

    image = create_icon(
        card,
        "image",
        "im",
        icon_width=200,
        icon_height=300,
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=10,
        min_margin_bottom=10,
        max_margin_left=20,
        max_margin_right=20,
        max_margin_bottom=20,
        max_margin_top=20
    )

    if card.size == 'sm':
        image.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[title, description, icons, additional_text, add_to_cart_button, rating, rating_text, reviews, reviews_text])
        title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[description, icons, additional_text, add_to_cart_button, rating, rating_text, reviews, reviews_text])
        description.set_neighbours(right_elements=[], left_elements=[], top_elements=[additional_text, rating, rating_text, reviews, reviews_text], bottom_elements=[icons, additional_text, add_to_cart_button, rating, rating_text, reviews, reviews_text])
        icons.set_neighbours(right_elements=[add_to_cart_button], left_elements=[add_to_cart_button], top_elements=[add_to_cart_button], bottom_elements=[add_to_cart_button])
        additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[rating_text, rating, reviews_text, reviews], bottom_elements=[rating_text, rating, reviews_text, reviews])
        rating.set_neighbours(right_elements=[rating_text, reviews, reviews_text], left_elements=[reviews, reviews_text], top_elements=[reviews, reviews_text], bottom_elements=[rating_text, reviews, reviews_text])
        rating_text.set_neighbours(right_elements=[reviews, reviews_text], left_elements=[reviews, reviews_text], top_elements=[reviews, reviews_text], bottom_elements=[reviews, reviews_text])
    elif card.size == 'md':
        title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        description.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        icons.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        add_to_cart_button.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        rating.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        rating_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        reviews.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        reviews_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    else:
        title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        description.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        icons.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        add_to_cart_button.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        rating.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        rating_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        reviews.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        reviews_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])

    card.add_children([title, description, icons, add_to_cart_button, additional_text, rating, rating_text, reviews, reviews_text, image])
    card.set_min_size_by_children()
    #card.set_max_size_by_children()
    cards.append(card)

for i in range(len(cards)-1):
    cards[i].set_neighbours(right_elements=[cards[i+1:]], bottom_elements=[cards[i+1:]])
content.add_children(cards)

header = create_header(body, min_width=1000, min_height=150, is_fullwidth=True)
logo = create_child(
    header,
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
nav = create_text_list(
    header,
    "nav",
    "n",
    TextList([TextElement('Home', label='nav_a'), TextElement('About Us', label='nav_a'),
              TextElement('Contacts', label='nav_a'), TextElement('Profile', label='nav_a')]),
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
search_div = create_search_div(
    header,
    min_width=200,
    min_height=60,
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

icls_icons = create_icons_list(
    header,
    "icls_icons",
    "icls",
    min_margin_left=10,
    min_margin_right=10,
    min_margin_top=10,
    min_margin_bottom=10,
    max_margin_left=20,
    max_margin_right=20,
    max_margin_bottom=10,
    max_margin_top=10
)
profile_icon = create_icon(
    icls_icons,
    "profile_icon",
    icon_label='p',
    icon_width=40,
    icon_height=40,
    min_margin_left=0,
    min_margin_right=10,
    min_margin_top=0,
    min_margin_bottom=0,
    max_margin_left=0,
    max_margin_right=10,
    max_margin_bottom=0,
    max_margin_top=0
)
cart_icon = create_icon(
    icls_icons,
    "cart_icon",
    icon_label='c',
    icon_width=40,
    icon_height=40,
    min_margin_left=0,
    min_margin_right=10,
    min_margin_top=0,
    min_margin_bottom=0,
    max_margin_left=0,
    max_margin_right=10,
    max_margin_bottom=0,
    max_margin_top=0
)
profile_icon.set_neighbours(right_elements=[cart_icon], left_elements=[cart_icon])
icls_icons.add_children([profile_icon, cart_icon])

sn_icons = create_icons_list(
    header,
    "sn_icons",
    "sn_icons",
    min_margin_left=10,
    min_margin_right=10,
    min_margin_top=10,
    min_margin_bottom=10,
    max_margin_left=20,
    max_margin_right=20,
    max_margin_bottom=10,
    max_margin_top=10
)
twitter_icon = create_icon(
    sn_icons,
    "twitter_icon",
    icon_label='t',
    icon_width=40,
    icon_height=40,
    min_margin_left=0,
    min_margin_right=10,
    min_margin_top=0,
    min_margin_bottom=0,
    max_margin_left=0,
    max_margin_right=10,
    max_margin_bottom=0,
    max_margin_top=0
)
vk_icon = create_icon(
    sn_icons,
    "vk_icon",
    icon_label='v',
    icon_width=40,
    icon_height=40,
    min_margin_left=0,
    min_margin_right=10,
    min_margin_top=0,
    min_margin_bottom=0,
    max_margin_left=0,
    max_margin_right=10,
    max_margin_bottom=0,
    max_margin_top=0
)
fb_icon = create_icon(
    sn_icons,
    "fb_icon",
    icon_label='f',
    icon_width=40,
    icon_height=40,
    min_margin_left=0,
    min_margin_right=10,
    min_margin_top=0,
    min_margin_bottom=0,
    max_margin_left=0,
    max_margin_right=10,
    max_margin_bottom=0,
    max_margin_top=0
)
twitter_icon.set_neighbours(right_elements=[vk_icon, fb_icon], left_elements=[vk_icon, fb_icon])
vk_icon.set_neighbours(right_elements=[fb_icon], left_elements=[fb_icon])
sn_icons.add_children([twitter_icon, vk_icon, fb_icon])

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
header.add_children([logo, nav, search_div, icls_icons, sn_icons])
header.rules = [And(nav.y == logo.y, logo.y == search_div.y),
                And(nav.y == logo.y, search_div.y >= nav.y + nav.row_count),
                And(search_div.y == logo.y, nav.y >= search_div.y + search_div.row_count)]

print(cards[0].min_width)
print(cards[0].min_height)
cards[0].table = Table(10, 10, width=cards[0].min_width, height=cards[0].min_height)
body.add_children([header, content])
find_solutions(cards[0])  # TODO BODY
print(header)


def create_body(body_model):
    header_json = create_header(body_model, header.models[1].m)
    body_json = BaseElementJSON(
        "body",
        x=0,
        y=0,
        width=ValueJSON(100, Measure.PERCENT),
        height=ValueJSON(100, Measure.PERCENT),
        margin_left=ValueJSON(0, Measure.PERCENT),
        margin_right=ValueJSON(0, Measure.PERCENT),
        margin_top=ValueJSON(0, Measure.PERCENT),
        margin_bottom=ValueJSON(0, Measure.PERCENT),
        label=body.label,
        align_content="start",
        center_horizontal=True,
        center_vertical=True
    )
    body_json.children.append(header_json)

    return body_json


def create_content(body_model, content_model):
    content_json = BaseElementJSON(
        "content",
        x=ValueJSON(body_model[content.x].as_long() * body.table.cell_width * 100 / body.width, Measure.PERCENT),
        y=ValueJSON(body_model[content.y].as_long() * body.table.cell_width * 100 / body.height, Measure.PERCENT),
        width=ValueJSON(body_model[content.col_count].as_long() * body.table.cell_width * 100 / body.width,
                        Measure.PERCENT),
        height=ValueJSON(body_model[content.row_count].as_long() * body.table.cell_height * 100 / body.height,
                         Measure.PERCENT),
        min_width=ValueJSON(content.min_width, Measure.PIXEL),
        min_height=ValueJSON(content.min_height, Measure.PIXEL),
        margin_left=ValueJSON(body_model[content.margin_left] * body.table.cell_width, Measure.PIXEL),
        margin_right=ValueJSON(body_model[content.margin_right] * body.table.cell_width, Measure.PIXEL),
        margin_top=ValueJSON(body_model[content.margin_top] * body.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(body_model[content.margin_bottom] * body.table.cell_height, Measure.PIXEL),
        label=content.label,
        fullwidth=content.is_fullwidth,
        justify_left=content.justify_left,
        justify_right=content.justify_right,
        center_horizontal=True,
        center_vertical=True
    )

    return content_json


def create_header(body_model, header_model):
    header_json = BaseElementJSON(
        "header",
        x=ValueJSON(body_model[header.x].as_long() * body.table.cell_width * 100 / body.width, Measure.PERCENT),
        y=ValueJSON(body_model[header.y].as_long() * body.table.cell_width * 100 / body.height, Measure.PERCENT),
        width=ValueJSON(body_model[header.col_count].as_long() * body.table.cell_width * 100 / body.width,
                        Measure.PERCENT),
        height=ValueJSON(body_model[header.row_count].as_long() * body.table.cell_height * 100 / body.height,
                         Measure.PERCENT),
        min_width=ValueJSON(header.min_width, Measure.PIXEL),
        min_height=ValueJSON(header.min_height, Measure.PIXEL),
        margin_left=ValueJSON(body_model[header.margin_left] * body.table.cell_width, Measure.PIXEL),
        margin_right=ValueJSON(body_model[header.margin_right] * body.table.cell_width, Measure.PIXEL),
        margin_top=ValueJSON(body_model[header.margin_top] * body.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(body_model[header.margin_bottom] * body.table.cell_height, Measure.PIXEL),
        label=header.label,
        fullwidth=header.is_fullwidth,
        justify_left=header.justify_left,
        justify_right=header.justify_right,
        center_horizontal=True,
        center_vertical=True
    )

    if logo in header.children:
        logo_json = IconButtonJSON(
            parent=header_json,
            icon_name="adjust",
            x=ValueJSON(header_model[logo.x].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                body_model), Measure.PERCENT),
            y=ValueJSON(header_model[logo.y].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                body_model),
                        Measure.PERCENT),
            width=ValueJSON(header_model[logo.col_count].as_long() * header.table.cell_width, Measure.PIXEL),
            height=ValueJSON(header_model[logo.row_count].as_long() * header.table.cell_height, Measure.PIXEL),
            min_width=ValueJSON(logo.min_width, Measure.PIXEL),
            min_height=ValueJSON(logo.min_height, Measure.PIXEL),
            margin_left=ValueJSON(header_model[logo.margin_left].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_right=ValueJSON(header_model[logo.margin_right].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_top=ValueJSON(header_model[logo.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(header_model[logo.margin_bottom].as_long() * header.table.cell_height,
                                    Measure.PIXEL),
            label=logo.label,
            font_size=ValueJSON(header_model[logo.col_count].as_long() * header.table.cell_width, Measure.PIXEL),
        )
        header_json.children.append(logo_json)

    if nav in header.children:
        nav_json = NavListJSON(
            nav_list=nav.text_list.text_list,
            parent=header_json,
            x=ValueJSON(header_model[nav.x].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                body_model), Measure.PERCENT),
            y=ValueJSON(header_model[nav.y].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                body_model), Measure.PERCENT),
            width=ValueJSON(
                header_model[nav.col_count].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                    body_model),
                Measure.PERCENT),
            height=ValueJSON(
                header_model[nav.row_count].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                    body_model),
                Measure.PERCENT),
            min_width=ValueJSON(nav.min_width, Measure.PIXEL),
            min_height=ValueJSON(nav.min_height, Measure.PIXEL),
            margin_left=ValueJSON(header_model[nav.margin_left].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_right=ValueJSON(header_model[nav.margin_right].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_top=ValueJSON(header_model[nav.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(header_model[nav.margin_bottom].as_long() * header.table.cell_height,
                                    Measure.PIXEL),
            label=nav.label,
            fullwidth=search_div.is_fullwidth,
            fullheight=search_div.is_fullheight,
            center_vertical=True,
            center_horizontal=True,
            flexgrow=nav.is_flexwidth,
            flexflow="row nowrap"
        )
        header_json.children.append(nav_json)

    if search_div in header.children:
        search_div_model = random_choose_model(search_div, header_model)
        search_justify = random.choice(["start", "end"])
        search_bar_div_json = BaseElementJSON(
            parent=header_json,
            tag="div",
            x=ValueJSON(
                header_model[search_div.x].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                    body_model),
                Measure.PERCENT),
            y=ValueJSON(
                header_model[search_div.y].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                    body_model),
                Measure.PERCENT),
            width=ValueJSON(header_model[
                                search_div.col_count].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                body_model),
                            Measure.PERCENT),
            height=ValueJSON(header_model[
                                 search_div.row_count].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                body_model), Measure.PERCENT),
            min_width=ValueJSON(search_div.min_width, Measure.PIXEL),
            min_height=ValueJSON(search_div.min_height, Measure.PIXEL),
            margin_left=ValueJSON(header_model[search_div.margin_left].as_long() * header.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(header_model[search_div.margin_right].as_long() * header.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(header_model[search_div.margin_top].as_long() * header.table.cell_height,
                                 Measure.PIXEL),
            margin_bottom=ValueJSON(header_model[search_div.margin_bottom].as_long() * header.table.cell_height,
                                    Measure.PIXEL),
            label=search_div.label,
            fullwidth=search_div.is_fullwidth,
            fullheight=search_div.is_fullheight,
            flexgrow=search_div.is_flexwidth,
            justify_left=search_justify == "start",
            justify_right=search_justify == "end"
        )

        search_bar_json = BaseElementJSON(
            parent=search_bar_div_json,
            tag="input",
            x=ValueJSON(search_div_model[search_div.children[
                0].x].as_long() * search_div.table.cell_width * 100 / search_div.get_width_with_parent(header_model),
                        Measure.PERCENT),
            y=ValueJSON(search_div_model[search_div.children[
                0].y].as_long() * search_div.table.cell_height * 100 / search_div.get_height_with_parent(header_model),
                        Measure.PERCENT),
            width=ValueJSON(search_div_model[search_div.children[0].col_count].as_long() * search_div.table.cell_width,
                            Measure.PIXEL),
            height=ValueJSON(
                search_div_model[search_div.children[0].row_count].as_long() * search_div.table.cell_height,
                Measure.PIXEL),
            min_width=ValueJSON(search_div.children[0].min_width, Measure.PIXEL),
            min_height=ValueJSON(search_div.children[0].min_height, Measure.PIXEL),
            margin_left=ValueJSON(
                search_div_model[search_div.children[0].margin_left].as_long() * search_div.table.cell_width,
                Measure.PIXEL),
            margin_right=ValueJSON(
                search_div_model[search_div.children[0].margin_right].as_long() * search_div.table.cell_width,
                Measure.PIXEL),
            margin_top=ValueJSON(
                search_div_model[search_div.children[0].margin_top].as_long() * search_div.table.cell_height,
                Measure.PIXEL),
            margin_bottom=ValueJSON(
                search_div_model[search_div.children[0].margin_bottom].as_long() * search_div.table.cell_height,
                Measure.PIXEL),
            label=search_div.children[0].label,
            text_align="left",
            fullwidth=search_div.children[0].is_fullwidth,
            fullheight=search_div.children[0].is_fullheight,
        )
        search_bar_div_json.children.append(search_bar_json)
        header_json.children.append(search_bar_div_json)

    if icls_icons in header.children:
        icls_icons_model = random_choose_model(icls_icons, header_model)
        icls_icons_justify = random.choice(["center", "start", "end"])
        icls_icons_json = BaseElementJSON(
            "div",
            x=ValueJSON(
                header_model[icls_icons.x].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                    body_model),
                Measure.PERCENT),
            y=ValueJSON(
                header_model[icls_icons.y].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                    body_model),
                Measure.PERCENT),
            width=ValueJSON(header_model[
                                icls_icons.col_count].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                body_model),
                            Measure.PERCENT),
            height=ValueJSON(
                header_model[
                    icls_icons.row_count].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                    body_model),
                Measure.PERCENT),
            min_width=ValueJSON(icls_icons.min_width, Measure.PIXEL),
            min_height=ValueJSON(icls_icons.min_height, Measure.PIXEL),
            margin_left=ValueJSON(
                header_model[icls_icons.margin_left].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_right=ValueJSON(
                header_model[icls_icons.margin_right].as_long() * header.table.cell_width, Measure.PIXEL),
            margin_top=ValueJSON(
                header_model[icls_icons.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(
                header_model[icls_icons.margin_bottom].as_long() * header.table.cell_height, Measure.PIXEL),
            label=icls_icons.label,
            parent=header_json,
            fullwidth=icls_icons.is_fullwidth,
            fullheight=icls_icons.is_fullheight,
            center_horizontal=icls_icons_justify == "center",
            center_vertical=False,
            justify_left=icls_icons_justify == "start",
            justify_right=icls_icons_justify == "end",
            flexflow="row nowrap"
        )

        for i in range(len(icls_icons.children)):
            icon_name = ""
            if icls_icons.children[i].label == 'p':
                icon_name = 'profile'
            elif icls_icons.children[i].label == 'c':
                icon_name = 'cart'
            icls_icons_json.children.append(
                IconButtonJSON(
                    icon_name=icon_name,
                    x=ValueJSON(icls_icons_model[icls_icons.children[
                        i].x].as_long() * icls_icons.table.cell_width * 100 / icls_icons.get_width_with_parent(
                        header_model), Measure.PERCENT),
                    y=ValueJSON(icls_icons_model[icls_icons.children[
                        i].y].as_long() * header.table.cell_height * 100 / icls_icons.get_height_with_parent(
                        header_model), Measure.PERCENT),
                    width=ValueJSON(
                        icls_icons_model[icls_icons.children[i].col_count].as_long() * icls_icons.table.cell_width,
                        Measure.PIXEL),
                    height=ValueJSON(
                        icls_icons_model[icls_icons.children[i].row_count].as_long() * icls_icons.table.cell_height,
                        Measure.PIXEL),
                    min_width=ValueJSON(
                        icls_icons_model[icls_icons.children[i].col_count].as_long() * icls_icons.table.cell_width,
                        Measure.PIXEL),
                    min_height=ValueJSON(
                        icls_icons_model[icls_icons.children[i].row_count].as_long() * icls_icons.table.cell_height,
                        Measure.PIXEL),
                    font_size=ValueJSON(
                        icls_icons_model[icls_icons.children[i].col_count].as_long() * icls_icons.table.cell_width,
                        Measure.PIXEL),
                    margin_left=ValueJSON(
                        icls_icons_model[icls_icons.children[i].margin_left].as_long() * icls_icons.table.cell_width,
                        Measure.PIXEL),
                    margin_right=ValueJSON(
                        icls_icons_model[icls_icons.children[i].margin_right].as_long() * icls_icons.table.cell_width,
                        Measure.PIXEL),
                    margin_top=ValueJSON(
                        icls_icons_model[icls_icons.children[i].margin_top].as_long() * icls_icons.table.cell_height,
                        Measure.PIXEL),
                    margin_bottom=ValueJSON(
                        icls_icons_model[icls_icons.children[i].margin_bottom].as_long() * icls_icons.table.cell_height,
                        Measure.PIXEL),
                    parent=icls_icons_json,
                    label=icls_icons.children[i].label
                )
            )
        sort_children(icls_icons_json)
        header_json.children.append(icls_icons_json)

    if sn_icons in header.children:
        sn_icons_model = random_choose_model(sn_icons, header_model)
        sn_icons_justify = random.choice(["center", "start", "end"])
        sn_icons_json = BaseElementJSON(
            "div",
            parent=header_json,
            x=ValueJSON(
                header_model[sn_icons.x].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                    body_model),
                Measure.PERCENT),
            y=ValueJSON(
                header_model[sn_icons.y].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                    body_model),
                Measure.PERCENT),
            width=ValueJSON(header_model[
                                sn_icons.col_count].as_long() * header.table.cell_width * 100 / header.get_width_with_parent(
                body_model), Measure.PERCENT),
            height=ValueJSON(header_model[
                                 sn_icons.row_count].as_long() * header.table.cell_height * 100 / header.get_height_with_parent(
                body_model), Measure.PERCENT),
            min_width=ValueJSON(sn_icons.min_width, Measure.PIXEL),
            min_height=ValueJSON(sn_icons.min_height, Measure.PIXEL),
            margin_left=ValueJSON(header_model[sn_icons.margin_left].as_long() * header.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(header_model[sn_icons.margin_right].as_long() * header.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(header_model[sn_icons.margin_top].as_long() * header.table.cell_height, Measure.PIXEL),
            margin_bottom=ValueJSON(header_model[sn_icons.margin_bottom].as_long() * header.table.cell_height,
                                    Measure.PIXEL),
            label=sn_icons.label,
            fullwidth=sn_icons.is_fullwidth,
            fullheight=sn_icons.is_fullheight,
            center_horizontal=sn_icons_justify == "center",
            center_vertical=False,
            justify_left=sn_icons_justify == "start",
            justify_right=sn_icons_justify == "end",
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
                    x=ValueJSON(sn_icons_model[sn_icons.children[
                        i].x].as_long() * sn_icons.table.cell_width * 100 / sn_icons.get_width_with_parent(
                        header_model),
                                Measure.PERCENT),
                    y=ValueJSON(sn_icons_model[sn_icons.children[
                        i].y].as_long() * sn_icons.table.cell_height * 100 / sn_icons.get_height_with_parent(
                        header_model),
                                Measure.PERCENT),
                    width=ValueJSON(sn_icons_model[sn_icons.children[
                        i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
                    height=ValueJSON(sn_icons_model[sn_icons.children[
                        i].row_count].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
                    min_width=ValueJSON(sn_icons_model[sn_icons.children[
                        i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
                    min_height=ValueJSON(sn_icons_model[sn_icons.children[
                        i].row_count].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
                    font_size=ValueJSON(sn_icons_model[sn_icons.children[
                        i].col_count].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
                    margin_left=ValueJSON(sn_icons_model[sn_icons.children[
                        i].margin_left].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
                    margin_right=ValueJSON(sn_icons_model[sn_icons.children[
                        i].margin_right].as_long() * sn_icons.table.cell_width, Measure.PIXEL),
                    margin_top=ValueJSON(sn_icons_model[sn_icons.children[
                        i].margin_top].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
                    margin_bottom=ValueJSON(sn_icons_model[sn_icons.children[
                        i].margin_bottom].as_long() * sn_icons.table.cell_height, Measure.PIXEL),
                    label=sn_icons.children[i].label
                )
            )
        sort_children(sn_icons_json)
        header_json.children.append(sn_icons_json)

    sort_children(header_json)
    return header_json


def sort_children(parent):
    arr = sorted(parent.children, key=lambda child: child.x.val)
    for i in range(len(arr)):
        if i - 1 >= 0 and arr[i].y.val > arr[i - 1].y.val and arr[i].x.val <= arr[i - 1].x.val + arr[i - 1].width.val:
            arr.append(arr.pop(i))
            i -= 1
        elif i + 1 < len(arr) and arr[i].y.val > arr[i + 1].y.val and arr[i].x.val + arr[i].width.val >= arr[
            i + 1].x.val:
            arr.append(arr.pop(i))
    parent.children = arr


def random_choose_model(child, parent_model):
    models = []
    print(child.label)
    print(child.models)
    for model in child.models:
        if model.parent.m == parent_model:
            models.append(model)
    return random.choice(models).m


def generate_html(parent):
    doc, tag, text = Doc().tagtext()
    styles = []
    generate_style(parent, styles)
    with tag('html'):
        with tag('head'):
            doc.stag("link", rel="stylesheet",
                     href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
            with tag('style'):
                doc.text("".join(styles))
        with tag('body'):
            generate_element_html(parent, doc, tag)
    res = doc.getvalue()
    return res


def generate_element_html(element, doc, tag):
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
                    generate_element_html(child, doc, tag)


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
        elif parent.justify_left:
            styles += "justify-content: start;\n"
        elif parent.justify_right:
            styles += "justify-content: end;\n"
        styles.append(f"display: flex;\nalign-content: {parent.align_content};\nflex-flow: {parent.flexflow};\n}}")
        for child in parent.children:
            generate_style(child, styles)
    else:
        styles.append("\n}\n")


for i in range(len(header.models)):
    with open(f'{i}_test.html', 'w') as f:
        f.write(generate_html(create_body(body.models[0].m)))
        f.close()
