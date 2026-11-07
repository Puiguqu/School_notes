# Week 18 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Basic_chatbot_using_nltk_Video_7_min

# Basic chatbot using nltk
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/cJoJ8/basic-chatbot-using-nltk

This curriculum outlines a 22-week sequence covering foundational and advanced concepts in Natural Language Processing (NLP). The initial phase (Weeks 1-4) focuses on introductory NLP and basic text processing techniques, establishing fundamental skills for language analysis. Subsequent topics delve into Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), exploring how language structure and meaning are mathematically represented. Weeks 9-12 cover advanced text analysis, specifically Text Categorization and Sentiment Analysis, followed by critical structural components like Syntax and Parsing.

The middle section introduces sophisticated applications, including Information Extraction and Information Retrieval (Weeks 13-16), demonstrating how computers derive actionable knowledge from unstructured text data. The course culminates in the study of Chatbots and Dialogue Systems (Weeks 17-18), featuring practical components such as "Basic chatbot using nltk" and extensive sessions on installing and configuring Rasa. Further practice is provided through activities like "Building a legal dialogue system" and dedicated modules on chatbot platforms. The final weeks (19-22) summarize the curriculum, integrating NLP concepts into real-world practice, concluding with a revision and exam period.

---

## 02_Installing_Rasa_Video_7_min

# Installing Rasa
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Pms6U/installing-rasa

The text contrasts basic keyword matching chatbots, built using platforms like NLTK, with modern, sophisticated frameworks. Rasa is presented as a more advanced chatbot platform, capable of utilizing deep learning and contemporary Natural Language Processing (NLP) approaches. The implementation of Rasa requires operating outside of environments like Jupyter Notebooks, typically within a Windows command prompt or terminal.

Installation proved tricky on Windows, although the process was comparatively smoother on a Mac. To install Rasa, the speaker utilized `pip install` within a virtual environment, ensuring a flexible and powerful package setup. The next critical step involves initializing Rasa, which triggers the creation of an initial project and the commencement of training the model.

This initial project setup is resource-intensive and time-consuming. The training process involves flushing output to the screen while the model learns, going through various epochs. The speaker noted a significant difference in performance, where the process took roughly one to two minutes on a high-specification MacBook Pro (16GB memory), but much longer on the lower-spec Windows machine. This highlights that the mileage of training heavily depends on the machine's specifications and processing power.

Once training is completed, the system prompts the user whether they wish to interact with the newly trained bot. The interactive session requires entering the Rasa shell to engage the system.

The demonstration showed the bot responding to inputs like "hello," "say good, and you," and "where do you live." The initial model appeared quite vague, providing generic responses and not fully grasping complex questions.

The server can be shut down, but the bot can be quickly restarted using the command `rasa shell`. Crucially, this command loads the previously trained model instantly, bypassing the entire resource-heavy training process. The text concludes by outlining that future steps will involve examining the configuration files to refine and extend the bot's behavior. This comprehensive guide detailed how to get a sophisticated Rasa chatbot up and running locally on a personal machine.

---

## 03_Configuring_Rasa_Video_4_min

# Configuring Rasa
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ykTrI/configuring-rasa

This course provides a comprehensive journey through Natural Language Processing (NLP) across 22 weeks, starting with an introduction to NLP principles (Weeks 1-2). Subsequent modules cover fundamental data handling, progressing from basic text processing (Weeks 3-4) to the core mechanics of Language Modelling (Weeks 5-6). The curriculum then delves into deeper linguistic analysis, focusing on Lexical Semantics (Weeks 7-8), followed by applications in Text Categorisation and Sentiment Analysis (Weeks 9-10).

Further technical expertise is built through the study of Syntax and Parsing (Weeks 11-12), and the critical skill of Information Extraction (Weeks 13-14). The focus broadens to practical AI application with Information Retrieval (Weeks 15-16) and advanced human-computer interaction via Chatbots and Dialogue Systems (Weeks 17-18).

Practical implementation is emphasized in Section 9.2, covering the basics of chatbots using NLTK, installing and configuring Rasa (including a 7-minute video on Rasa installation), and building a basic chatbot using Rasa Video and practice assignments. The latter part of the course explores advanced concepts, such as building a legal dialogue system and understanding chatbot platforms.

The course culminates with practical application in NLP in practice (Week 19), a final course summary (Week 20), a revision week (Week 21), and the final exam week (Week 22).

---

## 04_Basic_chatbot_using_Rasa_Video_4_min

# Basic chatbot using Rasa
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/oP2Cp/basic-chatbot-using-rasa

This analysis details the process of extending a default Rasa chatbot, moving beyond strictly rule-based frameworks. The initial approach, which leveraged NLTK, is characterized as rule-based, meaning a specific input results in a predictable, specific output. While suitable for certain applications, this method lacks generalization capabilities, making such systems brittle when faced with creative or unpredictable user inputs. Rasa provides advanced policies that address this limitation, offering much greater flexibility in dialogue management.

