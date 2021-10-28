from pprint import pprint
import pandas as pd
import requests
import os

import selenium.common.exceptions
from bs4 import BeautifulSoup, Tag, NavigableString
import cssutils
from selenium import webdriver

m_tags = {
    "n/a": -1,
    "nav": 0,
    "header": 1,
    "footer": 2,
    "content": 3,
    "control": 4,
    "form": 5,
}

parent_tags = {
    "n/a": -1,
    "nav": 0,
    "header": 1,
    "footer": 2,
    "content": 3,
    "control": 4,
    "form": 5,
    "div": 6,
    "section": 7,
    "aside": 8,
}


def parse_css(f):
    sheet = cssutils.parseFile(f)

    results = {}
    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            results[rule.selectorText] = rule.cssText
        elif rule.type == rule.MEDIA_RULE and len(list(set(rule.media.mediaText.split()) & {'screen', 'all'})) > 0:
            for r in rule:
                if r.type == rule.STYLE_RULE:
                    results[r.selectorText] = r.cssText

    return results


def get_element_information(element, element_label=None, filename=None):
    elem = {
        "filename": filename,
        "label": None,
        "parent_tag": -1,
        "id": "",
        "a": 0,
        "ul": 0,
        "ol": 0,
        "nav": 0,
        "form": 0,
        "input": 0,
        "img": 0,
        "svg": 0,
        "button": 0,
        "span": 0,
        "details": 0,
        "article": 0,
        "h1": 0,
        "h2": 0,
        "h3": 0,
        "h4": 0,
        "h5": 0,
        "h6": 0,
        "aside": 0,
        "table": 0,
        "copyright_word": 0,  # copyright or ©
        "is_footer": 0,
        "is_header": 0,
        "word_count": 0,
        "img_count": 0,
        "a_count": 0,
        "ul_count": 0,
        "ol_count": 0,
        "li_count": 0,
        "id_header": 0,
        "class_header": 0,
        "id_footer": 0,
        "class_footer": 0,
        "id_nav": 0,
        "class_nav": 0,
        "id_top": 0,
        "class_top": 0,
        "id_bottom": 0,
        "class_bottom": 0,
        "id_menu": 0,
        "class_menu": 0,
        "id_sidebar": 0,
        "class_sidebar": 0,
        "x": None,
        "y": None,
        "-x": None,
        "-y": None,
        "width": None,
        "height": None,
        "full-width": 0,
        "full-height": 0,
        "is_left": 0,
        "is_right": 0,
        "is_center": 0,
        "is_top": 0,
        "is_bottom": 0,
        "class": "",
        "el_html": element
    }

    tags = []
    for child in element.descendants:
        if child.name is not None:
            tags.append(str(child.name))
    if element.name in parent_tags.keys():
        elem["parent_tag"] = parent_tags[element.name]
    else:
        elem["parent_tag"] = -1
    if elem["parent_tag"] == parent_tags["header"]:
        elem["is_header"] = 1
    elif elem["parent_tag"] == parent_tags["footer"]:
        elem["is_footer"] = 1

    if len(tags) > 0:

        if "id" in element.attrs.keys():
            id = str(element["id"]).lower()
            elem["id"] = element["id"]
            if "head" in id:
                elem["id_header"] = 1
            if "foot" in id:
                elem["id_footer"] = 1
            if "nav" in id:
                elem["id_nav"] = 1
            if "top" in id:
                elem["id_top"] = 1
            if "bottom" in id:
                elem["id_bottom"] = 1
            if "menu" in id:
                elem["id_menu"] = 1
            if "side" in id:
                elem["id_sidebar"] = 1

        if "class" in element.attrs.keys():
            cl = ", ".join(element["class"]).lower()
            elem["class"] = ", ".join(element["class"])
            if "head" in cl:
                elem["class_header"] = 1
            if "foot" in cl:
                elem["class_footer"] = 1
            if "nav" in cl:
                elem["class_nav"] = 1
            if "top" in cl:
                elem["class_top"] = 1
            if "bottom" in cl:
                elem["class_bottom"] = 1
            if "menu" in cl:
                elem["class_menu"] = 1
            if "side" in cl or "left" in cl or "right" in cl:
                elem["class_sidebar"] = 1

        elem["img_count"] = len(element.find_all("img")) + len(element.find_all("svg"))
        elem["ul_count"] = len(element.find_all("ul"))
        elem["ol_count"] = len(element.find_all("ol"))
        elem["li_count"] = len(element.find_all("li"))

        for child in element:
            if isinstance(child, NavigableString):
                continue
            if isinstance(child, Tag):
                elem["word_count"] += len(child.text.split())
                if "copyright" in child.text or "©" in child.text:
                    elem["copyright_word"] = 1

        existing_children = list(set(tags) & set(elem.keys()))

        for existing_child in existing_children:
            elem[existing_child] = 1

        elem["label"] = element_label
    else:
        return None

    return elem


