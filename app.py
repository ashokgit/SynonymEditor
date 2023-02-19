import sys
from SynonymEditor import SynonymEditor

api_key = "YOUR_API_KEY_HERE"
model_engine = "text-davinci-003"
max_tokens = 500

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python3 app.py input.txt output.txt")
    sys.exit()

# Get command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Create synonym editor
editor = SynonymEditor(api_key, model_engine, max_tokens)

editor.edit_file(input_file, output_file)
