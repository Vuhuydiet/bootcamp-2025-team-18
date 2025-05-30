from dotenv import load_dotenv
import os

load_dotenv()

TRAVELDB_URL = os.getenv("TRAVELDB_URL")

if not TRAVELDB_URL:
  raise Exception("TRAVELDB_URL is not set in environment variables")

DEFAULT_EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2.gguf2.f16.gguf"