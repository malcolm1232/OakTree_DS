import pandas as pd
from pycaret.regression import *
import argparse
from get2_metric import get_accuracy, get_mean_absolute_percentage_error, get_dataframe

parser = argparse.ArgumentParser()
parser.add_argument('--path', type = str, help ='Write in Validation Set path as a CSV')
args = parser.parse_args()

#Load pretrained pycaret Model
final_model = load_model('final_model_Model10v1')

#Load validation set
df_val = pd.read_csv(args.path)

#Predict
predictions = predict_model(final_model, data = df_val)

#Get y_true, y_pred
y_pred = predictions['Label'].to_list()
y_true = df_val['y']

#get MAPE and accuracy metric
MAPE = get_mean_absolute_percentage_error(y_true, y_pred)
accuracy_col, accuracy_score = get_accuracy(y_true, y_pred)
get_dataframe(y_true, y_pred, accuracy_col)

# FYI
print('NOTE: Accuracy is defined as # count(abs error <= 3)/len(validation dataframe)\n')

#to save results into csv
end_df = get_dataframe(y_true, y_pred, accuracy_col)
print("[INFO] Saving Result as DataFrame_Result.csv...\n")
end_df.to_csv('DataFrame_Result.csv')

print("[REQUIRED] MAPE:",MAPE)
print("[REQUIRED] accuracy_score:",accuracy_score)
print("[REQUIRED] Saving Result as prediction_out.txt...\n")
with open ('prediction_out.txt', 'w') as f:
    f.write(str(y_pred))