def get_element_rect(url, element):
    options = webdriver.ChromeOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    window_width = driver.get_window_size()['width']
    page_height = driver.execute_script("return document.documentElement.scrollHeight")

    try:
        driver.get(url)
        page_height = driver.execute_script("return document.documentElement.scrollHeight")
    except Exception as e:
        print(e)
        return

    el = None



    if element['id'] is not None and element['id'] != "":
        try:
            el = driver.find_element_by_id(element['id'])
        except selenium.common.exceptions.NoSuchElementException as e:
            print(url)
            print(e)

    if el is None and element['class'] is not None and element['class'] != "":
        try:
            cl = element['class']
            if "," in cl:
                cl = element['class'][0:element['class'].index(",")]
            el = driver.find_element_by_class_name(cl)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(url)
            print(e)
    if el is None and element['parent_tag'] != parent_tags['div']:
        try:
            tag = list(parent_tags.keys())[list(parent_tags.values()).index(element['parent_tag'])]
            el = driver.find_element_by_tag_name(tag)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(url)
            print(e)
    if el:
        element['x'], element['y'] = el.location.values()
        element['height'], element['width'] = el.size.values()
        element['-x'] = element['x'] + element['width']
        element['-y'] = element['y'] + element['height']

        print("el name" + element["filename"])
        print("el height: " + str(element['height']))
        print("el -y: " + str(element['-y']))
        print("page height: " + str(page_height))

        if element['width'] / window_width > 0.75:
            element['full-width'] = 1
            element['is_center'] = 1
        if element['height'] / page_height > 0.75:
            element['full-height'] = 1

        if element['full-width'] == 0:
            if element['x'] < 200:
                element['is_left'] = 1
            elif abs(window_width - element['-x']) < 200:
                element['is_right'] = 1
            elif abs(abs(element['x']) - abs(window_width - element['-x'])) < 200:
                element['is_center'] = 1

        if element['full-height'] == 0 and element['is_left'] == 0 and element['is_right'] == 0:
            if element['y'] < 100:
                element['is_top'] = 1
            if abs(page_height - element['-y']) < page_height * 0.1:
                element['is_bottom'] = 1

    driver.close()


def get_element_from_file(file):
    soup = BeautifulSoup(file, 'html.parser')
    element = soup.find()

    return element


def save_test_data():
    arr = []
    header_files = os.listdir(os.getcwd() + "/train_header_html")
    for i in range(len(header_files)):
        header_file = open("train_header_html/" + header_files[i], 'r', encoding="utf8", errors="ignore")
        header_e = get_element_from_file(header_file)
        element = get_element_information(header_e, m_tags['header'], header_file.name)
        if element is not None:
            arr.append(element)
            get_rect("https://" + header_files[i][0:header_files[i].rindex(".html")].replace(',', '/'), header_e, element)
        header_file.close()

    footer_files = os.listdir(os.getcwd() + "/train_footer_html")
    for i in range(len(footer_files)):
        footer_file = open("train_footer_html/" + footer_files[i], 'r', encoding="utf8", errors="ignore")
        footer_e = get_element_from_file(footer_file)
        element = get_element_information(footer_e, m_tags['footer'], footer_file.name)
        if element is not None:
            arr.append(element)
            get_rect("https://" + footer_files[i][0:footer_files[i].rindex(".html")].replace(',', '/'), footer_e, element)
        footer_file.close()

    nav_files = os.listdir(os.getcwd() + "/train_side_nav_html")
    for i in range(len(nav_files)):
        nav_file = open("train_side_nav_html/" + nav_files[i], 'r', encoding="utf8", errors="ignore")
        nav_e = get_element_from_file(nav_file)
        element = get_element_information(nav_e, m_tags['nav'], nav_file.name)
        if element is not None:
            arr.append(element)
            get_rect("https://" + nav_files[i][0:nav_files[i].rindex(".html")].replace(',', '/'), nav_e, element)
        nav_file.close()

    #for e in arr:
    #    url = "https://" + e['filename'][0:e['filename'].rindex(".html")].split('/')[1].replace(',', '/')
    #    get_element_rect(url, e)

    df = pd.DataFrame(arr)
    df.to_csv('my_csv.csv', mode='w', index=False)


def save_new_teach_data(elements):
    pass


def get_html_from_url(url):
    main_tags = ['header', 'footer', 'main', 'section', 'nav', 'aside', 'section', 'div']

    res = requests.get(url)

    file = open('temp.html', 'w', encoding='utf-8')
    file.write(res.text)

    soup = BeautifulSoup(res.content, 'html.parser')

    arr = []

    for tag in main_tags:
        els = soup.find_all(tag)
        for el in els:
            arr.append(el)

    return arr


def get_elements_rect(url, elements):
    options = webdriver.ChromeOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    window_width = driver.get_window_size()['width']
    page_height = driver.execute_script("return document.body.scrollHeight")

    try:
        driver.get(url)
        page_height = driver.execute_script("return document.documentElement.scrollHeight")
        print(page_height)
    except Exception as e:
        print(e)
        return

    el = None

    for element in elements:
        if element['id'] is not None and element['id'] != "":
            try:
                el = driver.find_element_by_id(element['id'])
            except selenium.common.exceptions.NoSuchElementException as e:
                print(url)
                print(e)

        if el is None and element['class'] is not None and element['class'] != "":
            try:
                cl = element['class']
                if "," in cl:
                    cl = element['class'][0:element['class'].index(",")]
                el = driver.find_element_by_class_name(cl)
            except selenium.common.exceptions.NoSuchElementException as e:
                print(url)
                print(e)
        if el is None and element['parent_tag'] != parent_tags['div']:
            try:
                tag = list(parent_tags.keys())[list(parent_tags.values()).index(element['parent_tag'])]
                el = driver.find_element_by_tag_name(tag)
            except selenium.common.exceptions.NoSuchElementException as e:
                print(url)
                print(e)
        if el:
            element['x'], element['y'] = el.location.values()
            element['height'], element['width'] = el.size.values()
            element['-x'] = element['x'] + element['width']
            element['-y'] = element['y'] + element['height']

            if element['width'] / window_width > 0.75:
                element['full-width'] = 1
                element['is_center'] = 1
            if element['height'] / page_height > 0.75:
                element['full-height'] = 1

            if element['full-width'] == 0:
                if element['x'] < 100:
                    element['is_left'] = 1
                elif abs(window_width - element['-x']) < 100:
                    element['is_right'] = 1
                elif abs(abs(element['x']) - abs(window_width - element['-x'])) < 200:
                    element['is_center'] = 1

            if element['full-height'] == 0 and element['is_left'] == 0 and element['is_right'] == 0:
                if element['y'] < 100:
                    element['is_top'] = 1
                if abs(page_height - element['-y']) < page_height * 0.1:
                    element['is_bottom'] = 1

    driver.close()


def save_data(url):
    elements = get_html_from_url(url)

    pred_arr = []

    options = webdriver.ChromeOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    window_width = driver.get_window_size()['width']
    page_height = driver.execute_script("return document.body.scrollHeight")

    try:
        driver.get(url)
        page_height = driver.execute_script("return document.documentElement.scrollHeight")
        print(page_height)
    except Exception as e:
        print(e)

    for element in elements:
        e = get_element_information(element)
        if e is not None:
            pred_arr.append(e)
            get_elem_rect(driver, window_width, page_height, element, e)

    driver.close()
    #get_elements_rect(url, pred_arr)

    df = pd.DataFrame(pred_arr)
    df.to_csv('pred.csv', mode='w', index=False)


