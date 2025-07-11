from pathlib import Path
import os

from src.translate.pre_process import split_book
from src.translate.translate import DeeplTranslator

SOURCE_LANG = "EN"
TARGET_LANG = "DE"

### 1. PRE PROCESS ###
input_dir = Path("/") / "home" / "anf3fe" / "book_in_dir"
orig_path = input_dir / "the_idiot.txt"  # englische uebersetzung

with open(orig_path, "r") as f:
    raw = f.read()

PART_DELIMITERS = [
    "PART I\n\n",
    "PART II\n\n",
    "PART III\n\n",
    "PART IV\n\n",
]

CHAPTER_DELIMITERS = [
    "\nI.\n\n",
    "\nII.\n\n",
    "\nIII.\n\n",
    "\nIV.\n\n",
    "\nV.\n\n",
    "\nVI.\n\n",
    "\nVII.\n\n",
    "\nVIII.\n\n",
    "\nIX.\n\n",
    "\nX.\n\n",
    "\nXI.\n\n",
    "\nXII.\n\n",
    "\nXIII.\n\n",
    "\nXIV.\n\n",
    "\nXV.\n\n",
    "\nXVI.\n\n",
    "\nXVII.\n\n",
    "\nXVIII.\n\n",
    "\nXIX.\n\n",
    "\nXX.\n\n",
]

PARAGRAPH_DELIMITERS = [
    "\n\n",
]

organized_book = split_book(
    raw, PART_DELIMITERS, CHAPTER_DELIMITERS, PARAGRAPH_DELIMITERS
)

### 2. Translate ###
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
if DEEPL_API_KEY is None:
    raise EnvironmentError("Please save DEEPL_API_KEY as a environment var.")

translator = DeeplTranslator(DEEPL_API_KEY, SOURCE_LANG, TARGET_LANG)

num_chars, estimated_costs = translator.estimate_cost(raw)
print(f"Estimated costs for translation: {estimated_costs:.2f} Euro")
print(f"{num_chars} chars.")
user_in = input("Continue? [Y/N]")
if not user_in.lower == "y":
    print("Not translating.")
    exit()

t_book = translator.translate_book(organized_book)


print(t_book)
