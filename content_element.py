from layout_solver import *
import copy

# card_image = "example.com/image.png"
# card_carousel_images ["example.com/image.png", "example.com/image.png", ...]
# card_icons_list = ["add_to_wishlist", "compare"]
# card_text_chips = [("color", ["red", "blue", "pink"]), ...]
# card_icon_chips = [("memory", ["128 GB", "256 GB"]), ...]
# card_buttons = ["Add to Cart", "Buy Fast"]
# card_title_subtitle = [("title", "subtitle")]
# card_key_value = [("name", "Xiaomi")]
# card_icons_texts = [("icon", "text"), ...]


def create_content_element(body, min_width, min_height, is_fullwidth, card_size, card_title, card_description,
                           card_image, card_carousel_images: [], card_icons_list: [], card_text_chips: [],
                           card_icon_chips: [], card_buttons: [], card_title_subtitle: [],
                           card_key_value: [], card_icons_texts: []):
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
    for i in range(5):
        card = create_card_element(cards_el, i, card_size, card_title, card_description,
                           card_image, card_carousel_images, card_icons_list, card_text_chips,
                           card_icon_chips, card_buttons, card_title_subtitle,
                           card_key_value, card_icons_texts)
        cards.append(card)

    for i in range(len(cards) - 1):
        cards[i].set_neighbours(right_elements=cards[i + 1:], bottom_elements=cards[i + 1:])

    cards_el.add_children(cards)

    content.cards = cards_el
    content.add_child(cards_el)

    sidebar = create_sidebar(content)

    content.sidebar = sidebar
    content.add_child(sidebar)

    return content


def create_sidebar(parent):
    sidebar = create_div(
        parent,
        "sidebar",
        "sidebar",
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=10,
        min_margin_bottom=10,
        max_margin_left=20,
        max_margin_right=20,
        max_margin_top=20,
        max_margin_bottom=20,
        min_width=250,
        is_flexheight=True,
        center_vertical=True
    )
    #TODO

    return sidebar


