GPT-3 based Zero-shot Synonym Editor
==============
Replace words with synonyms while maintaining the original sentence structure and meaning for a given text using OpenAI GPT-3


Overview
--------

The Synonym Editor is a Python tool that uses OpenAI's GPT-3 language model to replace words in a text with synonyms while maintaining the original sentence structure. The tool can be used to edit text files, such as articles, essays, or reports, to improve their readability, diversity of language, and clarity.

Features
--------

- Replace exactly n words with a synonym in a sentence while preserving quotation marks and symbols
- Maintain the original sentence structure and meaning of the text.
- Use OpenAI's GPT-3 language model to ensure reliable and consistent word replacement.
- Edit multiple paragraphs and sentences at once.
- Save the edited text to a file.

Usage
-----

1. Clone the repository to your local machine:

```
git clone https://github.com/ashokgit/SynonymEditor

```

2. Install the required packages:

```
pip install -r requirements.txt

```

3. Set up your OpenAI API key. You can create an API key by signing up for OpenAI at . Once you have your API key, export it to your environment variables:

```
export OPENAI_API_KEY=your_api_key

```

4. Edit the input text file. The input file should be a plain text file with one or more paragraphs of text. You can edit the file in any text editor, such as Notepad, Sublime Text, or Vim.
5. Run the Synonym Editor with the input and output file paths:

```
python app.py input.txt output.txt

```

Replace `input.txt` with the path to your input file and `output.txt` with the path to your output file. The Synonym Editor will read the input file, replace words with synonyms using OpenAI's GPT-3 model, and save the edited text to the output file.

6. Check the output file for any errors or issues. You can open the file in any text editor to view the edited text.

License
-------

The Synonym Editor is licensed under the MIT License. See the `LICENSE` file for more information.

Acknowledgments
---------------

- This project uses the [OpenAI API](https://beta.openai.com/docs/api-reference/introduction) to perform language tasks.
