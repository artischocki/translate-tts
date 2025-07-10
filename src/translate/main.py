from pathlib import Path

from src.translate.pre_process import strip_gutenberg_chunks

input_dir = Path("/") / "home" / "anf3fe" / "book_in_dir"
orig_path = input_dir / "the_idiot.txt"  # englische uebersetzung

with open(orig_path, "r") as f:
    orig = f.read()


orig = strip_gutenberg_chunks(orig)
