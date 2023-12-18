from dotenv import load_dotenv, dotenv_values

load_dotenv()
dotenv_val = dotenv_values('.env')

BOT_TOKEN = dotenv_val['BOT_TOKEN']
