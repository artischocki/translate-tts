import re


def split_blob(blob: str, delimiters: list[str]) -> dict[str, str]:
    """
    This function splits large blobs of text into smaller units.
    For example a whole book into parts, or parts into chapters, or chapters
    into paragraphs.

    Args:
        delimiters:
            If any of these delimiters is hit, the blob will be split up
    Returns:
        The split up parts in a dict, with the corresponding delimiter as key
    """
    # 1. Sort delimiters by descending length so that longer tokens
    #    (e.g. "VI.") are tried before shorter ones ("I.")
    delimiters_sorted = sorted(delimiters, key=len, reverse=True)

    # 2. Build a capturing alternation of them
    pattern = "(" + "|".join(map(re.escape, delimiters_sorted)) + ")"

    # 3. Split, keeping delimiters
    tokens = re.split(pattern, blob)
    #    tokens == [prefix, delim1, chunk1, delim2, chunk2, ...]

    # 4. Zip up delimiters with the text that follows
    pairs = zip(tokens[1::2], tokens[2::2])

    # 5. Accumulate into a dict
    result = {}
    for delim, chunk in pairs:
        result.setdefault(delim, []).append(chunk)

    return result


def split_book(
    raw: str,
    part_delimiters: list[str],
    chapter_delimiters: list[str],
    paragraph_delimiters: list[str],
) -> dict[str, dict[str, list[str]]]:
    organized_book = {}

    # split into parts
    parts = split_blob(raw, part_delimiters)

    print("Organizing book...")

    for part_name in list(parts.keys()):
        # split parts into chapters
        chapters = split_blob(parts[part_name][0], chapter_delimiters)

        # strip \n from delimiters
        stripped_part_name = part_name.strip("\n")
        organized_book[stripped_part_name] = {}
        print(f"{stripped_part_name}:")

        for chapter_name in chapters:
            # split chapters into paragraphs
            paragraphs = split_blob(chapters[chapter_name][0], paragraph_delimiters)

            stripped_chapter_name = chapter_name.strip("\n")
            organized_book[stripped_part_name][stripped_chapter_name] = []

            for paragraph in list(paragraphs.values())[0]:
                # fill book
                paragraph = paragraph.replace("\n", " ")  # remove \n
                organized_book[stripped_part_name][stripped_chapter_name].append(
                    paragraph
                )
            print(
                f"    {stripped_chapter_name}: {len(list(paragraphs.values())[0])} paragraphs"
            )
    print("Done.")
    return organized_book
