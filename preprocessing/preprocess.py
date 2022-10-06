from numpy import full
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def data_preprocess(path):
    raw_data = pd.read_csv(path, sep='\t', header=None)
    raw_data.dropna(axis=0, inplace=True)
    items = list(raw_data[1])

    encoder = LabelEncoder()
    encoder.fit(items)
    encoded_item = encoder.transform(items)
    raw_data[1] = encoded_item

    data_list = []
    for sentence, label in zip(raw_data[0], raw_data[1]):
        data = []
        data.append(sentence)
        data.append(str(label))
        data_list.append(data)

    class_dict = {}
    for i, item in enumerate(encoder.classes_):
        class_dict[i] = item

    return data_list, class_dict


def data_split(full_data):
    train_data, valid_data = train_test_split(full_data, test_size=0.2, random_state=42)
    return train_data, valid_data