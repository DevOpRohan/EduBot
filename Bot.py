from openAiApi import OpenAIAPI
from preprocessing import ContentPreprocessor
from prompts import bot_sys_prompt, bot_prompt, bot_init_prompt2


class Bot:
    def __init__(self):
        self.llm = OpenAIAPI()
        self.prcessContent = ContentPreprocessor()

    async def chat(self, problem, solution):
        # 1. Retrieve the prerequisites
        prerequisites = await self.prcessContent.extract_prerequisites(problem, solution)

        # 2. Prepare Initial Messages
        messages = [
            {
                "role": "system",
                "content": bot_sys_prompt,
            },
            {
                "role": "user",
                "content": bot_prompt.format(problem=problem, solution=solution, prerequisites=prerequisites)
            },
            {
                "role": "user",
                "content": bot_init_prompt2
            },
        ]

        # 3.Run a while loop and add the response as role assitant, and display to user and let the user type then add it in message as role user
        while True:
            completion = await self.llm.chat_completion(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0,
                max_tokens=512,
            )
            response = completion.choices[0].message["content"]
            print("Bot Response:\n")
            print(response)

            # if response contain @conclude then break the loop
            if "@conclude" in response:
                break
            messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )
            user_input = input("\n\nEnter Your Response:\n ")
            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )
