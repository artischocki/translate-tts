import deepl
from tqdm import tqdm


class DeeplTranslator:
    def __init__(self, api_key: str, source_lang: str, target_lang: str):
        self._translator = deepl.Translator(api_key)
        self._source_lang = source_lang
        self._target_lang = target_lang

    def translate_text(self, text: str):
        result = self._translator.translate_text(
            text,
            source_lang=self._source_lang,
            target_lang=self._target_lang,
        )
        return result.text

    def translate_book(
        self, organized_book: dict[str, dict[str, list[str]]]
    ) -> dict[str, dict[str, list[str]]]:
        t_book = {}
        for part_name, part in tqdm(organized_book.items()):
            # translate part name
            t_part_name = self.translate_text(part_name)
            t_book[t_part_name] = {}
            for chapter_name, chapter in tqdm(
                part.items(), leave=False, desc=part_name
            ):
                # translate chapt name
                t_chapter_name = self.translate_text(chapter_name)
                t_book[t_part_name][t_chapter_name] = []

                for paragraph in tqdm(chapter, leave=False, desc=chapter_name):
                    t_paragraph = self.translate_text(paragraph)
                    t_book[t_part_name][t_chapter_name].append(t_paragraph)
        return t_book
