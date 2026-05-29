import spacy
from spacy import displacy
import re
import colorama
from colorama import Fore, Back, Style

colorama.init()
nlp = spacy.load('en_core_web_sm')

# Color map for entity labels
label_colors = {
    "ORG": Back.CYAN + Fore.BLACK,
    "PERSON": Back.MAGENTA + Fore.WHITE,
    "DATE": Back.BLUE + Fore.WHITE,
    "GPE": Back.YELLOW + Fore.BLACK,
    "PERCENT": Back.WHITE + Fore.BLACK,
    "WORK_OF_ART": Back.LIGHTMAGENTA_EX + Fore.WHITE,
}

google_text = "Google was founded on September 4, 1998, by computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet."

def ner_tagging():
    spacy_doc = nlp(google_text)

    # Print colored entities in context
    for token in spacy_doc:
        ent = token.ent_type_
        if ent:
            color = label_colors.get(ent, Back.WHITE + Fore.BLACK)
            print(f"{color}{token.text} [{ent}]{Style.RESET_ALL}", end=" ")
        else:
            print(token.text, end=" ")
    print()
    google_text_clean = re.sub(r'[^\w\s]', '', google_text).lower() # remove punctuation and lowercase
    print(google_text_clean)