Specific Rasa policies include Memoization, which dictates how the conversational stories are interpreted. Stories themselves define the 'happy path' and other pre-considered paths through the dialogue, offering a flexible alternative to rigid rules. Furthermore, the TED policy (Transformer Embedding Dialogue policy) represents a significant advancement in generalization. This policy allows for simultaneous next action prediction and entity recognition, enabling the chatbot to gracefully manage unexpected and unseen user inputs.

The current focus of the discussion, however, remains on the simplest use case: leveraging rules for immediate functionality extension. The configuration process begins by referencing `domain.yml`, which already contains necessary intents and responses. For the specific function of inquiry about hours, a new intent, `hours`, was added to the domain. A corresponding response, `utter_hours`, was also defined.

The Natural Language Understanding (`nlu.yml`) files are crucial for recognizing the `hours` intent. These files can accept various examples, including natural language phrases and regular expressions (regexes), to articulate how the intent might be expressed. To implement the functionality, a new rule was established, linking the detected `hours` intent to the `utter_hours` response. This structure successfully extends the rule-based framework with specific new functionality.

The system was trained and executed using the Rasa shell to demonstrate the rule's effectiveness. When prompted with "What are your hours?", the chatbot correctly activated the newly defined rule and produced the sensible response. Similarly, typing just "hours" successfully triggered the rule based on the regex match. The demonstration showed that these simple rule extensions allow for immediate functional enhancements, such as cheer-up responses. Ultimately, while rules provide basic functionality, the instructor strongly encourages exploring stories and advanced policies like the TED policy for achieving sophisticated conversational behavior. These advanced policies are necessary for dealing with complex and highly coherent dialogue.

---

## 05_Building_a_legal_dialogue_system_Reading_1h

# Building a legal dialogue system
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/EjGGg/building-a-legal-dialogue-system

Sharma, M., T. Russell-Rose, L. Barakat and A. Matsuo ' Building a legal dialogue system: development process, challenges and opportunities ', arXiv (2021). If this link is broken, please let us know via the Student Portal . Building a legal dialogue system Sharma, M., T. Russell-Rose, L. Barakat and A. Matsuo ' Building a legal dialogue system: development process, challenges and opportunities ', arXiv (2021). If this link is broken, please let us know via the Student Portal ....

---

## 06_Building_chatbots_Reading_1h

# Building chatbots
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jarlG/building-chatbots

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 7. Building chatbots Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 7. Mark as completed Dislike Report an issue

---

## 07_Activity_Building_your_own_chatbot_Reading_10_min

# Activity: Building your own chatbot
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/mqYKY/activity-building-your-own-chatbot

The primary objective of this exercise is the construction of a custom chatbot. Students have two suggested paths for starting this project. If configuring and installing Rasa is undesirable, utilizing the provided `nltk` example is recommended as the foundational starting point. Alternatively, students may proceed using the Rasa framework, which is intended for more complex development. When defining the chatbot's scope, the assistant should be assigned a simple task. Possible tasks include ordering a pizza or scheduling an appointment. Furthermore, the chatbot can be designed to act as an expert knowledgeable about a subject of the user's choice. For those employing the `nltk` example, specific technical enhancements are suggested. These enhancements include creating additional input/output pairs for broader functionality. Crucially, input variables must be captured using parentheses and indexed, exemplified by `%1`. Rules must be carefully ordered to successfully support both precedence and diversity in responses. Another technical detail involves implementing a simple memory stack, consistent with concepts covered in the lecture. If the student chooses to use Rasa, they are advised to extensively review the available documentation and tutorials. Finally, users are instructed to report any non-functional or broken links through the designated Student Portal.

---

## 08_Dialogue_systems_summary_Video_3_min

# Dialogue systems summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Jddr7/dialogue-systems-summary

This curriculum spans 22 weeks, systematically covering core Natural Language Processing (NLP) concepts, starting with foundational introductions (Weeks 1-2). The initial phase focuses on fundamental text processing (Weeks 3-4), transitioning into language modelling (Weeks 5-6) and exploring lexical semantics (Weeks 7-8) to understand word meaning. Subsequent topics involve advanced linguistic techniques, including text categorisation and sentiment analysis (Weeks 9-10), followed by syntax and parsing (Weeks 11-12). The course then moves into knowledge extraction, covering information extraction (Weeks 13-14) and information retrieval principles (Weeks 15-16). A significant portion is dedicated to chatbots and dialogue systems (Weeks 17-18), which includes practical assignments like building a legal dialogue system. These practical components utilize specific tools, detailed in sessions such as "Basic chatbot using nltk" and tutorials covering the installation, configuration, and basic use of Rasa Video. The learning trajectory concludes with practical application in Week 19 and a comprehensive course summary (Week 20). The final weeks are dedicated to revision (Week 21) and the culminating exam (Week 22).

---

