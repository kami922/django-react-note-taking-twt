import os
from dotenv import load_dotenv
import sys
load_dotenv()
print("test/y")
print(sys.executable)
print(os.environ.get("DB_PWD"))
print(os.getenv("DB_PWD"))