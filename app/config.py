from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Maximum upload size (5 MB)
MAX_FILE_SIZE = 5 * 1024 * 1024

# Maximum number of pages allowed in a resume
MAX_PDF_PAGES = 10

# Maximum extracted text length
MAX_TEXT_LENGTH = 30000

# Allowed PDF MIME types
ALLOWED_CONTENT_TYPES = {
    "application/pdf",
}
