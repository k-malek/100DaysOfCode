import pandas

def import_nato_data():
    nato_alfa_df=pandas.read_csv(r'nato_alphabet\nato_phonetic_alphabet.csv')
    letter_to_code={row['letter']:row['code'] for _, row in nato_alfa_df.iterrows()}
    return letter_to_code

def nato_translate(word):
    nato_mapping=import_nato_data()
    return [nato_mapping[letter] for letter in word.upper()] 
