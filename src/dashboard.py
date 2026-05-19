from config import client,model_name
import json

def dashboard_data(chunks):
    dashboard=[]
    for chunk in chunks:
        prompt=f"""
        Analyze the legal text.

        Extract:
        - risks
        - dates
        - stakeholders

        Return ONLY JSON.

        LEGAL TEXT:
        {chunk["text"]}
    
        """

        response=client.models.generate_content(
            model=model_name,
            contents=prompt)

        cleaned_response=response.text.strip("```json").strip("```")
        try:
            extracted_data=json.loads(cleaned_response)
            dashboard.append({
                'article': chunk["article"],
                'page': chunk["page"],
                'data': extracted_data
            })

        except:
            print("failed")

    return dashboard
        
