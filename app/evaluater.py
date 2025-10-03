import os

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate


class CVEvaluator:
    def __init__(self, openai_api_key):
        self.llm = ChatOpenAI(
            temperature=0, model="gpt-4", openai_api_key=openai_api_key
        )

        self.evaluation_template = """
        You are a recruitment expert. Analyze this CV against the following job description and provide a relevance score out of 100 with justification.

        Job Description:
        {job_description}

        CV:
        {cv_text}

        Respond in JSON format with the keys: score, strengths, weaknesses, match_percentage.
        """
        self.prompt = PromptTemplate(
            template=self.evaluation_template,
            input_variables=["job_description", "cv_text"],
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def evaluate_cv(self, job_description, cv_text):
        response = self.chain.run(job_description=job_description, cv_text=cv_text)
        return eval(response)  # Converts string response to dict
