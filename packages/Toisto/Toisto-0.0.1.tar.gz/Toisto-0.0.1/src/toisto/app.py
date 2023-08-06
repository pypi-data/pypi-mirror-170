"""Main module for Toisto."""

import difflib
import json
import os
import pathlib
import random
import readline  # pylint: disable=unused-import
import string


VOICES = dict(fi="Satu", nl="Xander")

def say(language: str, text: str) -> None:
    """Say the text in the specified language."""
    voice = VOICES[language]
    os.system(f"say --voice={voice} --interactive=bold '{text}'")


def red(text: str) -> str:
    """Return the text in red."""
    return f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"

def green(text: str) -> str:
    """Return thr text in green."""
    return f"\033[38;2;0;255;0m{text}\033[38;2;255;255;255m"


def colored_diff(old_text: str, new_text: str) -> str:
    """Return a colored string showing the diffs between old and new text."""
    result = ""
    codes = difflib.SequenceMatcher(a=old_text, b=new_text).get_opcodes()
    for operator, old_start, old_end, new_start, new_end in codes:
        old_fragment, new_fragment = old_text[old_start:old_end], new_text[new_start:new_end]
        if operator == "delete":
            result += red(old_fragment)
        elif operator == "insert":
            result += green(new_fragment)
        elif operator == "replace" and old_fragment.lower() != new_fragment.lower():
            result += (red(old_fragment) + green(new_fragment))
        else:
            result += old_fragment
    return result


def without_punctuation(text: str) -> str:
    """Remove text without punctuation."""
    return ''.join(char for char in text if char not in string.punctuation)


def match(text1: str, text2: str) -> bool:
    """Return whether the texts match."""
    return without_punctuation(text1.strip().lower()) == without_punctuation(text2.strip().lower())


def load_json(json_file_path: pathlib.Path, default=None):
    """Load the JSON from the file. Return default if file does not exist."""
    if json_file_path.exists():
        with json_file_path.open(encoding="utf-8") as json_file:
            return json.load(json_file)
    return default


def dump_json(json_file_path: pathlib.Path, contents) -> None:
    """Dump the JSON into the file."""
    with json_file_path.open("w", encoding="utf-8") as json_file:
        json.dump(contents, json_file)


def next_entry(entries, progress):
    """Return the next entry to quiz the user with."""
    min_progress = min(progress.get(str(entry), 0) for entry in entries)
    next_entries = [entry for entry in entries if progress.get(str(entry), 0) == min_progress]
    return random.choice(next_entries)


PROGRESS_JSON = pathlib.Path.home() / ".toisto-progress.json"
DECKS_FOLDER = pathlib.Path(__file__).parent / "decks"


def main():
    """Main program."""
    entries = []
    for deck in DECKS_FOLDER.glob("*.json"):
        for entry in load_json(deck):
            entries.extend([entry, dict(reversed(entry.items()))])

    progress = load_json(PROGRESS_JSON, default={})

    print("""Welcome to 'Toisto'!

    Practice as many words and phrases as you like, as long as you like. Hit Ctrl-C or Ctrl-D to quit.
    Toisto tracks how many times you correctly translate words and phrases. The fewer times you have
    translated a word or phrase successfully, the more often it is presented for you to translate.
    """)
    try:
        while True:
            entry = next_entry(entries, progress)
            question, answer = entry.values()
            question_language = list(entry.keys())[0]
            say(question_language, question)
            guess = input("> ")
            correct = match(guess, answer)
            key = str(entry)
            progress[key] = progress.setdefault(key, 0) + 2 if correct else -1
            diff = colored_diff(guess, answer)
            print(("✅ Correct" if correct else f'❌ Incorrect. The correct answer is "{diff}"') + ".\n")
    except (KeyboardInterrupt, EOFError):
        print()  # Make sure the shell prompt is displayed on a new line
    finally:
        dump_json(PROGRESS_JSON, progress)
