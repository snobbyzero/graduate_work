from layout_solver import *

# card_image = "example.com/image.png"
# card_carousel_images ["example.com/image.png", "example.com/image.png", ...]
# card_icons = ["add_to_wishlist", "compare"]
# card_text_chips = [("color", ["red", "blue", "pink"]), ...]
# card_icon_chips = [("memory", ["128 GB", "256 GB"]), ...]
# card_buttons = ["Add to Cart", "Buy Fast"]
# card_title_subtitle = [("title", "subtitle")]
# card_key_value = [("name", "Xiaomi")]


def create_content_element(body, min_width, min_height, is_fullwidth, card_size, card_title, card_description,
                           card_image, card_carousel_images: [], card_icons: [], card_text_chips: [], card_icon_chips: [], card_buttons: [], card_title_subtitle: [],
                           card_key_value: []):
    content = create_content(body, min_width=min_width, min_height=min_height, is_fullwidth=is_fullwidth)
    cards = []
    for i in range(5):
        card = create_card(
            content,
            i,
            card_size,
            min_margin_left=10,
            min_margin_right=10,
            min_margin_top=10,
            min_margin_bottom=10,
        )
        if card_title:
            title = create_text(
                card_title,
                card,
                min_width=200,
                label='title',
                min_margin_left=10,
                min_margin_right=10,
                min_margin_top=10,
                min_margin_bottom=10,
            )
            card.add_child(title)
            card.title = title

        if card_description:
            description = create_text(
                card_description,
                card,
                'description',
                is_flexwidth=True,
                min_margin_left=10,
                min_margin_right=10,
                min_margin_top=10,
                min_margin_bottom=10,
            )
            card.add_child(description)
            card.description = description

        if len(card_icons) > 0:
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
                max_margin_top=20
            )
            arr = []
            for icon in icons:
                icon = create_icon(
                    icons,
                    icon,
                    icon_label='card_icon',
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
                arr.append(icon)
            [arr[i].set_neighbours(right_elements=arr[i:], left_elements=arr[i:]) for i in range(len(arr))]
            icons.add_child(arr)

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
                max_margin_top=10
            )
            arr = []
            for card_button in card_buttons:
                button = create_text(
                    card_button,
                    card,
                    'card_button',
                    min_width=100,
                    min_margin_left=10,
                    min_margin_right=10,
                    min_margin_top=10,
                    min_margin_bottom=10
                )
                arr.append(button)
            [arr[i].set_neighbours(right_elements=arr[i:],  bottom_elements=arr[i:]) for i in range(len(arr))]
            buttons.add_children(arr)

            card.add_child(buttons)
            card.buttons = buttons

        if len(card_icon_chips) > 0:
            icon_chips = []
            for card_chip in card_icon_chips:
                # в нем хранятся текст и список чипов
                chip_div = create_div(
                    card,
                    f"{card_chip[0]}_div",
                    f"{card_chip[0]}_div",
                    min_margin_left=10,
                    min_margin_right=10,
                    min_margin_bottom=10,
                    min_margin_top=10,
                )
                title = create_text(
                    card_chip[0],
                    chip_div,
                    card_chip[0],
                    min_width=50,
                )
                chip_div.add_child(title)
                # список чипов
                chips_list = create_icons_list(
                    chip_div,
                    card_chip[1],
                    card_chip[1],
                    min_margin_left=10,
                    min_margin_right=10,
                    min_margin_bottom=10,
                    min_margin_top=10,
                )
                chip_div.add_child(chips_list)
                arr = []
                for chip in card_chip[1]:
                    ch = create_icon(
                        chip_div,
                        chip,
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
                title.set_neighbours(bottom_elements=chips_list)
                chip_div.title = title
                chip_div.chips_list = chips_list

                icon_chips.append(chip_div)
            card.add_child(icon_chips)
            card.icon_chips = icon_chips

        if card_image:
            image = create_icon(
                card,
                "card_image",
                "card_image",
                link=card_image,
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
            card.add_child(card_image)
            card.image = card_image

        if card.size == 'sm':
            if card.image:
                card.image.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[card.title, card.description, card_icons, card_icon_chips, card_buttons])

            if card.title:
                card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                          bottom_elements=[card.description, card_icons, card_icon_chips,
                                                           card_buttons])
            if card.description:
                card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                          bottom_elements=[card_icons, card_icon_chips, card_buttons])

            if card.icon_chips:
                card.icon_chipsset_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                          bottom_elements=[card_icons, card_buttons])

            if card.icons:
                card.title.set_neighbours(right_elements=[], left_elements=[], top_elements=[],
                                          bottom_elements=[card_buttons])

            sh = 0
            for child in card.children:
                print(child.label)
                if child.height:
                    print(child.height)
                    sh += child.height
                else:
                    print(child.min_height)
                    sh += child.min_height
                sh += child.min_margin_top + child.min_margin_bottom
            card.min_height = sh
            print(f"card minheight {card.min_height}")
            card.min_width = content.min_width // 3
        elif card.size == 'md': pass
            #title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #description.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #icons.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #add_to_cart_button.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #rating.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #rating_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #reviews.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #reviews_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
        else: pass
            #title.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #description.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #icons.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #additional_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #add_to_cart_button.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #rating.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #rating_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #reviews.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])
            #reviews_text.set_neighbours(right_elements=[], left_elements=[], top_elements=[], bottom_elements=[])

        # card.set_min_size_by_children()
        # card.max_height = 2000
        # card.min_height = 400
        # card.max_width = 2000
        # card.set_max_size_by_children()
        cards.append(card)

    for i in range(len(cards) - 1):
        cards[i].set_neighbours(right_elements=cards[i + 1:], bottom_elements=cards[i + 1:])

    content.add_children(cards)

    return content
