# 04_Basic_chatbot_using_Rasa_Video_4_min

# Basic chatbot using Rasa
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/oP2Cp/basic-chatbot-using-rasa

This analysis details the process of extending a default Rasa chatbot, moving beyond strictly rule-based frameworks. The initial approach, which leveraged NLTK, is characterized as rule-based, meaning a specific input results in a predictable, specific output. While suitable for certain applications, this method lacks generalization capabilities, making such systems brittle when faced with creative or unpredictable user inputs. Rasa provides advanced policies that address this limitation, offering much greater flexibility in dialogue management.

Specific Rasa policies include Memoization, which dictates how the conversational stories are interpreted. Stories themselves define the 'happy path' and other pre-considered paths through the dialogue, offering a flexible alternative to rigid rules. Furthermore, the TED policy (Transformer Embedding Dialogue policy) represents a significant advancement in generalization. This policy allows for simultaneous next action prediction and entity recognition, enabling the chatbot to gracefully manage unexpected and unseen user inputs.

The current focus of the discussion, however, remains on the simplest use case: leveraging rules for immediate functionality extension. The configuration process begins by referencing `domain.yml`, which already contains necessary intents and responses. For the specific function of inquiry about hours, a new intent, `hours`, was added to the domain. A corresponding response, `utter_hours`, was also defined.

The Natural Language Understanding (`nlu.yml`) files are crucial for recognizing the `hours` intent. These files can accept various examples, including natural language phrases and regular expressions (regexes), to articulate how the intent might be expressed. To implement the functionality, a new rule was established, linking the detected `hours` intent to the `utter_hours` response. This structure successfully extends the rule-based framework with specific new functionality.

The system was trained and executed using the Rasa shell to demonstrate the rule's effectiveness. When prompted with "What are your hours?", the chatbot correctly activated the newly defined rule and produced the sensible response. Similarly, typing just "hours" successfully triggered the rule based on the regex match. The demonstration showed that these simple rule extensions allow for immediate functional enhancements, such as cheer-up responses. Ultimately, while rules provide basic functionality, the instructor strongly encourages exploring stories and advanced policies like the TED policy for achieving sophisticated conversational behavior. These advanced policies are necessary for dealing with complex and highly coherent dialogue.

