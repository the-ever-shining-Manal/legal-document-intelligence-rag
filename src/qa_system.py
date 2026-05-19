

from config import client, model_name

def ask_llm(query,retrived_chunks):

    context='\n\n'.join([
        f"""
        ARTICLE:{chunk['article']}
        TITLE:{chunk['title']}
        PAGE:{chunk['page']}
        
        {chunk['text']}
        """
        for chunk in retrived_chunks
    ])

    prompt=f"""
    
    YOU ARE A LEGAL DOCUMENT ANALYSIS ASSISTANT
    
    USE ONLY THE PROVIDED CONTEXT
    
    FOR EVERY QUESTION YOU WILL RETURN:
    1- NAME OF THE ARTICLE
    2-NAME OF THE TITLE 
    3- NUMBER OF PAGE
    
    IMPORTANT RULES:
    1- DO NOT HALLUCINATE
    2- IF INFORMATION IS MISSING JUST SAY:
    "not found in provided document"
    
    CONTEXT:
    {context}
    
    QUESTION:
    {query}
    """

    response=client.models.generate_content(
        model=model_name,
        contents=prompt)
    return response.text
    

