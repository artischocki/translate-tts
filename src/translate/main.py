from pathlib import Path

from src.translate.pre_process import split_book

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