def create_card_element(parent, i, card_size, card_title, card_description, card_image, card_carousel_images: [], card_icons_list: [], card_text_chips: [],
                           card_icon_chips: [], card_buttons: [], card_title_subtitle: [],
                           card_key_value: [], card_icons_texts: []):
    card = create_card(
        parent,
        i,
        card_size,
        min_margin_left=10,
        min_margin_right=10,
        min_margin_top=10,
        min_margin_bottom=10,
        center_horizontal=True,
        center_vertical=True
    )
    card.title = None
    card.description = None
    card.image = None
    card.buttons = None
    card.icons_texts = []
    card.icons_chips_div = None
    card.icons = None

    if card_title:
        title = create_text(
            card_title,
            card,
            min_width=200,
            min_height=30,
            label='card_title',
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
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
            min_margin_top=10,
            min_margin_bottom=10,
            is_flexwidth=True
        )
        card.add_child(description)
        card.description = description

    if len(card_icons_list) > 0:
        icons = create_icons_list(
            card,
            'card_icons',
            'card_icons',
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=20,
            max_margin_top=20,
            is_flexwidth=True
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
            is_flexheight=True,
            is_flexwidth=True,
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

    if len(card_icon_chips) > 0:
        icons_chips_div = create_div(
            card,
            "icons_chips_div",
            "icons_chips_div",
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=10,
            max_margin_right=10,
            max_margin_bottom=10,
            max_margin_top=10,
            is_flexwidth=True,
            is_flexheight=True,
            min_width=100,
            min_height=100
        )
        icon_chips = []
        for card_chip in card_icon_chips:
            # в нем хранятся текст и список чипов
            chip_div = create_div(
                icons_chips_div,
                f"{card_chip[0]}_div",
                f"{card_chip[0]}_div",
                min_margin_left=10,
                min_margin_right=10,
                min_margin_bottom=10,
                min_margin_top=10,
                is_flexwidth=True,
            )
            title = create_text(
                card_chip[0],
                chip_div,
                card_chip[0],
                min_width=50,
                min_height=10
            )
            chip_div.add_child(title)
            # список чипов
            chips_list = create_icons_list(
                chip_div,
                f"{card_chip[0]}_list",
                f"{card_chip[0]}_list",
                min_margin_left=10,
                min_margin_right=10,
                min_margin_bottom=10,
                min_margin_top=10,
                is_fullwidth=True,
            )
            chip_div.add_child(chips_list)
            arr = []
            for chip in card_chip[1]:
                ch = create_icon(
                    chip_div,
                    chip + card_chip[0],
                    'icon_chip',
                    icon_width=30,
                    icon_height=30,
                    min_margin_left=0,
                    min_margin_right=10,
                    min_margin_top=0,
                    min_margin_bottom=10
                )
                arr.append(ch)
            # чип относительно другого чипа либо справа, либо снизу
            [arr[i].set_neighbours(right_elements=arr[i:], bottom_elements=arr[i:]) for i in range(len(arr))]
            chips_list.add_children(arr)
            title.set_neighbours(bottom_elements=[chips_list])
            chip_div.title = title
            chip_div.chips_list = chips_list
            chip_div.min_height = sum([chip_div.children[i].min_height + chip_div.children[i].min_margin_bottom +
                                       chip_div.children[i].min_margin_top for i in range(len(chip_div.children))])

            icon_chips.append(chip_div)
        icons_chips_div.add_children(icon_chips)
        icons_chips_div.min_height = sum([icons_chips_div.children[i].min_height + icons_chips_div.children[
            i].min_margin_bottom + icons_chips_div.children[i].min_margin_top for i in
                                          range(len(icons_chips_div.children))])
        card.add_child(icons_chips_div)
        card.icons_chips_div = icons_chips_div

    if card_image:
        image = create_icon(
            card,
            "card_image",
            "card_image",
            link=card_image,
            icon_width=200,
            icon_height=200,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
            max_margin_left=20,
            max_margin_right=20,
            max_margin_bottom=20,
            max_margin_top=20
        )
        card.add_child(image)
        card.image = image

    if card_icons_texts:
        arr = []
        for card_icon_text in card_icons_texts:
            icon_text = create_div(
                card,
                "card_icon_text",
                "card_icon_text",
                min_margin_left=5,
                min_margin_right=5,
                min_margin_bottom=5,
                min_margin_top=5,
            )
            icon = create_icon(
                icon_text,
                card_icon_text[0],
                "cit_icon",
                icon_width=20,
                icon_height=20,
                min_margin_left=0,
                min_margin_right=5,
                min_margin_bottom=0,
                min_margin_top=0,
            )
            text = create_text(
                card_icon_text[1],
                icon_text,
                label="cit_text",
                min_width=20,
                min_height=10,
            )
            icon.set_neighbours(right_elements=[text])
            icon_text.add_children([icon, text])
            icon_text.min_height = icon.height
            icon_text.min_width = 50

            arr.append(card_icons_texts)
            card.add_child(icon_text)
        card.icons_texts = arr

    if card.size == 'sm':
        if card.image:
            card.image.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                      bottom_elements=[card.title, card.description, card.icons,
                                                       card.buttons] + card.icons_texts)

        if card.title:
            card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=card.icons_texts,
                                      bottom_elements=[card.description, card.icons,
                                                       card.buttons] + card.icons_texts)
        if card.description:
            card.description.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                            bottom_elements=[card.icons, card.buttons] + card.icons_texts)

        if card.icons_chips_div:
            card.icons_chips_div.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
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

        card.rules = [And(card.icons.y > card.image.y)]
    # TODO сортировка ширина карточки описание под картинкой
    elif card.size == 'md':
        if card.image:
            card.image.set_neighbours(right_elements=[card.title, card.description, card.icons, card.buttons],
                                      top_elements=[card.title])

        if card.title:
            card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[card.icons],
                                      bottom_elements=[card.description, card.icons])
        if card.description:
            card.description.set_neighbours(bottom_elements=[card.buttons])
        if card.icons:
            card.icons.set_neighbours(left_elements=[card.buttons])

        card.min_height = 300
        # card.min_width = max(child.min_width + child.min_margin_right + child.min_margin_left for child in card.children)
        # card.min_width = card.image.width + card.image.min_margin_left + card.image.min_margin_right + max([child.min_width + child.min_margin_left + child.min_margin_right for child in card.children]) + 100
        card.min_width = 500

        # card.rules = [And(card.icons.y > card.title.y), And(card.icons.y < card.title.y)]
        card.rules = [And(card.title.y < card.image.y)]
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