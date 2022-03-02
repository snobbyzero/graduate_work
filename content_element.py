import random

from layout_solver import *
import copy

# card_inf = [
# {
#         "title": " ".join(faker.words(random.randint(1,3))),
#         "description": faker.text(max_nb_chars=200),
#         "image": faker.image_url(rand * 100, rand * 100),
#         "carousel_images": [faker.image_url(rand * 100, rand * 100), faker.image_url(rand * 100, rand * 100), ...]
# }
# ]
# card_image = "example.com/image.png"
# card_carousel_images ["example.com/image.png", "example.com/image.png", ...]
# card_icons_list = ["add_to_wishlist", "compare"]
# card_text_chips = [("color", ["red", "blue", "pink"]), ...]
# card_icon_chips = [("memory", ["128 GB", "256 GB"]), ...]
# card_buttons = ["Add to Cart", "Buy Fast"]
# card_title_subtitle = [("title", "subtitle")]
# card_key_value = [("name", "Xiaomi")]
# card_icons_texts = [("icon", "text"), ...]
# sidebar = {
#   is_nav: True,
#   nav: [(icon, name), (icon, name)]
#   filters: [(type, name, [name, name, name])]
#   sn_icons: ['vk', 'twitter', 'github']
# }

def create_content_element(body, min_width, min_height, is_fullwidth, card_size, cards_inf, card_icons_list: [],
                           card_buttons: [], card_key_value: [], card_icons_texts: [], sidebar, top):
    content = create_content(body, min_width=min_width, min_height=min_height, is_fullwidth=is_fullwidth)
    cards_el = create_div(
        content,
        "cards",
        "cards",
        is_flexwidth=True,
        is_flexheight=True,
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=10,
        min_margin_bottom=10,
        max_margin_left=10,
        max_margin_right=10,
        max_margin_top=10,
        max_margin_bottom=10,
    )
    cards = []
    for i in range(len(cards_inf)):
        card = create_card_element(cards_el, i, card_size, cards_inf[i]["title"], cards_inf[i]["description"],
                           cards_inf[i]["image"], cards_inf[i]["avatar"], card_icons_list, card_buttons, cards_inf[i]["titles_subtitles"],
                           card_key_value, card_icons_texts)
        cards.append(card)

    for i in range(len(cards) - 1):
        cards[i].set_neighbours(right_elements=cards[i + 1:], bottom_elements=cards[i + 1:])

    cards_el.add_children(cards)

    content.cards = cards_el
    content.add_child(cards_el)

    sidebar = create_sidebar(content, sidebar)

    content.sidebar = sidebar
    content.add_child(sidebar)

    return content


