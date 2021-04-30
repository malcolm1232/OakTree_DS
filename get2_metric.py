import numpy as np
import pandas as pd
import math
def get_mean_absolute_percentage_error(y_true, y_pred):
    # y_true, y_pred = check_arrays(y_true, y_pred)

    ## Note: does not handle mix 1d representation
    #if _is_1d(y_true):
    #    y_true, y_pred = _check_1d_array(y_true, y_pred)

    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def get_accuracy(y_true, y_pred):

    accuracy_list = []
    accuracy_metric = 0
    for true_val, pred_val in zip(y_true, y_pred):
        difference = math.sqrt((true_val - pred_val)**2)
        if difference <= 3:
            accuracy_list.append(1)
            accuracy_metric+=1
        else:
            accuracy_list.append(0)

    accuracy_score = accuracy_metric / len(y_true)
    # print('NOTE: Accuracy is defined as # count(abs error <= 3)/len(validation dataframe)')
    # print('')
    return accuracy_list, accuracy_score

def get_dataframe(y_true, y_pred, accuracy_col):
    # df1 = pd.DataFrame(y_true,columns=['True_Value'])
    df1 = y_true.reset_index(drop=True)
    df2 = pd.DataFrame(y_pred, columns=['Predicted'])
    df3 = pd.DataFrame(accuracy_col, columns=['Binary_Accuracy'])
    concat = pd.concat([df1, df2, df3], axis=1)
    # print("df1:", df1)

    return concat


    # accuracy_metric = accuracy_start/len(y_true)

    # return accuracy_metric

# a = [10,20,11,13]
# b = [10, 21, 40, 30]
#
# em = []
# accuracy_start = 0
# for i, x in zip(a,b):
#     c = i - x
#     print("c:",c)
#     if -3<= c <= 3:
#         print('accuracy +1!')
#         accuracy_start+=1
#
# print("accuracy_end:",accuracy_start)
# accuracy_metric = accuracy_start/len(a)
# print("accuracy_metric:",accuracy_metric)
