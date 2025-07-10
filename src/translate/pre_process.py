def strip_gutenberg_chunks(raw_txt: str):
    """
    At the beginning and at the end of every book there chunks of text from the
    Gutenberg Project.
    """

    # TODO ich hab keine Ahnung ob das immer so ist

    raw_txt = raw_txt.split("*** START OF THE PROJECT GUTENBERG EBOOK THE IDIOT ***")[1]
    raw_txt = raw_txt.split("*** END OF THE PROJECT GUTENBERG EBOOK THE IDIOT ***")[0]
    return raw_txt
