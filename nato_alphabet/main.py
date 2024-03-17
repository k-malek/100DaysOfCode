import pandas

def import_nato_data():
    try:
        nato_alfa_df=pandas.read_csv('nato_phonetic_alphabet.csv')
        letter_to_code={row['letter']:row['code'] for _, row in nato_alfa_df.iterrows()}
        return letter_to_code
    except FileNotFoundError:
        print("NATO phonetic alphabet csv source file is inaccessible from the current location")

def nato_translate(word:str) -> list | None:
    nato_mapping=import_nato_data()
    try:
        return [nato_mapping[letter] for letter in word.upper()]
    except KeyError:
        print("Incorrect word provided")
        return None
