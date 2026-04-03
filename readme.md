# create a virtual environment
To create a virtual environment, run the command python -m venv (your environment name).
If you're on a Mac, use python3 -m venv (your environment name).

# Move into your virtual environment
Activate the virtual environment by accessing it. Open your environment; inside you'll see a folder called Scripts, and within that, you'll find a file called activate. The command is as follows:

/(your environment name)/Scripts/activate or ./(your environment name)/Scripts/activate
Once activated, you should see a green name in the bottom left corner of your VS console with the name of your environment.

# Download the dependencies
Download the project dependencies; you will find a file called requirements. Run the following command: pip install -r requirements.txt or python -m pip install -r requirements.txt

# Run uvicorn to run the local server
To start the local server, run the command uvicorn app.main:app --reload

After running uvicorn you can test the application from your browser with localhost:8000

# Database integration into the chatbot (under development but testing is possible)
The project files include a .sql file corresponding to a PostgreSQL database. You must insert the data from this .sql file to perform tests, and you must have PostgreSQL installed.
To search for ingredients in the database, you currently have to do it manually. It only detects ingredients containing chicken, so to use a search like "I want recipes with chicken." Additionally, user saves have been added, and the bot remembers the user.
Also, when the bot asks for your name, just enter your name, for example "Alonso".

If you wish, you can add new users from scratch by interacting with the bot. The bot will ask for your name, and you should only enter your name. If you try it with Postman, it should have the following structure:

{
"prompt: "Alonso"
"session_id: "4" (this refers to the ID that the name has in the database)
}

# OpenAI API key
Create a .env file in the root of your project and paste your API key inside, ideally named "OPENAI_API_KEY"