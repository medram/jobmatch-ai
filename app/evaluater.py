from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

class CVEvaluator:
    def __init__(self, openai_api_key):
        self.llm = ChatOpenAI(temperature=0, model="gpt-4", openai_api_key=openai_api_key)
        
        self.evaluation_template = """
        Vous êtes un expert en recrutement. Analysez ce CV par rapport à la description de poste suivante et donnez un score de pertinence sur 100 avec une justification.

        Description de poste:
        {job_description}

        CV:
        {cv_text}

        Répondez au format JSON avec les clés: score, strengths, weaknesses, match_percentage.
        """
        self.prompt = PromptTemplate(
            template=self.evaluation_template,
            input_variables=["job_description", "cv_text"]
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def evaluate_cv(self, job_description, cv_text):
        response = self.chain.run(job_description=job_description, cv_text=cv_text)
        return eval(response)  # Convertit la réponse string en dict