# Prison Database 

![My image](https://github.com/Kartik-Chaurasiya/ds_pro/blob/master/dspro.png)
![My image](https://github.com/Kartik-Chaurasiya/ds_pro/blob/master/ER-Diagram_final_project.png)

##dataset link
[dataset link](https://www.kaggle.com/datasets/rajanand/prison-in-india?select=Jail+wise+population+of+prison+inmates.csv)

## To run it Follow these steps:


### Step 1
Clone the repository


### Step 2
Unzip dbms_backup.tar

Install and open pgAdmin


### Step 3
Open pgAdmin and create a database.

Right click the database and click restore(it will open a popup)

In first dropdown select directory

In second locate the unzipped dbms_backup file and click restore


### Step 4
Open the cloned directory in VScode or any code editor 

In terminal put command: cd ds_pro

In terminal put command: pip install -r requirements.txt [to install all requirements]

go to connection.py and change the credentials of your database


### Step 5
To run the code put command: streamlit run main.py
