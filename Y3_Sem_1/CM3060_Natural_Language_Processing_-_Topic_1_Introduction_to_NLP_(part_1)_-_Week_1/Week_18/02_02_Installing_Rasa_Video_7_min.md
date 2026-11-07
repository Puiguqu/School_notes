# 02_Installing_Rasa_Video_7_min

# Installing Rasa
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Pms6U/installing-rasa

The text contrasts basic keyword matching chatbots, built using platforms like NLTK, with modern, sophisticated frameworks. Rasa is presented as a more advanced chatbot platform, capable of utilizing deep learning and contemporary Natural Language Processing (NLP) approaches. The implementation of Rasa requires operating outside of environments like Jupyter Notebooks, typically within a Windows command prompt or terminal.

Installation proved tricky on Windows, although the process was comparatively smoother on a Mac. To install Rasa, the speaker utilized `pip install` within a virtual environment, ensuring a flexible and powerful package setup. The next critical step involves initializing Rasa, which triggers the creation of an initial project and the commencement of training the model.

This initial project setup is resource-intensive and time-consuming. The training process involves flushing output to the screen while the model learns, going through various epochs. The speaker noted a significant difference in performance, where the process took roughly one to two minutes on a high-specification MacBook Pro (16GB memory), but much longer on the lower-spec Windows machine. This highlights that the mileage of training heavily depends on the machine's specifications and processing power.

Once training is completed, the system prompts the user whether they wish to interact with the newly trained bot. The interactive session requires entering the Rasa shell to engage the system.

The demonstration showed the bot responding to inputs like "hello," "say good, and you," and "where do you live." The initial model appeared quite vague, providing generic responses and not fully grasping complex questions.

The server can be shut down, but the bot can be quickly restarted using the command `rasa shell`. Crucially, this command loads the previously trained model instantly, bypassing the entire resource-heavy training process. The text concludes by outlining that future steps will involve examining the configuration files to refine and extend the bot's behavior. This comprehensive guide detailed how to get a sophisticated Rasa chatbot up and running locally on a personal machine.

