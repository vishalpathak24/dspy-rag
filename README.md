# AIM
We need to implement basic RAG system and Optimize the prompts using DSPy.

# APPROACH
We needed domain specific Question and Answers. Due to limited time & resource i have focused on smaller pdf and sample questions generated from chat gpt.

# NOTE

Due to limited compute i have taken following assumptions
1. Embedding model is local LLAMA-3.1-1B (I needed to fix `LlamaCppEmbeddings` As current `LlamaCppEmbeddings` works with `.bin` i have modified to work with latest `gguf` files)
2. For Inference have utilized current `Ollama` version.

## STEPS

1. VECTOR STORE CREATION (`create_data_store.ipynb`) : 
    - In this notebook i have created vector database using local 
    - Context widow for this embedding model is reduced to avoid unnecessary memmory usage based on CHUNK Size
2. SIMPLE RAG (`simple-rag.ipynb`): 
    - Langchain based simple rag system using local `llama-3.1`
3. DSPY BASED PROMPT OPTIMISED RAG (`dspy-rag.ipynb`): 
    - This contains `DSPy` based Rag system along with metric (F1 Score) calculation
    - NOTE: I have not utilized `DSPy's` embedding libraries as vector store was created using  `LlamaCppEmbeddings` and documentation `DSPy` was not updated for local Llama embedings

4. COLLAB RUN (`dspy_rag_collabrun.ipynb`):
    Run done on collab space, but ran out of tokens for anthropic, i already have consumed OpenAI's limits :)

# RUN
### Dataset
1. System Manual (Of my previous company) ~17 Pages (Simple data and i am fimiliar with details)
2. GST Smart Guide Short (Top 5 Chapters of book)
3. GST Smart Guide

### Local Run
- I have tried running locally on small dataset (Manual) and local Ollama Server, But compute for single prompt was consuming significant time on local machine + Setup was 1B parameter was ignoring system instructions as shown in `dspy-rag.ipynb`.

### Colab Run
- I have setup the system in colab and (Since, using local Ollama setup was ignoring instruction + will need fixing on why system prompts were ignored). I used `Anthropic's - claude-3-opus` and was able to perform training and evaluation of metrics. But Further exploration (Other Dataset : GST Smart Guide Short, Exploration on response) could not be done as i ran out of tokens.


# Findings
On Manual Data : 
- SemanticF1 Score (As predicted by `DSPy's` prompt ) before training: 76.72, Post Training: 67.25
- Since, These score are algo generated on the fly by AI models their is no proper justification whether they have improved or not. I thought to evaluate with extra personal metric (with actual recall, precision ) of choice to be calculated together with this, But due to lack of time and resource have to stop this experiment as is.






