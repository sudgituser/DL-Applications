from flask import Flask, request
from model import SpellCheckerModule
from flask_cors import CORS

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()
CORS(app)

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    """
    Flask route for spell-checking text.

    Returns:
    - dict: A dictionary containing the corrected text and its grammar.
    """
    if request.method == 'POST':
        input_data = request.get_json()
        text = input_data['text']

        # Spell-check the text
        corrected_text = spell_checker_module.correct_spell(text)

        # Grammar-check the corrected text
        corrected_grammar = spell_checker_module.correct_grammar(corrected_text["corrected_sentence"])

        return {"corrected_text": corrected_text, "corrected_grammar": corrected_grammar}

@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    """
    Flask route for grammar-checking text from a file.

    Returns:
    - dict: A dictionary containing the corrected text from the file and its grammar.
    """
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8', errors='ignore')

        # Spell-check the text from the file
        corrected_file_text = spell_checker_module.correct_spell(readable_file)

        # Grammar-check the corrected text from the file
        corrected_file_grammar = spell_checker_module.correct_grammar(readable_file)

        return {"corrected_text": corrected_file_text, "corrected_file_grammar": corrected_file_grammar}

# python main
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
