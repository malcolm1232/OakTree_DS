""""
[Detailed Guide]

# STEP 1: Download and unzip file 
(It should be downloaded as OakTree_DS-main)

# STEP 2: Change current working path to path where you downloaded your file
cd Downloads/OakTree_DS-main
(eg. "cd C:/Users/malco/Downloads/OakTree_DS-main")

#Step 3: unzip file for pretrained model
tar -xf final_model_Model10v1.zip

# STEP 4: pip install requirements.txt
pip install -r requirements.txt 

# STEP 5: run python code
python final_pred_model.py --path=[validation_set.csv]
(eg1. "python final_pred_model.py --path=validation_set.csv")
(eg2. "python final_pred_model.py --path=C:/Users/malco/Desktop/datasets/validation_set.csv")

NOTE: REMEMBER TO TRANSFER YOUR validation_set.csv TO OakTree_DS-main (WORKING DIR)
""""

#Template Command Prompt run
[NOTE: For bottom to work, after downloading] 
1. Extract File
2. change validation set to validation_set.csv 
3. then transfer to /OakTree_DS-main]

cd Downloads/OakTree_DS-main
tar -xf final_model_Model10v1.zip
pip install -r requirements.txt
python final_pred_model.py --path=validation_set.csv

Files:
1. Scarlet Oak Report.doc (Word Document for Report)
2. final_pred_model.py (to run for prediction)
3. Working_final.ipynb (LSTM, Pycaret)(contains bulk of codes)
4. get2_metric.py (metric calculation for MAPE and accuracy)
5. Oak_Tree_AutoKeras.py (AutoKeras)
6. Oak_Tree_MLBox.py (mlbox)
7. Oak_Tree_TPOT.py (TPOT)
8. requirements.txt
9. readme.txt


