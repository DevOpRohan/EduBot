from openAiApi import OpenAIAPI
from prompts import bot_sys_prompt, bot_prompt, translator_sys_prompt, translator_prompt


class Bot:
    def __init__(self):
        self.llm = OpenAIAPI()

    async def translate(self, content, lang):
        messages = [
            {
                "role": "system",
                "content": translator_sys_prompt,
            },
            {
                "role": "user",
                "content": translator_prompt.format(content=content, lang=lang)
            }
        ]

        res = await self.llm.chat_completion(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            max_tokens=512
        )

        return res.choices[0].message["content"]

    async def chat(self, problem, solution):
        # 1. Prepare Initial Messages
        messages = [
            {
                "role": "system",
                "content": bot_sys_prompt,
            },
            {
                "role": "user",
                "content": bot_prompt.format(problem=problem, solution=solution)
            }
        ]


        #2.Run a while loop and add the response as role assitant, and display to user and let the user type then add it in message as role user
        while True:
            completion = await self.llm.chat_completion(
                model="gpt-4",
                messages=messages,
                temperature=0,
                max_tokens=512,
            )
            response = completion.choices[0].message["content"]

            res = await self.translate(response, "Hindi")

            print("Bot Response:\n")
            print(res)

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
            translated_input = await self.translate(user_input, "English")
            messages.append(
                {
                    "role": "user",
                    "content": "STUDENT_RESPONSE:\n" + translated_input
                }
            )

# TEST TRANSLATOR #
# bot = Bot()
# import asyncio
# x = asyncio.run(bot.translate("Hello", "Hindi"))
# print(x)