def get_xpath(element):
    xpath = "//" + element.name + "["

    attrs = get_attrs_xpath(element)
    if attrs != "":
        xpath += attrs + " and "
    children = element.findChildren(recursive=False)

    for child in children:
        child_attrs = get_attrs_xpath(child)
        if child_attrs != "":
            xpath += child.name + "[" + get_attrs_xpath(child) + "] and "
        else:
            xpath += child.name + " and "

    return xpath[:-5] + "]"
    #print(element.findChildren(recursive=False))


def get_attrs_xpath(element):
    s = ""
    attrs = element.attrs.keys()
    for attr in attrs:
        if attr == "class":
            for classname in element[attr]:
                s += "contains(@class, " + classname + ") or "
            #print(element["class"])
            #s += "@class='" + " ".join(element["class"]) + "'"
    if s[-4:] == " or ":
        return s[:-4]
    return s


def get_elem_rect(driver, window_width, page_height, element, table_el):
    el = None
    if "id" in element.attrs.keys():
        el = driver.find_element_by_id(element["id"])
    else:
        xpath = get_xpath(element)
        el = driver.find_element_by_xpath(xpath)

    if el:
        print(el.value_of_css_property("margin"))
        table_el['x'], table_el['y'] = el.location.values()
        table_el['height'], table_el['width'] = el.size.values()
        table_el['-x'] = table_el['x'] + table_el['width']
        table_el['-y'] = table_el['y'] + table_el['height']

        if table_el['width'] / window_width > 0.75:
            table_el['full-width'] = 1
            table_el['is_center'] = 1
        if table_el['height'] / page_height > 0.75:
            table_el['full-height'] = 1

        if table_el['full-width'] == 0:
            if table_el['x'] < 100:
                table_el['is_left'] = 1
            elif abs(window_width - table_el['-x']) < 100:
                table_el['is_right'] = 1
            elif abs(abs(table_el['x']) - abs(window_width - table_el['-x'])) < 200:
                table_el['is_center'] = 1

        if table_el['full-height'] == 0 and table_el['is_left'] == 0 and table_el['is_right'] == 0:
            if table_el['y'] < 100:
                table_el['is_top'] = 1
            if abs(page_height - table_el['-y']) < page_height * 0.1:
                table_el['is_bottom'] = 1


def get_rect(url, element, table_el):
    options = webdriver.ChromeOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    window_width = driver.get_window_size()['width']
    page_height = driver.execute_script("return document.body.scrollHeight")

    try:
        driver.get(url)
        page_height = driver.execute_script("return document.documentElement.scrollHeight")
        print(page_height)
    except Exception as e:
        print(e)
        return

    get_elem_rect(driver, window_width, page_height, element, table_el)

    driver.close()

class el:
    def __init__(self):
        self.name = "div"
        self.attrs = {id: "feed-link"}

elem = el()
print(elem.attrs.keys())
save_data("https://stackoverflow.com/questions/17255611/selenium-webdriver-getcssvalue-method/21306689")

# html_file = 'train_header_html/div_header.html'
# css_file = 'train_css/div_header.css'

# file = open(html_file, 'r', encoding="utf8", errors='ignore')


# soup = BeautifulSoup(file, 'lxml')

# parsed_elements = parse_html()

# css_dict = parse_css(css_file)

# for key in css_dict:
#    try:
#        styled_elements = soup.select(key)
#        for parsed_element in parsed_elements:
#            for styled_element in styled_elements:
#                if str(styled_element) in parsed_elements[parsed_element]['html']:
#                    if "css" in parsed_elements[parsed_element].keys():
#                        parsed_elements[parsed_element]["css"].add(css_dict[key])
#                    else:
#                        parsed_elements[parsed_element]["css"] = {css_dict[key]}
#    except NotImplementedError:
#        pass
#
# for parsed_element in parsed_elements:
#    print(parsed_element + ". " + parsed_elements[parsed_element]["tag"] + ", children: " + ", ".join(
#        parsed_elements[parsed_element]["children"]) + ", id: " + parsed_elements[parsed_element]["id"] + ", class: "
#          + ", ".join(parsed_elements[parsed_element]["class"]) + ", css:\n" + "\n".join(
#        parsed_elements[parsed_element]["css"]))
