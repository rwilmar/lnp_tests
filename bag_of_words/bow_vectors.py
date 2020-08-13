from preprocessing import preprocess_text
# Define text_to_bow_vector() below:


features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}

text = "Another five fish find another faraway fish."

def text_to_bow_vector(some_text, features_dictionary):
  bow_vector = (len(features_dictionary))*[0]
  tokens=preprocess_text(some_text)
  for token in tokens:
    feature_index=features_dictionary[token]
    bow_vector[feature_index]+=1
  return bow_vector,tokens


print(text_to_bow_vector(text, features_dictionary)[0])