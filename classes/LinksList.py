class LinksLists:
    def __init__(self, links, font_size_factor=1, is_vertical=False, word_height=10, word_width=10, min_height_c=0, min_width_c=0):
        self.links = links
        self.font_size_factor = font_size_factor

        # if false then horizontal
        self.is_vertical = is_vertical

        if is_vertical:
            longest_word = len(links[0])
            for i in range(1, links):
                length = len(links[i])
                if length > longest_word:
                    longest_word = length
            # side nav for example
            self.min_width = longest_word * font_size_factor + min_width_c
            self.min_height = word_height * font_size_factor * len(links) + min_height_c
        else:
            # header for example
            self.min_width = sum([len(links[i]) * font_size_factor * word_width for i in range(len(links))]) + min_width_c
            self.min_height = word_height * font_size_factor + min_height_c
