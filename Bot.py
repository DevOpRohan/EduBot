from openAiApi import OpenAIAPI
from prompts import bot_sys_prompt, bot_prompt, translator_sys_prompt, translator_prompt, format_content_sys_prompt, \
    format_content_prompt


class Bot:
    def __init__(self):
        self.llm = OpenAIAPI()

    async def chat(self, problem, solution, lang="Hindi"):
        # Format the problem and solution
        problem = await self.format_content(problem)
        solution = await self.format_content(solution)

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

        # 2.Run a while loop and add the response as role assitant, and display to user and let the user type then add it in message as role user
        while True:
            completion = await self.llm.chat_completion(
                model="gpt-4",
                messages=messages,
                temperature=0,
                max_tokens=512,
            )
            response = completion.choices[0].message["content"]
            print("Bot Response:\n")
            print(response)
            # if lan is not english then translate the response
            if lang != "English":
                res = await self.translate(response, lang)
                print("\nTranslated Response:\n")
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
            if lang != "English":
                user_input = await self.translate(user_input, "English")

            print("\n\n")

            messages.append(
                {
                    "role": "user",
                    "content": "STUDENT_RESPONSE:\n" + user_input
                }
            )

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

    async def format_content(self, content):
        messages = [
            {
                "role": "system",
                "content": format_content_sys_prompt,
            },
            {
                "role": "user",
                "content": format_content_prompt.format(content=content)
            }
        ]

        res = await self.llm.chat_completion(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            max_tokens=512
        )

        return res.choices[0].message["content"]

# TEST TRANSLATOR #
# bot = Bot()
# import asyncio
# x = asyncio.run(bot.translate("Hello", "Hindi"))
# print(x)

# Test Generalizer #
# bot = Bot()
# import asyncio
#
# problem = """"[string(Sophia works at a reputable art gallery. She earns a commission of latex(6\\%) on every artwork she sells. If she sells a painting for latex(\\$764), how much money does Sophia make in commission?)]
# """
#
# solution = """"[string(To find the amount of commission made, use the following formula Commission rate latex(\\times) retail price latex(=) amount of commission made Since the commission rate is a percentage, we have to convert it into a decimal first. So, latex(6 \\%=\\dfrac{6}{100}=0.06)),string(Now, using the formula and substituting the values, we get latex(0.06 \\times \\$ 764=\\$ 45.84)),string(Therefore, the amount of commission Sophia makes by selling a computer is latex(\\$ 45.84).)]
# """
# x = asyncio.run(bot.generalizer(problem, solution))
# print(x)
