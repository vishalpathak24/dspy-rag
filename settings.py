MODEL_PATH = "/home/vishal/.cache/huggingface/hub/models--bartowski--Llama-3.2-1B-Instruct-GGUF/snapshots/067b946cf014b7c697f3654f621d577a3e3afd1c/Llama-3.2-1B-Instruct-Q6_K.gguf"

PDF_FILE = "data/Manual Administration.pdf"
QUESTION_FILE = "data/question-manual.json"

VECTOR_STORE = "manual-store"

# CREATE DATASTORE
CHUNK_SIZE = 1000
CHUNK_OVER = 200

# RETREIVER
N_DOCS_RETREIVE = 10
SEARCH_METHOD = 'mmr' #'similarity_score_threshold' # 
SCORE_THRESH = 0.3

# MODEL PARAMS
TEMPRATURE = 0.2