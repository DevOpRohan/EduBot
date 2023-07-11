import asyncio
import re
from openAiApi import OpenAIAPI
from prompts import extract_prerequisites_sys_prompt, extract_prerequisites_prompt, extract_prerequisites_init_prompt2


class ContentPreprocessor:
    def __init__(self):
        self.llm = OpenAIAPI()

    async def extract_prerequisites(self, problem, solution):
        messages = [
            {
                "role": "system",
                "content": extract_prerequisites_sys_prompt,
            },
            {
                "role": "user",
                "content": extract_prerequisites_prompt.format(problem=problem, solution=solution)
            },
            {
                "role": "user",
                "content": extract_prerequisites_init_prompt2
            }
        ]
        completion = await self.llm.chat_completion(
            model="gpt-4",
            messages=messages,
            temperature=0,
            max_tokens=512,
        )

        prerequisites = completion.choices[0].message["content"]
        print("Prerequisites:\n")
        print(prerequisites)
        return prerequisites


## Test ##
# asyncio.run(ContentPreprocessor().extract_prerequisites("Find the derivative of y = x^2", "y' = 2x"))
#
