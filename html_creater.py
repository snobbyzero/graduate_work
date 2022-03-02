from yattag import Doc
import colorsys
from content_element import create_content_element
from footer_element import create_footer_element
from header_element import create_header_element
from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.IconButtonJSON import IconButtonJSON
from json_classes.Measure import Measure
from json_classes.NavListJSON import NavListJSON
from json_classes.SearchBarJSON import SearchBarJSON
from json_classes.ValueJSON import ValueJSON
from layout_solver import *
from faker import Faker

# random.seed(3)
# faker = Faker('ru_RU')
faker = Faker()

icons = ['profile', 'cart', 'wishlist', 'compare', 'search', 'rating']

body = create_body(1500, 10000)

word_style = random.choice(['capitalize', 'all_caps'])
if word_style == 'capitalize':
    nav_list = [faker.word().capitalize() for i in range(random.randint(4, 5))]
else:
    nav_list = [faker.word().upper() for i in range(random.randint(4, 5))]
header = create_header_element(
    body,
    min_width=1000,
    min_height=70,
    max_height=150,
    is_fullwidth=True,
    is_logo=True,
    nav_list=[],
    is_search=True,
    icls_icons_list=['home', 'users', 'envelope', 'music'],
    sn_icons_list=['vk', 'twitter', 'github']
)
cards = []
for i in range(10):
    profile = faker.profile()
    rand = random.randint(0, 10)
    cards.append({
        # "title": " ".join(faker.words(random.randint(1,3))),
        "title": None,
        "description": faker.text(max_nb_chars=200),
        # "description": None,
        "avatar": faker.image_url(rand * 20, rand * 20),
        # "avatar": None,
        "image": faker.image_url(rand * 100, rand * 100),
        "titles_subtitles": [(f"@{profile['username']}", profile['name'])]
        # "titles_subtitles": []
    })

content = create_content_element(
    body,
    min_width=1000,
    min_height=8000,
    is_fullwidth=True,
    cards_inf=cards,
    card_size=random.choice(['sm']),
    # card_size='sm',
    card_icons_list=[],
    card_buttons=[],
    card_key_value=[],
    card_icons_texts=[("wishlist", "45"), ("comment", "10"), ("retweet", "5"), ("share", "")],
    sidebar={
        'is_nav': True,
        'nav': [(random.choice(icons), faker.word().capitalize()) for i in range(random.randint(7, 10))],
        'sn_icons': ['twitter', 'vk', 'github']
    },
    top={

    }
)

footer = create_footer_element(
    body,
    min_width=1000,
    min_height=500,
    is_fullwidth=True,
    is_logo=True,
    vert_lists=[],
    links=[f"© ООО {faker.word()}", "Мобильная версия", "Вакансии"],
    sn_icons_list=['vk', 'twitter', 'github'],
    copyright_text=None,
    subscribe_form=None
)

body.add_children([header, content, footer])
header.set_neighbours(bottom_elements=[content])
content.set_neighbours(bottom_elements=[footer])
find_solutions(body)
print(footer)


def create_body(body_model):
    header_json = create_header_json(header, body_model, random_choose_model(header, body_model))
    content_json = create_content_json(content, body_model, random_choose_model(content, body_model))
    footer_json = create_footer_json(footer, body_model, random_choose_model(footer, body_model))
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
    body_json.children.append(content_json)
    body_json.children.append(footer_json)

    return body_json


