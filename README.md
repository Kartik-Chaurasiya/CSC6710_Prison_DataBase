# CSC6710_Prison_DataBase

This Project mainly focuses on creating a DataBase for each prison in India. This DataBase holds data related to all the prisons and prisoners in it. We have 11 tables in this database which holds information of prisons, prisoners, deaths in prisons, staff, ipc sections, budgets etc.

### The ER Diagram of the DataBase

<img width="899" alt="Screenshot 2022-11-15 at 11 13 58 AM" src="https://user-images.githubusercontent.com/79399756/202068917-f297b316-eb88-4408-ac93-0f74fd988582.png">

### Our Web Application created using Streamlit framework looks as below

<img width="1680" alt="Screenshot 2022-11-15 at 9 30 56 PM" src="https://user-images.githubusercontent.com/79399756/202069243-8e6e0719-a1f2-4ce9-841d-8c9ca904c607.png">

### How to access the Prisons DataBase

Step 1: Install PgAdmin and open it in your Desktop.

Installation Guide
https://www.pgadmin.org/

Step 2: Create a Database and right click you get restore option

<img width="1680" alt="Screenshot 2022-11-15 at 9 43 41 PM" src="https://user-images.githubusercontent.com/79399756/202071090-bf4069e4-17a6-4860-9872-f9b8a54376ae.png">

Step 3: Unzip DataBase_backup3.tar file in Data Base BackUp File and upload it as shown below

<img width="1680" alt="Screenshot 2022-11-15 at 9 44 02 PM" src="https://user-images.githubusercontent.com/79399756/202071297-78adc666-bc50-4c33-8a98-c5003b6101d6.png">

Step 4: Your DataBase is Ready.

### How to Access Web App

Step 1: Download Streamlit_Framework_Setup folder

Step 2: Open Command Prompt/Terminal in your desktop.
        Use command cd file-path(your file path)

Step 3: Next write the following command 
        pip install -r requirements.txt

Step 4: Next open the connection.py file and change the credentials 

Step 5: Run pip install streamlit 

Step 6: Finally run the following command
        streamlit run main.py for mac
        py -m streamlit run main.py for windows
        
Step 7: Your Web Application is opened in a new chrome tab

Link to the Prison DataSet:
https://www.kaggle.com/datasets/rajanand/prison-in-india?select=Jail+wise+population+of+prison+inmates.csv
