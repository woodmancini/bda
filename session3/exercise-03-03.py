import os

from google import genai


TEXT_FILE = "les_miserables.txt"
# QUESTION = "Who is Bishop Myriel?"
# KEYWORDS = ["bishop", "myriel", "digne"]
QUESTION = "Who is Fantine?"
KEYWORDS = ["fantine"]
MAX_LINES = 14

def useful_lines(path):
    """Yield non-empty lines from a text file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


def retrieve_context(path, keywords, max_lines):
    """Find a small chunk of text that matches the question."""
    matches = []
    extra_lines = 0

    for line in useful_lines(path):
        line_lower = line.lower()

        if any(keyword in line_lower for keyword in keywords):
            matches.append(line)
            # Keep two lines after a match so Gemini has a little context.
            extra_lines = 2
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
            break

    return "\n".join(matches)


context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

# Send only the retrieved context to Gemini.
prompt = f"""Use only this context to answer the question.

Question:
{QUESTION}

Context:
{context}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)

# First response:
    # Bishop Myriel is M. Charles-François-Bienvenu Myriel, who was the Bishop of Digne 
    # in 1815. He had occupied that position since 1806 and was an old man of about
    # seventy-five years of age at that time.

# Second response:
    # Fantine is the mistress of Félix Tholomyès, one of four "ravishing young women" 
    # (along with Favorite, Dahlia, and Zéphine). She is called "the Blonde" because 
    # of her beautiful, sunny hair.

    # The text describes her as still being "a little like a working-woman" and 
    # "not yet entirely divorced from her needles," retaining "something of the "
    # "serenity of toil" and "that flower of honesty which survives the first fall in woman." 
    # Compared to the other three, Fantine is "still in her first illusions" and is explicitly 
    # described as a "good girl," in contrast to the others who are called "philosophical young women."

# 1. Which lines were retrieved?
    # Non-empty lines containing any of the given keywords, plus the following two lines in each case.
    # A maximum of 8 lines total.
# 2. Did Gemini have enough context?
    # It gave much more information about Fantine - presumably there were more references to her in the
    # text. This would make sense given that increasing max_lines to 14 yielded more information.
# 3. What would improve this tiny RAG system?
    # Increasing max_lines might improve results.

# Second response with 14 lines context:
    # Fantine is a young woman, the mistress of Félix Tholomyès. She is called "the Blonde" because of 
    # her beautiful, sunny hair and is described as a lovely blonde with fine teeth. She is one of four 
    # "ravishing young women" who are "perfumed and radiant," still a little like working-women.

    # Fantine is characterized as a "good girl," still in her "first illusions," and less experienced and 
    # emancipated than her companions, Favorite, Dahlia, and Zéphine. Her love for Tholomyès is a "first "
    # "love, a sole love, a faithful love."

    # She is said to have "blossom[ed] from the dregs of the people," bearing "the sign of the anonymous and 
    # the unknown." She was born at Montreuil-sur-Mer, never knew her father or mother, and had no family name
    #  or baptismal name; she received the name Fantine from a random passerby when she was a very small child. 
    # At the age of ten, she went into service with farmers, and at fifteen, she came to Paris "to seek her fortune." 
    # She worked for her living, and then loved Tholomyès.