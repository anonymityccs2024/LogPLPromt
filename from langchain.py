import langchain

from langchain.schema import OpenAISettings
from langchain.prompts import DefaultQAPrompt
from langchain.retrievers import ElasticsearchRetriever


openai_settings = OpenAISettings(
    api_key="sk-xQAWOr32U3v3ANNwO22xN5KVHyxTxTs2Uq1VXzOEIfI6NDre", 
    model="gpt-3.5-turbo"        
)


retriever = ElasticsearchRetriever(
    host="localhost",               
    port=9200,                     
    index_name="index-name"    
)


qa_chain = RetrievalQAChain(
    retriever=retriever,
    lm_settings=openai_settings,
    prompt=DefaultQAPrompt()
)