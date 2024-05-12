from spellchecker import SpellChecker
import requests
import json
import re

class SpellCheckerModule:
    def __init__(self):
        """
        Constructor for SpellCheckerModule class.
        Initializes the SpellChecker object with English language and a distance of 3.
        """
        self.spell_check = SpellChecker(language='en', distance=3)

    def clean_word(self, word):
        """
        Custom function to clean the word from special characters while retaining hyphens and commas.

        Args:
        - word (str): The word to be cleaned.

        Returns:
        - tuple: A tuple containing the cleaned word and any special characters found.
        """
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word)
        special_chars = ''.join(re.findall(r'[^a-zA-Z0-9]', word))
        return cleaned_word, special_chars

    def correct_spell(self, text):
        """
        Corrects spelling errors in the given text and returns the corrected result along with a map
        of each wrong word and its probable candidates.

        Args:
        - text (str): The input text to be spell-checked.

        Returns:
        - dict: A dictionary containing the corrected sentence and the word-candidates map.
        """
        # Reusing the initialized SpellChecker object
        spell_check = self.spell_check

        words = text.split()
        corrected_words = []
        word_candidates_map = {}

        for word in words:
            # Check if the word is a special character
            if not word.isalnum():
                if re.match(r'^[^\w]+', word):
                    # If the word starts with any non-alphanumeric character,
                    # do spell-checking for the part without these special characters
                    cleaned_word, special_chars_start = self.clean_word(word)

                    # Continue with spell-checking for non-special characters
                    corrected_word = str(spell_check.correction(cleaned_word))
                    candidates = spell_check.candidates(cleaned_word)

                    # Store the original word and its candidates in the map
                    if candidates is not None and cleaned_word.lower() != list(candidates)[0].lower():
                        word_candidates_map[cleaned_word] = list(candidates)

                    # Add the corrected word with special characters to the list
                    corrected_words.append(special_chars_start + corrected_word)
                    continue

                elif re.search(r'[^\w]+$', word):
                    print("word", word)
                    # If the word ends with any non-alphanumeric character,
                    # do spell-checking for the part without these special characters
                    cleaned_word, special_chars_end = self.clean_word(word)
                    print("cleaned_word", cleaned_word)
                    print("special_chars_end", special_chars_end)
                    # Continue with spell-checking for non-special characters
                    corrected_word = str(spell_check.correction(cleaned_word))
                    candidates = spell_check.candidates(cleaned_word)
                    print("candidates", candidates)
                    # Store the original word and its candidates in the map
                    if candidates is not None and cleaned_word.lower() != list(candidates)[0].lower():
                        word_candidates_map[cleaned_word] = list(candidates)

                    # Add the corrected word with special characters to the list
                    corrected_words.append(corrected_word + special_chars_end)
                    continue

                # Replace the wrong word with the corrected word and re-insert special characters
                corrected_words.append(word)
                continue

            # Continue with spell-checking for non-special characters
            corrected_word = str(spell_check.correction(word))
            candidates = spell_check.candidates(word)

            # Store the original word and its candidates in the map
            if candidates is not None and word.lower() != list(candidates)[0].lower():
                word_candidates_map[word] = list(candidates)

            # Replace the wrong word with the corrected word in the sentence
            corrected_words.append(corrected_word)

        corrected_sentence = " ".join(corrected_words)

        # Return a map with each wrong word and its probable candidates
        result = {
            "corrected_sentence": corrected_sentence,
            "word_candidates_map": word_candidates_map
        }

        return result

    def correct_grammar(self, text):
        """
        Corrects grammar errors in the given text using an external API.

        Args:
        - text (str): The input text to be grammar-checked.

        Returns:
        - dict: The response from the grammar correction API.
        """
        try:
            url = "http://390a-34-125-183-28.ngrok-free.app/getresponse"

            payload = json.dumps({
                "sentence": [
                    text
                ]
            })
            headers = {
                'Content-Type': 'application/json',
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            # Check if the API call was successful
            if response.status_code == 200:
                return response.json()
            else:
                # Handle the case when the API call was not successful
                return {"error": f"API call failed with status code {response.status_code}"}
        except requests.exceptions.RequestException as e:
            # Handle exceptions, such as network issues
            return {"error": f"Request failed: {str(e)}"}

if __name__ == "__main__":
    # Instantiate the SpellCheckerModule
    obj = SpellCheckerModule()

    # Example input text
    message = "Hello world. I like mashine learning. appple. bananana"

    # Spell-check the message
    result = obj.correct_spell(message)

    # Grammar-check the corrected sentence
    print(obj.correct_grammar(result["corrected_sentence"]))

    # Print the result
    print("Corrected Sentence:", result["corrected_sentence"])
    print("Word Candidates Map:", result["word_candidates_map"])
