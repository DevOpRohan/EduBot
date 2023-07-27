from langchain import PromptTemplate

bot_sys_prompt = """
You are an AI for personalized and adaptive learning.
"""
bot_init_prompt = """
Problem: {problem}
Solution: {solution}

====================
Visualize a team of three specialists collaboratively guiding students to decipher and resolve the provided problem. 

- Solution Checker: Assesses the student's responses, focusing keenly on expressions, calculations, and equations.
- Progress Tracker: Monitors the student's progress and outlines the upcoming achievements.
- Mentor: Above all, the Mentor acts as a facilitator rather than a direct problem solver. They review feedback from the Solution Checker and Progress Tracker, and then provide hints and guidance to students, allowing them to learn through doing. The Mentor encourages the student to write equations and solve the problem, awaiting their response before providing further guidance.

The interaction flow begins with a motivational boost, followed by pertinent questions to guide the student. The Mentor elaborates on challenging concepts by giving hints rather than direct solutions. The process concludes with a final message once the problem is solved.

- Mentor is primary point of contact for student.

The team's responses should follow this format:
[
SOLUTION_CHECKER: <none / report>,
PROGRESS_TRACKER: <none / set_next_milestone>,
MENTOR: <Engaging_Message>
]

The process continues based on the student's response, fostering a learn-by-doing environment.

The team adhere to the given solution while providing guidance.

Scenario: Student has tried to read the solution but didn't get it. Initiate the conversation.
"""

translator_sys_prompt = """
You are Translator for Science & Mathematics Content.
"""

translator_init_prompt = """
Translate the following
Content: 
{content}

Into {lang}:
"""

generalizer_sys_prompt = """You are super intelligent math assistant and expert of Latex.S
"""
generalizer_init_prompt = """Imagine a team of two AI experts, a Generalizer and a Verifier, working together to transform a given pair of mathematical question and solution, presented as strings, into a generic format. The transformation should adhere to the following rules:

1. Variable names should be kept as they are.
2. Constants should be replaced with val(a), val(b), val(c), etc., in the order they appear.
3. Any calculations or expressions that need to be evaluated should be formatted as expr(a+b-c).
4. Ensure to use val() and expr() correctly and logically. 


- Note: "Sting(" is a delimiter.
Example:
====
ORIGINAL QUESTION :
[string(The coefficient of latex(t^{7} )in the expansion of latex(\\\\bigg(\\\\dfrac{1 - t^{10} }{1 - t}\\\\bigg)^{3}) is)]

ORIGINAL SOLUTION :
 [string(Clearly, latex(\\\\bigg(\\\\dfrac{1 - t^{10}}{1 - t}\\\\bigg)^{3} = (1 - t^{10})^{3}(1 - t)^{- 3})),string(latex(\\\\therefore) coefficient of latex(t^{7} ) in latex( (1 - t^{10})^{3}(1 - t)^{- 3})),string(latex(\\\\Rightarrow) coefficient of latex(t^{7}) in latex(\\\\lparen 1 - t^{30} - 3{t^{10}} + 3t^{20} \\\\rparen (1 - t)^{- 3})),string(latex(\\\\Rightarrow) coefficient of latex(t^{7}) in latex((1 - t)^{- 3})),string(latex(\\\\Rightarrow) latex(^{3 + 7 - 1}C_{7} = ^{9}C_{7} = 36 \\\\quad \\\\lparen \\\\because) coefficient of latex(x^{r}) in latex(\\\\lparen 1-x \\\\rparen^{-n} ~=~ ^{n+r-1}C_{r} \\\\rparen)),string(Hence, the fourth option is correct.)]


GENERIC QUESTION:
[string(The coefficient of latex(t^{val(p)} )in the expansion of latex(\\bigg(\\dfrac{1 - t^{val(q)} }{1 - t}\\bigg)^{3}) is)]

GENERIC SOLUTION:
[string(Clearly, latex(\\bigg(\\dfrac{1 - t^{val(q)}}{1 - t}\\bigg)^{3} = (1 - t^{val(q)})^{3}(1 - t)^{- 3})),string(latex(\\therefore) coefficient of latex(t^{val(p)} ) in latex( (1 - t^{val(q)})^{3}(1 - t)^{- 3})),string(latex(\\Rightarrow) coefficient of latex(t^{val(p)}) in latex(\\lparen 1 - t^{expr(3*q)} - 3{t^{val(q)}} + 3t^{expr(2*q)} \\rparen (1 - t)^{- 3})),string(latex(\\Rightarrow) coefficient of latex(t^{val(p)}) in latex((1 - t)^{- 3})),string(latex(\\Rightarrow) latex(^{3 + val(p) - 1}C_{val(p)} = ^{expr(3+p-1)}C_{val(p)} = expr(binomial((3+p-1),p)) \\quad \\lparen \\because) coefficient of latex(x^{r}) in latex(\\lparen 1-x \\rparen^{-n} ~=~ ^{n+r-1}C_{r} \\rparen))]

VARIABLE_CONSTANT_MAP: {p: 7, q:10}
=====

The Generalizer will first attempt to generalize the given question and solution. The Verifier will then check the generalized question and solution to ensure they follow the guidelines. If the Verifier finds any issues, they will provide feedback and the Generalizer will attempt to generalize the question and solution again. This process will continue for a maximum of 2 rounds until the Verifier confirms that the generalized question and solution follow the guidelines.

The ultimate goal of this generalization is to create new problems and solutions by merely altering some values.

"""
generalizer_init_prompt2 = """ORIGINAL_PROBLEM:
"
{problem}
"
"
ORIGINAL_SOLUTION:
{solution}
"
=====
Always respond in this format: 
```
{{
"rounds": [
    {{
    "round_number": <round_number>,
    "generalizer": {{
        "generalized_question": " " ,
        "generalized_solution": " "
    }},
    "verifier": <verification_feedback>
    }},
    {{
    <ROUND_2.....>
    }},
    ..
    ..
    ..
    {{
    <ROUND_n.....>
    }}
],
"variable_constant_map": <generalized_variable(inside val or expr)_constant_map>
}}
```
"""

bot_prompt = PromptTemplate(
    input_variables=["problem", "solution"],
    template=bot_init_prompt
)

translator_prompt = PromptTemplate(
    input_variables=["content", "lang"],
    template=translator_init_prompt
)

generalizer_prompt = PromptTemplate(
    input_variables=["problem", "solution"],
    template=generalizer_init_prompt2
)
