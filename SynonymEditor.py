import openai
from nltk import sent_tokenize
import re


class SynonymEditor:

    def __init__(self, api_key, model_engine, max_tokens):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.max_tokens = max_tokens

    # Play with the prompts here and change the return index to change and see the effect of the prompt on the output quality
    # Note that the longer the prompt, higher the token used and hence the billing
    def _get_prompt(self, sentence):
        prompts = [
            "Replace exactly one word with a synonym while preserving __QUOTE__ in the following sentence:\n"+sentence+"\n",
            f"Instruction: Replace max two words with a synonym while maintaining the original sentence structure and meaning for the following text:\n{sentence}\nOutput:",
            f"Instruction: Replace max two words with a synonym while maintaining the original sentence structure and meaning for an input sentence.\nExample\nInput: This is a sentence with word1 and word2.\nOutput: This is a sentence with [synonym of word1] and word2.\n###\nInput: {sentence}\nOutput:",
        ]
        return prompts[0]

    # Call the OpenAI API here
    def __call_ai(self, sentence):
        prompt = self._get_prompt(sentence)
        response = openai.Completion.create(
            model=self.model_engine,
            prompt=prompt,
            temperature=0.6,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return self._post_process_sentence(response.choices[0].text.strip())

    # Split the paragraph to preserve quotation marks
    def _split_into_sentences(self, text):
        text = text.replace('"', '__QUOTE__')
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        sentences = sent_tokenize(text)
        return sentences

    def _post_process_sentence(self, text):
        return text.replace('__QUOTE__', '"')

    # Preprocess the text, perform edit task and join back to get the original format
    def _edit_text(self, text):
        edited_text = ""
        paragraphs = text.split("\n\n")
        edited_paragraphs = []
        for paragraph in paragraphs:
            sentences = self._split_into_sentences(paragraph)
            edited_sentences = []
            for sentence in sentences:
                new_sentence = self.__call_ai(sentence)
                edited_sentences.append(new_sentence)

            # join edited sentences to form an edited paragraph
            edited_paragraph = ' '.join(edited_sentences)
            edited_paragraphs.append(edited_paragraph)

        # join edited paragraphs to form edited text
        edited_text = '\n\n'.join(edited_paragraphs)

        return edited_text

    # File Read Write operation
    def edit_file(self, input_file, output_file):
        print("Opening File")
        with open(input_file, "r", encoding="utf8", errors="ignore") as f:
            text = f.read()
        print("Editing")
        edited_text = self._edit_text(text)
        print("Finishing up")
        with open(output_file, "w") as f:
            f.write(edited_text)
        print("Done!")
