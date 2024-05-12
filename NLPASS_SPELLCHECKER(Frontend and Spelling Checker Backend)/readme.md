spellchecker-app/
|-- frontend/
|   |-- ...
|-- backend/
    |-- app.py
    |-- requirements.txt

Prerequisites -
    - Python and node js should be installed in machine
    - any editor of your choice preferrably vs-code
    
Steps to setup backend flask api-
    - Import spellchecker app folder in your vs code
    - Navigate to the Backend Directory: cd backend
    - Run below command on terminal to create python virtual env
        python -m venv venv
    - Run below command on terminal 
        on window - .\venv\Scripts\activate
        on mac - source venv/bin/activate
    - Run below command on terminal to install python libraries
        pip install -r requirements.txt
    - Run below command on terminal to start backend flask app
        python app.py
Steps to setup frontend app -
    - Run below command on terminal to install frontend libraries
        npm install
    - Run below command on terminal to start frontend server
        npm start
Steps to setup Grammer checker flask app on google collab 
    - Open google collab
    - Upload GrammerCheckerFLASKAPI_On_Collab.ipynb notebook on collab
    - Run all cells in notebook
    - Integrate spellchecker backend flask with grammer checker running in collab
        Copy the ngrok url after execution of last cell of notebook url should look like below
        Append /getresponse to copied url. final url should look like below
          example url - http://b740-35-243-213-187.ngrok-free.app/getresponse
        Paste the url to line-90 of model.py file which is inside backend folder
Test the app -
    Open browser and hit http://localhost:3000/ endpoint
    Type or paste any misspelled text in the text area.
    - Find only misspelled words 
        Enter space after pasting or typing text
        You should see a loader in "Misspelled words NLP suggestions" card
        Once processing completes, it will show all misspelled words and corresponding ai suggested corrected words
    - Correct all misspellings and get corrected text
        Click correct button
        It will process all text and replace misspelled text with correct text given by ai powered flask app
        Also it will gives all misspelled words and their corresponding AI suggested correct words in second card