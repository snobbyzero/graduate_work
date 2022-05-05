import colorsys
import random
from faker import Faker

from classes.BaseElement import BaseElement
from content_element import create_content_element
from footer_element import create_footer_element
from header_element import create_header_element
from datetime import datetime
import time
import matplotlib.pyplot as plt

from json_classes.BaseElementJSON import BaseElementJSON
from json_classes.Measure import Measure
from json_classes.ValueJSON import ValueJSON
from layout_solver import create_body, find_solutions
from yattag import Doc


times = []
times_all = []


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


def generate_element_html(element, doc, tag):
    if element.tag == 'input':
        doc.stag(element.tag, ('type', 'text'), ('class', element.label), ('placeholder', element.text))
    elif element.tag == 'img':
        doc.stag(element.tag, ('src', element.text), ('alt', element.label), ('class', element.label))
    elif element.tag == 'checkbox':
        with tag('div'):
            doc.attr(('class', element.label))
            doc.stag("input", ('type', 'checkbox'), ('id', element.label))
            with tag('label'):
                if element.text != "":
                    doc.text(element.text)
                doc.attr(('for', element.label))
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


def generate_color():
    black = random.choice(["#0e1111", "#333", "#28282B"])
    white = random.choice(["#fafafa", "#f5f5f5", "#eeeeee"])

    h = random.uniform(0.1, 1.0)
    s = random.uniform(0.2, 0.8)
    v = random.uniform(0.4, 0.8)
    v2 = v + 0.15
    #(f"H: {h}, S: {s}, V: {v}")
    primary = colorsys.hsv_to_rgb(h, s, v)
    secondary = colorsys.hsv_to_rgb(h, s, v2)
    primary = f"#{'%02x%02x%02x' % (int(primary[0] * 255), int(primary[1] * 255), int(primary[2] * 255))}"
    secondary = f"#{'%02x%02x%02x' % (int(secondary[0] * 255), int(secondary[1] * 255), int(secondary[2] * 255))}"
    return primary, secondary, black, white


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
    font-family: "Helvetica", sans-serif;
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
    input[type='checkbox'] {{
        transform: scale(1.5);
        margin-right: 15px;
        }}
        """
    )


def test_solver(elements_count):
    start_time = datetime.now()
    body = create_body(10000, 10000)

    for i in range(elements_count):
        el = BaseElement(
            'el'+str(i),
            label='el'+str(i),
            min_width=100,
            max_width=200,
            min_height=100,
            max_height=200,
            min_margin_bottom=10,
            min_margin_top=10,
            min_margin_right=10,
            min_margin_left=10,
            max_margin_bottom=10,
            max_margin_top=10,
            max_margin_right=10,
            max_margin_left=10
        )
        body.add_child(el)
    [body.children[i].set_neighbours(bottom_elements=body.children[i:], right_elements=body.children[i:]) for i in range(len(body.children))]

    find_solutions(body)

    end_time = datetime.now()-start_time
    times.append((end_time.seconds * 1000000 + end_time.microseconds) / 1000000)

    print(f"count: {elements_count}; time all: {end_time}")
    return body


def create_body_json(body, body_model):
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

    return body_json


def sort_children(parent):
    arr = sorted(parent.children, key=lambda child: (child.y.val - child.margin_top.val, child.x.val))

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
    for child in parent.children:
        div = []
        if len(child.left) + len(child.right) > 0:
            div = [child]
            for another_child in child.min_bottom + child.min_top:
                if len(another_child.right) + len(another_child.left) > 0:
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
                                div = []
            div_json = None
            # То есть есть элементы, которые можно объединить в один див
            if len(div) > 1:
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


def test_all(body):
    start_time = datetime.now()
    body_model = body.models[0].m
    body_json = create_body_json(body, body_model)

    for el in body.children:
        el_json = BaseElementJSON(
            "button",
            x=ValueJSON(body_model[el.x].as_long(), Measure.PIXEL),
            y=ValueJSON(body_model[el.x].as_long(), Measure.PIXEL),
            width=ValueJSON(body_model[el.col_count].as_long(), Measure.PIXEL),
            height=ValueJSON(body_model[el.row_count].as_long(), Measure.PIXEL),
            margin_top=ValueJSON(body_model[el.margin_top].as_long(), Measure.PIXEL),
            margin_bottom=ValueJSON(body_model[el.margin_bottom].as_long(), Measure.PIXEL),
            margin_right=ValueJSON(body_model[el.margin_right].as_long(), Measure.PIXEL),
            margin_left=ValueJSON(body_model[el.margin_left].as_long(), Measure.PIXEL),
            label=el.label,
            parent=body_json,
            css={'color': 'primary'}
        )
        body_json.children.append(el_json)
    sort_children(body_json)
    group(body, body_model, body_json)

    with open(f'test_test.html', 'w') as f:
        f.write(generate_html(body_json))
        f.close()

    end_time = datetime.now() - start_time
    times_all.append((end_time.seconds * 1000000 + end_time.microseconds) / 1000000 + times[len(times_all)])
    print(f"count: {len(body.children)}, time: {end_time}")

for i in range(2, 26):
    body = test_solver(i)
    test_all(body)


plt.figure()
plt.plot([i for i in range(2, 26)], times, marker='o', mfc='g')
plt.plot([i for i in range(2, 26)], times_all, color='red', marker='o', mfc='g')
plt.xticks([i for i in range(2, 26)])
plt.xlabel('Кол-во элементов')
plt.ylabel('Сек')
plt.show()