def create_content_json(content, body_model, content_model):
    content_json = BaseElementJSON(
        "content",
        x=ValueJSON(body_model[content.x].as_long() * body.table.cell_width * 100 / body.width, Measure.PERCENT),
        y=ValueJSON(body_model[content.y].as_long() * body.table.cell_width * 100 / body.height, Measure.PERCENT),
        width=ValueJSON(body_model[content.col_count].as_long() * body.table.cell_width * 100 / body.width,
                        Measure.PERCENT),
        height=ValueJSON(body_model[content.row_count].as_long() * body.table.cell_height * 100 / body.height,
                         Measure.PERCENT),
        min_width=ValueJSON(content.min_width, Measure.PIXEL),
        margin_left=ValueJSON(body_model[content.margin_left].as_long() * body.table.cell_width, Measure.PIXEL),
        margin_right=ValueJSON(body_model[content.margin_right].as_long() * body.table.cell_width, Measure.PIXEL),
        margin_top=ValueJSON(body_model[content.margin_top].as_long() * body.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(body_model[content.margin_bottom].as_long() * body.table.cell_height, Measure.PIXEL),
        label=content.label,
        fullwidth=content.is_fullwidth,
        justify_left=content.justify_left,
        justify_right=content.justify_right,
        align_content="flex-start",
        center_horizontal=False,
        center_vertical=False,
        flexflow="row nowrap"
    )

    sidebar_model = random_choose_model(content.sidebar, content_model)
    sidebar = content.sidebar
    sidebar_json = BaseElementJSON(
        "aside",
        x=ValueJSON(content_model[sidebar.x].as_long() * content.table.cell_width * 100 / sidebar.get_width_with_parent(content_model), Measure.PERCENT),
        y=ValueJSON(content_model[sidebar.y].as_long() * content.table.cell_width * 100 / sidebar.get_height_with_parent(content_model), Measure.PERCENT),
        width=ValueJSON(content_model[sidebar.col_count].as_long() * content.table.cell_width, Measure.PIXEL),
        height=ValueJSON(content_model[sidebar.row_count].as_long() * content.table.cell_height, Measure.PIXEL),
        min_width=ValueJSON(sidebar.min_width, Measure.PIXEL),
        margin_left=ValueJSON(content_model[sidebar.margin_left].as_long() * content.table.cell_width, Measure.PIXEL),
        margin_right=ValueJSON(content_model[sidebar.margin_right].as_long() * content.table.cell_width, Measure.PIXEL),
        margin_top=ValueJSON(content_model[sidebar.margin_top].as_long() * content.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(content_model[sidebar.margin_bottom].as_long() * content.table.cell_height, Measure.PIXEL),
        label=sidebar.label,
        fullwidth=sidebar.is_fullwidth,
        justify_left=sidebar.justify_left,
        justify_right=True,
        align_content="flex-start",
        center_horizontal=False,
        center_vertical=False,
        flexflow="row nowrap",
    )

    if sidebar.nav_div:
        nav_div_json = create_div(sidebar.nav_div, sidebar, sidebar_model, content_model)
        nav_div_model = random_choose_model(sidebar.nav_div, sidebar_model)
        for i in range(len(sidebar.nav_div.children)):
            link = sidebar.nav_div.children[i]
            link_json = create_div(link, sidebar.nav_div, nav_div_model, sidebar_model)
            link_model = random_choose_model(link, nav_div_model)
            text = link.text
            icon = link.icon

            icon_json = IconButtonJSON(
                icon.name,
                x=ValueJSON(
                    link_model[icon.x].as_long() * link.table.cell_width * 100 / link.get_width_with_parent(
                        nav_div_model), Measure.PERCENT),
                y=ValueJSON(
                    link_model[icon.y].as_long() * link.table.cell_height * 100 /link.get_height_with_parent(
                        nav_div_model), Measure.PERCENT),
                width=ValueJSON(link_model[icon.col_count].as_long() * link.table.cell_width, Measure.PIXEL),
                height=ValueJSON(link_model[icon.row_count].as_long() * link.table.cell_height, Measure.PIXEL),
                margin_right=ValueJSON(link_model[icon.margin_right].as_long() * link.table.cell_width,
                                       Measure.PIXEL),
                margin_left=ValueJSON(link_model[icon.margin_left].as_long() * link.table.cell_width,
                                      Measure.PIXEL),
                margin_top=ValueJSON(link_model[icon.margin_top].as_long() * link.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(link_model[icon.margin_bottom].as_long() * link.table.cell_height,
                                        Measure.PIXEL),
                font_size=ValueJSON(1.5,
                                    Measure.EM),
                label=icon.label,
            )
            link_json.children.append(icon_json)

            text_json = BaseElementJSON(
                "h5",
                x=ValueJSON(link_model[text.x].as_long() * link.table.cell_width * 100 / link.get_width_with_parent(
                    nav_div_model), Measure.PERCENT),
                y=ValueJSON(link_model[text.y].as_long() * link.table.cell_height * 100 / link.get_height_with_parent(
                    nav_div_model), Measure.PERCENT),
                width=ValueJSON(
                    link_model[text.col_count].as_long() * link.table.cell_width * 100 / link.get_width_with_parent(
                        nav_div_model), Measure.PERCENT),
                height=ValueJSON(
                    link_model[text.row_count].as_long() * link.table.cell_height * 100 / link.get_height_with_parent(
                        nav_div_model), Measure.PERCENT),
                min_width=ValueJSON(text.min_width, Measure.PIXEL),
                margin_right=ValueJSON(link_model[text.margin_right].as_long() * link.table.cell_width, Measure.PIXEL),
                margin_left=ValueJSON(link_model[text.margin_left].as_long() * link.table.cell_width, Measure.PIXEL),
                margin_top=ValueJSON(link_model[text.margin_top].as_long() * link.table.cell_height, Measure.PIXEL),
                margin_bottom=ValueJSON(link_model[text.margin_bottom].as_long() * link.table.cell_height,
                                        Measure.PIXEL),
                text=text.text,
                text_align="start",
                label=text.label,
                flexgrow=text.is_flexwidth,
                font_size=ValueJSON(1.5, Measure.EM),
                css={"color": "primary", "font-weight": random.choice(["600", "700"])}
            )
            link_json.children.append(text_json)

            nav_div_json.children.append(link_json)
        sidebar_json.children.append(nav_div_json)

    content_json.children.append(sidebar_json)

    # TODO TOP
    #top_model = random_choose_model(content.top, content_model)
    #top = content.top
    #top_json = None

    cards_model = random_choose_model(content.cards, content_model)
    cards_json = create_div(content.cards, content, content_model, body_model, Measure.PERCENT)

    card = content.cards.children[0]
    card_model = random_choose_model(card, cards_model)
    icons = card.icons
    if icons:
        icons_model = random_choose_model(icons, card_model)
    buttons = card.buttons
    if buttons:
        buttons_model = random_choose_model(buttons, card_model)
    for i in range(len(content.cards.children)):
        card = content.cards.children[i]
        card_json = create_div(card, content.cards, cards_model, content_model)

        title = card.title
        if title:
            title_json = BaseElementJSON(
                "h5",
                x=ValueJSON(card_model[title.x].as_long() * card.table.cell_width * 100 / card.get_width_with_parent(
                    cards_model), Measure.PERCENT),
                y=ValueJSON(card_model[title.y].as_long() * card.table.cell_height * 100 / card.get_height_with_parent(
                    cards_model), Measure.PERCENT),
                width=ValueJSON(
                    card_model[title.col_count].as_long() * card.table.cell_width * 100 / card.get_width_with_parent(
                        cards_model), Measure.PERCENT),
                height=ValueJSON(
                    card_model[title.row_count].as_long() * card.table.cell_height * 100 / card.get_height_with_parent(
                        cards_model), Measure.PERCENT),
                min_width=ValueJSON(title.min_width, Measure.PIXEL),
                margin_right=ValueJSON(card_model[title.margin_right].as_long() * card.table.cell_width, Measure.PIXEL),
                margin_left=ValueJSON(card_model[title.margin_left].as_long() * card.table.cell_width, Measure.PIXEL),
                margin_top=ValueJSON(card_model[title.margin_top].as_long() * card.table.cell_height, Measure.PIXEL),
                margin_bottom=ValueJSON(card_model[title.margin_bottom].as_long() * card.table.cell_height,
                                        Measure.PIXEL),
                text=title.text,
                text_align="start",
                label=title.label,
                flexgrow=title.is_flexwidth,
                css={"color": "primary", "font-weight": random.choice(["500", "600", "700"])}
            )
            card_json.children.append(title_json)

        description = card.description
        if description:
            description_json = BaseElementJSON(
                "p",
                x=ValueJSON(
                    card_model[description.x].as_long() * card.table.cell_width * 100 / card.get_width_with_parent(
                        cards_model), Measure.PERCENT),
                y=ValueJSON(
                    card_model[description.y].as_long() * card.table.cell_height * 100 / card.get_height_with_parent(
                        cards_model), Measure.PERCENT),
                width=ValueJSON(card_model[
                                    description.col_count].as_long() * card.table.cell_width * 100 / card.get_width_with_parent(
                    cards_model), Measure.PERCENT),
                height=ValueJSON(card_model[
                                     description.row_count].as_long() * card.table.cell_height * 100 / card.get_height_with_parent(
                    cards_model), Measure.PERCENT),
                min_width=ValueJSON(description.min_width, Measure.PIXEL),
                margin_right=ValueJSON(card_model[description.margin_right].as_long() * card.table.cell_width,
                                       Measure.PIXEL),
                margin_left=ValueJSON(card_model[description.margin_left].as_long() * card.table.cell_width,
                                      Measure.PIXEL),
                margin_top=ValueJSON(card_model[description.margin_top].as_long() * card.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(card_model[description.margin_bottom].as_long() * card.table.cell_height,
                                        Measure.PIXEL),
                text=description.text,
                text_align="start",
                label=description.label,
                flexgrow=description.is_flexwidth,
                css={"overflow": "hidden"}
            )
            card_json.children.append(description_json)
        avatar_div = card.avatar_div
        if avatar_div:
            avatar_div_json = create_div(
                avatar_div,
                card,
                card_model,
                cards_model
            )
            avatar_div_model = random_choose_model(avatar_div, card_model)
            avatar = avatar_div.avatar
            avatar_json = BaseElementJSON(
                "img",
                x=ValueJSON(
                    avatar_div_model[
                        avatar.x].as_long() * avatar_div.table.cell_width * 100 / avatar_div.get_width_with_parent(
                        card_model), Measure.PERCENT),
                y=ValueJSON(
                    avatar_div_model[
                        avatar.y].as_long() * avatar_div.table.cell_height * 100 / avatar_div.get_height_with_parent(
                        card_model), Measure.PERCENT),
                width=ValueJSON(avatar_div_model[avatar.col_count].as_long() * avatar_div.table.cell_width,
                                Measure.PIXEL),
                height=ValueJSON(avatar_div_model[avatar.row_count].as_long() * avatar_div.table.cell_height,
                                 Measure.PIXEL),
                min_width=ValueJSON(avatar.min_width, Measure.PIXEL),
                min_height=ValueJSON(avatar.min_height, Measure.PIXEL),
                margin_right=ValueJSON(avatar_div_model[avatar.margin_right].as_long() * avatar_div.table.cell_width,
                                       Measure.PIXEL),
                margin_left=ValueJSON(avatar_div_model[avatar.margin_left].as_long() * avatar_div.table.cell_width,
                                      Measure.PIXEL),
                margin_top=ValueJSON(avatar_div_model[avatar.margin_top].as_long() * avatar_div.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(avatar_div_model[avatar.margin_bottom].as_long() * avatar_div.table.cell_height,
                                        Measure.PIXEL),
                max_height=ValueJSON(avatar_div_model[avatar.row_count].as_long() * avatar_div.table.cell_height,
                                     Measure.PIXEL),
                text=avatar.link,
                label=avatar.label,
                css={
                    "border-radius": f"{avatar_div_model[avatar.col_count].as_long() * avatar_div.table.cell_width // 2}px"}
            )
            avatar_div_json.children.append(avatar_json)
            card_json.children.append(avatar_div_json)
        image_div = card.image_div
        if image_div:
            image_div_json = create_div(
                image_div,
                card,
                card_model,
                cards_model
            )
            image_div_model = random_choose_model(image_div, card_model)
            image = image_div.image
            image_json = BaseElementJSON(
                "img",
                x=ValueJSON(
                    image_div_model[
                        image.x].as_long() * image_div.table.cell_width * 100 / image_div.get_width_with_parent(
                        card_model), Measure.PERCENT),
                y=ValueJSON(
                    image_div_model[
                        image.y].as_long() * image_div.table.cell_height * 100 / image_div.get_height_with_parent(
                        card_model), Measure.PERCENT),
                width=ValueJSON(image_div_model[image.col_count].as_long() * image_div.table.cell_width, Measure.PIXEL),
                height=ValueJSON(image_div_model[image.row_count].as_long() * image_div.table.cell_height,
                                 Measure.PIXEL),
                min_width=ValueJSON(image.min_width, Measure.PIXEL),
                min_height=ValueJSON(image.min_height, Measure.PIXEL),
                margin_right=ValueJSON(image_div_model[image.margin_right].as_long() * image_div.table.cell_width,
                                       Measure.PIXEL),
                margin_left=ValueJSON(image_div_model[image.margin_left].as_long() * image_div.table.cell_width,
                                      Measure.PIXEL),
                margin_top=ValueJSON(image_div_model[image.margin_top].as_long() * image_div.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(image_div_model[image.margin_bottom].as_long() * image_div.table.cell_height,
                                        Measure.PIXEL),
                max_height=ValueJSON(image_div_model[image.row_count].as_long() * image_div.table.cell_height,
                                     Measure.PIXEL),
                text=image.link,
                label=image.label
            )
            image_div_json.children.append(image_json)
            card_json.children.append(image_div_json)

        if icons:
            icons_json = create_div(icons, card, card_model, cards_model)
            for icon in icons.children:
                icon_json = IconButtonJSON(
                    icon.name,
                    x=ValueJSON(
                        icons_model[icon.x].as_long() * icons.table.cell_width * 100 / icons.get_width_with_parent(
                            card_model), Measure.PERCENT),
                    y=ValueJSON(
                        icons_model[icon.y].as_long() * icons.table.cell_height * 100 / icons.get_height_with_parent(
                            card_model), Measure.PERCENT),
                    width=ValueJSON(icons_model[icon.col_count].as_long() * icons.table.cell_width, Measure.PIXEL),
                    height=ValueJSON(icons_model[icon.row_count].as_long() * icons.table.cell_height, Measure.PIXEL),
                    margin_right=ValueJSON(icons_model[icon.margin_right].as_long() * icons.table.cell_width,
                                           Measure.PIXEL),
                    margin_left=ValueJSON(icons_model[icon.margin_left].as_long() * icons.table.cell_width,
                                          Measure.PIXEL),
                    margin_top=ValueJSON(icons_model[icon.margin_top].as_long() * icons.table.cell_height,
                                         Measure.PIXEL),
                    margin_bottom=ValueJSON(icons_model[icon.margin_bottom].as_long() * icons.table.cell_height,
                                            Measure.PIXEL),
                    font_size=ValueJSON(icons_model[icon.col_count].as_long() * icons.table.cell_width,
                                        Measure.PIXEL),
                    label=icon.label,
                )
                icons_json.children.append(icon_json)
            sort_children(icons_json)
            card_json.children.append(icons_json)

        titles_subtitles = card.titles_subtitles
        if titles_subtitles:
            titles_subtitles_model = random_choose_model(titles_subtitles, card_model)
            titles_subtitles_div_json = create_div(titles_subtitles, card, card_model, cards_model, Measure.PERCENT)
            for i in range(len(titles_subtitles.children)):
                title_subtitle = titles_subtitles.children[i]
                title_subtitle_model = random_choose_model(title_subtitle, titles_subtitles_model)
                title = title_subtitle.children[0]
                subtitle = title_subtitle.children[1]
                title_subtitle_div = create_div(title_subtitle, titles_subtitles, titles_subtitles_model, card_model)
                title_json = BaseElementJSON(
                    "h5",
                    x=ValueJSON(
                        title_subtitle_model[
                            title.x].as_long() * title_subtitle.table.cell_width * 100 / title_subtitle.get_width_with_parent(
                            titles_subtitles_model), Measure.PERCENT),
                    y=ValueJSON(
                        title_subtitle_model[title.y].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    width=ValueJSON(
                        title_subtitle_model[title.col_count].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    height=ValueJSON(
                        title_subtitle_model[title.row_count].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    min_width=ValueJSON(title.min_width, Measure.PIXEL),
                    margin_right=ValueJSON(
                        title_subtitle_model[title.margin_right].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_left=ValueJSON(
                        title_subtitle_model[title.margin_left].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_top=ValueJSON(
                        title_subtitle_model[title.margin_top].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_bottom=ValueJSON(
                        title_subtitle_model[title.margin_bottom].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    text=title.text,
                    text_align="start",
                    label=title.label,
                    flexgrow=title.is_flexwidth,
                    css={"color": "primary", "font-weight": random.choice(["500", "600", "700"])}
                )
                subtitle_json = BaseElementJSON(
                    "h5",
                    x=ValueJSON(
                        title_subtitle_model[
                            subtitle.x].as_long() * title_subtitle.table.cell_width * 100 / title_subtitle.get_width_with_parent(
                            titles_subtitles_model), Measure.PERCENT),
                    y=ValueJSON(
                        title_subtitle_model[subtitle.y].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    width=ValueJSON(
                        title_subtitle_model[subtitle.col_count].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    height=ValueJSON(
                        title_subtitle_model[subtitle.row_count].as_long() * title_subtitle.table.cell_width * 100 /
                        title_subtitle.get_width_with_parent(titles_subtitles_model), Measure.PERCENT),
                    min_width=ValueJSON(subtitle.min_width, Measure.PIXEL),
                    margin_right=ValueJSON(
                        title_subtitle_model[subtitle.margin_right].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_left=ValueJSON(
                        title_subtitle_model[subtitle.margin_left].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_top=ValueJSON(
                        title_subtitle_model[subtitle.margin_top].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    margin_bottom=ValueJSON(
                        title_subtitle_model[subtitle.margin_bottom].as_long() * title_subtitle.table.cell_width,
                        Measure.PIXEL),
                    text=subtitle.text,
                    text_align="start",
                    label=subtitle.label,
                    flexgrow=subtitle.is_flexwidth,
                    css={"filter": "brightness(3.0)"}
                )
                title_subtitle_div.children.append(title_json)
                title_subtitle_div.children.append(subtitle_json)
                titles_subtitles_div_json.children.append(title_subtitle_div)
            card_json.children.append(titles_subtitles_div_json)
        if buttons:
            buttons_div_json = create_div(buttons, card, card_model, cards_model)
            for i in range(len(buttons.children)):
                if i == 0:
                    css = {"color": "primary"}
                else:
                    css = {"color": "secondary"}
                button_json = BaseElementJSON(
                    "button",
                    x=ValueJSON(
                        buttons_model[
                            buttons.children[
                                i].x].as_long() * buttons.table.cell_width * 100 / buttons.get_width_with_parent(
                            card_model), Measure.PERCENT),
                    y=ValueJSON(
                        buttons_model[
                            buttons.children[
                                i].y].as_long() * buttons.table.cell_height * 100 / buttons.get_height_with_parent(
                            card_model), Measure.PERCENT),
                    width=ValueJSON(buttons_model[buttons.children[i].col_count].as_long() * buttons.table.cell_width,
                                    Measure.PIXEL),
                    height=ValueJSON(buttons_model[buttons.children[i].row_count].as_long() * buttons.table.cell_height,
                                     Measure.PIXEL),
                    margin_right=ValueJSON(
                        buttons_model[buttons.children[i].margin_right].as_long() * buttons.table.cell_width,
                        Measure.PIXEL),
                    margin_left=ValueJSON(
                        buttons_model[buttons.children[i].margin_left].as_long() * buttons.table.cell_width,
                        Measure.PIXEL),
                    margin_top=ValueJSON(
                        buttons_model[buttons.children[i].margin_top].as_long() * buttons.table.cell_height,
                        Measure.PIXEL),
                    margin_bottom=ValueJSON(
                        buttons_model[buttons.children[i].margin_bottom].as_long() * buttons.table.cell_height,
                        Measure.PIXEL),
                    padding_right=ValueJSON(1, Measure.EM),
                    padding_left=ValueJSON(1, Measure.EM),
                    padding_top=ValueJSON(0.5, Measure.EM),
                    padding_bottom=ValueJSON(0.5, Measure.EM),
                    label=buttons.children[i].label,
                    text=buttons.children[i].text,
                    text_align="center",
                    css=css
                )
                buttons_div_json.children.append(button_json)
            sort_children(buttons_div_json)
            card_json.children.append(buttons_div_json)

        icons_texts = card.icons_texts
        if icons_texts:
            for icon_text in icons_texts:
                icon_text_model = random_choose_model(icon_text, card_model)
                icon_text_json = create_div(
                    icon_text,
                    card,
                    card_model,
                    cards_model,
                )
                icon = icon_text.icon
                icon_json = IconButtonJSON(
                    icon.name,
                    x=ValueJSON(
                        icon_text_model[
                            icon.x].as_long() * icon_text.table.cell_width * 100 / icon_text.get_width_with_parent(
                            card_model), Measure.PERCENT),
                    y=ValueJSON(
                        icon_text_model[
                            icon.y].as_long() * icon_text.table.cell_height * 100 / icon_text.get_height_with_parent(
                            card_model), Measure.PERCENT),
                    width=ValueJSON(icon_text_model[icon.col_count].as_long() * icon_text.table.cell_width,
                                    Measure.PIXEL),
                    height=ValueJSON(icon_text_model[icon.row_count].as_long() * icon_text.table.cell_height,
                                     Measure.PIXEL),
                    margin_right=ValueJSON(icon_text_model[icon.margin_right].as_long() * icon_text.table.cell_width,
                                           Measure.PIXEL),
                    margin_left=ValueJSON(icon_text_model[icon.margin_left].as_long() * icon_text.table.cell_width,
                                          Measure.PIXEL),
                    margin_top=ValueJSON(icon_text_model[icon.margin_top].as_long() * icon_text.table.cell_height,
                                         Measure.PIXEL),
                    margin_bottom=ValueJSON(icon_text_model[icon.margin_bottom].as_long() * icon_text.table.cell_height,
                                            Measure.PIXEL),
                    font_size=ValueJSON(icon_text_model[icon.col_count].as_long() * icon_text.table.cell_width,
                                        Measure.PIXEL),
                    label=icon.label,
                )
                text = icon_text.text
                text_json = BaseElementJSON(
                    "p",
                    x=ValueJSON(
                        icon_text_model[
                            text.x].as_long() * icon_text.table.cell_width * 100 / icon_text.get_width_with_parent(
                            card_model), Measure.PERCENT),
                    y=ValueJSON(
                        icon_text_model[
                            text.y].as_long() * icon_text.table.cell_height * 100 / icon_text.get_height_with_parent(
                            card_model), Measure.PERCENT),
                    width=ValueJSON("auto", Measure.WORD),
                    height=ValueJSON(icon_text_model[
                                         text.row_count].as_long() * icon_text.table.cell_height * 100 / icon_text.get_height_with_parent(
                        card_model), Measure.PERCENT),
                    min_width=ValueJSON(text.min_width, Measure.PIXEL),
                    margin_right=ValueJSON(icon_text_model[text.margin_right].as_long() * icon_text.table.cell_width,
                                           Measure.PIXEL),
                    margin_left=ValueJSON(icon_text_model[text.margin_left].as_long() * icon_text.table.cell_width,
                                          Measure.PIXEL),
                    margin_top=ValueJSON(icon_text_model[text.margin_top].as_long() * icon_text.table.cell_height,
                                         Measure.PIXEL),
                    margin_bottom=ValueJSON(
                        icon_text_model[text.margin_bottom].as_long() * icon_text.table.cell_height,
                        Measure.PIXEL),
                    text=text.text,
                    text_align="start",
                    label=text.label,
                    flexgrow=text.is_flexwidth,
                    css={"font-weight": random.choice(["500", "600", "700"])}
                )
                icon_text_json.children.append(icon_json)
                icon_text_json.children.append(text_json)
                card_json.children.append(icon_text_json)

        sort_children(card_json)
        group(card, card_model, card_json)
        sort_children(card_json)

        cards_json.children.append(card_json)

    content_json.children.append(cards_json)
    return content_json


def create_footer_json(footer, body_model, footer_model):
    footer_json = BaseElementJSON(
        "footer",
        x=ValueJSON(body_model[footer.x].as_long() * body.table.cell_width * 100 / body.width, Measure.PERCENT),
        y=ValueJSON(body_model[footer.y].as_long() * body.table.cell_width * 100 / body.height, Measure.PERCENT),
        width=ValueJSON(100,
                        Measure.PERCENT),
        height=ValueJSON(body_model[footer.row_count].as_long() * body.table.cell_height * 100 / body.height,
                         Measure.PERCENT),
        min_width=ValueJSON(footer.min_width, Measure.PIXEL),
        margin_left=ValueJSON(0, Measure.PIXEL),
        margin_right=ValueJSON(0, Measure.PIXEL),
        margin_top=ValueJSON(body_model[footer.margin_top].as_long() * body.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(body_model[footer.margin_bottom].as_long() * body.table.cell_height, Measure.PIXEL),
        label=footer.label,
        fullwidth=footer.is_fullwidth,
        justify_left=footer.justify_left,
        justify_right=footer.justify_right,
        center_horizontal=True,
        center_vertical=True
    )
    div_footer = footer.div_footer
    div_footer_model = random_choose_model(div_footer, footer_model)

    div_footer_json = create_div(div_footer, footer, footer_model, body_model, Measure.PERCENT)

    logo = div_footer.logo
    if logo:
        logo_json = IconButtonJSON(
            parent=div_footer_json,
            icon_name="adjust",
            x=ValueJSON(div_footer_model[
                            logo.x].as_long() * div_footer.table.cell_width * 100 / div_footer.get_width_with_parent(
                footer_model), Measure.PERCENT),
            y=ValueJSON(div_footer_model[
                            logo.y].as_long() * div_footer.table.cell_height * 100 / div_footer.get_height_with_parent(
                footer_model),
                        Measure.PERCENT),
            width=ValueJSON(div_footer_model[logo.col_count].as_long() * div_footer.table.cell_width, Measure.PIXEL),
            height=ValueJSON(div_footer_model[logo.row_count].as_long() * div_footer.table.cell_height, Measure.PIXEL),
            min_width=ValueJSON(logo.min_width, Measure.PIXEL),
            min_height=ValueJSON(logo.min_height, Measure.PIXEL),
            margin_left=ValueJSON(div_footer_model[logo.margin_left].as_long() * div_footer.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(div_footer_model[logo.margin_right].as_long() * div_footer.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(div_footer_model[logo.margin_top].as_long() * div_footer.table.cell_height,
                                 Measure.PIXEL),
            margin_bottom=ValueJSON(div_footer_model[logo.margin_bottom].as_long() * div_footer.table.cell_height,
                                    Measure.PIXEL),
            label=logo.label,
            font_size=ValueJSON(div_footer_model[logo.col_count].as_long() * div_footer.table.cell_width,
                                Measure.PIXEL),
        )
        div_footer_json.children.append(logo_json)

    links = div_footer.links
    if links:
        links_json = NavListJSON(
            nav_list=links.text_list.text_list,
            parent=div_footer_json,
            x=ValueJSON(div_footer_model[
                            links.x].as_long() * div_footer.table.cell_width * 100 / div_footer.get_width_with_parent(
                footer_model), Measure.PERCENT),
            y=ValueJSON(div_footer_model[
                            links.y].as_long() * div_footer.table.cell_height * 100 / div_footer.get_height_with_parent(
                footer_model), Measure.PERCENT),
            width=ValueJSON(
                div_footer_model[
                    links.col_count].as_long() * div_footer.table.cell_width * 100 / div_footer.get_width_with_parent(
                    footer_model),
                Measure.PERCENT),
            height=ValueJSON(
                div_footer_model[
                    links.row_count].as_long() * div_footer.table.cell_height * 100 / div_footer.get_height_with_parent(
                    footer_model),
                Measure.PERCENT),
            min_width=ValueJSON(links.min_width, Measure.PIXEL),
            min_height=ValueJSON(links.min_height, Measure.PIXEL),
            margin_left=ValueJSON(div_footer_model[links.margin_left].as_long() * div_footer.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(div_footer_model[links.margin_right].as_long() * div_footer.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(div_footer_model[links.margin_top].as_long() * div_footer.table.cell_height,
                                 Measure.PIXEL),
            margin_bottom=ValueJSON(div_footer_model[links.margin_bottom].as_long() * div_footer.table.cell_height,
                                    Measure.PIXEL),
            label=links.label,
            fullwidth=links.is_fullwidth,
            fullheight=links.is_fullheight,
            center_vertical=True,
            center_horizontal=True,
            flexgrow=links.is_flexwidth,
            flexflow="row nowrap"
        )
        div_footer_json.children.append(links_json)

    sn_icons = div_footer.sn_icons
    if sn_icons:
        sn_icons_model = random_choose_model(sn_icons, div_footer_model)
        random_justify(sn_icons)
        sn_icons_json = create_div(sn_icons, div_footer, div_footer_model, footer_model)

        for i in range(len(sn_icons.children)):
            sn_icons_json.children.append(
                IconButtonJSON(
                    parent=sn_icons_json,
                    icon_name=sn_icons.children[i].name,
                    x=ValueJSON(sn_icons_model[sn_icons.children[
                        i].x].as_long() * sn_icons.table.cell_width * 100 / sn_icons.get_width_with_parent(
                        div_footer_model),
                                Measure.PERCENT),
                    y=ValueJSON(sn_icons_model[sn_icons.children[
                        i].y].as_long() * sn_icons.table.cell_height * 100 / sn_icons.get_height_with_parent(
                        div_footer_model),
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
        div_footer_json.children.append(sn_icons_json)

    vert_lists = div_footer.vert_lists
    if vert_lists:
        vert_lists_model = random_choose_model(vert_lists, div_footer_model)
        vert_lists_json = create_div(vert_lists, div_footer, div_footer_model, footer_model)
        for vert_list in vert_lists.children:
            vert_list_model = random_choose_model(vert_list, vert_lists_model)
            vert_list_json = create_div(vert_list, vert_lists, vert_lists_model, div_footer_model,
                                        flexflow="column nowrap")
            title = vert_list.title
            link_list = vert_list.list
            title_json = BaseElementJSON(
                "h5",
                parent=vert_list_json,
                x=ValueJSON(vert_list_model[
                                title.x].as_long() * vert_list.table.cell_width * 100 / vert_list.get_width_with_parent(
                    vert_lists_model), Measure.PERCENT),
                y=ValueJSON(vert_list_model[
                                title.y].as_long() * vert_list.table.cell_height * 100 / vert_list.get_height_with_parent(
                    vert_lists_model), Measure.PERCENT),
                width=ValueJSON(vert_list_model[
                                    title.col_count].as_long() * vert_list.table.cell_width * 100 / vert_list.get_width_with_parent(
                    vert_lists_model), Measure.PERCENT),
                height=ValueJSON(vert_list_model[
                                     title.row_count].as_long() * vert_list.table.cell_height * 100 / vert_list.get_height_with_parent(
                    vert_lists_model), Measure.PERCENT),
                min_width=ValueJSON(title.min_width, Measure.PIXEL),
                margin_right=ValueJSON(vert_list_model[title.margin_right].as_long() * vert_list.table.cell_width,
                                       Measure.PIXEL),
                margin_left=ValueJSON(vert_list_model[title.margin_left].as_long() * vert_list.table.cell_width,
                                      Measure.PIXEL),
                margin_top=ValueJSON(vert_list_model[title.margin_top].as_long() * vert_list.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(vert_list_model[title.margin_bottom].as_long() * vert_list.table.cell_height,
                                        Measure.PIXEL),
                text=title.text,
                text_align="center",
                label=title.label,
                flexgrow=title.is_flexwidth,
                css={"color": "primary", "font-weight": random.choice(["500", "600", "700"])}
            )
            link_list_json = NavListJSON(
                link_list.text_list.text_list,
                parent=vert_list_json,
                x=ValueJSON(vert_list_model[
                                link_list.x].as_long() * vert_list.table.cell_width * 100 / vert_list.get_width_with_parent(
                    vert_lists_model), Measure.PERCENT),
                y=ValueJSON(vert_list_model[
                                link_list.y].as_long() * vert_list.table.cell_height * 100 / vert_list.get_height_with_parent(
                    vert_lists_model), Measure.PERCENT),
                width=ValueJSON(
                    vert_list_model[
                        link_list.col_count].as_long() * vert_list.table.cell_width * 100 / vert_list.get_width_with_parent(
                        vert_lists_model),
                    Measure.PERCENT),
                height=ValueJSON(
                    vert_list_model[
                        link_list.row_count].as_long() * vert_list.table.cell_height * 100 / vert_list.get_height_with_parent(
                        vert_lists_model),
                    Measure.PERCENT),
                min_width=ValueJSON(link_list.min_width, Measure.PIXEL),
                min_height=ValueJSON(link_list.min_height, Measure.PIXEL),
                margin_left=ValueJSON(vert_list_model[link_list.margin_left].as_long() * vert_list.table.cell_width,
                                      Measure.PIXEL),
                margin_right=ValueJSON(vert_list_model[link_list.margin_right].as_long() * vert_list.table.cell_width,
                                       Measure.PIXEL),
                margin_top=ValueJSON(vert_list_model[link_list.margin_top].as_long() * vert_list.table.cell_height,
                                     Measure.PIXEL),
                margin_bottom=ValueJSON(
                    vert_list_model[link_list.margin_bottom].as_long() * vert_list.table.cell_height,
                    Measure.PIXEL),
                label=link_list.label,
                fullwidth=link_list.is_fullwidth,
                fullheight=link_list.is_fullheight,
                center_vertical=True,
                center_horizontal=True,
                flexgrow=link_list.is_flexwidth,
                flexflow="column nowrap"
            )
            vert_list_json.children.append(title_json)
            vert_list_json.children.append(link_list_json)
            vert_lists_json.children.append(vert_list_json)
        div_footer_json.children.append(vert_lists_json)

    sort_children(div_footer_json)
    group(div_footer, div_footer_model, div_footer_json)
    footer_json.children.append(div_footer_json)
    return footer_json


def create_header_json(header, body_model, header_model):
    header_json = BaseElementJSON(
        "header",
        x=ValueJSON(body_model[header.x].as_long() * body.table.cell_width * 100 / body.width, Measure.PERCENT),
        y=ValueJSON(body_model[header.y].as_long() * body.table.cell_width * 100 / body.height, Measure.PERCENT),
        width=ValueJSON(100,
                        Measure.PERCENT),
        height=ValueJSON(body_model[header.row_count].as_long() * body.table.cell_height * 100 / body.height,
                         Measure.PERCENT),
        min_width=ValueJSON(header.min_width, Measure.PIXEL),
        min_height=ValueJSON(header.min_height, Measure.PIXEL),
        margin_left=ValueJSON(0, Measure.PIXEL),
        margin_right=ValueJSON(0, Measure.PIXEL),
        margin_top=ValueJSON(body_model[header.margin_top].as_long() * body.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(body_model[header.margin_bottom].as_long() * body.table.cell_height, Measure.PIXEL),
        label=header.label,
        fullwidth=header.is_fullwidth,
        justify_left=header.justify_left,
        justify_right=header.justify_right,
        center_horizontal=True,
        center_vertical=True
    )
    div_header = header.div_header
    div_header_model = random_choose_model(div_header, header_model)

    div_header_json = create_div(div_header, header, header_model, body_model, Measure.PERCENT)

    logo = div_header.logo
    if logo:
        logo_json = IconButtonJSON(
            parent=div_header_json,
            icon_name="adjust",
            x=ValueJSON(div_header_model[
                            logo.x].as_long() * div_header.table.cell_width * 100 / div_header.get_width_with_parent(
                header_model), Measure.PERCENT),
            y=ValueJSON(div_header_model[
                            logo.y].as_long() * div_header.table.cell_height * 100 / div_header.get_height_with_parent(
                header_model),
                        Measure.PERCENT),
            width=ValueJSON(div_header_model[logo.col_count].as_long() * div_header.table.cell_width, Measure.PIXEL),
            height=ValueJSON(div_header_model[logo.row_count].as_long() * div_header.table.cell_height, Measure.PIXEL),
            min_width=ValueJSON(logo.min_width, Measure.PIXEL),
            min_height=ValueJSON(logo.min_height, Measure.PIXEL),
            margin_left=ValueJSON(div_header_model[logo.margin_left].as_long() * div_header.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(div_header_model[logo.margin_right].as_long() * div_header.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(div_header_model[logo.margin_top].as_long() * div_header.table.cell_height,
                                 Measure.PIXEL),
            margin_bottom=ValueJSON(div_header_model[logo.margin_bottom].as_long() * div_header.table.cell_height,
                                    Measure.PIXEL),
            label=logo.label,
            font_size=ValueJSON(div_header_model[logo.col_count].as_long() * div_header.table.cell_width,
                                Measure.PIXEL),
        )
        div_header_json.children.append(logo_json)

    nav = div_header.nav
    if nav:
        nav_json = NavListJSON(
            nav_list=nav.text_list.text_list,
            parent=div_header_json,
            x=ValueJSON(div_header_model[
                            nav.x].as_long() * div_header.table.cell_width * 100 / div_header.get_width_with_parent(
                header_model), Measure.PERCENT),
            y=ValueJSON(div_header_model[
                            nav.y].as_long() * div_header.table.cell_height * 100 / div_header.get_height_with_parent(
                header_model), Measure.PERCENT),
            width=ValueJSON(
                div_header_model[
                    nav.col_count].as_long() * div_header.table.cell_width * 100 / div_header.get_width_with_parent(
                    header_model),
                Measure.PERCENT),
            height=ValueJSON(
                div_header_model[
                    nav.row_count].as_long() * div_header.table.cell_height * 100 / div_header.get_height_with_parent(
                    header_model),
                Measure.PERCENT),
            min_width=ValueJSON(nav.min_width, Measure.PIXEL),
            min_height=ValueJSON(nav.min_height, Measure.PIXEL),
            margin_left=ValueJSON(div_header_model[nav.margin_left].as_long() * div_header.table.cell_width,
                                  Measure.PIXEL),
            margin_right=ValueJSON(div_header_model[nav.margin_right].as_long() * div_header.table.cell_width,
                                   Measure.PIXEL),
            margin_top=ValueJSON(div_header_model[nav.margin_top].as_long() * div_header.table.cell_height,
                                 Measure.PIXEL),
            margin_bottom=ValueJSON(div_header_model[nav.margin_bottom].as_long() * div_header.table.cell_height,
                                    Measure.PIXEL),
            label=nav.label,
            fullwidth=nav.is_fullwidth,
            fullheight=nav.is_fullheight,
            center_vertical=True,
            center_horizontal=True,
            flexgrow=nav.is_flexwidth,
            flexflow="row nowrap",
            css={'font-weight': random.choice(['500', '600', '700']), 'color': '--primary'}
        )
        div_header_json.children.append(nav_json)

    search_div = div_header.search_div
    if search_div:
        search_div_model = random_choose_model(search_div, div_header_model)
        random_justify(search_div)
        search_bar_div_json = create_div(search_div, div_header, div_header_model, header_model, Measure.PERCENT)

        search_bar_json = BaseElementJSON(
            parent=search_bar_div_json,
            tag="input",
            x=ValueJSON(search_div_model[search_div.children[
                0].x].as_long() * search_div.table.cell_width * 100 / search_div.get_width_with_parent(
                div_header_model),
                        Measure.PERCENT),
            y=ValueJSON(search_div_model[search_div.children[
                0].y].as_long() * search_div.table.cell_height * 100 / search_div.get_height_with_parent(
                div_header_model),
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
        search_button = IconButtonJSON(
            parent=search_bar_div_json,
            icon_name='search',
            x=ValueJSON(search_div_model[search_div.children[
                0].x].as_long() * search_div.table.cell_width * 100 / search_div.get_width_with_parent(
                div_header_model), Measure.PERCENT),
            y=ValueJSON(search_div_model[search_div.children[
                0].y].as_long() * search_div.table.cell_height * 100 / search_div.get_height_with_parent(
                div_header_model), Measure.PERCENT),
            width=ValueJSON(
                search_div_model[search_div.children[0].row_count].as_long() * search_div.table.cell_height // 2,
                Measure.PIXEL),
            height=ValueJSON(
                search_div_model[search_div.children[0].row_count].as_long() * search_div.table.cell_height,
                Measure.PIXEL),
            font_size=ValueJSON(
                search_div_model[search_div.children[0].row_count].as_long() * search_div.table.cell_height // 2,
                Measure.PIXEL),
            margin_right=ValueJSON(0, Measure.PIXEL),
            margin_left=ValueJSON(
                -search_div_model[search_div.children[0].row_count].as_long() * search_div.table.cell_height,
                Measure.PIXEL),
            margin_top=ValueJSON(0, Measure.PIXEL),
            margin_bottom=ValueJSON(0, Measure.PIXEL),
            label='search_butt',
        )
        search_bar_div_json.children.append(search_bar_json)
        search_bar_div_json.children.append(search_button)
        div_header_json.children.append(search_bar_div_json)

    icls_icons = div_header.icls_icons
    if icls_icons:
        icls_icons_model = random_choose_model(icls_icons, div_header_model)
        random_justify(icls_icons)
        icls_icons_json = create_div(icls_icons, div_header, div_header_model, header_model)

        for i in range(len(icls_icons.children)):
            icls_icons_json.children.append(
                IconButtonJSON(
                    icon_name=icls_icons.children[i].name,
                    x=ValueJSON(icls_icons_model[icls_icons.children[
                        i].x].as_long() * icls_icons.table.cell_width * 100 / icls_icons.get_width_with_parent(
                        div_header_model), Measure.PERCENT),
                    y=ValueJSON(icls_icons_model[icls_icons.children[
                        i].y].as_long() * header.table.cell_height * 100 / icls_icons.get_height_with_parent(
                        div_header_model), Measure.PERCENT),
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
        div_header_json.children.append(icls_icons_json)

    sn_icons = div_header.sn_icons
    if sn_icons:
        sn_icons_model = random_choose_model(sn_icons, div_header_model)
        random_justify(sn_icons)
        sn_icons_json = create_div(sn_icons, div_header, div_header_model, header_model)

        for i in range(len(sn_icons.children)):
            sn_icons_json.children.append(
                IconButtonJSON(
                    parent=sn_icons_json,
                    icon_name=sn_icons.children[i].name,
                    x=ValueJSON(sn_icons_model[sn_icons.children[
                        i].x].as_long() * sn_icons.table.cell_width * 100 / sn_icons.get_width_with_parent(
                        div_header_model),
                                Measure.PERCENT),
                    y=ValueJSON(sn_icons_model[sn_icons.children[
                        i].y].as_long() * sn_icons.table.cell_height * 100 / sn_icons.get_height_with_parent(
                        div_header_model),
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
        div_header_json.children.append(sn_icons_json)

    sort_children(div_header_json)
    group(div_header, div_header_model, div_header_json)
    header_json.children.append(div_header_json)
    return header_json


def sort_children(parent):
    arr = sorted(parent.children, key=lambda child: (child.y.val, child.x.val))

    # if arr[j].y.val > arr[i].y.val:
    #    arr[i], arr[j] = arr[j], arr[i]

    parent.children = arr


def group(parent, parent_model, parent_json):
    for child in parent.children:
        child.right = []
        child.left = []
        child.top = []
        child.bottom = []
        for another_child in parent.children:
            if child.label != another_child.label:
                child_x = parent_model[child.x].as_long()
                child_y = parent_model[child.y].as_long()
                child_width = parent_model[child.col_count].as_long()
                child_height = parent_model[child.row_count].as_long()
                child_margin_left = parent_model[child.margin_left].as_long()
                child_margin_right = parent_model[child.margin_right].as_long()
                child_margin_bottom = parent_model[child.margin_bottom].as_long()
                child_margin_top = parent_model[child.margin_top].as_long()
                another_child_x = parent_model[another_child.x].as_long()
                another_child_y = parent_model[another_child.y].as_long()
                another_child_width = parent_model[another_child.col_count].as_long()
                another_child_height = parent_model[another_child.row_count].as_long()
                another_child_margin_left = parent_model[another_child.margin_left].as_long()
                another_child_margin_right = parent_model[another_child.margin_right].as_long()
                another_child_margin_bottom = parent_model[another_child.margin_bottom].as_long()
                another_child_margin_top = parent_model[another_child.margin_top].as_long()

                if ((child_x + child_width + child_margin_right <= another_child_x - another_child_margin_left) and
                        (
                                another_child_y - another_child_margin_top < child_y - child_margin_top <= another_child_y + another_child_height + another_child_margin_bottom or
                                child_y - child_margin_top < another_child_y - another_child_margin_top <= child_y + child_height + child_margin_bottom)
                ):
                    child.right.append(another_child)
                elif ((
                              another_child_x + another_child_width + another_child_margin_right <= child_x - child_margin_left) and
                      (
                              another_child_y - another_child_margin_top <= child_y - child_margin_top <= another_child_y + another_child_height + another_child_margin_bottom or
                              child_y - child_margin_top <= another_child_y - another_child_margin_top <= child_y + child_height + child_margin_bottom)
                ):
                    child.left.append(another_child)
                elif ((child_y + child_height + child_margin_bottom <= another_child_y - another_child_margin_top) and
                      (
                              another_child_x - another_child_margin_left <= child_x - child_margin_left <= another_child_x + another_child_width + another_child_margin_right or
                              child_x - child_margin_left <= another_child_x - another_child_margin_left <= child_x + child_width + child_margin_right)
                ):
                    child.bottom.append(another_child)
                elif ((
                              another_child_y + another_child_height + another_child_margin_bottom <= child_y - child_margin_top) and
                      (
                              another_child_x - another_child_margin_left <= child_x - child_margin_left <= another_child_x + another_child_width + another_child_margin_right or
                              child_x - child_margin_left <= another_child_x - another_child_margin_left <= child_x + child_width + child_margin_right)
                ):
                    child.top.append(another_child)
        child.min_bottom = []
        child.min_top = []
        if len(child.bottom) > 0:
            arr = []
            min_d = 100000
            for another_child in child.bottom:
                s = parent_model[another_child.y].as_long() - parent_model[another_child.margin_top].as_long() - \
                    parent_model[child.y].as_long() - parent_model[child.margin_bottom].as_long() - parent_model[
                        child.row_count].as_long()
                # t = (
                #        parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <= parent_model[another_child.x].as_long() - parent_model[another_child.margin_left].as_long() <= parent_model[child.x].as_long() + parent_model[child.col_count].as_long() + parent_model[child.margin_right].as_long() and
                #        parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <= parent_model[another_child.x].as_long() + parent_model[another_child.col_count].as_long() + parent_model[another_child.margin_right].as_long() <= parent_model[child.x].as_long() + parent_model[child.col_count].as_long() + parent_model[child.margin_right].as_long()
                # )
                if s < min_d:
                    min_d = s
                    arr = [another_child]
                elif s == min_d:
                    arr.append(another_child)
            child.min_bottom = arr
        if len(child.top) > 0:
            arr = []
            min_d = 100000
            for another_child in child.top:
                s = parent_model[child.y].as_long() - parent_model[child.margin_top].as_long() - parent_model[
                    another_child.y].as_long() - parent_model[another_child.margin_bottom].as_long() - parent_model[
                        another_child.row_count].as_long()
                if s < min_d:
                    min_d = s
                    arr = [another_child]
                elif s == min_d:
                    arr.append(another_child)
            child.min_top = arr
        print("\n\nneighbours")
        print(child.name)
        if child.name == 'card_icon_text':
            print()
        print("Right:" + ",".join(ch.name for ch in child.right))
        print("Left:" + ",".join(ch.name for ch in child.left))
        print("Bottom:" + ",".join(ch.name for ch in child.bottom))
        print("Top:" + ",".join(ch.name for ch in child.top))
    for child in parent.children:
        div = []
        if len(child.left) + len(child.right) > 0:
            div = [child]
            print("----------")
            print("child name: " + child.name)
            for another_child in child.min_bottom + child.min_top:
                if len(another_child.right) + len(another_child.left) > 0:
                    print("Min top bottom children")
                    print(another_child.name)
                    t = (
                            parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <= parent_model[
                        another_child.x].as_long() - parent_model[another_child.margin_left].as_long() <= parent_model[
                                child.x].as_long() + parent_model[child.col_count].as_long() + parent_model[
                                child.margin_right].as_long() and
                            parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <= parent_model[
                                another_child.x].as_long() + parent_model[another_child.col_count].as_long() +
                            parent_model[
                                another_child.margin_right].as_long() <= parent_model[child.x].as_long() + parent_model[
                                child.col_count].as_long() + parent_model[child.margin_right].as_long()
                    )
                    d = (
                            parent_model[another_child.x].as_long() - parent_model[
                        another_child.margin_left].as_long() <= parent_model[
                                another_child.x].as_long() - parent_model[child.margin_left].as_long() <= parent_model[
                                another_child.x].as_long() + parent_model[another_child.col_count].as_long() +
                            parent_model[
                                another_child.margin_right].as_long() and
                            parent_model[another_child.x].as_long() - parent_model[
                                another_child.margin_left].as_long() <= parent_model[
                                child.x].as_long() + parent_model[another_child.col_count].as_long() +
                            parent_model[another_child.margin_right].as_long() <= parent_model[
                                another_child.x].as_long() +
                            parent_model[another_child.col_count].as_long() + parent_model[
                                another_child.margin_right].as_long()
                    )
                    if t or d:
                        div.append(another_child)
                        for neighbour in another_child.right + another_child.left:
                            # если координаты внутри координат элемента
                            nt = (
                                    parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <=
                                    parent_model[
                                        neighbour.x].as_long() - parent_model[neighbour.margin_left].as_long() <=
                                    parent_model[
                                        child.x].as_long() + parent_model[child.col_count].as_long() + parent_model[
                                        child.margin_right].as_long() and
                                    parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() <=
                                    parent_model[
                                        neighbour.x].as_long() + parent_model[neighbour.col_count].as_long() +
                                    parent_model[neighbour.margin_right].as_long() <= parent_model[child.x].as_long() +
                                    parent_model[child.col_count].as_long() + parent_model[child.margin_right].as_long()
                            )
                            # если сосед под или над элементом
                            nu = (
                                    (parent_model[child.y].as_long() - parent_model[child.margin_top].as_long() >=
                                     parent_model[neighbour.y].as_long() + parent_model[neighbour.row_count].as_long() +
                                     parent_model[neighbour.margin_bottom].as_long())
                                    or
                                    (parent_model[neighbour.y].as_long() - parent_model[
                                        neighbour.margin_top].as_long() >= parent_model[child.y].as_long() +
                                     parent_model[child.row_count].as_long() + parent_model[
                                         child.margin_bottom].as_long())
                            )
                            # если одна из координат соседа вне координат элемента
                            nw = (
                                    (parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() >=
                                     parent_model[neighbour.x].as_long() - parent_model[
                                         neighbour.margin_left].as_long() and
                                     parent_model[neighbour.x].as_long() + parent_model[neighbour.col_count].as_long() +
                                     parent_model[neighbour.margin_right].as_long() <= parent_model[child.x].as_long() +
                                     parent_model[child.col_count].as_long() + parent_model[
                                         child.margin_right].as_long())
                                    or
                                    (parent_model[neighbour.x].as_long() + parent_model[neighbour.col_count].as_long() +
                                     parent_model[neighbour.margin_right].as_long() >= parent_model[child.x].as_long() +
                                     parent_model[child.col_count].as_long() + parent_model[
                                         child.margin_right].as_long() and
                                     parent_model[child.x].as_long() - parent_model[child.margin_left].as_long() >=
                                     parent_model[neighbour.x].as_long() - parent_model[
                                         neighbour.margin_left].as_long())
                            )

                            # если координаты элемента внутри координат соседа
                            nd = (
                                    parent_model[neighbour.x].as_long() - parent_model[
                                neighbour.margin_left].as_long() <= parent_model[
                                        neighbour.x].as_long() - parent_model[child.margin_left].as_long() <=
                                    parent_model[
                                        neighbour.x].as_long() + parent_model[neighbour.col_count].as_long() +
                                    parent_model[
                                        neighbour.margin_right].as_long() and
                                    parent_model[neighbour.x].as_long() - parent_model[
                                        neighbour.margin_left].as_long() <= parent_model[
                                        child.x].as_long() + parent_model[neighbour.col_count].as_long() +
                                    parent_model[neighbour.margin_right].as_long() <= parent_model[
                                        neighbour.x].as_long() +
                                    parent_model[neighbour.col_count].as_long() + parent_model[
                                        neighbour.margin_right].as_long()
                            )
                            if nt or nd:
                                div.append(neighbour)
                            elif nw and nu:
                                print(f"nw neighbour:  {neighbour.label}")
                                div = []
            div_json = None
            # То есть есть элементы, которые можно объединить в один див
            if len(div) > 1:
                print(", ".join(el.name for el in div))
                arr = []
                for el in div:
                    for el_json in parent_json.children:
                        if el.label == el_json.label:
                            arr.append(el_json)
                if len(arr) > 1:
                    for el_json in arr:
                        if hasattr(el_json, "div"):
                            div_json = el_json.div
                            break
                    if not div_json:
                        div_json = BaseElementJSON(
                            "div",
                            ValueJSON(0, Measure.WORD),
                            ValueJSON(0, Measure.WORD),
                            ValueJSON(max([child.min_width + child.min_margin_right + child.min_margin_left for child in
                                           div]), Measure.PIXEL),
                            ValueJSON(0, Measure.WORD),
                            ValueJSON(0, Measure.PIXEL),
                            ValueJSON(0, Measure.PIXEL),
                            ValueJSON(0, Measure.PIXEL),
                            ValueJSON(0, Measure.PIXEL),
                            "unite_div" + str(len(arr)) + parent_json.label + arr[0].label,
                            center_horizontal=parent_json.center_horizontal,
                            center_vertical=parent_json.center_vertical,
                            flexflow=parent_json.flexflow,
                            flexgrow=1,
                            justify_left=parent_json.justify_left,
                            justify_right=parent_json.justify_right
                        )
                        # parent_json.children.append(div_json)
                    for el_json in arr:
                        if not hasattr(el_json, "div"):
                            div_json.children.append(el_json)
                            el_json.div = div_json
                            el_json.parent = div_json
                            el_json.width = get_new_width(el_json, parent_json)
                    sort_children(div_json)
                    div_json.x = ValueJSON(min(el.x.val for el in div_json.children), Measure.PIXEL)
                    div_json.y = ValueJSON(min(el.y.val for el in div_json.children), Measure.PIXEL)
                    div_json.height = ValueJSON(max(el.height.val for el in div_json.children),
                                                Measure.WORD)  # для сортировки, в хтмл не используется
                    print(f"div_json.x: {div_json.x}")
                    print(f"div_json.y: {div_json.y}")
    for i in range(len(parent_json.children) - 1, -1, -1):
        if hasattr(parent_json.children[i], "div"):
            if parent_json.children[i].div not in parent_json.children:
                parent_json.children.append(parent_json.children[i].div)
            parent_json.children.pop(i)


def get_new_width(el_json, prev_parent_json):
    width = el_json.width
    if el_json.width.measure == Measure.PERCENT:
        if prev_parent_json.width.measure == Measure.PIXEL:
            width = ValueJSON(el_json.width.val * el_json.parent.width.val / prev_parent_json.width.val,
                              Measure.PERCENT)
    return width


def random_choose_model(child, parent_model):
    models = []
    print(child.name)
    print(len(child.models))

    for model in child.models:
        # if model.parent.m == parent_model:
        models.append(model)

    print(f"{child.label} models count: {len(models)}")
    return random.choice(child.models).m


def generate_html(parent):
    doc, tag, text = Doc().tagtext()
    styles = []
    generate_html_style(styles)
    generate_style(parent, styles)
    with tag('html'):
        with tag('head'):
            doc.stag("link", rel="stylesheet",
                     href="https://pro.fontawesome.com/releases/v5.13.0/css/all.css")
            doc.stag("link", rel="stylesheet",
                     href="http://fortawesome.github.io/Font-Awesome/assets/font-awesome/css/font-awesome.css")
            with tag('style'):
                doc.text("".join(styles))
        with tag('body'):
            generate_element_html(parent, doc, tag)
    res = doc.getvalue()
    return res


def random_justify(parent):
    # rc = random.choice([0, 1, 2])
    rc = random.choice([1, 2])
    if rc == 0:
        parent.center_horizontal = True
    elif rc == 1:
        parent.justify_right = True
    else:
        parent.justify_left = True


def generate_element_html(element, doc, tag):
    if element.tag == 'input':
        doc.stag(element.tag, ('type', 'text'), ('class', element.label))
    elif element.tag == 'img':
        doc.stag(element.tag, ('src', element.text), ('alt', element.label), ('class', element.label))
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


def generate_html_style(styles):
    primary, secondary, black, white = generate_color()
    theme = random.choice([0, 1])
    if theme == 0:
        font_color = "--white"
        background = "--black"
    else:
        font_color = "--black"
        background = "--white"
    styles.append(
        f"""html {{
    font-size: {random.uniform(1.0, 1.2)}em;
    --primary: {primary};
    --secondary: {secondary};
    font: "Roboto","Arial",sans-serif;
    --black: {black};
    --white: {white};
    --color: {font_color};
    --background: {background};
    color: var({font_color});
    background: var({background});
    }}
    a, a:hover, a:focus, a:active {{
    text-decoration: none;
    color: inherit;
    }}
    input, textarea, select {{ font-family:inherit; }}
        """
    )


def generate_color():
    black = random.choice(["#0e1111", "#333", "#28282B"])
    white = random.choice(["#fafafa", "#f5f5f5", "#eeeeee"])

    h = random.uniform(0.3, 1.0)
    s = random.uniform(0.2, 0.8)
    v = random.uniform(0.4, 0.8)
    v2 = v + 0.15
    print(f"H: {h}, S: {s}, V: {v}")
    primary = colorsys.hsv_to_rgb(h, s, v)
    secondary = colorsys.hsv_to_rgb(h, s, v2)
    primary = f"#{'%02x%02x%02x' % (int(primary[0] * 255), int(primary[1] * 255), int(primary[2] * 255))}"
    secondary = f"#{'%02x%02x%02x' % (int(secondary[0] * 255), int(secondary[1] * 255), int(secondary[2] * 255))}"
    return primary, secondary, black, white


def generate_style(parent, styles):
    styles.append(
        f""".{parent.label} {{
        flex-grow: {parent.flexgrow};
        flex-basis: {parent.width};
        font-size: {parent.font_size};   
        min-width:{parent.min_width};
        min-height:{parent.min_height};
        max-height:{parent.max_height};
        margin-right: {parent.margin_right};
        margin-left: {parent.margin_left};
        margin-top: {parent.margin_top};
        margin-bottom: {parent.margin_bottom};
        padding-left: {parent.padding_left};
        padding-right: {parent.padding_right};
        padding-top: {parent.padding_top};
        padding-bottom: {parent.padding_bottom};
        text-align: {parent.text_align};
        """)

    if parent.tag == 'button':
        styles += style_button()
    elif parent.tag == 'header':
        styles += style_header()
    elif parent.tag == 'footer':
        styles += style_footer()
    elif parent.tag == 'aside':
        styles += style_aside()
    elif parent.tag == 'input':
        styles += style_input()
    for key in parent.css.keys():
        if key != "color":
            styles += f"{key}: {parent.css[key]};\n"

    styles += get_element_colors(parent)
    if len(parent.children) > 0:
        if parent.center_vertical:
            styles += "align-items: center;\n"
        else:
            styles += "align-items: flex-start;\n"
        if parent.center_horizontal:
            styles += "justify-content: center;\n"
        elif parent.justify_left:
            styles += "justify-content: start;\n"
        elif parent.justify_right:
            styles += "justify-content: end;\n"
        styles += f"display: flex;\nalign-content: {parent.align_content};\nflex-flow: {parent.flexflow};\n}}"

        children = []
        for child in parent.children:
            if child.label not in [ch.label for ch in children]:
                children.append(child)
        for child in children:
            generate_style(child, styles)
    else:
        styles.append("\n}\n")


def get_element_colors(el):
    if el.tag == "button":
        if el.css["color"] == "primary":
            colors_type = random.choice(["background", "text"])
            if colors_type == "background":
                text_color = random.choice(["--black", "--white"])
                return f"""
                background: var(--primary);
                color: var({text_color});
                """
            elif colors_type == "text":
                return """
                    box-sizing: border-box;
                    -moz-box-sizing: border-box;
                    -webkit-box-sizing: border-box;
                    border: 2px solid;
                    border-color: var(--primary);
                    color: var(--primary);
                    background: var(--background);
                """
        elif el.css["color"] == "secondary":

            return """
                    box-sizing: border-box;
                    -moz-box-sizing: border-box;
                    -webkit-box-sizing: border-box;
                    border: 2px solid;
                    border-color: var(--secondary);
                    color: var(--secondary);
                    background: var(--background);
                """
    elif el.tag == "i":
        color = random.choice(["--color", "--primary", "--secondary"])
        if color == "--color":
            return f"""
            color: var({color});
            filter: brightness(3.0);
            """
        return f"""
        color: var({color});
        """
    elif el.tag == "h5" and "color" in el.css.keys():
        if el.css["color"] == "primary":
            return f"""
            color: var({random.choice(['--color', '--primary'])});
            """
    return ""


def style_input():
    roundness = random.randint(2, 20)
    border_size = random.randint(1, 3)
    border_color = random.choice(['--primary', '--black', '--secondary'])
    return (
        f"""
        border-radius: {roundness}px;
        padding-left: 10px;
        border: {border_size}px var({border_color}) solid;
        """
    )


def style_button():
    roundness = random.randint(2, 20)
    font_weight = random.choice([500, 600, 700])
    return (
        f"""border: 0;
        border-radius: {roundness}px;
        font-weight: {font_weight};
        cursor: pointer;
        """
    )


def style_aside():
    return f"""
    border-right: 1px solid #dfdee2;
    """


def style_header():
    return f"""
        background: var({random.choice(["--secondary", "--background"])});
        border-bottom: 1px solid #dfdee2;
    """


def style_footer():
    return f"""
        background: var({random.choice(["--secondary", "--background"])});
        border-top: 1px solid #dfdee2;
    """


def create_div(child, parent, parent_model, parent_parent_model, measure=Measure.PIXEL, flexflow="row wrap"):
    if measure == Measure.PIXEL:
        width = ValueJSON(parent_model[child.col_count].as_long() * parent.table.cell_width, measure)
        height = ValueJSON(parent_model[child.row_count].as_long() * parent.table.cell_height, measure)
    else:
        width = ValueJSON(
            parent_model[child.col_count].as_long() * parent.table.cell_width * 100 / parent.get_width_with_parent(
                parent_parent_model), measure)
        height = ValueJSON(
            parent_model[child.row_count].as_long() * parent.table.cell_height * 100 / parent.get_height_with_parent(
                parent_parent_model), measure)
    return BaseElementJSON(
        "div",
        x=ValueJSON(parent_model[child.x].as_long() * parent.table.cell_width * 100 / parent.get_width_with_parent(
            parent_parent_model), Measure.PERCENT),
        y=ValueJSON(parent_model[child.y].as_long() * parent.table.cell_height * 100 / parent.get_height_with_parent(
            parent_parent_model), Measure.PERCENT),
        width=width,
        height=height,
        margin_left=ValueJSON(parent_model[child.margin_left].as_long() * parent.table.cell_width, Measure.PIXEL),
        margin_right=ValueJSON(parent_model[child.margin_right].as_long() * parent.table.cell_width, Measure.PIXEL),
        margin_top=ValueJSON(parent_model[child.margin_top].as_long() * parent.table.cell_height, Measure.PIXEL),
        margin_bottom=ValueJSON(parent_model[child.margin_bottom].as_long() * parent.table.cell_height, Measure.PIXEL),
        min_width=ValueJSON(child.min_width, Measure.PIXEL),
        label=child.label,
        center_horizontal=child.center_horizontal,
        center_vertical=child.center_vertical,
        fullwidth=child.is_fullwidth,
        justify_left=child.justify_left,
        justify_right=child.justify_right,
        flexgrow=child.is_flexwidth,
        flexflow=flexflow,
    )


for i in range(len(footer.models)):
    with open(f'{i}_test.html', 'w') as f:
        f.write(generate_html(create_body(body.models[0].m)))
        f.close()
