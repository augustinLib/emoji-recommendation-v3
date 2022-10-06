import torch
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def calc_accuracy(X,Y):
    max_vals, max_indices = torch.max(X, 1)
    train_acc = (max_indices == Y).sum().data.cpu().numpy()/max_indices.size()[0]
    return train_acc


def new_softmax(a) : 
    c = np.max(a) 
    exp_a = np.exp(a-c) 
    sum_exp_a = np.sum(exp_a)
    y = (exp_a / sum_exp_a) * 100
    return np.round(y, 3)
