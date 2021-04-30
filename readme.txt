#Template CMD run
[NOTE: For bottom to work, after downloading, 
1. Extract File
2. change validation set to validation_set.csv 
3. then transfer to /OakTree_DS-main]

cd downloads/OakTree_DS-main
tar -xf final_model_Model10v1.zip
pip install -r requirements.txt
python final_pred_model.py --path=validation_set.csv



""""
[Detailed Guide]
# STEP 1: Change current working path to path where you downloaded your file
cd [Path_working_directory]
eg. "cd C:/Users/malco/Downloads/OakTree_DS-main"

#Step 2: unzip file for pretrained model
tar -xf final_model_Model10v1.zip

# STEP 3: pip install requirements.txt
pip install -r requirements.txt 


# STEP 4: run python code
python final_pred_model.py --path=[validation_set.csv]
eg1. "python final_pred_model.py --path=validation_set.csv"
eg2. "python final_pred_model.py --path=C:/Users/malco/Desktop/datasets/validation_set.csv"

""""




