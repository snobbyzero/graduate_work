class TextList:
    def __init__(self, text_list, is_vertical=False):
        self.text_list = text_list

        # if false then horizontal
        self.is_vertical = is_vertical

        if is_vertical:
            longest_word = text_list[0]
            for i in range(1, len(text_list)):
                length = len(text_list[i].text)
                if length > len(longest_word.text):
                    longest_word = text_list[i]
            # side nav for example
            self.min_width = longest_word.min_width
            self.min_height = sum([el.min_height for el in text_list])
        else:
            # header for example
            highest_word = text_list[0]
            for i in range(1, len(text_list)):
                height = text_list[i].min_height
                if height > highest_word.min_height:
                    highest_word = text_list[i]
            self.min_width = sum([len(text_list[i].text) for i in range(len(text_list))])
            self.min_height = highest_word.min_height
