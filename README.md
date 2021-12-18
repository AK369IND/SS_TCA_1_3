# SS_TCA_1_3

I tried deploying on Github pages, it couldn't display jinja2 content even though I followed all instructions. 
I tried deploying on heroku, it build with 0 errors, all dependencies done, yet the app link displays error.

But the app runs on local server. To run the app via bash terminal:

Create a virtual environment, so that it doesn't interfere with your system's packages

    py -m venv venv 
    venv/Scripts/activate 
    
Install packages

    pip install flask 
    pip install flask_session
    pip install requests
    
Run the app

    python -m flask run