def create_sidebar(parent, sidebar):
    sidebar_div = create_div(
        parent,
        "sidebar",
        "sidebar",
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=0,
        min_margin_bottom=10,
        max_margin_left=20,
        max_margin_right=20,
        max_margin_top=20,
        max_margin_bottom=20,
        min_width=400,
        is_flexheight=True,
        center_vertical=True
    )
    #TODO
    if sidebar['is_nav']:
        nav_div = create_div(sidebar_div, 'sidebar_nav_div', 'sidebar_nav_div', is_flexheight=True, min_width=300, min_height=1000)
        for el in sidebar['nav']:
            link = create_div(nav_div, 'sidebar_nav_link', 'sidebar_nav_link', min_width=250, min_height=40, min_margin_right=10, min_margin_left=10,min_margin_bottom=10,min_margin_top=10, center_vertical=True)
            icon = create_icon(link, el[0], 'sidebar_nav_icon', min_margin_right=5, min_margin_left=5)
            text = create_text(el[1], link, 'sidebar_nav_text', min_width=100, min_height=30)
            link.add_children([icon, text])
            link.text = text
            link.icon = icon
            icon.set_neighbours(right_elements=[text], left_elements=[text])
            nav_div.add_child(link)

        sidebar_div.add_child(nav_div)
        sidebar_div.nav_div = nav_div

        if len(sidebar['sn_icons']) > 0:
            sn_icons = create_icons_list(
                sidebar_div,
                "sidebar_sn_icons",
                "sidebar_sn_icons",
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
            for icon in sidebar['sn_icons']:
                ic = create_icon(
                    sn_icons,
                    icon,
                    icon_label='sidebar_sn_icon',
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

            sidebar_div.add_child(sn_icons)
            sidebar_div.sn_icons = sn_icons

        sidebar_div.nav_div.set_neighbours(top_elements=[sidebar_div.sn_icons], bottom_elements=[sidebar_div.sn_icons])
    else:
        arr = []
        for element in sidebar['filters']:
            if element['type'] == 'checkbox':
                pass
            elif element['type'] == 'input':
                pass
            elif element['type'] == 'switcher':
                pass

    return sidebar_div


def create_card_element(parent, i, card_size, card_title, card_description, card_image, card_avatar, card_icons_list: [],
                        card_buttons: [], card_titles_subtitles: [],
                        card_key_value: [], card_icons_texts: []):
    print(f"title: {card_title}")
    card = create_card(
        parent,
        i,
        card_size,
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=10,
        min_margin_bottom=10,
        center_vertical=True
    )
    card.title = None
    card.description = None
    card.image = None
    card.buttons = None
    card.icons_texts = []
    card.icons = None
    card.titles_subtitles = None
    card.avatar_div = None

    if card_title:
        title = create_text(
            card_title,
            card,
            min_width=200,
            min_height=30,
            label='card_title',
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=0,
            min_margin_bottom=10,
            is_flexwidth=True
        )
        card.add_child(title)
        card.title = title

    if card_description:
        description = create_text(
            card_description,
            card,
            'card_description',
            min_height=100,
            min_width=200,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=0,
            min_margin_bottom=10,
            is_flexwidth=True
        )
        card.add_child(description)
        card.description = description

    if len(card_titles_subtitles) > 0:
        titles_subtitles = create_div(
            card,
            "titles_subtitles_div",
            "titles_subtitles_div",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_left=10,
            max_margin_right=10,
            max_margin_bottom=10,
            max_margin_top=10,
            min_width=150,
            min_height=100,
            is_flexwidth=True
        )
        arr = []
        for ts in card_titles_subtitles:
            title_subtitle = create_div(
                titles_subtitles,
                "title_subtitle_div",
                "title_subtitle_div",
                min_margin_left=0,
                min_margin_right=0,
                min_margin_top=0,
                min_margin_bottom=0,
                max_margin_left=10,
                max_margin_right=10,
                max_margin_bottom=10,
                max_margin_top=10,
                is_flexwidth=random.choice([True, False]),
                min_width=120,
                min_height=75,
            )
            title = create_text(
                ts[0],
                title_subtitle,
                min_width=50,
                min_height=25,
                label='card_t',
                min_margin_left=0,
                min_margin_right=10,
                min_margin_top=0,
                min_margin_bottom=0,
                is_flexwidth=True
            )
            subtitle = create_text(
                ts[1],
                title_subtitle,
                min_width=50,
                min_height=25,
                label='card_subt',
                min_margin_left=0,
                min_margin_right=0,
                min_margin_top=0,
                min_margin_bottom=0,
                is_flexwidth=True
            )
            title.set_neighbours(bottom_elements=[subtitle], right_elements=[subtitle])
            title_subtitle.add_children([title, subtitle])
            arr.append(title_subtitle)
        [arr[i].set_neighbours(bottom_elements=arr[i:]) for i in range(len(arr))]
        titles_subtitles.add_children(arr)

        card.add_child(titles_subtitles)
        card.titles_subtitles = titles_subtitles

    if len(card_icons_list) > 0:
        icons = create_icons_list(
            card,
            'card_icons',
            'card_icons',
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=0,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=20,
            max_margin_top=20,
            is_flexwidth=random.choice([True, False])
        )
        arr = []
        for icon in card_icons_list:
            icon = create_icon(
                icons,
                icon,
                icon_label='card_icon',
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
            arr.append(icon)
        [arr[i].set_neighbours(right_elements=arr[i:], left_elements=arr[i:]) for i in range(len(arr))]
        icons.add_children(arr)

        card.add_child(icons)
        card.icons = icons

    if len(card_buttons) > 0:
        buttons = create_div(
            card,
            "buttons_div",
            "buttons_div",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=10,
            max_margin_right=10,
            max_margin_bottom=10,
            max_margin_top=10,
            is_flexwidth=random.choice([True, False]),
            min_width=150,
            min_height=250,
        )
        arr = []
        for card_button in card_buttons:
            button = create_text(
                card_button,
                buttons,
                'card_button',
                min_width=150,
                min_height=40,
                min_margin_left=0,
                min_margin_right=0,
                min_margin_top=5,
                min_margin_bottom=5
            )
            arr.append(button)
        [arr[i].set_neighbours(right_elements=arr[i:], bottom_elements=arr[i:]) for i in range(len(arr))]
        buttons.add_children(arr)
        buttons.min_height = sum(
            [arr[i].min_height + arr[i].min_margin_top + arr[i].min_margin_bottom for i in range(len(arr))])

        card.add_child(buttons)
        card.buttons = buttons

    if card_avatar:
        avatar_div = create_div(
            card,
            "card_avatar_div",
            "card_avatar_div",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=20,
            max_margin_top=20,
            center_horizontal=True,
        )
        avatar = create_icon(
            avatar_div,
            "card_avatar",
            "card_avatar",
            link=card_avatar,
            icon_width=50,
            icon_height=50,
            min_margin_left=0,
            min_margin_right=0,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_left=0,
            max_margin_right=0,
            max_margin_bottom=0,
            max_margin_top=0,
        )
        avatar_div.height=avatar.height
        avatar_div.width=avatar.width

        avatar_div.add_child(avatar)
        avatar_div.avatar = avatar

        card.add_child(avatar_div)
        card.avatar_div = avatar_div

    if card_image:
        image_div = create_div(
            card,
            "card_img_div",
            "card_img_div",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=20,
            max_margin_top=20,
            center_horizontal=True,
            is_flexheight=True
        )
        size = random.choice([200, 220, 240, 250, 260, 270, 280, 300])
        image = create_icon(
            image_div,
            "card_image",
            "card_image",
            link=card_image,
            icon_width=size,
            icon_height=size,
            min_margin_left=0,
            min_margin_right=0,
            min_margin_top=0,
            min_margin_bottom=0,
            max_margin_left=0,
            max_margin_right=0,
            max_margin_bottom=0,
            max_margin_top=0,
        )
        image_div.min_height=image.height
        image_div.min_width=image.width

        image_div.add_child(image)
        image_div.image = image

        card.add_child(image_div)
        card.image_div = image_div

    if card_icons_texts:
        arr = []
        for card_icon_text in card_icons_texts:
            icon_text = create_div(
                card,
                "card_icon_text",
                "card_icon_text",
                min_margin_left=10,
                min_margin_right=10,
                min_margin_bottom=10,
                min_margin_top=0,
                center_horizontal=True,
                center_vertical=True
            )
            icon = create_icon(
                icon_text,
                card_icon_text[0],
                "cardit_icon",
                icon_width=20,
                icon_height=20,
                min_margin_left=0,
                min_margin_right=5,
                min_margin_bottom=0,
                min_margin_top=0,
                max_margin_left=0,
                max_margin_right=10,
            )
            text = create_text(
                card_icon_text[1],
                icon_text,
                label="cardit_text",
                min_width=20,
                min_height=20,
                max_width=30
            )
            icon_text.icon = icon
            icon_text.text = text
            icon.set_neighbours(right_elements=[text])
            icon_text.add_children([icon, text])
            icon_text.min_height = icon.height
            icon_text.width = 50

            arr.append(icon_text)
            card.add_child(icon_text)
        card.icons_texts = arr

    if card.size == 'sm':
        if card.avatar_div:
            card.avatar_div.set_neighbours(right_elements=[card.title, card.titles_subtitles], bottom_elements=[card.image_div, card.description, card.icons,
                                                       card.buttons, card.title] + card.icons_texts)

        if card.titles_subtitles:
            card.titles_subtitles.set_neighbours(right_elements=[], left_elements=[card.avatar_div], bottom_elements=[card.description, card.icons,
                                                       card.buttons, card.title, card.image_div] + card.icons_texts)

        if card.image_div:
            card.image_div.is_flexwidth = True
            card.image_div.set_neighbours(right_elements=[], left_elements=[], top_elements=[card.avatar_div, card.titles_subtitles, card.title, card.description],
                                      bottom_elements=[card.title, card.description, card.icons,
                                                       card.buttons] + card.icons_texts)

        if card.title:
            card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[card.titles_subtitles]+card.icons_texts,
                                      bottom_elements=[card.description, card.icons,
                                                       card.buttons] + card.icons_texts)

        if card.description:
            card.description.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                            bottom_elements=[card.icons, card.buttons] + card.icons_texts)

        if card.icons:
            card.icons.set_neighbours(right_elements=[], left_elements=[card.buttons], top_elements=card.icons_texts,
                                      bottom_elements=card.icons_texts)

        if card.buttons:
            card.buttons.set_neighbours(top_elements=card.icons_texts, bottom_elements=card.icons_texts)

        sh = 0
        for child in card.children:
            if child.height:
                sh += child.height
            else:
                sh += child.min_height
            sh += child.min_margin_top + child.min_margin_bottom
        card.min_height = sh
        # card.min_width = max(child.min_width + child.min_margin_right + child.min_margin_left for child in card.children)
        card.min_width = 300
        card.max_width = 450

        #card.rules = [And(card.icons.y > card.image_div.y), And(card.title.y < card.image_div.y)]
    # TODO сортировка ширина карточки описание под картинкой
    elif card.size == 'md':
        if card.avatar_div:
            card.avatar_div.set_neighbours(right_elements=[card.title, card.titles_subtitles],
                                           bottom_elements=[card.image_div, card.description, card.icons, card.title,
                                                            card.buttons] + card.icons_texts)

        if card.titles_subtitles:
            card.titles_subtitles.set_neighbours(right_elements=[], left_elements=[card.avatar_div], top_elements=[],
                                      bottom_elements=[card.description, card.icons, card.title, card.image_div]+card.icons_texts)
        if card.image_div:
            card.image_div.set_neighbours(right_elements=[card.description, card.icons, card.buttons],
                                          top_elements=[card.title, card.titles_subtitles, card.avatar_div], bottom_elements=card.icons_texts)

        if card.title:
            card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[card.icons],
                                      bottom_elements=[card.description, card.icons]+card.icons_texts)
        #if card.description:
        #    card.description.set_neighbours(bottom_elements=[card.buttons]+card.icons_texts)

        if card.icons:
            card.icons.set_neighbours(left_elements=[card.buttons], bottom_elements=card.icons_texts, top_elements=card.icons_texts)
        if card.buttons:
            card.buttons.set_neighbours(bottom_elements=card.icons_texts, top_elements=card.icons_texts)

        card.min_height = 800
        # card.min_width = max(child.min_width + child.min_margin_right + child.min_margin_left for child in card.children)
        # card.min_width = card.image.width + card.image.min_margin_left + card.image.min_margin_right + max([child.min_width + child.min_margin_left + child.min_margin_right for child in card.children]) + 100
        card.min_width = 500
        card.max_width = 650

        # card.rules = [And(card.icons.y > card.title.y), And(card.icons.y < card.title.y)]
        #card.rules = [And(card.title.y < card.image_div.y)]
        #card.rules = [And(card.title.y > card.image_div.y), And(card.title.y < card.image_div.y), And(card.buttons.x < card.icons_texts[0].x)]
    else:
        pass
    # title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # description.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # icons.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # add_to_cart_button.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # rating.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # rating_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # reviews.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
    # reviews_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])

    # card.set_min_size_by_children()
    # card.max_height = 2000
    # card.min_height = 400
    # card.max_width = 2000
    # card.set_max_size_by_children()

    return card