
from .base_custom_role_template import BaseCustomRoleTemplate
from .custom_role import CustomRole


PROMPT = """
<s>[INST] <<SYS>>
{persona}
{scenario}
This is how {role_name} should talk
{examples_of_dialogue}
Then the roleplay chat between {you_name} and {role_name} begins.
This is the {you_name} and {role_name} memory module.
{long_history}
[{personality} {role_name} talks a lot with descriptions You only need to output {role_name}'s dialogue, no need to output {you_name}'s dialogue]
{short_history}
Your response should be short and contain up to three sentences of no more than 20 words each.
<</SYS>>
{you_name}：{input} [/INST]
"""

PERSONALITY_PROMPT = "{role_name}'s personality: {personality}"

SCENARIO_PROMPT = "Circumstances and context of the dialogue: {scenario}"


class EnglishCustomRoleTemplate(BaseCustomRoleTemplate):

    def format(self, custom_role: CustomRole) -> str:

        # 获取prompt参数
        role_name = custom_role.role_name
        persona = custom_role.persona
        examples_of_dialogue = custom_role.examples_of_dialogue
        you_name = "{you_name}"
        long_history = "{long_history}"
        short_history = "{short_history}"
        input = "{input}"

        # 格式化性格简述
        personality = custom_role.personality
        if personality != None and personality != '':
            personality = PERSONALITY_PROMPT.format(
                role_name=role_name, personality=personality)
        else:
            personality = ""

        # 格式化情景简述
        scenario = custom_role.scenario
        if scenario != None and scenario != '':
            scenario = SCENARIO_PROMPT.format(scenario=scenario)
        else:
            scenario = ""

        # Generate the prompt to be sent to the language model
        prompt = PROMPT.format(
            role_name=role_name, persona=persona, personality=personality,
            scenario=scenario, examples_of_dialogue=examples_of_dialogue, you_name=you_name,
            long_history=long_history, short_history=short_history, input=input
        )

        return prompt
