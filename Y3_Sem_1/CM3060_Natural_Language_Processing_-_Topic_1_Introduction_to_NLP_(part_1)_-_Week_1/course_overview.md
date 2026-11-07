# CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## Table of Contents

- [Week 1](#week_1)
- [Week 10](#week_10)
- [Week 11](#week_11)
- [Week 12](#week_12)
- [Week 13](#week_13)
- [Week 14](#week_14)
- [Week 15](#week_15)
- [Week 16](#week_16)
- [Week 17](#week_17)
- [Week 18](#week_18)
- [Week 19](#week_19)
- [Week 2](#week_2)
- [Week 20](#week_20)
- [Week 21](#week_21)
- [Week 3](#week_3)
- [Week 4](#week_4)
- [Week 5](#week_5)
- [Week 6](#week_6)
- [Week 7](#week_7)
- [Week 8](#week_8)
- [Week 9](#week_9)

## Week 1

### 01_Welcome_and_introduction_to_the_course_Video_5_min_Get_started

# Welcome and introduction to the course
Video • 5 min
Get started - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/dJl41/welcome-and-introduction-to-the-course

This course provides a comprehensive journey through Natural Language Processing (NLP), bridging both theoretical background and practical applications. NLP is a growing discipline intersecting with computer science, data science, linguistics, and psychology. The study will utilize the Python programming language within a Jupyter environment to illustrate practical techniques. A key learning objective is evaluating the strengths and weaknesses of rule-based versus statistical approaches to NLP. Students will learn to select appropriate statistical language analysis techniques for specific problems and use specialized NLP software libraries. The curriculum will also explore formal grammars and linguistically principled methods, followed by building and evaluating applied NLP solutions.

The course structure is divided into ten major topics, beginning with an introduction to NLP, covering its scope, impact, and various paradigms. Topic Two focuses on fundamental text processing, teaching students to manipulate unstructured data, tokenization, normalization, and defining text corpora. Topic Three introduces language modeling, exploring basic statistical analyses of language data and introducing topic modeling techniques. Next, Topic Four delves into lexical semantics, focusing on how word meanings are represented, utilizing word embeddings and semantic similarity techniques to build applications.

Topic Five addresses text categorization, applying it specifically to sentiment analysis, and introducing concepts like supervised classification and feature extraction. Topic Six moves to linguistically principled approaches, examining the fundamentals of grammar and parsing, including syntax analysis and the probabilistic introduction to parsing. Topic Seven covers information extraction, defining what data is extracted, focusing on named entities and relation extraction, and building corresponding pipelines.

Topic Eight focuses on information retrieval and search, analyzing central data structures and applying techniques such as Boolean search and vector space models. Topic Nine addresses interactive NLP applications, specifically dialogue systems and chatbots. This section involves analyzing human conversation properties, dialogue system architectures, and concepts like speech acts and slot filling.

Finally, Topic Ten examines the practical application of NLP in industry, featuring guest speakers who offer insights into real-world experiences. This concluding module discusses various contexts for NLP, necessary skills for career pursuit, and the future trajectory of the NLP field. (Total: 25 sentences)

---

### 02_Course_syllabus_Reading_10_min

# Course syllabus
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/eKsOb/course-syllabus

Natural language processing (NLP) is defined as the process of machines extracting information from natural human languages. This field represents a crucial and rapidly growing target for advanced computer science techniques. The module provides students with a solid grasp and practical experience in the specialized techniques used in NLP. It complements other modules within the program that deal with the processing and interpretation of data by machines. The core grounding provided by the module encompasses both rule-based and statistical approaches to NLP. The curriculum involves a blend of theoretical study and practical, hands-on application using widely accepted software packages. The focus of this module is specifically on text processing and working with text-based natural language within computer programs. Students will learn how formal grammars can be utilized to perform detailed text analysis. Furthermore, the course teaches how statistical analysis can be applied to extract information and classify text content. Practical implementation involves working in an appropriate programming environment dedicated to NLP workflows. This requires utilizing specific libraries to execute complex NLP workflows. Upon completion, students must be able to explain and evaluate the relative merits of rule-based versus statistical approaches to NLP. They will be able to select suitable statistical language analysis techniques for any given problem scenario. A key practical skill is utilizing software tools such as corpus readers, stemmers, taggers, and parsers to analyze existing texts. Finally, students will evaluate the application of statistical techniques in fields like classification, information extraction, and probabilistic parsing. They will also be able to define formal grammars for various fragments of a natural language.

---

### 03_Reading_list_Reading_10_min

# Reading list
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/OuK3y/reading-list

This reading list provides a comprehensive and technical foundation across the fields of Natural Language Processing (NLP), Data Science, Information Retrieval (IR), and computational text analysis.

A core theoretical reference is Jurafsky and J.H. Martin's *Speech and language processing*, which provides advanced coverage (2026; 3rd ed.). For an accessible introduction to NLP using Python, Bird, Klein, and Loper offer *Natural language processing with Python* (2019). Practical implementation skills are emphasized by Perkins in *Python 3 text processing with NLTK 3 cookbook* (2014). Antić details advanced recipe-based language tasks in *Python natural language processing cookbook* (2021).

The application of data principles is thoroughly covered by Provost and Fawcett in *Data science for business* (2013). This expertise is complemented by VanderPlas's *Python data science handbook* (2016), offering essential tools for data handling. Schütze, Manning, and Raghavan's *Introduction to information retrieval* (2008) serves as the foundational text for search engine and indexing concepts.

Specific applications of text analysis are explored in Hovy's *Text analysis in Python for social scientists* (2020). The corpus-based methods perspective is introduced via Church’s *Unix™ for poets* (1994), an exploration of language through Unix. Furthermore, Lewis et al. contribute technical depth regarding text categorization research in their paper, 'Rcv1: A new benchmark collection for text categorization research' (2004).

The entirety of the recommended reading is available through the Online Library within the Cambridge Core collection. The inclusion of these sources ensures mastery over both the theoretical underpinnings and the practical application of language processing techniques. The materials collectively guide students from basic textual discovery to complex data mining and advanced natural language modeling.

Logistically, the reading list includes a specific technical note: "Issues If any of these links are broken, please let us know via the Student Portal." This emphasizes the necessity of verifying the integrity of all provided resources. The compiled bibliography represents a deep dive into the intersection of computer science and linguistics. These books and papers are critical resources for implementing language processing tasks across various domains.

---

### 04_Introduction_to_NLP_Video_6_min

# Introduction to NLP
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/yKXLb/introduction-to-nlp

This comprehensive 22-week curriculum systematically explores the field of Natural Language Processing (NLP), starting with foundational concepts and progressing toward advanced practical applications. Week 1 provides an introduction to NLP, covering its history, core concepts, and real-world applications via various videos, readings, and practice assignments. The course then moves into fundamental text processing, dedicated over Weeks 3 and 4, before transitioning to the modeling phase in Weeks 5 and 6, focusing on language modelling.

Next, the curriculum delves into the meaning and structure of language: Week 7 and 8 address Lexical Semantics, while Weeks 11 and 12 focus on Syntax and Parsing to understand sentence structure. Practical applications begin in Week 9 and 10 with Text Categorisation and Sentiment Analysis, followed by advanced data gathering techniques in Weeks 13 and 14 via Information Extraction.

Weeks 15 through 18 cover Information Retrieval and Chatbots/Dialogue Systems, demonstrating how NLP systems interact with users and manage vast amounts of data. The program culminates with dedicated sessions in Week 19 focusing on NLP in practice, followed by a Course Summary and a Revision week. The final phase includes the examination week, completing the intensive study of NLP principles.

---

### 05_NLP_applications_part_1_Video_7_min

# NLP applications part 1
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ku0Hy/nlp-applications-part-1

Natural Language Processing (NLP) is a rich, multi-disciplinary field, drawing knowledge from various perspectives. Its foundation is informed not only by computer science and data science but also by information science and computational linguistics. The field adopts multiple methodological paradigms, notably statistical methods and symbolic methods. Over the past few decades, statistical methods have emerged as the dominant paradigm in NLP. Historically, NLP began as an academic discipline confined mostly to research labs. However, in the last decade or decade and a half, it has successfully transitioned into widespread practical applications.

The core problems within NLP can be framed as different types of challenges, including classification problems, regression problems, and sequence labeling problems. Solutions are developed to address these problems, which ultimately lead to the observed applications. These applications showcase the breadth and richness of the field.

Text categorization is a highly valuable application, crucial for managing the abundance of unstructured data. Large news organizations like Reuters, Bloomberg, and the BBC rely on text categorization to filter and distribute news stories at an industrial scale. Similarly, search engines use this technique to make sense of indexed documents and incoming user queries. A more personal application is spam filtering, where text categorization techniques defend against unwanted daily email spam.

One of the earliest significant applications of NLP was machine translation, which emerged in the 1960s and 1970s. Modern examples, such as Google Translate, demonstrate its effectiveness across multiple languages, serving both consumer and professional interpreting needs.

To combat information overload, text summarization has become essential. Summarization tools help abstract massive amounts of text down to its most critical elements. This functionality is built into various tools, including word processors and the snippet generations displayed in modern web search results.

Chatbots and dialogue systems have gained massive popularity in recent years, particularly since around 2016 and 2017. These systems are highly visible in consumer devices like smart speakers (e.g., Alexa). NLP-driven dialogue systems are also integrated into smartphones, whether running Apple or Android operating systems.

Furthermore, advanced telephone call handling systems represent industrial-scale dialogue systems. These systems are used in sectors like travel, hospitality, and banking to effectively and productively manage customer communications.

The course syllabus outlines a structured progression through these concepts. Topics include basic text processing, language modeling, lexical semantics, and syntax and parsing. Specific advanced topics include text categorization and sentiment analysis (Week 9/10) and information extraction (Week 13/14). Finally, the curriculum dedicates substantial time to mastering advanced systems like chatbots and dialogue systems (Week 17/18).

---

### 06_NLP_applications_part_2_Video_8_min

# NLP applications part 2
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ej0DE/nlp-applications-part-2

This 22-week course provides a comprehensive journey through Natural Language Processing, starting with an introductory module on NLP's history, syllabus, and various applications. The initial phase (Weeks 2-4) establishes foundational knowledge through the study of basic text processing techniques. Subsequently, the course delves into predictive modeling with Language Modelling (Weeks 5-6), focusing on how text sequences are structured and predicted. Next, Weeks 7 and 8 explore Lexical Semantics, which examines the meaning and relationships between words within a corpus. Weeks 9 and 10 introduce practical data handling through Text Categorisation and Sentiment Analysis, enabling the classification and emotional evaluation of text. The focus then shifts to structural analysis in Weeks 11 and 12, covering detailed Syntax and Parsing of language. Following this, Weeks 13 and 14 detail Information Extraction, the process of identifying and pulling specific, critical data points from unstructured text. Weeks 15 and 16 cover Information Retrieval, detailing how efficient search systems locate relevant documents within large data sets. The advanced stage of the course (Weeks 17-18) focuses on human-computer interaction through Chatbots and Dialogue Systems. The program concludes with Weeks 19 and 20 dedicated to NLP in practice and course summary, followed by a dedicated revision and final examination week.

---

### 07_History_of_NLP_Video_15_min

# History of NLP
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/YKIfL/history-of-nlp

Natural Language Processing (NLP) is a rich and diverse field whose history stretches back significantly, far from being a recent phenomenon. The field has constantly evolved, characterized by cyclical shifts between various methodological approaches, including symbolic, statistical, and neural techniques. Understanding this history allows us to contextualize contemporary concepts and recognize that complex modern systems often rely on simpler, fundamental ideas.

The historical journey began in the 1940s and 1950s with two foundational paradigms: automata theory and information theoretic models. The concept of automata originated from Alan Turing’s model of algorithmic computation, which serves as a cornerstone of modern computer science. Concurrently, linguist Noam Chomsky utilized Finite State Machines to model and characterize natural language grammar.

Another influential figure, Claude Shannon, adapted entropy from thermodynamics—a measure of randomness—to quantify the information content of a

---

### 08_Introduction_to_NLP_Reading_1h

# Introduction to NLP
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/6MKeO/introduction-to-nlp

Jurafsky, D. and J.H. Martin Speech and language processing . (2008; 2nd ed.). Chapter 1. If this link is broken, please let us know via the Student Portal . Introduction to NLP Jurafsky, D. and J.H. Martin Speech and language processing . (2008; 2nd ed.). Chapter 1. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## Week 10

### 01_Intro_to_sentiment_analysis_Video_15_min

# Intro to sentiment analysis
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ylmC2/intro-to-sentiment-analysis

This comprehensive curriculum covers the evolution of Natural Language Processing (NLP), commencing with foundational knowledge from Weeks 1 through 4, which focus on general introductions and basic text processing techniques. The core theoretical understanding progresses through Weeks 5 and 6 by detailing Language Modelling, followed by Weeks 7 and 8 which explore Lexical Semantics. A major focus area, Weeks 9 and 10 (Topic 5), is dedicated to Text Categorisation and Sentiment Analysis, featuring intensive practical learning. This segment includes specific modules such as "Intro to sentiment analysis" videos, supervised learning assignments, and detailed readings on lexicons and the Reuters Corpus. Subsequent phases delve into structural analysis, starting with Weeks 11 and 12 on Syntax and Parsing, and advancing to Weeks 13 and 14 covering Information Extraction. Weeks 15 and 16 introduce Information Retrieval (IR), while Weeks 17 and 18 address advanced applications in Chatbots and Dialogue Systems. The curriculum culminates in Week 19 and 20, where students apply these concepts in "NLP in practice" and review the course summary. The entire learning sequence is structured over 20 weeks, preparing students for the concluding revision week (Week 21) and the final examination (Week 22).

---

### 02_Sentiment_analysis_using_supervised_learning_Video_10_min

# Sentiment analysis using supervised learning
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/0vwwD/sentiment-analysis-using-supervised-learning

The process discussed focuses on sentiment analysis using supervised machine learning techniques implemented in a Jupyter Notebook environment. The initial step involves utilizing the NLTK `movie reviews` corpus, which contains 2000 movie reviews, providing designated test and training datasets. A list of documents is constructed by iterating through all categories and reviewing every movie review in the corpus. This list includes both positive and negative class labels, which serves as the target variable for classification.

Feature extraction is the core of the sentiment analysis, relying on the frequency distribution of words. All text is converted to lowercase, and an NLTK frequency distribution is instantiated based on the words in the corpus. Crucially, only the top $N$ most common words are selected to form the `word features`. The starting experiments began with a small value, $N=5$, to ensure functions returned in a reasonable time frame.

A specific document feature extraction function is then implemented, which converts the document into a set for faster matching operations. This function generates a dictionary where, for each word within the top $N$ `word features`, it checks for the word's presence in the document, creating a boolean (True/False) pair. For instance, with $N=5$, almost every document contained these common words, leading to many True values.

Initial training used $N=5$ features with a Naive Bayes Classifier, achieving an accuracy of $0

---

### 03_Learning_to_classify_text_Reading_1h

# Learning to classify text
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jlslf/learning-to-classify-text

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 6, pp.221-228. Sections 1 to 1.4 in the above online book version If this link is broken, please let us know via the Student Portal . Learning to classify text Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 6, pp.221-228....

---

### 04_Sentiment_analysis_using_lexicons_Video_5_min

# Sentiment analysis using lexicons
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/H2GMD/sentiment-analysis-using-lexicons

This course on Natural Language Processing (NLP) begins with foundational concepts, dedicating Weeks 1 through 4 to introductions and basic text processing techniques. The focus then shifts to semantics, with Weeks 5 and 6 addressing language modelling, followed by a deep dive into lexical semantics during Weeks 7 and 8. A significant module covers text categorization and sentiment analysis (Weeks 9 and 10), which includes specific analyses like "Sentiment analysis using lexicons," supervised learning classification, and the use of corpora such as the Reuters Corpus Volume 1. The technical progression continues into structural NLP, dedicating Weeks 11 and 12 to syntax and parsing. Subsequent weeks introduce advanced information management techniques, specifically information extraction (Weeks 13 and 14) and information retrieval (Weeks 15 and 16). The curriculum culminates with practical applications in conversational AI, covering chatbots and dialogue systems in Weeks 17 and 18. The final weeks (19 and 20) consolidate knowledge through "NLP in practice" and a comprehensive course summary. The schedule also incorporates numerous learning components, including practice assignments, video lectures, and focused readings on specific sub-topics like lexicons for sentiment and affect. The course concludes with a revision and exam period.

---

### 05_Discovering_sentiment_analysis_Reading_1h

# Discovering sentiment analysis
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/opK97/discovering-sentiment-analysis

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 6 pp.167-169....

---

### 06_Reuters_Corpus_Volume_1_Reading_1h

# Reuters Corpus Volume 1
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/57Bd1/reuters-corpus-volume-1

Lewis, D.D., Y. Yang, T.G. Rose and F. Li ' Rcv1: A new benchmark collection for text categorization research' , Journal of machine learning research 5 2004, pp.361-397. If this link is broken, please let us know via the Student Portal . Reuters Corpus Volume 1 Lewis, D.D., Y. Yang, T.G. Rose and F. Li ' Rcv1: A new benchmark collection for text categorization research' , Journal of machine learning research 5 2004, pp.361-397. If this link is broken, please let us know via the Student Portal ....

---

### 07_Lexicons_for_sentiment,_affect_and_connotation_Reading_1h

# Lexicons for sentiment, affect and connotation
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/czF59/lexicons-for-sentiment-affect-and-connotation

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 22 in the provided link. If this link is broken, please let us know via the Student Portal . Lexicons for sentiment, affect and connotation Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 22 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 08_Text_categorisation_summary_Video_2_min

# Text categorisation summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/lfQ1O/text-categorisation-summary

Topic 5 provided a comprehensive review of text categorization and sentiment analysis, building upon prior learning objectives. The core objectives included understanding categorization fundamentals, exploring sentiment analysis techniques, and evaluating classification methodologies. The discussion began by reviewing various text categorization methods from a conceptual perspective. Initially, the rule-based approach was examined, where high accuracy could be achieved. However, a critical limitation of the rule-based method is its extreme difficulty in scaling and maintaining consistency over large datasets.

The focus then shifted to statistical formalisms, specifically highlighting the application of Naive Bayes. Naive Bayes is presented as a valuable baseline classifier, particularly effective for handling high-dimensional datasets. The methodology involves a set of tunable parameters for optimization. Fundamentally, the process relies upon Bayes’ formula, which established specific terminology for Bayesian classification.

The concepts were explored using a generalized model, where outcomes are represented not just by probabilities, but by areas on a grid of possible outcomes. This generalized view allowed for a detailed thought experiment, such as the "Steve librarian" scenario. Sentiment classification represents a specialized application of this Bayesian approach.

To implement sentiment analysis, a four-step process was walked through using a small toy example. A crucial technical detail discussed in this process was the application of Laplace smoothing. This technique aids in preventing zero probabilities during classification. Practical techniques for implementing these models involved utilizing tools like NLTK.

Beyond supervised learning, the discussion addressed scenarios where training data is unavailable or severely limited. In such cases, manually curated word lists or sentiment lexicons can be employed. These lexicons serve as a non-data-driven method for determining sentiment. The Reuters Corpus Volume 1 was referenced as a practical resource for lexical studies.

The course materials further elaborated on these topics, including a "Sentiment analysis using supervised learning" module (10 min video). Furthermore, a segment titled "Sentiment analysis using lexicons" (5 min video) covered the lexical approach. The supplementary reading on "Lexicons for sentiment, affect and connotation" highlighted this aspect of NLP.

In summary, text classification methods range from high-maintenance rule systems to robust statistical approaches like Naive Bayes. Sentiment analysis applies these principles to classify text based on emotional tone. The next topic in the course will pivot from text processing to exploring the structural complexity of syntax and parsing.

---

## Week 11

### 01_Introduction_and_learning_objectives_Video_1_min

# Introduction and learning objectives
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8EryH/introduction-and-learning-objectives

This course is structured over 22 weeks, beginning with the fundamental concepts of NLP (Week 1-2) and foundational skills like basic text processing (Week 3-4). The curriculum then progresses to crucial modeling techniques, starting with language modelling (Week 5-6) and advancing into lexical semantics (Week 7-8). Next, the focus shifts to applied analysis, covering text categorisation and sentiment analysis (Week 9-10). A major section is dedicated to syntax and parsing (Week 11-12), detailing advanced methods such as Context-free grammars, Constituency parsing, Dependency parsing, and Probabilistic parsing. Subsequently, the study moves into specialized knowledge retrieval, including Information extraction (Week 13-14) and Information retrieval (Week 15-16). The course then examines interactive systems through the study of Chatbots and dialogue systems (Week 17-18). Practical application is reinforced in the final topics, covering NLP in practice and a comprehensive course summary (Week 19-20). The program concludes with a dedicated revision week followed by the final exam week (Week 21-22).

---

### 02_Intro_to_syntax_and_parsing_Video_11_min

# Intro to syntax and parsing
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/omekd/intro-to-syntax-and-parsing

Syntax and parsing examine how words are arranged in language, moving beyond the intuitive understanding of native languages. Within Natural Language Processing (NLP), syntax specifically refers to the arrangement of words to determine if a sequence is legitimate. The concept of constituency is central, meaning groups of words function as a single unit. A grammar is fundamentally an inventory detailing all possible constituents for a given language. For instance, noun phrases like "Harold the Barrel" and "The Barking slugs" share a common syntactic behavior, allowing them to substitute for one another in similar environments.

To model this structure formally, linguists use Context-Free Grammars (CFGs), also known as phrase-structure grammars. A CFG is composed of a set of production rules and a lexicon, which is the collection of valid words in the language. These production rules allow movement from a symbol on the left to a combination of symbols on the right, governed by an arrow ($\rightarrow$).

The components of a CFG are non-terminals (e.g., NP, Determiner, N) and terminal symbols (the actual words). In CFGs, one symbol on the left is always a non-terminal, and the right side is a combination of non-terminal and/or terminal symbols. For example, an NP (Noun Phrase) can be generated by a Determiner followed by a Nominal or a Proper Noun. CFGs can be applied for language generation or to recognize and assign structure within language.

When used for structure recognition, the resulting hierarchical structure is visualized as a parse tree. This tree depicts how various constituents combine upward until they reach the root, known as the start symbol (S), which typically represents a complete sentence. The set of strings derivable from the start symbol defines the language, while derivable strings are considered grammatical, and non-derivable strings are ungrammatical. Syntactic parsing is the specific process of mapping a string of words onto its corresponding

---

### 03_Context-free_grammars_and_recursion_Video_10_min

# Context-free grammars and recursion
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/tMZCy/context-free-grammars-and-recursion

This comprehensive NLP course begins with foundational knowledge, covering basic text processing in the initial weeks. Students then explore Language Modelling and Lexical Semantics to understand how the probability and meaning of words contribute to text understanding. Practical applications follow, focusing on Text Categorisation and Sentiment Analysis to classify and evaluate text content. A major focus is placed on Syntax and Parsing, detailed by the study of Context-free grammars, Constituency grammars, and Dependency parsing. The course delves deeply into parsing methods, including probabilistic parsing, and experiments with understanding these complex linguistic structures. Next, the focus shifts to extracting knowledge through Information Extraction and Information Retrieval techniques. Advanced interaction is covered through the study of Chatbots and Dialogue Systems, preparing students for real-world NLP challenges. The curriculum culminates with applying these principles in NLP in practice, followed by a course summary, revision, and final examination.

---

### 04_Constituency_grammars_Reading

# Constituency grammars
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/3EUTj/constituency-grammars

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 18 in the provided link. If this link is broken, please let us know via the Student Portal . Constituency grammars Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Check chapter 18 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 05_Constituency_parsing_Reading_1h

# Constituency parsing
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/r5evt/constituency-parsing

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 18. If this link is broken, please let us know via the Student Portal . Constituency parsing Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 18. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 06_Dependency_parsing_in_practice_Video_5_min

# Dependency parsing in practice
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/R82VA/dependency-parsing-in-practice

This text provides a detailed comparative analysis of two software libraries, NLTK and spaCy, used for performing dependency parsing in Natural Language Processing (NLP). The core demonstration revolves around analyzing the sentence: "I shot an elephant in my pajamas."

The process begins by exploring dependency parsing, which operates similarly to context-free grammar (CFG) formalism but focuses on directional relationships between words. Using NLTK, a dependency grammar is instantiated, mirroring a process used for CFGs, starting from a defined string. This process results in a projective dependency parser application. When applied to the sample sentence, the parser produces parse trees that illustrate a crucial finding: prepositional phrase attachment ambiguity.

This ambiguity shows two interpretations: one where "the elephant is in the pajamas," represented by a deeply nested cascade bracketing structure. The second interpretation shows that the "in my pajamas" relation attaches to the subject ("I") rather than the direct object ("elephant"). This demonstrates that dependency relations effectively represent the same ambiguity present in constituency structures.

A similar analysis is performed using spaCy, another widely recognized NLP toolkit. To execute spaCy, the library requires downloading and loading a specific model, namely `en_core_web_assembly`, which creates an active NLP object. This object is then applied to the sentence to yield structured results within a document object.

SpaCy’s output is presented by iterating through the tokens, displaying the text, the token's dependency label, and a corresponding explanation. For example, "I" is labeled as the nominal subject, and "shot" is identified as the sentence root. Tokens like "an" (determiner), "elephant" (direct object), "in" (preposition), "my" (possessive/possession modifier), and "pajamas" (propositional object) are precisely categorized.

While the first view shows the token and its dependency label, the second view focuses on structural relationships. The system allows for visualizing ancestors, such as the ancestor of "I" being "shot" (though the root "shot" has no ancestor). Conversely, it can show children, detailing the terms linked to each head word.

Finally, the text explores a composite structure visualization called the subtree for each term. This subtree representation illustrates the full dependency structure radiating from a specific word. For instance, the subtree for "elephant" maps onto itself, showing its connections to "an," "in," and "my pajamas." These practical examples in NLTK and spaCy highlight how dependency parsing provides useful, informative, and accurate insights into direct word relations within a sentence structure.

---

### 07_Probabilistic_parsing_Video_6_min

# Probabilistic parsing
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/vLJwk/probabilistic-parsing

This comprehensive syllabus spans 22 weeks, covering the foundational to advanced aspects of Natural Language Processing (NLP). The initial modules introduce NLP concepts, progressing through basic text processing, and developing language modeling techniques. Subsequent topics delve into lexical semantics and advanced analysis methods, notably covering text categorization and sentiment analysis. Syntax and parsing constitutes a major phase, where concepts are introduced, including Context-Free Grammars and Constituency Grammars. This phase extensively examines parsing techniques, detailing Dependency parsing and the application of Probabilistic parsing. Building on linguistic structure, the course moves to applied tasks such as Information extraction and Information retrieval. Furthermore, advanced application modules explore the development of Chatbots and dialogue systems. The program concludes with dedicated sessions on applying NLP in practice, followed by a course summary and revision period.

---

### 08_Dependency_parsing_Reading_1h

# Dependency parsing
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Wh4XQ/dependency-parsing

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 19. If this link is broken, please let us know via the Student Portal . Dependency parsing Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 19. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## Week 12

### 01_Syntax_and_parsing_summary_Video_2_min

# Syntax and parsing summary
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/yGth5/syntax-and-parsing-summary

The provided text is a comprehensive recap of Topic 6, focusing on the fundamentals of syntax and parsing within Natural Language Processing (NLP). The initial learning objectives for this topic were threefold: to understand the conceptual fundamentals of grammars and parsing, to examine practical applications of syntax analysis techniques, and to explore probabilistic approaches to parsing. The discussion began by reviewing the concept of constituency, which is fundamental to grammatical analysis. Specifically, the text detailed the utilization of Context-Free Grammars (CFGs) for generating and assigning structure to linguistic units.

CFG approaches, often referred to as phrase structure grammar, operate using production rules and parse trees. These tools allow one to progress from a designated starting symbol, S, toward generating an interpretation of a sentence or utterance. A key function of this process is determining whether the input sentence is grammatically permissible or ungrammatical.

In contrast to constituency-based parsing, the analysis then transitioned to Dependency Grammar. This approach changes the perspective by focusing not on how words combine, but rather on the inherent relationships between individual words. Dependency grammar uses specific formulas involving binary asymmetric relationships to structure the data.

This relationship mapping culminates in the creation of a labeled directed graph. In this graph, the central or 'head' element is typically a tensed verb. Dependency relations subsequently flow from these heads to their dependent components.

However, a significant shortcoming of the standard Context-Free Grammar was addressed during the review. It was observed that CFGs often produce numerous equally plausible parses for a given input. This can lead to an undesirable "overload of possibilities."

The text reflected on human cognitive processes, noting that in reality, humans tend to focus on the single, most probable parse, rather than maintaining dozens of equally viable options. To address this limitation, the focus shifted toward implementing probabilistic approaches in parsing. These methods incorporate probabilities directly by attaching probabilities to the production rules and individual production rules. This probabilistic viewpoint allows the system to prioritize the most likely grammatical structure.

The accompanying course outline provides crucial contextual information regarding the structure of the curriculum. The modules covered range from Week 1 (Introduction to NLP, part 1) through Topic 10 (NLP in practice, Week 19).

Topic 6, Syntax and Parsing, is spread across two weeks, specifically Weeks 11 and 12. Other significant topics include Language Modelling (Weeks 5 and 6), Lexical Semantics (Weeks 7 and 8), and Text Categorization and Sentiment Analysis (Weeks 9 and 10).

Later sections of the curriculum detail specialized fields like Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16). Dialogue systems, specifically Chatbots, are covered in Weeks 17 and 18.

The course mandates a Mid-term coursework submission, which is a graded assignment expected to take two hours to complete. The entire instructional period spans until Week 22, dedicated to exam preparation. The transcript itself serves as a detailed summary, covering the transition from conceptual understanding to practical and probabilistic applications in syntax analysis. The technical concepts of grammar, parsing, constituency, and dependency graphs remain the core findings of this review.

---

## Week 13

### 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

### 02_Introduction_to_information_extraction_Video_10_min

# Introduction to information extraction
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/RNy0B/introduction-to-information-extraction

Information Extraction (IE) is a fundamental concept in NLP concerned with converting unstructured natural language data, which possesses implicit structure, into explicitly structured data. This process is essentially a transformation, taking raw input strings and aiming to output formalized database entries. Practically, IE allows the construction of applications designed to extract specific semantic content, such as the who, what, when, and where from text. A basic, formulaic example is the automated markup of text, where algorithms identify patterns like dates, phone numbers, and URLs. This simple extraction provides value by enabling interactive features, such as linking a date to a calendar application. More complex applications include building systems that summarize vast amounts of business news, or curating massive scholarly literature to find subtle, valuable relations.

IE involves several distinct subtasks that address the complexity of extracting meaning. The first is Named Entity Recognition (NER), which identifies proper nouns and objects—like people, places, or companies—and resolves them to unique canonical database identifiers. Next is Relation Extraction, which determines how the identified entities relate to one another. For instance, it identifies if "Person A is employed by Organization B" or "Organization B is based in Location C."

Building upon this, Event Extraction identifies specific episodes or events in which those entities participate, which helps construct a coherent timeline. Event Coreference is necessary because linguistic devices often refer back to events using pronouns, and this task resolves these indirect mentions to a unique event instance. Finally, Temporal Event Expression Extraction addresses the "when" by identifying and resolving various expressions of dates, times, and durations related to the events.

The definition of these relations is not universal; it depends heavily on the problem being solved. One example is the ACE evaluation exercise, which proposes a taxonomy of six top-level categories, including "business/lasting personal," "part-whole relations," and "organization affiliation relations," tailored for Newswire reporting. In contrast, the Unified Medical Language System (UMLS) is highly specialized for medicine, dealing with concepts like bodily locations and injuries. Other systems include DBpedia, which systematizes knowledge derived from Wikipedia infoboxes, and WordNet, which defines relations based on hyponym ("is-a") and instance relationships. Ultimately, researchers often employ bespoke systems of relations created specifically to solve a targeted, problem-centric task.

---

### 03_Relation_extraction_Video_14_min

# Relation extraction
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/l87oQ/relation-extraction

This comprehensive course curriculum spans twenty-two weeks, systematically covering foundational to advanced concepts in Natural Language Processing (NLP). The initial phase focuses on the fundamentals, beginning with an introduction to NLP (Weeks 1-2) followed by mastering basic text processing techniques (Weeks 3-4). The progression then moves into theoretical underpinnings, including language modelling (Weeks 5-6) and the analysis of word meaning through lexical semantics (Weeks 7-8).

Weeks 9 and 10 delve into practical application by covering text categorization and sentiment analysis, while the subsequent weeks (11-12) are dedicated to structural analysis through syntax and parsing. The focus shifts to Information Extraction (Weeks 13-14), which introduces key concepts like relation extraction, POS tagging, and practical implementation using tools such as nltk.

Following information extraction, the course addresses Information Retrieval (Weeks 15-16), a critical aspect of information management. The curriculum culminates in advanced conversational AI, examining Chatbots and Dialogue Systems (Weeks 17-18). The final weeks are dedicated to applying these skills in real-world contexts, covering NLP in practice and a comprehensive course summary (Weeks 19-20). The schedule concludes with a dedicated revision week and the final examination (Weeks 21-22).

---

### 04_POS_tagging_Video_5_min

# POS tagging
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/D0izE/pos-tagging

This transcript introduces Part-of-Speech (POS) tagging, focusing on its role as a vital middle stage in a high-level NLP processing pipeline. Previously, information extraction focused on elementary tags like sentence segmentation and tokenization, followed by sequential processing stages such as POS tagging, Named Entity Recognition (NER), and relation extraction. This lesson specifically drills into the mechanics of POS tagging, which is defined as assigning words to a specific lexical category based on a defined tag set.

To commence the practical demonstration, the speaker utilizes a Jupyter notebook and imports the NLTK library. A sample sentence, sourced from the Reuters corpus, is first tokenized, separating the continuous text into distinct terms. Next, a POS tagger is downloaded from NLTK and applied to the tokenized sentence. The resulting output provides each term alongside its corresponding lexical category tag, such as NNP (proper noun), VBZ (third person singular present tense of a verb), VBN (past participle), and VBG (gerund form).

The core importance of tagging lies in resolving the inherent ambiguity found in human language and syntactic structures. A representative example provided is the ambiguous phrase, "They refuse to permit us to obtain the refuse permit." Although visually identical in spelling, the words "refuse," "permit," and "refuse" (as a noun) are contextually distinct.

The POS tagger successfully navigated this ambiguity, correctly tagging the forms as verbs or nouns based on their usage within the sentence structure. For instance, the instances of "refuse" and "permit" when acting as verbs were correctly categorized, while the noun forms within "the refuse permit" were properly identified as nouns. This demonstrates the tagger's ability to accurately determine lexical categories despite identical spelling.

The transcript further discusses various types of tag sets, noting that they can vary significantly in size, complexity, and level of detail. The default tag set utilized by NLTK is the UPENN tagset. By examining this tagset, the speaker illustrates detailed categories like PRP (personal pronoun), VBP (third person singular present tense of a verb), and DT (determiner).

In summary, POS tagging is a foundational technique for classifying words into predefined categories, enabling more sophisticated NLP operations. The practical demonstration validates its efficacy in resolving lexical ambiguity present in written text. The conclusion sets the stage for subsequent lessons, promising to utilize POS tagging to perform advanced transformations, specifically identifying named entities and extracting relations.

---

### 05_POS_tagging_Reading_1h

# POS tagging
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/9UQ2v/pos-tagging

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 5. If this link is broken, please let us know via the Student Portal . POS tagging Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 5. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 06_Information_extraction_using_nltk_Video_7_min

# Information extraction using nltk
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/okCsP/information-extraction-using-nltk

This course structure provides a comprehensive progression through various disciplines of Natural Language Processing (NLP), spanning introductory concepts through advanced applications. The initial weeks (1-4) establish foundational knowledge, covering general introductions to NLP and fundamental basic text processing techniques. Following this, the curriculum delves into semantic and statistical modeling, focusing on Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8) to understand word meaning and probability.

The middle section focuses on applied linguistic tasks, starting with Text Categorization and Sentiment Analysis (Weeks 9-10) to classify and gauge emotional content in data. This is followed by a detailed study of Syntax and Parsing (Weeks 11-12), which analyzes the grammatical structure of sentences. A significant portion of the course is dedicated to Information Extraction (Weeks 13-14), covering concepts like Relation Extraction, utilizing tools such as NLTK, and performing Point-of-Sale (POS) tagging.

The technical depth continues with Information Retrieval (Weeks 15-16), which addresses how relevant information is found within large datasets. Advanced interaction methods are explored through Chatbots and Dialogue Systems (Weeks 17-18), focusing on conversational AI design. The latter stages transition to practical usage, examining NLP in practice (Weeks 19-20) and concluding with a course summary and revision period (Week 21). The module structure culminates in the final examination week (Week 22).

---

### 07_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/t7oEl/information-extraction

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 7. If this link is broken, please let us know via the Student Portal . Information extraction Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 7. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 08_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Yuglz/information-extraction

Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 20. If this link is broken, please let us know via the Student Portal . Information extraction Jurafsky, D. and J.H. Martin Speech and language processing . (2021; 3rd draft ed.). Chapter 20. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## Week 14

### 01_Chunking_Video_7_min

# Chunking
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/u9RJ9/chunking

Information extraction relies heavily on the process of chunking, which is defined as identifying meaningful chunks within a body of text. For the purposes of this practical example using NLTK, these meaningful chunks are typically conceptualized as noun phrases (NP). To begin, NLTK is utilized, often paired with a sentence that has already been parts-of-speech (POS) tagged. A crucial step involves defining a pattern for the desired noun phrase using a regular expression. The initial grammar definition stipulates an NP consists of an optional determiner, followed by zero or more adjectives, concluding with a noun. This grammar is applied using the `nltk.RegexpParser` class, which is instantiated with the defined grammar. Running the parser successfully identifies the NP structure based on the determiner-adjective-noun pattern. However, the basic grammar is inherently limited; it fails to correctly identify complex examples, such as dropping the word "measures" in "Any new policy measures."

To accommodate complexity, the grammar must be modified significantly. An updated grammar might include an optional determiner, zero or more adjectives (like the comparative form, JJR), and one or more nouns (such as the plural form, NNS). By incorporating these structures, the parser can successfully recognize more intricate NP examples like "earliest stages." Furthermore, grammars can be extended to span multiple lines to handle increasingly complex linguistic structures. When parsing a sentence like "Rapunzel let down her long golden hair," the parser requires a refined grammar to accurately capture the entire phrase. This refinement involves including possessives (a determiner or possessive) in the pattern and correctly defining the sequence of adjectives and nouns.

A key concept in regular expressions is greedy matching, which dictates that if a grammar defines a sequence of two or more nouns, the parser will capture the first match it encounters. This leads to the concept of chinking, which is the inverse of chunking. Chinking involves chunking the entire sequence of text and then specifically removing or ignoring undesired bits. This is achieved by defining negative matching within the grammar, such as targeting sequences of past tense and prepositions.

Finally, a standard method for marking up these labeled sequences is using IOB tags (Beginning, Inside, Outside). The 'B' tag marks the beginning of a chunk, 'I' marks the subsequent words inside the chunk, and 'O' marks text outside any identified chunk. For example, in "the yellow dog," 'the' might be tagged as the beginning of the NP, while 'yellow' and 'dog' would be inside. This IOB system allows for highly flexible notation, enabling the representation of multiple, non-overlapping chunk types for sophisticated information extraction.

---

### 02_Extracting_noun_chunks_with_spaCy_Video_4_min

# Extracting noun chunks with spaCy
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/6sF6U/extracting-noun-chunks-with-spacy

This comprehensive course covers the full spectrum of Natural Language Processing, starting with foundational concepts (Topics 1 and 2) and progressing through structured language understanding. Early modules focus on fundamental processes like basic text processing, followed by the critical development of Language Modelling (Topic 3), which predicts the probability of word sequences. Lexical semantics (Topic 4) is explored in depth, focusing on the meaning and relationships of words, culminating in Text Categorisation and Sentiment Analysis (Topic 5).

Next, the course delves into grammatical structure via Syntax and Parsing (Topic 6), which determines the hierarchy and relationships between words in a sentence. A major focus is Information Extraction (Topic 7), employing specific techniques such as Named Entity Recognition (NER) and noun phrase chunking (e.g., with spaCy) to pull structured data from unstructured text. These concepts build toward Information Retrieval (Topic 8) and the implementation of sophisticated Chatbots and Dialogue Systems (Topic 9).

The later stages apply these theoretical findings to real-world scenarios in NLP practice (Topic 10), integrating all learned skills into functional systems. The final weeks serve as a dedicated Revision week, followed by the culminating Exam week, solidifying the comprehensive knowledge acquired across all topics.

---

### 03_Playing_with_grammar_Reading_1h

# Playing with grammar
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ztCud/playing-with-grammar

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 2. Playing with grammar Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 2. Mark as completed Dislike Report an issue

---

### 04_NER_with_spaCy_Video_2_min

# NER with spaCy
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/kTxjv/ner-with-spacy

This summary provides a comprehensive overview of Named Entity Recognition (NER) as demonstrated through the use of the `spaCy` library, alongside contextual information regarding the NLP curriculum structure.

The core demonstration involves applying `spaCy` to the task of NER within a Jupyter Notebook environment. The process begins by importing and imposing `spaCy`, followed by loading small English language models trained on web data. A simple news article, which contains several interesting entities related to the iPhone 12 launch, is then defined for processing. The loaded model is called on this article, which yields a marked-up document containing identified entities. To analyze the results, the code iterates through the document entities, printing the entity text, the starting character position, the ending character position, and the assigned label.

The initial findings showcase several recognized entities, demonstrating the model's ability to handle various types of data. For instance, the digit "12" is accurately identified as a cardinal, starting at position seven and ending at nine. "Apple" is correctly labeled as an organization, alongside another instance of "Apple" being identified as an organization. The system successfully recognizes "US" as a geopolitical entity, and various dates are identified as cardinals. Specific individuals, such as "Tim Cook" and "Dan Ives," are identified as persons, and "Wedbush Securities" is recognized as an organization.

While generally accurate, the model exhibits minor errors, noting that "iPhones" is misclassified as an organization and "many years" is incorrectly categorized as a person. Experimentation with the API is encouraged using personal content. Further details regarding the sample data set are available in the official `spaCy` documentation.

Crucially, the text defines named entities into two distinct categories for classification. The first category consists of actual named entities, which include people, nationalities, political groups, facilities, organizations, and geopolitical entities. Additionally, this category covers other specific types such as locations, products, events, works of arts, law, and languages.

The second, complementary category includes elements that are not strictly named entities but are commonly recognized during the NER task. These include numerical quantities such as dates, times, percentages, money, and other general numerical data.

The curriculum context provided shows that NER falls within Topic 7: Information extraction, spanning Week 13 (Part 1) and Week 14 (Part 2). This module is supported by various educational resources, including "NER with spaCy Video" (2 minutes duration) and "Information extraction Reading" (1 hour duration).

The broader course structure spans 22 weeks, starting with introductory topics like "Introduction to NLP" in Week 1 and continuing through "Language modelling" (Weeks 5 and 6). Advanced topics include "Syntax and parsing" (Week 11) and culminates in "Information retrieval" (Week 15 and 16) and "Chatbots and dialogue systems" (Week 17 and 18).

Specific practical resources related to Information Extraction include a "Practice Assignment" (10 minutes) and a lab focusing on "Experimenting with noun phrase chunking" (1 hour). Additional material also covers how to extract noun chunks using "spaCy" and playing with grammar reading.

These structured materials emphasize the depth of the information extraction process, providing practical hands-on exercises for students. The content ensures that learners have access to both theoretical understanding and technical application skills related to NLP techniques like NER.

---

### 05_Named_entity_recognition_Reading_1h

# Named entity recognition
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/kSZbD/named-entity-recognition

Russell-Rose, T. ' Zipf's Law: How can something so simple explain so much ', Information Interaction (2010). If this link is broken, please let us know via the Student Portal . Named entity recognition Russell-Rose, T. ' Zipf's Law: How can something so simple explain so much ', Information Interaction (2010). If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 06_Information_extraction_Reading_1h

# Information extraction
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jLxHI/information-extraction

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 5. Information extraction Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 5. Mark as completed Dislike Report an issue

---

### 07_Information_extraction_summary_Video_1_min

# Information extraction summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/adLwx/information-extraction-summary

This comprehensive course structure progresses through fundamental to advanced concepts in Natural Language Processing (NLP). The initial weeks establish the foundation with an introduction to NLP and basic text processing techniques. Subsequently, the focus shifts to predictive and semantic understanding through Language Modelling, followed by Lexical Semantics to analyze vocabulary meaning. The curriculum then moves into applications, covering Text Categorisation and Sentiment Analysis, before addressing the structural analysis of language via Syntax and Parsing. Information Extraction forms a major section, delving into techniques such as NER (Named Entity Recognition) and specific noun phrase chunking, often utilizing tools like spaCy. Further technical detail is provided through assignments and specific modules on chunking videos and grammar reading. The study extends to Information Retrieval, which focuses on finding relevant data, and advanced systems like Chatbots and Dialogue Systems. The course culminates by exploring NLP in practice, followed by a final course summary, revision, and examination.

---

## Week 15

### 01_Introduction_and_learning_objectives_Video_1_min

# Introduction and learning objectives
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8EryH/introduction-and-learning-objectives

This course is structured over 22 weeks, beginning with the fundamental concepts of NLP (Week 1-2) and foundational skills like basic text processing (Week 3-4). The curriculum then progresses to crucial modeling techniques, starting with language modelling (Week 5-6) and advancing into lexical semantics (Week 7-8). Next, the focus shifts to applied analysis, covering text categorisation and sentiment analysis (Week 9-10). A major section is dedicated to syntax and parsing (Week 11-12), detailing advanced methods such as Context-free grammars, Constituency parsing, Dependency parsing, and Probabilistic parsing. Subsequently, the study moves into specialized knowledge retrieval, including Information extraction (Week 13-14) and Information retrieval (Week 15-16). The course then examines interactive systems through the study of Chatbots and dialogue systems (Week 17-18). Practical application is reinforced in the final topics, covering NLP in practice and a comprehensive course summary (Week 19-20). The program concludes with a dedicated revision week followed by the final exam week (Week 21-22).

---

### 02_Boolean_retrieval_Video_10_min

# Boolean retrieval
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/1OGCf/boolean-retrieval

This course provides a comprehensive survey of Natural Language Processing (NLP), beginning with introductory concepts and progressing through basic text processing methods. Core theoretical topics include Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), which establish foundational principles of word meaning and context. The curriculum then delves into higher-level analysis, covering Text Categorisation and Sentiment Analysis (Weeks 9-10), Syntax and Parsing (Weeks 11-12), and Information Extraction (Weeks 13-14). A significant section focuses on Information Retrieval (Weeks 15-16), detailing mechanisms such as Boolean retrieval, Ranked retrieval + term weighting, and the Vector Space Model. Further topics explore conversational AI, covering Chatbots and Dialogue Systems (Weeks 17-18), while also addressing NLP in practice. The latter part of the course synthesizes these concepts, culminating in a detailed course summary (Week 20). The final weeks are dedicated to Revision (Week 21) and Exam preparation (Week 22).

---

### 03_Ranked_retrieval_+_term_weighting_Video_8_min

# Ranked retrieval + term weighting
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/EEQE7/ranked-retrieval-term-weighting

The discussion introduces information retrieval by contrasting two paradigms: Boolean retrieval and ranked retrieval. Boolean retrieval is a set-based approach utilizing Boolean operators such as AND, OR, and NOT, allowing for complex search strings, exemplified by a recruiter's search for Java developers. This method offers a very high degree of control, allowing users to articulate precise queries, and its transparency allows tracing results back to specific keywords. Furthermore, Boolean retrieval facilitates reproducibility, a crucial requirement in scientific and legal research, ensuring results are demonstrably consistent over time and across users.

However, the modern, commoditized nature of web search changes user behavior, leading to "satisficing," where users only seek the first few results deemed "good enough." To better support this dynamic, the concept of ranked retrieval is introduced, which returns matching documents in a specific order, most commonly by relevance. In ranked retrieval, the query terms are typically unstructured keywords, and the system must calculate a relevance score for each document.

The foundational representation for this scoring is the term-document matrix, where each document is treated as a count vector of length $V$, representing the total vocabulary. This leads to the "bag of words" model, which is a mathematical set ignoring the order of words within a document or query. To assign weight to these terms, the concept of term frequency (TF) is employed. TF measures a document's "aboutness" and is defined as the number of times a term $t$ appears in document $d$.

To damp the effect of highly frequent words, TF is often calculated using the log function, specifically $1 + \log(\text{TF})$, where $\text{TF}$ is the term frequency, and adding one accounts for the mathematical property that $\log(1)$ is zero. Next, the mechanism of inverse document frequency (IDF) is introduced, which accounts for a term's informativeness across the entire collection.

Rare terms are inherently more informative than ubiquitous ones, similar to the function of stop words. Document frequency ($\text{DF}$) is defined as the number of documents that contain term $t$. Since high $\text{DF}$ indicates a common term, IDF is calculated as the logarithmic inverse of document frequency: $\log(N / \text{DF}_t)$, where $N$ is the total number of documents in the collection.

The popular and effective term weighting scheme, TF-IDF, is the product of the two weights: $\text{TF-IDF} = \text{TF} \times \text{IDF}$. This measure balances both how often a term appears in a specific document (TF) and how rare it is across the collection (IDF). Finally, the overall ranking score for a particular query-document pair is the sum of all the TF-IDF weights for the terms intersecting between the query and the document. This method, widely implemented in NLP platforms like NLTK and scikit-learn, determines the final order of returned documents.

---

### 04_Boolean_retrieval_Reading

# Boolean retrieval
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/1hSYN/boolean-retrieval

Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval. (Cambridge: Cambridge University Press, 2008). 'Boolean retrieval' . If this link is broken, please let us know via the Student Portal . Boolean retrieval Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval. (Cambridge: Cambridge University Press, 2008). 'Boolean retrieval' . If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 05_Vector_space_model_Video_5_min

# Vector space model
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ukW9Y/vector-space-model

This extensive NLP curriculum is structured into ten major topics, beginning with foundational concepts in Weeks 1-4, introducing the core methodology of NLP and basic text processing. The course progresses through Language Modelling (Weeks 5-6) and deep into Lexical Semantics (Weeks 7-8), covering how meaning is processed in text. Key technical areas include Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by the structural analysis of Syntax and Parsing (Weeks 11-12) and Information Extraction (Weeks 13-14). The later stages focus heavily on Information Retrieval (Weeks 15-16), detailing techniques such as Boolean retrieval, Ranked retrieval with term weighting, and the Vector Space Model. Specific modules also cover practical application domains, including Information Retrieval (Weeks 15-16), Chatbots and Dialogue Systems (Weeks 17-18), and diverse applications in NLP in Practice (Weeks 19-20). Throughout the program, foundational concepts are reinforced by assignments covering Boolean retrieval, Vector Space Model assignments, and activities exploring various IR models. The curriculum concludes with a comprehensive summary, revision week, and examination week, ensuring mastery of all advanced NLP concepts.

---

### 06_Question_answering_Reading_1h

# Question answering
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/TeTUz/question-answering

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Check chapter 11 in the provided link. If this link is broken, please let us know via the Student Portal . Question answering Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Check chapter 11 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 07_Activity_Exploring_IR_models_Reading_1h

# Activity: Exploring IR models
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/pVVUK/activity-exploring-ir-models

This activity explores Information Retrieval (IR) models by requiring the computation of TF.IDF values for the document matrix, using the specified IDF values: car=1.75, vehicle=2.18, insurance=1.72, and best=1.60. The subsequent steps involve calculating the TF.IDF values for the query ‘best car insurance’ and finally ranking each document based on the cosine measure.

---

## Week 16

### 01_Representing_documents_Video_7_min

# Representing documents
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/4ugLx/representing-documents

The text details the practical application of the Bag of Words (BoW) model for document representation in Natural Language Processing (NLP) and information retrieval. The process involves turning unstructured text data into structured, quantifiable features.

The primary tools utilized are `CountVectorizer` from Scikit-learn, which generates vectors based on term counts, and `NLTK`, used for initial text tokenization. The workflow begins by importing these tools and defining helper functions for basic text processing.

For a sample corpus, the vectorizer is instantiated, and the crucial `fit_transform` method is called on the set of input sentences. This fitting step establishes the vocabulary across all documents, generating the feature matrix $X$.

The feature matrix $X$ is initially produced as a sparse matrix, representing the data efficiently. Conceptually, each entry in $X$ is interpreted as a tuple: (Document ID, Term ID, Count). The vocabulary size is determined by the range of Term IDs, which reached 121 in the initial sample.

This sparse representation can be converted into a dense matrix using NumPy. The dense form displays each document on a separate line, with a feature vector of all 121 term occurrences listed for every document.

A key function of the vectorizer is providing `feature_names`, which maps the Term IDs to their corresponding vocabulary words. To apply the vectorizer to new data, such as a new sentence, only the `transform` method is used, utilizing the vocabulary learned during the initial `fit`.

The process demonstrates how to use the BoW model for elementary information processing. However, the vocabulary can be significantly refined using preprocessing techniques.

One critical refinement is the application of stop words. By instructing the vectorizer to remove common terms (e.g., using `stop_words='english'`), the vocabulary size was successfully reduced from 121 to 76. Stop words are generally considered less informative.

Another powerful method is document frequency (DF) filtering, which addresses the concept of Inverse Document Frequency (IDF). This technique eliminates terms that are too ubiquitous.

By setting a maximum document frequency (`max_df`), such as three, the vectorizer removes terms that appear in more than that number of documents. This filtering further reduced the vocabulary size from 121 to 119, and subsequently to 114 when the threshold was lowered.

Ultimately, the text illustrates the complete pipeline for creating a Bag of Words model. This model allows for the translation of linguistic data into numerical vectors.

The combination of `CountVectorizer`, tokenization, stop word removal, and document frequency filtering provides a robust framework for various Information Retrieval and Natural Language Processing tasks. This approach is fundamental for tasks like searching and information sharing.

---

### 02_Term_weighting_using_TF.IDF_Video_5_min

# Term weighting using TF.IDF
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/h4wVF/term-weighting-using-tf-idf

This course provides a comprehensive journey through Natural Language Processing (NLP), beginning with foundational concepts (Weeks 1-2) and progressing through basic text processing techniques (Weeks 3-4). Subsequent modules focus on advanced linguistic understanding, specifically introducing Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8). The curriculum then shifts to applied NLP, covering Text Categorisation and Sentiment Analysis (Weeks 9-10) and detailed linguistic structure through Syntax and Parsing (Weeks 11-12).

Further specialized topics include Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16), where key technical methodologies are covered. Crucially, Week 16 details "Term weighting using TF.IDF," a core concept for document representation and search. Additional IR topics explored include semantic search, query expansion for professional search, and the practice of Boolean search.

The final stages of the course expand into interactive systems, studying Chatbots and Dialogue Systems (Weeks 17-18), before concluding with application and review. Week 19 and 20 focus on practical NLP implementations and a comprehensive course summary, culminating in a final revision and exam period.

---

### 03_Capturing_semantics_Reading_1h

# Capturing semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ElvaK/capturing-semantics

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 3. Capturing semantics Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 3. Mark as completed Dislike Report an issue

---

### 04_Semantic_search_Video_9_min

# Semantic search
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/i43ss/semantic-search

This segment provides an overview of representing documents and implementing various weighting schemes within a conceptual search engine framework. Although real search engines are far more complex, this exercise offers insight into building a functional system in a limited scope. The project utilizes the IMDB dataset, a semi-structured database containing fields such as rank, title, genre, and a free-text description field used for searching. From a search engine perspective, this catalog serves as the corpus being indexed. A critical concept introduced is "Query Term Expansion," which is vital in web search. This expansion directly solves the "vocabulary mismatch problem," where users' keywords may not perfectly match the terminology used in documents, despite a conceptual match. To address this, the process employs Word2Vec via the Gensim library for query term expansion. The setup begins in a Jupiter notebook environment with necessary library imports. Specifically, the Whoosh library is imported to build the open-source search engine. Gensim is also imported, facilitating dense factors and similarity matching with linguistic data. A pre-trained model, `model.bin`, is used, sourced from repositories like vectors.npl.eu. This specific model is trained on an English language corpus using the word2vec continuous skipgram algorithm. Crucially, this model utilizes 100 dimensions and a window size of 10. Variables are set for the dataset path (CSV format) and the index path, which functions like the inverted index (postings lists). The search engine structure is defined, emphasizing the parsing of queries against the title and description fields. After instantiation, the Gensim model is loaded using the defined path. The system features a "Get similar words" method, which calls the model's most similar function to retrieve top matching terms for a given search query. Demonstrating its function, searching for the term "Galactic" yields matching terms such as "intergalactic" and "interstellar." To perform the search, the initial term is joined with these expanded words using a large OR statement, mirroring boolean retrieval. This query expansion process successfully identifies relevant films, such as "Guardians of the Galaxy," demonstrating the semantic search capability. A second test using the query "gigantic" successfully expands to terms like "Colossal," returning the movie "Colossal." Other useful Gensim methods demonstrated include "Doesn't_match" and "Most_similar_to_given" for NLP applications. In summary, Whoosh serves as the robust search engine library, while Gensim augments it with semantic search capability for query expansion. This integration allows for refined search outcomes by addressing vocabulary mismatch effectively.

---

### 05_Query_expansion_for_professional_search_Reading_1h

# Query expansion for professional search
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/lZyOv/query-expansion-for-professional-search

Russell-Rose, T., P. Gooch and U. Kruschwitz ' Interactive query expansion for professional search applications ', Business Information Review, 2021. If this link is broken, please let us know via the Student Portal . Query expansion for professional search Russell-Rose, T., P. Gooch and U. Kruschwitz ' Interactive query expansion for professional search applications ', Business Information Review, 2021. If this link is broken, please let us know via the Student Portal ....

---

### 06_Activity_Exploring_Boolean_search_Reading_10_min

# Activity: Exploring Boolean search
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/waS0C/activity-exploring-boolean-search

the attached pdf file and follow the instructions to work through the exercise. 8.209 Exploring Boolean search.pdf PDF File Activity: Exploring Boolean search the attached pdf file and follow the instructions to work through the exercise. 8.209 Exploring Boolean search.pdf PDF File Mark as completed Dislike Report an issue

---

### 07_IR_summary_Video_3_min

# IR summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/PpN9D/ir-summary

This comprehensive course spans 22 weeks, commencing with foundational knowledge in NLP (Weeks 1-2) and moving into essential basic text processing techniques (Weeks 3-4). The curriculum then delves into language modelling (Weeks 5-6) to understand statistical text generation and lexical semantics (Weeks 7-8) to define word meanings. Subsequent topics include text categorisation and sentiment analysis (Weeks 9-10), followed by the structural analysis of syntax and parsing (Weeks 11-12). The focus then shifts to practical data retrieval, covering information extraction (Weeks 13-14) and information retrieval (Weeks 15-16). Topic 8 emphasizes advanced IR practices, detailing document representation, term weighting using TF.IDF, semantic search, and effective query expansion and Boolean search. The advanced application phase introduces chatbots and dialogue systems (Weeks 17-18), showcasing how NLP is applied in real-world scenarios (Week 19). The final weeks consolidate these concepts in a course summary and revision period (Weeks 20-21). The study culminates in the examination week (Week 22).

---

## Week 17

### 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

### 02_Properties_of_human_conversation_Video_9_min

# Properties of human conversation
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/CN1S9/properties-of-human-conversation

This comprehensive course spans 22 weeks, beginning with fundamental concepts in NLP (Weeks 1-2). The initial phase focuses on basic text processing (Weeks 3-4), establishing the groundwork for analyzing raw data. Key concepts then progress to Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), which define how language structure and meaning are understood. The subsequent modules cover advanced linguistic analysis, including Text Categorization and Sentiment Analysis (Weeks 9-10) and detailed Syntax and Parsing (Weeks 11-12). The course emphasizes knowledge extraction through dedicated sections on Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). A major focus is placed on interactive systems, detailed across Weeks 17 and 18, covering Chatbots and Dialogue Systems. Furthermore, practical application is reinforced by Week 19, dedicated to "NLP in Practice," and Week 20, serving as the Course Summary. Weeks 21 and 22 are allocated for revision and the final exam. All modules utilize varied learning formats, including video lectures, reading materials, and practice assignments, such as those related to properties of human conversation and speech acts.

---

### 03_Chatbots_Video_10_min

# Chatbots
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/lJU4t/chatbots

Chatbots are categorized as simple dialogue systems, designed primarily for conversation, entertainment, or therapeutic value rather than strictly completing specific tasks. Although early chatbots were highly hyped, they have found functional places in both home and office environments. Examples include Facebook's BlenderBot and Microsoft's Xiaoice. Underlying these systems are two primary classes of architecture: rule-based or data-driven (corpus-based).

The rule-based approach is exemplified by ELIZA, the first-ever chatbot developed by Joseph Weizenbaum in 1966. ELIZA operates as a Rogerian psychotherapist, reflecting the participant's own thoughts without dispensing clinical advice. Functionally, it utilizes rules, often implemented as a Regular Expression (RegEx), which map input patterns to production rules. For instance, the pattern `you love me` might transform into the question, "What makes you think I love you?"

These transformations are linked to specific keywords (e.g., "I," "my"), which are ranked by specificity. This ranking mechanism instantiates Grice's maxims, ensuring the response is as relevant as possible to the user's utterance. Furthermore, ELIZA maintains dialogue coherence by employing a memory or stack of previous transformations, triggered by the keyword "my."

The complementary corpus-based approach is highly data-driven, relying on machine learning paradigms trained on large datasets. These corpora can include call-center transcripts, movie dialogues, or pseudo dialogues derived from sources like Twitter exchanges. When using live usage data for training, confidence metrics must be

---

### 04_Task-based_dialogue_systems_Video_11_min

# Task-based dialogue systems
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/V5lat/task-based-dialogue-systems

This comprehensive course is structured over 22 weeks, designed to provide a deep dive into Natural Language Processing (NLP), starting with an introduction to the field. The initial phase focuses on foundational concepts, covering basic text processing techniques and transitioning into language modeling, which addresses how sequences of words are predicted. Semantic understanding is explored through Lexical Semantics, followed by the practical application of Text Categorisation and Sentiment Analysis. The core structural elements of language are then addressed through Syntax and Parsing, enabling the analysis of grammatical structures. Subsequent topics focus on extracting specific knowledge, covering Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). A major advanced focus is placed on Chatbots and Dialogue Systems (Weeks 17-18), including detailed study of properties of human conversation, task-based systems, and design/evaluation methodologies. Furthermore, the curriculum integrates these concepts through NLP in Practice (Weeks 19-20), serving as a real-world application context. The course concludes with a Course Summary and a dedicated Revision Week (Week 21). The final week (Week 22) is reserved for the comprehensive examination.

---

### 05_Design_and_evaluation_Video_9_min

# Design and evaluation
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Fr4vx/design-and-evaluation

Designing dialogue systems is an interactive process that requires drawing upon principles from human-computer interaction (HCI). Consequently, the User-Centered Design process is essential to guide and shape the development of these conversational products. This process requires studying user tasks to develop a deep, evidence-based understanding of who the user is, what their capabilities are, and their context. Following this, simulations and prototypes are iteratively built and then tested directly with users to gather crucial feedback.

A standard framework for this is ISO 9241-210, which dictates identifying the need, specifying the context of use, producing design solutions/prototypes, and finally evaluating them with users. Importantly, the entire design process is iterative, as feedback is used to refine the context of use and requirements, refining the solution until acceptance criteria are met. Another model, Design Council's Double Diamond, frames design as starting with divergent thinking (research), moving to convergent thinking (defining the problem), then design exploration (ideation), and finally delivering a narrowed-down prototype.

Due to the high cost of building and revising complex dialogue systems, researchers frequently employ the Wizard of Oz technique. This method involves inserting a human researcher into the loop to emulate complex behaviors, allowing research and feedback gathering without needing to build the actual, expensive system in advance.

Evaluation in Natural Language Processing (NLP) can be automated, using metrics like BLEU or ROUGE, which are based on patterns of co-occurrence and n-grams in benchmark and test data. However, because generative chat conversations are highly diverse, manual evaluation is typically necessary.

Manual evaluation follows two main approaches: participant evaluation and observer evaluation. In participant evaluation, the user taking part in the dialogue administers an evaluation using questionnaires across eight dimensions, such as fluency, interestingness, and engagingness. Observer evaluation involves third-party annotators assessing a complete conversation, often comparing it via an AB test against a benchmark system on scales like humanness and knowledgeable.

For task-based dialogue systems, evaluation focuses on measuring task success—whether the user completed the task within appropriate time and effort—or user satisfaction via questionnaires. Alternatively, quantitative measures include examining slot error rates, and calculating slot precision, recall, or the F-measure to gauge accuracy.

Finally, ethical considerations are paramount in NLP. Since machine learning systems are trained on data, they inevitably replicate and amplify existing societal biases, including gender stereotypes. Researchers must be aware that these biases can be propagated through the ML approaches, similar to the issues observed with the Microsoft Tay chatbot. Furthermore, safeguarding privacy is critical; dialogue agents may inadvertently capture private information, such as passwords, which should never be used as training data.

---

### 06_Chatbots_and_dialogue_systems_Reading

# Chatbots and dialogue systems
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ILRm4/chatbots-and-dialogue-systems

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Refer to chapter 25 in the provided link. If this link is broken, please let us know via the Student Portal . Chatbots and dialogue systems Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Refer to chapter 25 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 07_Activity_Exploring_speech_acts_Reading_10_min

# Activity: Exploring speech acts
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/StEif/activity-exploring-speech-acts

This document outlines a communicative exercise requiring the examination and labeling of a conversation using specific speech act categories. These categories include Constatives, which commit the speaker to a proposition like claiming or denying. Directives aim to get the addressee to perform an action, such as asking or inviting. Commissives involve committing to a future course of action, like promising or planning. Finally, Acknowledgements express reactions to an action, such as thanking or greeting.

The conversation begins with C1 stating the need to travel in May. A2 initiates the dialogue by inquiring about the desired day of travel in May. C3 clarifies the necessity of the travel, specifying a required meeting attendance from the 12th to the 15th. A4 then seeks the destination city for the flight. C5 confirms the destination as Seattle.

A6 directs the conversation toward the preferred departure time from Pittsburgh. C7 reports that there are few options available for non-stop travel. A8 counters this by stating that three non-stop options are available for the day. C9 requests the detailed schedule of these options. A10 meticulously lists the three flights. The first departs PGH at 10:00am and arrives in Seattle at an unspecified time. The second option departs PGH at 5:55pm and arrives in Seattle at 8pm. The last flight departs PGH at 8:15pm, arriving in Seattle at 10:28pm.

C11 makes a selection, opting for the "5ish flight on the night before on the 11th." A12 confirms this choice, detailing the specific logistics. This itinerary involves departing at 5:55pm, arriving in Seattle at 8pm, and being assigned as U.S. Air flight 115. C13 provides a simple acknowledgement of this decision.

A14 then verifies the originally stated return date of May 15th. C15 affirms this date, clarifying that the return is "at the end of the day." A16 then notes that there are two non-stops available for the return journey. C17 acts to clarify the calendar logistics, asking for the day of the week corresponding to the 15th. A18 provides the necessary calendar information, confirming that the 15th is a Friday.

C19 then proposes a modification to the travel plan, suggesting a stay extension until Sunday. A20 accepts the suggestion, indicating agreement with the new schedule. The conversation concludes with A20 stating that an activity is planned for Sunday, leaving the planning process incomplete. This exercise demonstrates the practical application of classifying conversational functions within a real-world travel scenario.

---

## Week 18

### 01_Basic_chatbot_using_nltk_Video_7_min

# Basic chatbot using nltk
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/cJoJ8/basic-chatbot-using-nltk

This curriculum outlines a 22-week sequence covering foundational and advanced concepts in Natural Language Processing (NLP). The initial phase (Weeks 1-4) focuses on introductory NLP and basic text processing techniques, establishing fundamental skills for language analysis. Subsequent topics delve into Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), exploring how language structure and meaning are mathematically represented. Weeks 9-12 cover advanced text analysis, specifically Text Categorization and Sentiment Analysis, followed by critical structural components like Syntax and Parsing.

The middle section introduces sophisticated applications, including Information Extraction and Information Retrieval (Weeks 13-16), demonstrating how computers derive actionable knowledge from unstructured text data. The course culminates in the study of Chatbots and Dialogue Systems (Weeks 17-18), featuring practical components such as "Basic chatbot using nltk" and extensive sessions on installing and configuring Rasa. Further practice is provided through activities like "Building a legal dialogue system" and dedicated modules on chatbot platforms. The final weeks (19-22) summarize the curriculum, integrating NLP concepts into real-world practice, concluding with a revision and exam period.

---

### 02_Installing_Rasa_Video_7_min

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

### 03_Configuring_Rasa_Video_4_min

# Configuring Rasa
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ykTrI/configuring-rasa

This course provides a comprehensive journey through Natural Language Processing (NLP) across 22 weeks, starting with an introduction to NLP principles (Weeks 1-2). Subsequent modules cover fundamental data handling, progressing from basic text processing (Weeks 3-4) to the core mechanics of Language Modelling (Weeks 5-6). The curriculum then delves into deeper linguistic analysis, focusing on Lexical Semantics (Weeks 7-8), followed by applications in Text Categorisation and Sentiment Analysis (Weeks 9-10).

Further technical expertise is built through the study of Syntax and Parsing (Weeks 11-12), and the critical skill of Information Extraction (Weeks 13-14). The focus broadens to practical AI application with Information Retrieval (Weeks 15-16) and advanced human-computer interaction via Chatbots and Dialogue Systems (Weeks 17-18).

Practical implementation is emphasized in Section 9.2, covering the basics of chatbots using NLTK, installing and configuring Rasa (including a 7-minute video on Rasa installation), and building a basic chatbot using Rasa Video and practice assignments. The latter part of the course explores advanced concepts, such as building a legal dialogue system and understanding chatbot platforms.

The course culminates with practical application in NLP in practice (Week 19), a final course summary (Week 20), a revision week (Week 21), and the final exam week (Week 22).

---

### 04_Basic_chatbot_using_Rasa_Video_4_min

# Basic chatbot using Rasa
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/oP2Cp/basic-chatbot-using-rasa

This analysis details the process of extending a default Rasa chatbot, moving beyond strictly rule-based frameworks. The initial approach, which leveraged NLTK, is characterized as rule-based, meaning a specific input results in a predictable, specific output. While suitable for certain applications, this method lacks generalization capabilities, making such systems brittle when faced with creative or unpredictable user inputs. Rasa provides advanced policies that address this limitation, offering much greater flexibility in dialogue management.

Specific Rasa policies include Memoization, which dictates how the conversational stories are interpreted. Stories themselves define the 'happy path' and other pre-considered paths through the dialogue, offering a flexible alternative to rigid rules. Furthermore, the TED policy (Transformer Embedding Dialogue policy) represents a significant advancement in generalization. This policy allows for simultaneous next action prediction and entity recognition, enabling the chatbot to gracefully manage unexpected and unseen user inputs.

The current focus of the discussion, however, remains on the simplest use case: leveraging rules for immediate functionality extension. The configuration process begins by referencing `domain.yml`, which already contains necessary intents and responses. For the specific function of inquiry about hours, a new intent, `hours`, was added to the domain. A corresponding response, `utter_hours`, was also defined.

The Natural Language Understanding (`nlu.yml`) files are crucial for recognizing the `hours` intent. These files can accept various examples, including natural language phrases and regular expressions (regexes), to articulate how the intent might be expressed. To implement the functionality, a new rule was established, linking the detected `hours` intent to the `utter_hours` response. This structure successfully extends the rule-based framework with specific new functionality.

The system was trained and executed using the Rasa shell to demonstrate the rule's effectiveness. When prompted with "What are your hours?", the chatbot correctly activated the newly defined rule and produced the sensible response. Similarly, typing just "hours" successfully triggered the rule based on the regex match. The demonstration showed that these simple rule extensions allow for immediate functional enhancements, such as cheer-up responses. Ultimately, while rules provide basic functionality, the instructor strongly encourages exploring stories and advanced policies like the TED policy for achieving sophisticated conversational behavior. These advanced policies are necessary for dealing with complex and highly coherent dialogue.

---

### 05_Building_a_legal_dialogue_system_Reading_1h

# Building a legal dialogue system
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/EjGGg/building-a-legal-dialogue-system

Sharma, M., T. Russell-Rose, L. Barakat and A. Matsuo ' Building a legal dialogue system: development process, challenges and opportunities ', arXiv (2021). If this link is broken, please let us know via the Student Portal . Building a legal dialogue system Sharma, M., T. Russell-Rose, L. Barakat and A. Matsuo ' Building a legal dialogue system: development process, challenges and opportunities ', arXiv (2021). If this link is broken, please let us know via the Student Portal ....

---

### 06_Building_chatbots_Reading_1h

# Building chatbots
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jarlG/building-chatbots

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 7. Building chatbots Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 7. Mark as completed Dislike Report an issue

---

### 07_Activity_Building_your_own_chatbot_Reading_10_min

# Activity: Building your own chatbot
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/mqYKY/activity-building-your-own-chatbot

The primary objective of this exercise is the construction of a custom chatbot. Students have two suggested paths for starting this project. If configuring and installing Rasa is undesirable, utilizing the provided `nltk` example is recommended as the foundational starting point. Alternatively, students may proceed using the Rasa framework, which is intended for more complex development. When defining the chatbot's scope, the assistant should be assigned a simple task. Possible tasks include ordering a pizza or scheduling an appointment. Furthermore, the chatbot can be designed to act as an expert knowledgeable about a subject of the user's choice. For those employing the `nltk` example, specific technical enhancements are suggested. These enhancements include creating additional input/output pairs for broader functionality. Crucially, input variables must be captured using parentheses and indexed, exemplified by `%1`. Rules must be carefully ordered to successfully support both precedence and diversity in responses. Another technical detail involves implementing a simple memory stack, consistent with concepts covered in the lecture. If the student chooses to use Rasa, they are advised to extensively review the available documentation and tutorials. Finally, users are instructed to report any non-functional or broken links through the designated Student Portal.

---

### 08_Dialogue_systems_summary_Video_3_min

# Dialogue systems summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Jddr7/dialogue-systems-summary

This curriculum spans 22 weeks, systematically covering core Natural Language Processing (NLP) concepts, starting with foundational introductions (Weeks 1-2). The initial phase focuses on fundamental text processing (Weeks 3-4), transitioning into language modelling (Weeks 5-6) and exploring lexical semantics (Weeks 7-8) to understand word meaning. Subsequent topics involve advanced linguistic techniques, including text categorisation and sentiment analysis (Weeks 9-10), followed by syntax and parsing (Weeks 11-12). The course then moves into knowledge extraction, covering information extraction (Weeks 13-14) and information retrieval principles (Weeks 15-16). A significant portion is dedicated to chatbots and dialogue systems (Weeks 17-18), which includes practical assignments like building a legal dialogue system. These practical components utilize specific tools, detailed in sessions such as "Basic chatbot using nltk" and tutorials covering the installation, configuration, and basic use of Rasa Video. The learning trajectory concludes with practical application in Week 19 and a comprehensive course summary (Week 20). The final weeks are dedicated to revision (Week 21) and the culminating exam (Week 22).

---

## Week 19

### 01_Introduction_to_Topic_10_Video_2_min

# Introduction to Topic 10
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/4mNzQ/introduction-to-topic-10

This summary outlines the focus, objectives, technical content, and structure of Topic 10: NLP in Practice.

The current course topic shifts significantly from previous modules, which focused on scholarly material, theory, and practice. Topic 10 focuses exclusively on the latter, emphasizing practical application over abstract theory. The overarching theme is centered on the practical implementation and application of Natural Language Processing (NLP) techniques.

There are two primary course learning objectives for this problem-centric topic. The first objective requires students to consider appropriate language analysis techniques for specific, real-world problems. The second objective involves understanding and utilizing the practical tooling available in the NLP field.

The instructional approach for Topic 10 differs from previous courses. Instead of the instructor imparting years of personal experience, this topic utilizes interviews with various community experts. These featured guests contribute unique insights, collectively bringing many decades of NLP experience to the curriculum.

The third learning objective addresses NLP skills and competencies vital for prospective professionals. This focuses on the expected knowledge required to be hired as an NLP specialist. A significant finding from these expert discussions is the importance of basic engineering skills. Students must learn to contextualize NLP techniques within broader software engineering and data science frameworks.

Beyond immediate practice, the topic also addresses NLP trends and future developments. The instructors used the interviews to question experts about what is currently "hot" and what is predicted to be hot in the future.

The detailed curriculum structure shows a broad progression of NLP topics before reaching Topic 10. Earlier topics covered basic text processing (Weeks 3-4), language modelling (Weeks 5-6), and lexical semantics (Weeks 7-8). Further subjects included text categorization and sentiment analysis (Week 9-10), syntax and parsing (Week 11-12), and information extraction (Week 13-14). Information retrieval was studied in Weeks 15-16, followed by chatbots and dialogue systems in Weeks 17-18.

Topic 10 itself is highly structured and resource-intensive. It features a comprehensive lineup of specialized discussions and readings. These include specific interviews with experts such as Phil Gooch, Diana Maynard, David Elworthy, Richard Jackson, and Udo Kruschwitz.

The technical readings within this module cover advanced topics necessary for modern NLP practice. Key subjects include an exploration of neural networks and neural language models. Furthermore, the material delves into sequence labelling for tasks like identifying parts of speech and named entities. Students also engage with concepts related to deep learning architectures for sequence processing. The curriculum dedicates specific sessions, such as the "Neural networks and neural language models Reading," to these advanced concepts. The overall structure covers both the introductory aspects of Topic 10 (Week 19) and a final Course Summary (Week 20).

---

### 02_Phil_Gooch_interview_Video_16_min

# Phil Gooch interview
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/BTLoq/phil-gooch-interview

This course provides a comprehensive 22-week curriculum, beginning with introductory concepts (Weeks 1-2) and moving into basic text processing (Weeks 3-4). The study then transitions to core linguistic components, covering Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8) to establish word meaning and probability. Key applications include Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by an exploration of grammatical structure through Syntax and Parsing (Weeks 11-12). Further focus is placed on specialized data operations, specifically Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). Interaction capabilities are addressed through dedicated modules on Chatbots and Dialogue Systems (Weeks 17-18). The syllabus culminates in Week 19, shifting to advanced practices, which includes topics like neural networks, deep learning architectures for sequence processing, and sequence labelling for parts of speech and named entities. This practical phase also features multiple interviews and professional insights from industry experts. The course concludes with a final summary (Week 20), a revision week (Week 21), and the culminating examination (Week 22).

---

### 03_Neural_networks_and_neural_language_models_Reading_1h

# Neural networks and neural language models
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/OxGcn/neural-networks-and-neural-language-models

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 6. If this link is broken, please let us know via the Student Portal . Neural networks and neural language models Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 6. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 04_Diana_Maynard_interview_Video_24_min

# Diana Maynard interview
Video • 24 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/MZyEJ/diana-maynard-interview

This interview provides a comprehensive, reflective overview of the current state, challenges, and future trajectory of Natural Language Processing (NLP). Diana Maynard discusses the maturation of the field, moving past early hype cycles toward more practical, nuanced applications.

Here is a detailed summary of the key themes and insights:

---

## 📚 Summary of the Interview

### 1. The Current State: Maturation and Challenges
The discussion immediately addresses the growing complexity and accountability required in modern NLP:

*   **The "Black Box" Problem:** As NLP models become more powerful (especially deep learning models), they enter a "dangerous area of black box NLP." This lack of transparency raises serious concerns.
*   **The Rise of Explainability (XAI):** Consequently, the research focus has shifted toward **explainability**. Developing tools that not only *work* but can also *explain how they work* is now a critical area of study.
*   **High-Impact Domains:** NLP is making massive inroads into specialized fields:
    *   **Biomedical Fields:** This area has immense potential to revolutionize modern medicine and accelerate scientific discovery.
    *   **Conversational Agents:** Chatbots and conversational AI are rapidly evolving beyond simple, scripted tools, becoming more complex and essential to modern life.

### 2. The Future: Navigating the Hype Cycle
When discussing predictions 5 to 10 years out, Maynard adopts a cautious, realistic tone, referencing the Gartner Hype Cycle:

*   **Past the Peak:** She notes that NLP has already passed the "peak of inflated expectations" (around 2020) and is entering the "trough of disillusionment."
*   **The Shift in Perception:** The industry has changed dramatically:
    *   **Past (15 years ago):** Researchers had to spend a year convincing skeptics *that* NLP was necessary.
    *   **Present:** Everyone *demands* NLP tools, but often without a deep understanding of the field's inherent **limitations**.
*   **The Plateau of Productivity:** She predicts that the field will eventually exit the trough and move into a state of "plateau productivity." In this phase:
    *   NLP will become a **natural, underlying part of everyday life**, often working "under the surface" that most people won't notice.
    *   Conversational agents and speech technologies will be "massively advanced."

### 3. The Core Bugbear: Communication and Understanding
In a personal reflection, Maynard identifies the single biggest obstacle facing the field: the disconnect between researchers and the wider world.

*   **Lack of Conceptual Understanding:** Many people outside of the NLP field have only superficial knowledge (e.g., having heard of GPT-3). This leads to two dangerous extremes:
    1.  Believing the technology can "magically do everything."
    2.  Dismissing it as a niche field of limited utility.
*   **The Communication Barrier:** She stresses that the complexity of NLP is incredibly difficult to explain without providing very concrete, practical examples.

---

## 💡 Key Takeaways for Learning NLP

For students and researchers, this interview highlights several critical professional and academic shifts:

| Concept | Traditional View (Past) | Modern Reality (Present/Future) |
| :--- | :--- | :--- |
| **Focus** | Pure capability (Can the model perform the task?) | **Explainability (XAI)** (Why and how did the model perform the task?) |
| **Hype Cycle** | Constant, rapid, exponential growth. | **Maturation** (Moving toward stability and realistic application). |
| **Application Scope** | General, experimental demonstrations. | **Specialization** (Biomedical sciences, complex dialogue systems). |
| **Industry Challenge** | Lack of investment/skepticism. | **Misunderstanding Limitations** (Over-promising and under-delivering expectations). |
| **Core Skill** | Coding/Model building. | **Communication** (Bridging the gap between complex ML and real-world stakeholder needs). |

---

### 05_Sequence_labelling_for_parts_of_speech_and_named_entities_Reading_1h

# Sequence labelling for parts of speech and named entities
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/zk2On/sequence-labelling-for-parts-of-speech-and-named-entities

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 17. If this link is broken, please let us know via the Student Portal . Sequence labelling for parts of speech and named entities Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 17. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 06_David_Elworthy_interview_Video_22_min

# David Elworthy interview
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/4l1lE/david-elworthy-interview

This curriculum outlines a comprehensive 22-week study of Natural Language Processing (NLP), beginning with foundational concepts in Weeks 1 and 2. The course progresses into basic text processing during Weeks 3 and 4, followed by an intensive two-part exploration of Language Modelling in Weeks 5 and 6. Subsequently, the focus shifts to deeper linguistic analysis, covering Lexical Semantics (Weeks 7 and 8), and then moving into Text Categorisation and Sentiment Analysis (Weeks 9 and 10). Weeks 11 and 12 delve into Syntax and Parsing, while Weeks 13 and 14 are dedicated to the techniques of Information Extraction. The latter half of the course covers Information Retrieval (Weeks 15 and 16) and Chatbots and Dialogue Systems (Weeks 17 and 18). Weeks 19 through 20 introduce advanced methodologies, including Neural Networks and Deep Learning Architectures for sequence processing, supplemented by various interviews and readings. The schedule concludes with a Revision Week and the final Examination Week.

---

### 07_Deep_learning_architectures_for_sequence_processing_Reading_1h

# Deep learning architectures for sequence processing
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/9ntJa/deep-learning-architectures-for-sequence-processing

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 13. If this link is broken, please let us know via the Student Portal . Deep learning architectures for sequence processing Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 13. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 08_Richard_Jackson_interview_Video_18_min

# Richard Jackson interview
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ZENPm/richard-jackson-interview

Based on the interview transcript, here is a comprehensive summary covering the current trends, future predictions, and critical observations within the field of Natural Language Processing (NLP).

***

## 🎙️ Interview Summary: The State and Future of NLP

The interview provided a detailed look at the current challenges in NLP, emphasizing that the field is rapidly moving toward understanding data and ensuring system transparency, while also pointing to a massive shift in how humans interact with technology.

### 🟢 Current Hot Topics in NLP

The current focus in NLP is shifting heavily toward **data understanding** and improving the robustness of large language models (LLMs).

*   **Data-Centric Approach:** There is a major trend toward understanding the underlying data aspects of NLP. While powerful foundation models (like BERT and its variants) are still heavily used as base models for research, the difficulty lies in properly tuning them for specific, real-world tasks.
*   **The Generalization Gap:** A significant problem is observed when researchers rely solely on **fitting models to specific datasets.** This leads to poor generalization performance and suboptimal performance in real-world environments.
*   **The Rise of Interpretability:** A critical new area of focus is the development of **interpretability tools** (such as Google's LIT). This is particularly crucial in highly regulated industries where it is mandatory to explain *why* an AI system made a certain classification.
*   **Engineering Hurdles:** The initial discussion highlighted that despite impressive modeling achievements, the technical challenge often reverts to "good old classic engineering skills"—making complex systems talk to each other correctly and achieving true scalability.

### 🚀 Predictions for the Future (5–10 Years)

When asked what will be "hot" in the near future, the interviewee offered a bold prediction centered on interaction and automation:

*   **Speech-to-Code Translation:** The most promising area is NLP systems that can **translate natural human speech directly into functional code.**
*   **Impact:** This would be a revolutionary change, allowing people to speak about what they want a machine to do, and having that intent automatically translated into a process that automates complex tasks. This would democratize programming and open up automation capabilities to a much wider range of people.
*   **A Note of Caution:** Despite the excitement, the interviewee was less optimistic about a complete "AI revolution" in the immediate term, noting that even defining the *right question* remains a major challenge.

### 📉 Critical Observations and Systemic Challenges

Beyond technical advancements, the interviewee raised two important critiques regarding the ecosystem of research and industry:

1.  **The Commercialization Gap (The "Bugbear"):**
    *   The speaker expressed a personal frustration with the poor transition of academic research into commercial products.
    *   Researchers often publish interesting papers, placing restrictive licenses on the code (e.g., on GitHub).
    *   However, the commercial wing of organizations frequently lacks the internal interface or knowledge needed to engage with early-stage research. As a result, promising work stalls because the procurement process is too burdensome for something that isn't yet a polished product.
2.  **Complexity and Data Limits:**
    *   The interviewee acknowledged that the biggest challenge in certain domains (like biology) is inherent complexity. Since language is a portal to express biology, the difficulty in the underlying subject means that even with advanced NLP, the data itself is fundamentally difficult to manage.

---

### 09_Udo_Kruschwitz_interview_Video_22_min

# Udo Kruschwitz interview
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/APWGG/udo-kruschwitz-interview

This comprehensive course covers the breadth of Natural Language Processing (NLP), beginning with introductory concepts in Weeks 1 and 2. Foundational knowledge progresses through Basic Text Processing (Weeks 3-4), Language Modelling (Weeks 5-6), and detailed Lexical Semantics (Weeks 7-8). Intermediate topics include Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by the critical linguistic skills of Syntax and Parsing (Weeks 11-12). The curriculum then shifts to information handling, covering Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). Advanced applications focus on Chatbots and Dialogue Systems (Weeks 17-18), culminating in a practical deep dive in Week 19. This final week introduces modern NLP, specifically detailing Neural Networks and Neural Language Models. Technical elements reviewed include sequence labelling for Parts of Speech and Named Entities, and Deep Learning architectures for sequence processing. The course concludes with a Course Summary (Week 20), a Revision Week (Week 21), and the final Exam Week (Week 22).

---

## Week 2

### 01_Introduction_to_the_development_environment_Video_4_min

# Introduction to the development environment
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8Z5Xr/introduction-to-the-development-environment

This curriculum spans 22 weeks, providing a comprehensive introduction to Natural Language Processing (NLP), starting with fundamental technical setup. The initial phase (Weeks 1-2) focuses on establishing the development environment using Python and Jupyter, coupled with a critical introduction to evaluation metrics, such as precision and recall. Basic text processing techniques are covered in Weeks 3 and 4, transitioning into advanced linguistic analysis through Language Modelling (Weeks 5-6). Lexical semantics, which deals with the meaning of words, forms the core of Weeks 7 and 8.

The course then delves into practical applications, including Text Categorisation and Sentiment Analysis in Weeks 9 and 10. Students explore the structural components of language by studying Syntax and Parsing over Weeks 11 and 12. The focus shifts to Knowledge Discovery with Information Extraction (Weeks 13-14), teaching methods for pulling specific data from unstructured text.

Subsequently, the curriculum addresses how information is accessed through Information Retrieval (Weeks 15-16). The study culminates in advanced interaction systems, specifically Chatbots and Dialogue Systems, detailed across Weeks 17 and 18. Weeks 19 and 20 transition the theory into practical application and a comprehensive course summary. The final phase includes a Revision week and Exam week (Weeks 21-22), solidifying the learning objectives across all ten topics.

---

### 02_Python_tutorial_Reading_1h

# Python tutorial
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Gtk3G/python-tutorial

Please read the following Python tutorial: Python ' The Python Tutorial ' (2021). If this link is broken, please let us know via the Student Portal . Python tutorial Please read the following Python tutorial: Python ' The Python Tutorial ' (2021). If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 03_JupyterLab_user_guide_Reading_1h

# JupyterLab user guide
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/aE6TH/jupyterlab-user-guide

The provided text directs users to several essential Jupyter guides, including the JupyterLab user guide, and specific instructions for different components. These guides cover key technical areas: the JupyterLab interface, the text editor, Notebooks, and Code consoles. Should any of the listed links be broken, users are instructed to report the issue via the Student Portal. Finally, administrative actions such as "Mark as completed," "Dislike," or "Report an issue" are available for the user to take.

---

### 04_NLP_platforms_and_toolkits_Video_8_min

# NLP platforms and toolkits
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/YaDZj/nlp-platforms-and-toolkits

The foundation of this course utilizes Python as the programming language and Jupyterlab as the development environment. This combination is advantageous because Python provides robust support for manipulating unstructured data and general language data. The current discussion focuses on analyzing various Natural Language Processing (NLP) platforms and toolkits.

One of the most prominent and established NLP toolkits is NLTK, or the Natural Language Toolkit. NLTK boasts a long history, dating back to its creation at the University of Pennsylvania in 2001. Crucially, its origins lie in symbolic or formal linguistics, rather than solely in a machine learning or statistical background. This formal linguistic root gives NLTK a unique angle.

NLTK is highly valuable for teaching and learning due to its design principles of simplicity, consistency, modularity, and extensibility. It provides a simple framework and clear building blocks that are easy to learn and apply. Furthermore, NLTK is tightly integrated with data, including many built-in text corpora, allowing for rapid analysis.

The toolkit facilitates numerous language processing tasks, including string processing, identifying collocations, machine learning operations, parsing, semantic interpretation, and utilizes built-in evaluation metrics. However, a key technical limitation is that NLTK is not always considered "state of the art," nor is it optimized for high runtime performance necessary for live production systems.

While NLTK is powerful, it is not the only option available for NLP tasks. Scikit-learn is introduced as a primary machine learning library, capable of handling many NLP problems by recasting them as machine learning tasks. Gensim is another vital toolkit, specializing in word embedding, lexical semantics, and topic modeling for structured extraction from unstructured data.

For applications requiring industrial-strength performance in production systems, spaCy is recommended as a strong alternative to NLTK. Textacy is a specialized niche tool built upon spaCy and TextBlob, dedicated to Simplified Text Processing. Deep learning frameworks like TensorFlow and PyTorch are also mentioned, though they require more complex setup and often specialized hardware.

Finally, the scope includes examining chatbot development libraries and systems, which represent a high-level, scripting approach to building dialogue systems. The course structure systematically covers these topics, starting with basic text processing, language modeling, and lexical semantics. Later modules focus on text categorization, syntax/parsing, information extraction, and information retrieval. The final sections dedicate attention to advanced chatbot development and overall course summary.

---

### 05_Language_processing_and_Python_Reading_1h

# Language processing and Python
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/km0xu/language-processing-and-python

Please read the following extracts from the Language Processing and Python chapter: Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Sections 1, 5 and 6. If this link is broken, please let us know via the Student Portal ....

---

### 06_Introduction_to_evaluation_Video_4_min

# Introduction to evaluation
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/7rDiB/introduction-to-evaluation

This curriculum provides a comprehensive 20-week journey through Natural Language Processing (NLP), structured into distinct conceptual modules. The foundational weeks (Weeks 1-2) focus on setting up the development environment using Python and Jupyter, alongside rigorous training in evaluation metrics, specifically measuring precision and recall. The core mechanics begin with Week 3 and 4, dedicated to basic text processing, before progressing into language modelling in Weeks 5 and 6. The understanding of meaning is deepened during Weeks 7 and 8, which cover Lexical Semantics.

Subsequent topics build upon these foundations, commencing with Text Categorization and Sentiment Analysis in Weeks 9 and 10. Structural understanding is addressed via Syntax and Parsing in Weeks 11 and 12, followed by Information Extraction (IE) in Weeks 13 and 14. The focus then shifts to practical data retrieval with Information Retrieval (IR) in Weeks 15 and 16.

Interaction and dialogue are introduced in Weeks 17 and 18, covering Chatbots and Dialogue Systems. The latter half of the course culminates in a practical application phase, featuring NLP in Practice (Week 19). The curriculum concludes with a final course summary (Week 20), followed by a revision week (Week 21) leading into the final exam week (Week 22). The program emphasizes both theoretical knowledge and practical application through numerous practice assignments throughout the entire duration.

---

### 07_Evaluation_metrics_Video_5_min

# Evaluation metrics
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ORIoC/evaluation-metrics

The provided material details the critical concepts of evaluation metrics within Natural Language Processing (NLP), arguing against the sole reliance on accuracy for performance measurement. The transcript introduces the limitations of accuracy, exemplified by a fictitious spam classifier operating on an unbalanced dataset. In such scenarios, high accuracy can be misleadingly achieved simply by predicting the majority class every time. A more compelling example involves a hospital system designed to predict cancerous tumors from medical scans. In this critical context, the classes—tumor and not tumor—are also unbalanced. The major issue is the differential cost of errors, where a False Negative (missing an actual tumor) is life-threatening. This serious disparity in error costs indicates that accuracy is an unsuitable primary metric.

To address this inadequacy, the concept of the Confusion Matrix is introduced as the foundational tool for comparison. This matrix compares the actual values, referred to as the ground truth, against the system's predicted values. The key components derived from this matrix are defined as True Positives (TP), False Positives (FP), False Negatives (FN), and True Negatives (TN).

The accuracy metric is initially defined as the proportion of correct predictions over all predictions, corresponding to the diagonal elements of the matrix divided by the total dataset size. However, the discussion pivots to two more robust metrics: Recall and Precision.

Recall, or sensitivity, is mathematically defined as the proportion of true positives over all actual positive cases (TP / (TP + FN)). Essentially, it measures how many of the actual tumors the system successfully detected. Conversely, Precision is calculated as the portion of true positives among all predicted positive cases (TP / (TP + FP)). Precision addresses the rate of correctness for the system’s positive predictions.

Fictitious examples demonstrate how these metrics provide a far more effective illustration of performance on unbalanced datasets than raw accuracy. By calculating Recall and Precision, researchers gain a principled baseline against which subsequent algorithmic iterations can be compared. This methodical approach is vital for improving system performance in fields like NLP.

The supplementary course outline contextualizes these concepts within a larger curriculum. The studies progress through various topics, starting with the Introduction to NLP and foundational Python/Jupyter environment skills. Subsequent modules cover Basic text processing, Language modelling, Lexical semantics, and Text categorisation and sentiment analysis. Core areas like Syntax and parsing, Information extraction, and Information retrieval are also covered over subsequent weeks. The dedicated evaluation section (Week 2, Topic 1.4) reinforces the importance of these specialized metrics. The overall structure provides a comprehensive framework for mastering advanced NLP methodologies.

---

### 08_Measuring_precision_and_recall_Reading_1h

# Measuring precision and recall
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/0d520/measuring-precision-and-recall

Perkins, J. Python 3 text processing with NLTK 3 cookbook . (Birmingham: Packt Publishing Ltd, 2014). Chapter 7, pp.201-213. Measuring precision and recall Perkins, J. Python 3 text processing with NLTK 3 cookbook . (Birmingham: Packt Publishing Ltd, 2014). Chapter 7, pp.201-213. Mark as completed Dislike Report an issue

---

### 09_Topic_1_summary_Video_4_min

# Topic 1 summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/BMl15/topic-1-summary

This curriculum provides a comprehensive, 22-week introduction to Natural Language Processing (NLP), progressing from foundational concepts to advanced applications.

The initial weeks establish the necessary technical foundation, covering development environments like Python and JupyterLab, alongside essential principles of NLP platforms. A critical early focus is placed on evaluation, where students learn to measure performance using metrics such as precision and recall.

The middle segment delves into core text mechanics, beginning with basic text processing (Week 3/4) and advancing to the principles of Language Modelling (Week 5/6). This study then moves into understanding the deeper meaning of text through Lexical Semantics (Week 7/8).

Following semantic analysis, the curriculum tackles classification problems, dedicating time to Text Categorisation and Sentiment Analysis (Week 9/10). The focus then shifts to the structural organization of language, exploring Syntax and Parsing techniques in depth (Week 11/12).

Students further learn how to extract specific data points from unstructured text via Information Extraction (Week 13/14) and master the retrieval of relevant documents using Information Retrieval (Week 15/16). These concepts pave the way for practical application in conversational AI, specifically Chatbots and Dialogue Systems (Week 17/18).

The coursework culminates in a review of NLP in practice (Week 19), followed by a course summary and final revision period (Weeks 20/21). The program concludes with an exam week (Week 22), ensuring a full mastery of the ten core NLP topics.

---

## Week 20

### 01_Course_summary_Video_4_min

# Course summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Wgri5/course-summary

This course provided a comprehensive journey through the field of Natural Language Processing (NLP), integrating both deep theoretical background and practical industry applications. The program aimed to illustrate how NLP connects not only with data science and machine learning but also critically with linguistics and psychology. Throughout the modules, the focus was on applying NLP techniques to solve various real-world problems. Technically, the instruction heavily utilized the Python programming language and the Jupyter environment to demonstrate complex concepts.

The curriculum systematically covered ten major topics, starting with the fundamental introduction to NLP paradigms and the crucial foundations of evaluation. Topic 2 covered essential text processing, teaching techniques for manipulating and learning from unstructured data. Building upon this, Topic 3 introduced sophisticated ways to model language, focusing on statistical approaches and topic modeling. In Topic 4, the course addressed word meaning representation, contrasting symbolic/curated approaches with modern distributional approaches, and applying basic semantic similarity techniques.

Topic 5 specialized in text categorization, demonstrating its practical use specifically in sentiment analysis. The curriculum then moved into linguistic principles in Topic 6, introducing syntax, grammars, and the integration of probabilistic concepts into the parsing process. Topic 7 focused on Information Extraction, teaching methods for recognizing and extracting critical entities within text. Following this, Topic 8 covered Information Retrieval and search, detailing the relevant data structures and principles applicable to NLP.

Topic 9 addressed the interactive nature of NLP by guiding students through designing and building dialogue systems and simple chatbots. This topic reflected how human conversation functions to build functional architectures. Finally, Topic 10 transitioned to NLP in practice, featuring industry guest speakers. These experts conveyed how NLP is applied in industry, the challenges faced, and the core competencies sought in specialized NLP roles. The course provided practical experience and emphasized that NLP is a fascinating field requiring diverse skill sets. Participants were encouraged to pursue final projects, offering opportunities to explore their own innovative ideas in the subject. The overall journey successfully bridged academic theory with the high demands of modern technological application.

---

## Week 21

### 01_Exam_preparation_Reading_10_min

# Exam preparation
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/cuiL8/exam-preparation

This comprehensive 22-week course in Natural Language Processing (NLP) begins with fundamentals, covering Introduction to NLP, Basic text processing, Language modelling, and Lexical semantics. The curriculum progresses to advanced analytical topics, including Text categorisation/Sentiment analysis, Syntax and parsing, Information extraction, Information retrieval, and Chatbots and dialogue systems, concluding with NLP in practice, course summary, and dedicated revision and exam preparation.

---

## Week 3

### 01_Introduction_and_learning_objectives_Video_11_min

# Introduction and learning objectives
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ZjNpC/introduction-and-learning-objectives

This text provides a foundational introduction to basic text processing and Natural Language Processing (NLP). The course objectives include differentiating between rule-based and statistical approaches to NLP, exploring appropriate statistical language analysis techniques, and utilizing software tools like corpus readers and stemmers. Furthermore, the curriculum involves studying text corpora and introducing various NLP software libraries. The specific learning goals for this topic center on text processing fundamentals, applying these techniques, and manipulating unstructured data.

Unstructured data is globally pervasive and constitutes a significant volume in enterprise studies. This data exists in many forms, including printed paper documents, emails, social media posts, and customer feedback. Critical textual information is often found in open-ended survey responses, web pages, and transcripts of

---

### 02_Text_processing_fundamentals_(part_1)_Video_10_min

# Text processing fundamentals (part 1)
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/khiZb/text-processing-fundamentals-part-1

This course provides a comprehensive, modular introduction to Natural Language Processing (NLP) over a 22-week period, beginning with foundational concepts in Week 1 and 2. The learning immediately transitions into Basic Text Processing in Weeks 3 and 4, focusing on fundamentals like sentence segmentation, word tokenization, and text normalization, which are crucial for handling unstructured data. Following preprocessing, Weeks 5 and 6 introduce Language Modelling, exploring how systems predict sequences of words. The curriculum then delves into Lexical Semantics in Weeks 7 and 8, examining the meaning and relationships between individual words.

A major application focus begins in Weeks 9 and 10 with Text Categorization and Sentiment Analysis, techniques used to classify text and determine emotional tone. The focus shifts structurally in Weeks 11 and 12 to Syntax and Parsing, detailing the grammatical structure of sentences. Subsequently, Weeks 13 and 14 cover Information Extraction, the process of pulling specific, meaningful data points from text.

The advanced topics continue with Information Retrieval in Weeks 15 and 16, a key mechanism for searching and retrieving relevant documents. Weeks 17 and 18 introduce Chatbots and Dialogue Systems, demonstrating how NLP enables conversational interaction. The practical culmination of the course occurs in Weeks 19 and 20, where NLP is explored in real-world applications and the course is summarized. The final weeks, 21 and 22, are dedicated to revision and examination.

---

### 03_Text_processing_fundamentals_(part_2)_Video_7_min

# Text processing fundamentals (part 2)
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/OL4vH/text-processing-fundamentals-part-2

This text provides a detailed look into the fundamentals of text processing, specifically focusing on the higher-level challenges of linguistic ambiguity. Building upon the discussion of lexical ambiguity from previous materials, this segment focuses on ambiguities encountered at the sentence and discourse levels. At an elementary level of analysis, words within a sentence are classified by different syntactic categories, such as nouns, verbs, adjectives, pronouns, determiners, prepositions, and conjunctions. For instance, the word "book" demonstrates ambiguity because it can function as a noun ("I read the book") or as a verb ("I booked a flight").

Syntactic analysis attempts to determine the correct sequence of these categories for a string of words, often resolving ambiguities, such as tagging the string "book that flight" as verb, determiner, noun. However, determining the correct sequence is often impossible, leading to various forms of ambiguity. Structural ambiguities arise when syntactically similar sentences have distinct meanings, such as comparing "time flies like an arrow" to "fruit flies like a banana."

Moving beyond elementary syntactic thinking, a more structured approach analyzes the grammar of sentences using formal methods. A major challenge is resolving Prepositional Phrase Attachment, where it is unclear which preceding element modifies the attached phrase. For example, in the phrase "the man on the hill with a telescope," it is uncertain whether the man or the observer is holding the telescope. Parsing aims to construct a tree structure that indicates how various elements combine to form the composite meaning of the utterance.

Furthermore, a significant technical hurdle in text processing is sentence segmentation: accurately determining where a sentence begins and where it ends. While punctuation marks like periods or exclamation marks might indicate boundaries, language data presents numerous exceptions to simple rule-based separation. This lack of consistent rules is a core reason why statistical techniques are often considered more robust in Natural Language Processing (NLP) than purely rule-based methods.

The broader course content outlines a comprehensive curriculum covering foundational NLP skills and advanced concepts. The curriculum begins with fundamental text processing topics, including sentence segmentation, word tokenization, and text normalization. Following these fundamentals, the course progresses to Language Modelling and Lexical Semantics. Specialized topics include Text Categorisation and Sentiment Analysis, alongside detailed studies of Syntax and Parsing. The later stages cover practical NLP applications such as Information Extraction, Information Retrieval, and Chatbots and Dialogue Systems. The entire curriculum spans various weeks, leading to a course summary and final examinations, ensuring a deep dive into the technical aspects of processing natural language data.

---

### 04_Reading_Representing_text_Reading_1h

# Reading: Representing text
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/tlGXH/reading-representing-text

Provost, F. and T. Fawcett Data science for business: what you need to know about data mining and data-analytic thinking . (California: O'Reilly Media, Inc., 2013). Pages 251-277. Reading: Representing text Provost, F. and T. Fawcett Data science for business: what you need to know about data mining and data-analytic thinking . (California: O'Reilly Media, Inc., 2013). Pages 251-277. Mark as completed Dislike Report an issue

---

### 05_Sentence_segmentation_Video_5_min

# Sentence segmentation
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/DkElp/sentence-segmentation

This course structure spans 22 weeks, systematically progressing through the fundamental concepts of Natural Language Processing (NLP). The initial phase, Weeks 1 and 2, provides the foundational Introduction to NLP (part 1 and part 2). Basic text processing is covered intensively in Week 3, focusing on essential techniques like Sentence Segmentation, Word Tokenization, and Text Normalisation. Week 4 deepens the understanding of basic text processing fundamentals before the course transitions into language modelling in Weeks 5 and 6.

The focus then shifts to meaning and structure, starting with Lexical Semantics in Weeks 7 and 8. These topics prepare students for Text Categorisation and Sentiment Analysis, which are covered comprehensively in Weeks 9 and 10. The study moves into grammatical structure with Syntax and Parsing in Weeks 11 and 12. Subsequent major modules address complex data extraction and management.

Information Extraction is introduced in Weeks 13 and 14, followed by Information Retrieval in Weeks 15 and 16. The course then explores interactive AI with Chatbots and Dialogue Systems across Weeks 17 and 18. The curriculum culminates in practical application, dedicated to NLP in Practice in Week 19 and a course summary in Week 20. The final weeks allocate time for revision and examination.

---

### 06_Word_tokenization_Video_4_min

# Word tokenization
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/pBuFT/word-tokenization

The provided material details the process and application of word tokenization within the field of Natural Language Processing (NLP). Tokenization is a critical step in basic text processing, serving to segment a character string into its constituent words or tokens. While English generally relies heavily on whitespace as a reliable delimiter between words, this simplicity often masks numerous linguistic exceptions.

To investigate these complexities, the demonstration utilizes the `nltk` (Natural Language Toolkit) library within a Jupyter Notebook environment. The video first discusses the necessity of robust tokenizers because simple whitespace splitting fails in specific cases. The initial setup involves importing `nltk` and preparing sample text designed to showcase various challenging structures.

Initially, the text is subjected to sentence tokenization to correctly segment the input into distinct sentences. This preparatory step confirms that standard methods can reasonably divide sentences using appropriate delimiters. Subsequently, the word tokenizer is applied, executing a list comprehension across each segmented sentence.

The analysis of the first sentence, which is the simplest, reveals that only the punctuation, such as the full stop, is tokenized as a separate unit. The second sentence is used to examine special characters, notably an email address. `nltk` correctly splits the email address based on the `@` character, which is considered a reasonable tokenization approach. Furthermore, the tokenizer successfully keeps complex date formats intact as a single cohesive token, which is the desired outcome.

The third sentence highlights the handling of possessive and contracted forms. The possessive `'s` is treated distinctly; for example, in a possessive form, the word segment is kept, but the possessive apostrophe and letter are separated into individual tokens. Similarly, contractions like "aren't" are split into two separate tokens: "are" and the possessive marker "n't."

The fourth sentence demonstrates the handling of contractions like "it's," which are also split into multiple tokens (e.g., "it" and "'s"). Conversely, the tokenizer successfully keeps hyphenated words together, treating them as a single, meaningful unit.

A second, more complex test case involving specialized text elements is then introduced. This text includes a URL, various company names, and proper names for further evaluation. The tokenizer splits the URL at the colon, showing its ability to handle technical separators. Importantly, both company names are retained as single tokens, preserving their integrity. Proper names are also tokenized accurately, consistent with the findings from the simpler test.

In conclusion, the out-of-the-box `nltk` word tokenize function demonstrates high accuracy for English text across diverse challenging scenarios. However, the presentation strongly cautions that the choice of a "correct" tokenization method is not absolute. The ultimate definition of a valid tokenization strategy must be derived from a heuristic approach dictated by the researcher's specific primary goal. This goal determines whether a contraction must be treated as one token or multiple tokens.

---

### 07_Text_normalisation_Video_6_min

# Text normalisation
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/VyAuw/text-normalisation

This extensive course systematically introduces Natural Language Processing (NLP), beginning with foundational concepts in Week 1 and 2. Week 3 focuses on basic text processing, detailing crucial techniques such as sentence segmentation (5 min video), word tokenization (4 min video), and text normalization (6 min video), with corresponding practice assignments. These fundamentals address representing unstructured data, moving the learner from initial concepts to practical processing techniques.

The curriculum then advances into Language Modelling (Weeks 5 and 6), establishing how linguistic structure predicts and understands language patterns. Following this, Lexical Semantics is introduced in Weeks 7 and 8, focusing on the meaning and relationships of words within text.

Weeks 9 and 10 cover Text Categorization and Sentiment Analysis, teaching how to classify texts and determine emotional tone. The discussion then shifts to deep linguistic analysis, dedicating Weeks 11 and 12 to Syntax and Parsing. This phase emphasizes understanding the grammatical structure of sentences.

Subsequently, the course explores applied knowledge through Information Extraction (Weeks 13 and 14), extracting specific data points from documents. This is followed by Information Retrieval (Weeks 15 and 16), focusing on finding relevant information from large datasets.

Weeks 17 and 18 focus on the specialized area of Chatbots and Dialogue Systems, covering the complex interaction mechanisms of conversational AI. The learning culminates in Weeks 19 and 20, which address NLP in practice and provide a comprehensive course summary. Finally, Weeks 21 and 22 are designated for revision and exam preparation, reinforcing all technical concepts learned.

---

### 08_Tokenization_and_more_Reading_1h

# Tokenization and more
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Cr4lD/tokenization-and-more

Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval . (Cambridge: Cambridge University Press, 2008). Chapter 2, pp.21-22. If this link is broken, please let us know via the Student Portal . Tokenization and more Schütze, H., C.D. Manning and P. Raghavan Introduction to information retrieval . (Cambridge: Cambridge University Press, 2008). Chapter 2, pp.21-22. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## Week 4

### 01_Regular_expressions_part_1_Video_8_min

# Regular expressions part 1
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/SMZsu/regular-expressions-part-1

Regular expressions (regex) are a fundamental tool for processing text, providing a formal language to define text strings and character sequences. In practice, regex allows users to express patterns for advanced operations such as matching, replacing, or substitution within textual data. As data scientists frequently handle noisy or unstructured textual data, regex offers a flexible and efficient mechanism for necessary transformations and data cleaning. The transcript focuses on five specific sub-topics within regular expressions: disjunction, negation, optionality, aliases, and anchors, with a deep dive into the former two.

To begin, the Python standard library `re` is imported, allowing manipulation of a variable defined as `text`. The `re.sub()` method is highlighted as the core function, which substitutes a defined `pattern` with a specified replacement string across the `text` variable. An initial example demonstrates finding and replacing all instances of the word "the" with the character 'x'. However, the initial pattern fails to capture all instances because it was case-sensitive, missing the uppercase 'T'.

This leads to the concept of disjunction, which is implemented using square brackets `[]`. Disjunction allows the pattern to match characters preceded by either an uppercase 'T' or a lowercase 't', thereby correcting the initial case-sensitivity error. Other practical applications of disjunction include using character ranges (e.g., `0-9` to match digits or `A-Z` to match all uppercase letters). Disjunction can also be extended to match specific words using the vertical pipe symbol (`|`), allowing a pattern to match "or" or "the" simultaneously.

The next major concept introduced is negation, which enables the inverse operation—matching anything that is *not* a certain type of character. Negation is achieved by placing a caret operator (`^`) immediately before a range definition. For instance, if `[0-9]` matches digits, then `[^0-9]` matches any character that is not a digit. By substituting these non-digit characters with an empty string, the text is effectively reduced to only its digits.

This negation technique is highly adaptable and can be applied to any character range. An example shows using `[^a-z]` to match and eliminate any character that is not a lowercase letter. The combined use of disjunctions and negations provides flexible, low-level tools for powerful textual transformations. Mastery of these simple yet flexible regex tools allows for complex data cleansing and pattern recognition in various NLP applications.

---

### 02_Regular_expressions_part_2_Video_11_min

# Regular expressions part 2
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/AVgt0/regular-expressions-part-2

This curriculum provides a structured progression through various domains of Natural Language Processing (NLP), commencing with foundational concepts in Weeks 1 and 2. The core module on basic text processing (Weeks 3-4) heavily emphasizes practical technical skills, including extensive use of Regular Expressions (Parts 1 & 2) and the application of Stop Words for data cleanup. Subsequent learning focuses on Text Corpora (Week 4), introducing the necessary resources for linguistic analysis and experimentation. The program then delves into advanced linguistic concepts, covering Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8). Further technical development is achieved through Text Categorization and Sentiment Analysis (Weeks 9-10), bridging basic processing with applied classification. The modules transition into deeper structural analysis, covering Syntax and Parsing (Weeks 11-12) and subsequently focusing on complex Information Extraction (Weeks 13-14). Practical applications are explored via Information Retrieval (Weeks 15-16), followed by specialized systems such as Chatbots and Dialogue Systems (Weeks 17-18). The course culminates by integrating these diverse techniques within broader contexts, addressing NLP in Practice (Week 19) and concluding with a comprehensive course summary and revision week.

---

### 03_Stop_words_Video_4_min

# Stop words
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zJwBM/stop-words

Stop words are defined as high-frequency words common across different document types and genres. These words offer little lexical content and tend not to contribute significantly to differentiation between texts. For example, common English stop words include "and," "or," "the," and "of." In machine learning tasks, such as document classification, these common words often introduce noise rather than providing meaningful signal. Consequently, they are typically filtered out during the preprocessing phase of text analysis.

However, it is crucial to recognize that stop words are highly language-specific, meaning the English list differs fundamentally from those in French or German. Furthermore, there is no universal list of stop words; the selection must depend entirely on the specific goal of the application. To begin processing, the Natural Language Toolkit (NLTK) is imported to access built-in stop word lists.

The procedure involves importing the NLTK stop word list and printing the extensive list available. To practically use these words, the English stop word list is first stored in a variable named `stopwords`. This list is then cast to a set type to ensure subsequent computational operations execute faster.

Text tokens are extracted from the document using NLTK’s tokenization function. Subsequently, a simple list comprehension is utilized to iterate through the tokenized words. This comprehension filters out any word that exists within the defined `stopwords` set. This process effectively transforms the text by removing high-frequency common phrases, for example, changing "most of the time" to "most time use white space."

A critical caution must be applied when implementing stop word removal. Over-applying the filter can be detrimental to specialized texts. For instance, if filtering Shakespeare's plays, the removal of words like "to" and "be" could result in an empty list, which is clearly inappropriate for that literary corpus.

Beyond English, NLTK provides available lists for other languages. The transcript demonstrated accessing and reviewing the stop words provided for German and also noted the availability of French stop word lists. This basic technique is fundamental to text processing applications, but it must be used with extreme caution. Users must carefully consider which words should definitively be included in their specific stop word list.

---

### 04_Regular_expressions_Reading_1h

# Regular expressions
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/SP5HV/regular-expressions

Please read the following extract on regular expressions: Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 2, Section 2.6 In the event that the draft of the 3rd edition does not contain the chapter reference you require, please refer to the second edition, Chapter 2, pp.17-26. If this link is broken, please let us know via the Student Portal . Regular expressions Please read the following extract on regular expressions: Jurafsky, D. and J.H....

---

### 05_Text_corpora_Video_10_min

# Text corpora
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ldPwQ/text-corpora

This comprehensive course provides a structured exploration of Natural Language Processing (NLP), starting with introductory concepts in Week 1 and Week 2. The foundational stage then transitions into Basic Text Processing (Weeks 3 and 4), covering critical technical details like Regular expressions, the handling of Stop words, and the utilization of Text corpora. Subsequent modules deepen linguistic understanding through Language Modelling (Weeks 5 and 6) and the principles of Lexical Semantics (Weeks 7 and 8).

The course progresses to analyzing the structure of language by covering Syntax and Parsing in Weeks 11 and 12. Key applications begin with Text Categorisation and Sentiment Analysis (Weeks 9 and 10), followed by modules focused on Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16).

The final thematic blocks address interactive and practical NLP systems. Weeks 17 and 18 are dedicated to Chatbots and Dialogue Systems, while Week 19 focuses on applying NLP in real-world practice. The curriculum concludes with a comprehensive Course Summary in Week 20, followed by a Revision Week (Week 21) and Exam Week (Week 22).

---

### 06_Accessing_text_corpora_Reading_1h

# Accessing text corpora
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/tf9TE/accessing-text-corpora

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2009). Section 2.1, pp.39-51. If this link is broken, please let us know via the Student Portal . Accessing text corpora Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2009). Section 2.1, pp.39-51. If this link is broken, please let us know via the Student Portal ....

---

### 07_Text_processing_summary_Video_4_min

# Text processing summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/zP0Nf/text-processing-summary

This summary focuses on Topic 2: Basic Text Processing, covering the fundamentals of manipulating unstructured data in NLP.

The course objectives for text processing were defined as understanding fundamentals, applying techniques, and manipulating unstructured data. A primary task in processing natural language is resolving the considerable ambiguity present in human language. Before intent or structure can be determined, ambiguity must be addressed at various linguistic levels. The basic level of analysis begins with lexical analysis, essentially known as tokenization. Various approaches to tokenization and whitespace exist, but they require smarter techniques to identify appropriate tokens.

Stemming is a crude process of chopping word endings to reduce them to a common root, though this root may not always be a genuine word. Lemmatization solves this issue by analyzing the process in a more linguistically principled manner. Lemmatization considers the syntactic context to identify the correct lemma or root for each input word. Morphology refers to the shape of words; English is less morphologically complex than languages like German, which exhibits complex compounding behavior.

The next stage involves syntax, which analyzes the syntactic role of each word to interpret the sentence structure. Syntax also presents ambiguity, exemplified by the phrase, "I saw the man on the hill with a telescope." Solving this requires utilizing contextual information rather than syntax alone. Sentence boundary detection is another challenging task; while simple rules based on punctuation help, exceptions are common in linguistic data.

Regular expressions offer a highly flexible tool, enabling diverse text processing tasks. These expressions are used effectively to extract specific data points, such as URLs, email addresses, and dates. Furthermore, stop word removal is a necessary step, but there is no definitive universal list for English or any language. The selection of a stop word list must depend entirely on the specific application or goal being pursued.

Finally, text corpora—large samples of textual data—allow for various linguistic and stylistic analyses. Four types of corpora were briefly examined: isolated, categorized, overlapping, and temporal. The entire process of text data handling moves toward advanced topics like language modeling. The associated coursework includes dedicated modules on Regular Expressions (Parts 1 & 2), Stop Words, and Text Corpora. The curriculum progresses through these stages, leading eventually to advanced treatments of language and NLP in practice.

---

## Week 5

### 01_Introduction_and_Learning_Objectives_Video_2_min

# Introduction and Learning Objectives
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/2RgnI/introduction-and-learning-objectives

This comprehensive course spans 20 weeks, systematically covering the foundational concepts and advanced applications of Natural Language Processing (NLP). The initial phase (Weeks 1-4) establishes core NLP principles and fundamental skills in basic text processing, including accessing and experimenting with large text corpora. The curriculum progresses into Language Modelling (Weeks 5-6), detailing how simple statistics and conditional frequency distributions are used to compute language probabilities and generate realistic text. Lexical semantics and Text Categorization (Weeks 7-10) address the meaning of words, focusing heavily on sentiment analysis and classification techniques.

Further technical depth is achieved through Syntax and Parsing (Weeks 11-12), which provides the framework for analyzing the grammatical structure of text. This is followed by Information Extraction and Information Retrieval (Weeks 13-16), teaching methods for extracting key facts and effectively searching large databases. The study then moves into practical interaction design via Chatbots and Dialogue Systems (Weeks 17-18). The course culminates in Week 19, where NLP is applied to real-world scenarios, followed by a final course summary and subsequent revision and exam periods. These modules ensure a complete understanding of how complex linguistic structures are handled by computational systems.

---

### 02_Computing_simple_statistics_Video_13_min

# Computing simple statistics
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/2US9n/computing-simple-statistics

This practical NLP session shifts focus from academic NLP to applied examples using the NLTK library within a Jupyter Notebook environment. The exercise begins by importing NLTK and accessing several introductory example texts, each serving as a unique corpus. These eight texts provide diverse linguistic data, including novels (Moby Dick by Herman Melville, Sense and Sensibility by Jane Austen), religious works (Bible), political writings, and specialized collections like the Chat Corpus and Wall Street Journal articles. A corpus is defined as a body of text, allowing for comparisons between different linguistic sources.

Initial analysis involves checking the sheer size of the texts using the `len()` method, noting, for instance, that Text 1 (Moby Dick) contains approximately 260,000 words, while Text 6 (Monty Python) is much smaller, at 16,967 words. A critical distinction is then drawn between word tokens and word types. Tokenization is the process of breaking a string into individual components, which are called tokens. In contrast, word types represent unique, non-duplicate words within the text.

To find the number of word types, the set operator is applied to the text, which effectively removes all duplicates. The length of this resulting set represents the total vocabulary or number of word types. Text 1, despite having 260,000 tokens, consists of significantly fewer word types, totaling 19,000.

This comparison leads to the calculation of Lexical Diversity, a measure of text variability. This diversity is mathematically defined as the length of the set of the text (word types) divided by the length of the text (word tokens). The function applied to Text 1 yields a lexical diversity figure of 0.074, while Text 8 shows a higher diversity of 0.22, offering insight into linguistic richness across different genres.

The next analytical stage explores frequency distribution, which counts how many times each word type occurs, utilizing the built-in NLTK method `FreqDist`. Applying `FreqDist` to Text 1 reveals that punctuation marks (like the comma) and common function words (like 'the' and 'of') are the most frequent items. The `FreqDist` object can output the most common terms (e.g., the top 10) or confirm the occurrence of a specific term.

Visualization of frequency distributions often reveals a power law curve, which suggests that in natural languages, a few words appear extremely frequently while many others are used sparingly.

The final core concept introduced is collocations, which are groups of words that stick together more frequently than would occur by chance (e.g., "red wine"). Collocations are analogous to bigrams but exhibit a stronger contextual affinity. Analyzing collocations in Text 1 yields characteristic phrases such as "Sperm Whale" and "Moby Dick

---

### 03_Conditional_frequency_distributions_Video_7_min

# Conditional frequency distributions
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/84iA9/conditional-frequency-distributions

This course is structured across 22 weeks, progressing through fundamental concepts of Natural Language Processing (NLP) and culminating in applied NLP projects. The early weeks establish the foundation with general NLP introductions (Weeks 1-2) and subsequent basic text processing techniques (Weeks 3-4). A major focus is dedicated to Language Modelling (Weeks 5-6), which covers computing simple statistics, conditional frequency distributions, and the generation of fake news. The curriculum then moves into understanding meaning, detailing Lexical Semantics (Weeks 7-8) before advancing to text categorisation and sentiment analysis (Weeks 9-10).

Structural analysis is introduced in Weeks 11-12 through Syntax and Parsing, allowing for the identification of grammatical relationships within text. The field then transitions to advanced information handling, covering Information Extraction (Weeks 13-14) and subsequently Information Retrieval (Weeks 15-16). Further specialization is found in Weeks 17-18, dedicated to developing sophisticated Chatbots and Dialogue Systems.

The final modules wrap up the theoretical knowledge by exploring NLP in Practice (Week 19) and providing a comprehensive course summary (Week 20). The entire progression is supported by theoretical readings, practical assignments, and laboratory exercises, such as those involving Unix for Poets and text generation, leading up to a final revision and examination (Weeks 21-22).

---

### 04_Generating_fake_news_Video_4_min

# Generating fake news
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/MWKD0/generating-fake-news

This series investigates how Natural Language Toolkit (NLTK) can be utilized to generate synthetic, or "fake," news content. The core technique employed involves the generation of bigrams, which are defined as all word pairs within a given sentence. To demonstrate this, the NLTK method `bigrams` is applied to a sentence, such as "the cat sat on the mat," resulting in pairs like "cat sat," "sat on," and "on the."

The generation process begins by acquiring a source of news data, which is sourced from the Brown Corpus. Specifically, the text corpus is filtered using `brown.words`, limiting the data to records where `categories equals news`.

The bigrams extracted from this corpus are then compiled into a Conditional Frequency Distribution (CFD). This CFD holds statistical information about which word is most likely to follow any given word.

A custom algorithm, dubbed `generate text`, is subsequently defined to utilize this CFD for text generation. This method requires three inputs: the CFD, a specified starting word, and the desired number of output words.

The iterative nature of `generate text` is critical to its function. It begins by printing the starting word. It then consults the CFD to identify the most common word that follows the current word. This highly probable word is printed, and the loop repeats, searching for the most common bigram following this newly generated word.

This sequential lookup and printing process allows the system to build a continuous chain of words, effectively generating random, yet statistically probable, text. Testing the CFD trained on the news corpus reveals common patterns, such as the prevalence of "New" being followed by city names like "New York" or "New Orleans."

When the `generate text` method is initiated starting with the word "new," the system successfully produces a simulated news snippet, such as "New York City, and the first time, the President Kennedy, and the first time."

This simulated output demonstrates a sound principle, illustrating how modern fake news generators operate by reproducing crude modeling patterns found within natural language.

However, the simple bigram model exhibits limitations. For instance, the generated text frequently converges and gets stuck in loops, as seen when starting with "the," which results in repetitive phrases like "President Kennedy on the first time."

To improve the model’s quality and variability, two primary methods can be implemented. One technique involves increasing the pattern length beyond strings of length two (bigrams), upgrading to trigrams (strings of length three). The second improvement is introducing randomness. Instead of always selecting the maximum probability word from the CFD, a random selection can be chosen from the list of bigrams associated with the current word.

Despite its simplicity, this custom generator, built using only half a dozen lines of code, provides a fundamental understanding of language modeling. It serves as a basic, demonstrable tool for experimenting with text generation principles in NLP. This entire process highlights how statistical language modeling is the foundational mechanism for large-scale text synthesis.

---

### 05_Accessing_text_corpora_Reading_1h

# Accessing text corpora
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/MGp0Z/accessing-text-corpora

Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2.2-2.3 (pp.52-59). If this link is broken, please let us know via the Student Portal . Accessing text corpora Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2.2-2.3 (pp.52-59). If this link is broken, please let us know via the Student Portal ....

---

### 06_Unix_for_Poets_Reading_1h

# Unix for Poets
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jM6g2/unix-for-poets

Church, K.W. 'Unix™ for poets' , Notes of a course from the European Summer School on Language and Speech Communication, Corpus Based Methods (1994). If this link is broken, please let us know via the Student Portal . Unix for Poets Church, K.W. 'Unix™ for poets' , Notes of a course from the European Summer School on Language and Speech Communication, Corpus Based Methods (1994). If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## Week 6

### 01_Intro_to_language_modelling_Video_9_min

# Intro to language modelling
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ALrrl/intro-to-language-modelling

This comprehensive course outlines a progression through advanced Natural Language Processing (NLP), beginning with introductory concepts and basic text processing techniques (Weeks 1–4). The core technical focus is Statistical Language Modelling (Weeks 5–6), which involves detailed study on estimating probabilities and evaluating the performance of language models. A key related technique is Topic Modelling (Section 3.3), dedicated to experiments in understanding and analyzing textual themes. The curriculum then expands into deep linguistic analysis, covering Lexical Semantics (Weeks 7–8) and Syntax and Parsing (Weeks 11–12). Practical applications begin with Text Categorisation and Sentiment Analysis (Weeks 9–10), moving into structured data extraction via Information Extraction (Weeks 13–14) and Information Retrieval (Weeks 15–16). Furthermore, the course addresses complex human-computer interaction through Chatbots and Dialogue Systems (Weeks 17–18). Specialized skills are reinforced by the module on NLP in Practice (Weeks 19–20), synthesizing the diverse techniques learned. The entire course structure is supplemented by video lessons, practice assignments, and peer-graded assessments across all major topics. The final weeks (Week 21 and Week 22) are dedicated to revision and the examination, ensuring full mastery of the covered domain.

---

### 02_Estimating_probabilities_Video_9_min

# Estimating probabilities
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/uwN8g/estimating-probabilities

Language modeling involves estimating the probabilities of word sequences found within a training corpus. Initially, these probabilities are calculated by simply counting the occurrences of specific word patterns in the available data. However, this counting approach is limited because training corpora are finite, leading to the critical problem of sparse data. If a specific utterance or word sequence is not found in the training data, its probability is assigned a zero value. To manage this, the Markov assumption is employed, which dictates conditioning a word's probability on only a shorter, localized fragment of its history, such as bigrams or trigrams.

The starting point for probability estimation is the Maximum Likelihood Estimator (MLE). The MLE calculates the probability of a word $w_i$ given its preceding word $w_{i-1}$ as: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i)}{\text{Count}(w_{i-1})}$. Although simple, this method fails when data is sparse, as it assigns a zero probability to any unobserved bigram.

To overcome the sparse data problem, language modelers seek to "smooth" the probability distribution. This involves shifting probability mass from highly likely events to potential, yet unseen, events in the vocabulary.

One simple technique is Laplace smoothing, which adds one to all observed counts. This yields the smoothed probability estimate: $P(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1} w_i) + 1}{\text{Count}(w_{i-1}) + |\text{V}|}$, where $|\text{V}|$ is the size of the vocabulary. Although effective, Laplace smoothing is considered a crude approach and more advanced schemes are often preferred in statistical language modeling.

Two more robust schemes for dealing with sparse counts are backoff and interpolation. Backoff operates by progressively falling back to a lower-order model if sufficient evidence is lacking in a higher-order model. For example, the system attempts to estimate $P(w_i | \text{history})$ using a trigram; if its count is zero, it "backs off" to the bigram estimate.

This process continues down the hierarchy—from trigram to bigram, and finally to the unigram model—with specific weighting factors applied at each level. Interpolation offers an alternative strategy where all models (trigram, bigram, and unigram) are utilized simultaneously. Instead of backing off, interpolation mixes the estimates by assigning weights, denoted as $\lambda_1, \lambda_2,$ and $\lambda_3$, to each level. These weights must be chosen such that $\lambda_1 + \lambda_2 + \lambda_3 = 1$. In essence, interpolation provides a balanced estimate derived from multiple contextual levels, creating a more robust model than a pure backoff approach.

---

### 03_Evaluating_language_models_Video_6_min

# Evaluating language models
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/DlqVs/evaluating-language-models

This course provides a comprehensive progression through Natural Language Processing (NLP), starting with foundational concepts (Weeks 1-4) and moving into core linguistic modeling techniques. Key early topics include Basic Text Processing (Weeks 3-4) and a deep dive into Language Modelling (Weeks 5-6), covering probability estimation and model evaluation. Subsequent focus shifts to advanced modeling, specifically introducing Topic Modelling (Week 3.3) for discovering abstract themes within text data. The syllabus then tackles linguistic meaning, starting with Lexical Semantics (Weeks 7-8), which concerns the meaning of individual words. The course progresses through complex structural analysis, dedicated to Text Categorisation and Sentiment Analysis (Weeks 9-10), followed by Syntax and Parsing (Weeks 11-12). Further advanced topics include Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16), essential for data mining and searching. Finally, the curriculum addresses applied systems through Chatbots and Dialogue Systems (Weeks 17-18) and culminates in practical applications and course summation (Weeks 19-20). The structure is heavily supported by various multimedia resources, including specialized videos, practice assignments, and peer-graded learning modules.

---

### 04_Language_modelling_Reading

# Language modelling
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/Alt02/language-modelling

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 3 If this link is broken, please let us know via the Student Portal . Language modelling Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 3 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 05_Topic_modelling_Video_11_min

# Topic modelling
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/70J53/topic-modelling

Topic modeling is an investigation technique similar to language modeling, aiming to find patterns and relationships within vast quantities of text data. However, unlike language modeling which models individual word sequences, topic modeling searches for

---

### 06_Topic_modelling_Reading

# Topic modelling
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/exW1V/topic-modelling

Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks . (Birmingham: Packt Publishing Ltd, 2021). Chapter 6, pp.185-201. If this link is broken, please let us know via the Student Portal. Topic modelling Antić, Z. Python natural language processing cookbook: over 50 recipes to understand, analyze, and generate text for implementing language processing tasks ....

---

### 07_Language_modelling_summary_Video_3_min

# Language modelling summary
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/7cMt2/language-modelling-summary

This course provides a comprehensive introduction to Natural Language Processing (NLP), structured across twenty weeks of specialized topics. The early weeks focus on foundational concepts, starting with an introduction to NLP, followed by essential basic text processing techniques. The program then dives deeply into Language Modelling, covering the theory, estimating probabilities, and the crucial evaluation of language models.

A significant module is dedicated to Topic Modelling, teaching methods for experimentation and understanding how abstract themes are derived from large texts. Progression continues with Lexical Semantics, which examines the meaning of words, before moving into Text Categorization and Sentiment Analysis. Technical skills expand further through Syntax and Parsing, which focuses on the structural analysis of language.

The latter half of the course emphasizes advanced applications, starting with Information Extraction and subsequently covering Information Retrieval techniques. The curriculum then addresses interactive NLP systems, introducing Chatbots and Dialogue Systems. Finally, the course concludes by applying these concepts through NLP in Practice and a comprehensive course summary. The structure ensures a complete mastery of core NLP methodologies, culminating in revision and examination periods.

---

## Week 7

### 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

### 02_Lexical_semantics_Video_7_min

# Lexical semantics
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/AwdkF/lexical-semantics

This course provides a comprehensive 22-week journey through Natural Language Processing (NLP), commencing with introductory modules in Week 1 and Week 2. Basic text processing skills are developed in Weeks 3 and 4, laying the foundation for more advanced language comprehension. The focus then shifts to Language Modelling during Weeks 5 and 6, followed by an intensive study of Lexical Semantics in Weeks 7 and 8. Week 7 is particularly detailed, covering topics such as WordNet, semantic similarity, and associated readings and assignments. Subsequently, the curriculum addresses practical applications in Weeks 9 and 10, focusing on Text Categorisation and Sentiment Analysis. The course progression continues with fundamental linguistic analysis, covering Syntax and Parsing in Weeks 11 and 12. Information processing deepens with dedicated modules on Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16). Finally, the later stages tackle advanced conversational AI, exploring Chatbots and Dialogue Systems (Weeks 17 and 18), culminating in practical NLP case studies in Weeks 19 and 20. The entire program concludes with a dedicated revision week (Week 21) and final examinations (Week 22).

---

### 03_WordNet_Video_6_min

# WordNet
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Rr7NY/wordnet

This summary focuses exclusively on the technical concepts and findings presented in the transcript, adhering to the 25-sentence limit while preserving all core information.

1. The discussion introduces WordNet, a lexical resource, utilizing it within a Jupyter Notebook environment by importing it as `WN` from `nltk.corpus`.
2. A fundamental concept in WordNet is the synset, which conceptually groups words into sets of synonyms.
3. Accessing these groups is performed by calling the method `WN.synsets` on a given term, such as "motorcar."
4. The result for "motorcar" is an indexed synset, exemplified by `car.n.01`, signifying the primary noun sense of the word "car."
5. In contrast, the term "spell" is shown to be far more complex, possessing numerous synsets (approximately 10 or 11), illustrating semantic ambiguity.
6. Drilling into a specific synset, like `car.n.01`, reveals its members—five synonyms in this case—which collectively form that synset.
7. WordNet is noted not to be indexed on individual terms, but rather on abstract concepts.
8. This abstract concept can be explicitly defined using a definition method, such as the definition for `car.n.01` ("a motor vehicle four wheels, usually propelled by an internal combustion engine").
9. The set of all individual members belonging to a synset are referred to as its lemmas.
10. Lemmas represent a linguistically principled process, similar to lemmatization, reducing various tokens to a common root.
11. The demonstration of "car" highlights that multiple senses correspond to multiple synsets; for example, five different synsets exist for the word "car."
12. By iterating through these senses, the transcript shows distinct meanings, including "wheeled vehicle," "railway car," "gondola," "elevator car," and "cable car."
13. The text then shifts focus to traversing the hierarchy within WordNet, exploring hyponyms (child terms) and hypernyms (parent terms).
14. By instantiating `motorcar` with the `car.n.01` sense, the hyponyms for that synset (`types_of_motorcar`) can be retrieved.
15. Conversely, retrieving the hypernym allows the user to move upward from the synset to its parent term.
16. The concept of polyhierarchy is introduced, explaining that a single concept can be defined in multiple ways, thus having multiple parents.
17. This complexity is demonstrated by using the `hypernym_paths` method, which reveals two distinct lineage paths for "motorcar."
18. The first parent path runs from `car.n.01` up through "wheeled vehicle" and "container."
19. The second parent path from "car" follows a different lineage, passing through "conveyance vehicle" before reaching the common parent "entity."
20. This illustrates that different ancestral paths lead up to a shared root node.
21. Key concepts introduced include the hierarchy of WordNet, the crucial role of synsets as conceptual representations, and the methods for navigating this structure.
22. The process of walking up and down the hierarchy enables the discovery of parent and child relationships within the lexicon.
23. The provided course outline shows that WordNet usage culminates in calculating semantic similarity in subsequent modules.
24. Further learning paths involve topics like Basic text processing, Language modelling, and Lexical semantics.
25. These tools provide the foundational knowledge necessary for advanced NLP tasks, such as Text categorisation and Information extraction.

---

### 04_Semantic_similarity_using_WordNet_Video_6_min

# Semantic similarity using WordNet
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/jtJOG/semantic-similarity-using-wordnet

This comprehensive 22-week curriculum initiates the study of Natural Language Processing (NLP) with introductory topics (Weeks 1 & 2) and progresses to basic text processing techniques (Weeks 3 & 4). Foundational concepts are built upon in Language Modelling (Weeks 5 & 6), which forms the basis for semantic analysis. Lexical Semantics is covered extensively (Weeks 7 & 8), involving specific study materials such as the WordNet Video (6 min), various assignments (10 min duration), and in-depth readings. Week 7 introduces semantic similarity using WordNet through focused videos and practical assignments, including a 1-hour Reading module. The curriculum then moves to practical application, covering Text Categorisation and Sentiment Analysis (Weeks 9 & 10) and formal language structure via Syntax and Parsing (Weeks 11 & 12). Subsequent advanced stages focus on extracting knowledge, tackling Information Extraction (Weeks 13 & 14) and Information Retrieval (Weeks 15 & 16). The final major concepts address interaction design through Chatbots and Dialogue Systems (Weeks 17 & 18) and practical application in NLP (Weeks 19 & 20). The course culminates in a final revision week (Week 21) and the examination period (Week 22).

---

### 05_WordNet_Reading_1h

# WordNet
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/CDwg5/wordnet

Read the following chapter on categorising and tagging words: Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019). Chapter 2 - Refer to Section 5 If this link is broken, please let us know via the Student Portal . WordNet Read the following chapter on categorising and tagging words: Bird, S., E. Klein and E. Loper Natural language processing with Python: analyzing text with the natural language toolkit . (2019)....

---

### 06_Lexical_semantics_Reading_1h

# Lexical semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/3ePrf/lexical-semantics

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5. In the event that the draft of the 3rd edition does not contain the chapter reference you require, please refer to the second edition, Chapter 19, pp.623-631. If this link is broken, please let us know via the Student Portal . Lexical semantics Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5....

---

### 07_Activity_Exploring_semantic_similarity_Reading_1h

# Activity: Exploring semantic similarity
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/4hJ2a/activity-exploring-semantic-similarity

Task 1 1. Explain what is meant by the following terms and give one example of each from WordNet: Synonym Antonym Hyponym Hypernym Meronym Holonym 2. Pick two of WordNet’s similarity metrics and briefly explain how they calculate the degree of similarity between two concepts. Activity: Exploring semantic similarity Task 1 1. Explain what is meant by the following terms and give one example of each from WordNet: Synonym Antonym Hyponym Hypernym Meronym Holonym 2....

---

## Week 8

### 01_Intro_to_word_embeddings_Video_16_min

# Intro to word embeddings
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/cUvLX/intro-to-word-embeddings

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 02_Vector_semantics_Reading_1h

# Vector semantics
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/BSaa8/vector-semantics

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5 If this link is broken, please let us know via the Student Portal . Vector semantics Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 03_Word_embeddings_in_practice_Video_8_min

# Word embeddings in practice
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/rHypB/word-embeddings-in-practice

This course provides a comprehensive progression through Natural Language Processing (NLP), beginning with introductory concepts and basic text processing techniques (Weeks 1-4). Early instruction transitions into Language Modelling (Weeks 5-6), establishing probabilistic frameworks for understanding language structure. A significant focus is placed on Lexical Semantics (Weeks 7-8), specifically detailing Vector Semantics and introducing word embeddings. The curriculum covers advanced topics like Word2vec and word vector algebra, utilizing practice assignments and experiments to grasp the semantic properties of embeddings and analyze bias. Subsequent modules apply these concepts to Text Categorisation and Sentiment Analysis (Weeks 9-10), moving into supervised learning paradigms. Structural analysis is addressed through Syntax and Parsing (Weeks 11-12), which examines the grammatical rules governing sentence construction. The course then delves into information gathering, covering Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). These foundational skills are built upon to develop complex systems, notably Chatbots and Dialogue Systems (Weeks 17-18). The study culminates in practical applications in NLP (Week 19), followed by a comprehensive course summary and final revision (Weeks 20-22).

---

### 04_Word2vec_Reading

# Word2vec
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/jAjR4/word2vec

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.5. If this link is broken, please let us know via the Student Portal . Word2vec Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.5. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 05_Word_vector_algebra_Video_5_min

# Word vector algebra
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/CGpdf/word-vector-algebra

This video and associated material explore the unexpected and powerful capability of word embeddings: their ability to perform vector algebra. Word embeddings are fundamentally dense vectors that encapsulate the context in which words appear. These vectors allow researchers to find conceptual similarities between terms, but their most crucial function is enabling meaningful pattern discovery through vector arithmetic. Historically, verbal reasoning tasks, such as A is to B as C is to ?, rely on human intuition, but these embeddings, trained using word2vec and Gensim, can perform these calculations.

The technique involves treating words as vectors in a high-dimensional space, allowing operations like addition and subtraction to yield conceptually related results. For instance, demonstrating a relational analogy, the process involves taking the target vector, subtracting the source concept, and adding the context concept. If we seek the relationship (woman is to ?) given (man is to king), the calculation approximates: $\text{Vector}(\text{King}) - \text{Vector}(\text{Man}) + \text{Vector}(\text{Woman})$. Using the Google News model, this operation successfully yielded 'queen' as the top result.

This illustrates how the embeddings encode abstract concepts, not just vocabulary. Further examples showcase the power of this semantic encoding. When asked to define the geographic relationship: Berlin is to Germany as Paris is to ?, the model successfully extracted 'France.' This demonstrates that encyclopedic knowledge is effectively encoded within the dense factors of the word2vec models.

The capabilities extend beyond simple factual relationships, touching upon syntactic patterns. Applying vector algebra to inflections, the operation (Have - Be) relative to 'has' correctly identified 'is' as the third-person singular form. Similarly, for adjective transformations, the analogy $\text{Longest} - \text{Short}$ relative to 'longest' resulted in 'shortest.'

Semantic relationships are also found through transformations like antonymy. Using the structure $\text{Dark} - \text{Light}$ relative to 'longest,' the system accurately identified 'short' as the appropriate antonym to 'long.' The model can even handle complex grammatical shifts, such as finding the proper pronoun transformation when $\text{He}$ is to $\text{She}$ as $\text{Him}$ is to ?, successfully outputting 'her.'

Furthermore, the models can perform rudimentary categorization tasks, identifying the odd one out in a list, as demonstrated by correctly classifying 'cereal' among 'Breakfast, Dinner, and Lunch.' This comprehensive application confirms the incredible flexibility of word embeddings for a wide variety of Natural Language Processing (NLP) tasks. The associated course content details these methods under "Vector semantics and embeddings," emphasizing the practical application of word vector algebra. This approach provides a deep insight into how language models capture grammar, knowledge, and context simultaneously within dense vector representations.

---

### 06_Semantic_properties_of_embeddings_Reading_1h

# Semantic properties of embeddings
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/56nOO/semantic-properties-of-embeddings

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.7. Semantic properties of embeddings Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.7. Mark as completed Dislike Report an issue

---

### 07_Bias_and_embeddings_Reading_1h

# Bias and embeddings
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/3a5q2/bias-and-embeddings

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.8 If this link is broken, please let us know via the Student Portal . Bias and embeddings Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 5, section 5.8 If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

### 08_Lexical_semantics_summary_Video_4_min

# Lexical semantics summary
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/xPRmE/lexical-semantics-summary

This course provides a comprehensive, 22-week curriculum spanning foundational to advanced Natural Language Processing (NLP) techniques. Initial modules introduce NLP fundamentals (Weeks 1-4), progressing quickly into core language modeling principles (Weeks 5-6). A significant technical focus is dedicated to Lexical Semantics (Weeks 7-8), specifically detailing vector semantics, word embeddings, and the Word2vec algorithm. Key technical deep dives involve understanding the mathematical basis of word vector algebra and analyzing the semantic properties and biases inherent in these embeddings. The curriculum then advances to practical applications, covering Text Categorization and Sentiment Analysis (Weeks 9-10). Further specialized topics include the structural complexity of Syntax and Parsing (Weeks 11-12), followed by Information Extraction and Information Retrieval methodologies (Weeks 13-16). Later weeks apply these concepts to modern conversational AI, exploring Chatbots and Dialogue Systems (Weeks 17-18). The course culminates with an application-based module on NLP in practice (Week 19), concluding with a course summary and revision week. The technical journey moves from basic text processing to complex modeling, from tokenization to deep vector representation and structured language understanding.

---

## Week 9

### 01_Introduction_and_learning_objectives_Video_1_min

# Introduction and learning objectives
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/8EryH/introduction-and-learning-objectives

This course is structured over 22 weeks, beginning with the fundamental concepts of NLP (Week 1-2) and foundational skills like basic text processing (Week 3-4). The curriculum then progresses to crucial modeling techniques, starting with language modelling (Week 5-6) and advancing into lexical semantics (Week 7-8). Next, the focus shifts to applied analysis, covering text categorisation and sentiment analysis (Week 9-10). A major section is dedicated to syntax and parsing (Week 11-12), detailing advanced methods such as Context-free grammars, Constituency parsing, Dependency parsing, and Probabilistic parsing. Subsequently, the study moves into specialized knowledge retrieval, including Information extraction (Week 13-14) and Information retrieval (Week 15-16). The course then examines interactive systems through the study of Chatbots and dialogue systems (Week 17-18). Practical application is reinforced in the final topics, covering NLP in practice and a comprehensive course summary (Week 19-20). The program concludes with a dedicated revision week followed by the final exam week (Week 21-22).

---

### 02_Intro_to_text_classification_Video_8_min

# Intro to text classification
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/3VYBk/intro-to-text-classification

This comprehensive 22-week course introduces the foundational concepts of Natural Language Processing (NLP), starting with introductory topics in Weeks 1 and 2. Early focus areas include Basic Text Processing (Weeks 3 and 4), followed by Language Modelling, which covers probability concepts necessary for understanding text generation (Weeks 5 and 6). The course then delves into Lexical Semantics (Weeks 7 and 8), examining the meaning of words and phrases. A major section focuses on Text Categorisation and Sentiment Analysis (Weeks 9 and 10), introducing crucial classification methods like Bayesian classification and Multinomial Naive Bayes, which heavily utilizes Bayes' theorem. Technical skills are enhanced through extensive practice assignments, such as those dedicated to Naive Bayes and Bayes' theorem. Later topics transition into structural analysis, covering Syntax and Parsing (Weeks 11 and 12), and specialized data manipulation via Information Extraction and Information Retrieval (Weeks 13–16). The curriculum culminates with advanced dialogue systems, exploring Chatbots and Dialogue Systems (Weeks 17 and 18), before concluding with a practical overview of NLP applications (Weeks 19 and 20). The entire learning structure is reinforced by laboratory experiments, discussion prompts, and dedicated revision time. The course ensures students gain both theoretical knowledge and practical experience across the entire NLP pipeline.

---

### 03_Bayes'_theorem_Video_7_min

# Bayes' theorem
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/QNgrV/bayes-theorem

This discussion delves into Naive Bayes and Bayesian classification, beginning with a detailed review of Bayes’ Theorem. The fundamental concept of Bayes’ theorem is that new evidence should be used to update prior beliefs, rather than being treated in isolation to determine them. To illustrate this, the transcript presents a mental puzzle: determining whether a shy, meticulous colleague is more likely a librarian or a farmer. Intuitive judgment often favors a librarian based on stereotypes, neglecting the crucial role of prior probabilities.

In reality, the prior probability heavily favors farmers; for instance, in the UK in 2014, the ratio of farmers to librarians was significantly weighted, often approximated at 9:1. A rational judgment must factor in both the descriptive evidence and these baseline population probabilities. Bayes’ theorem formalizes this update process: the probability of a hypothesis given the evidence is equivalent to the hypothesis probability multiplied by the probability of the evidence given the hypothesis, divided by the probability of the evidence.

To make this concrete, a scenario involving 100 randomly sampled people is analyzed, maintaining the 90 (farmers) to 10 (librarians) prior probability ratio. If 40% of librarians and 10% of farmers fit the description, a mathematical calculation reveals that the probability of the individual being a librarian is approximately 31%. This finding critically demonstrates that the evidence does not outweigh the strong prior probability.

This concept can be generalized to a neutral case, where confidence might be 50%, illustrating that the relative proportions of areas are used to calculate relative probabilities. Mathematically, the probability of the evidence given the hypothesis is calculated as the proportion of the highlighted area divided by the total highlighted area.

Conceptualizing Bayes' theorem using areas, the area corresponding to the probability of Hypothesis (H) multiplied by the probability of Evidence given H defines a specific region. The overall probability of the evidence (the denominator) is the sum of the relevant rectangles. Ultimately, the core takeaway is that evidence serves to update existing beliefs, not establish them from scratch.

The supplementary material outlines the educational structure for this topic, covering NLP from Week 1 through Week 20. Key topics include Basic Text Processing (Weeks 3-4), Language Modelling (Weeks 5-6), Lexical Semantics (Weeks 7-8), and Text Categorisation/Sentiment Analysis (Week 9 and 10). Specific instructional modules dedicated to this subject matter include "Bayes' theorem" (7 min) and "Bayesian classification" (10 min). Furthermore, specialized modules exist for "Multinomial naive Bayes" (7 min) and "Naive Bayes classification." These modules confirm that Naive Bayes and its related classification techniques are central components of the course curriculum.

---

### 04_Bayesian_classification_Video_10_min

# Bayesian classification
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/FG8sn/bayesian-classification

This course provides a comprehensive study of Natural Language Processing, beginning with foundational concepts in Weeks 1 and 2. The curriculum progresses to basic text processing techniques, covering initial data manipulation in Weeks 3 and 4. Key intermediate concepts involve Language Modelling (Weeks 5 and 6) and the analysis of Lexical Semantics (Weeks 7 and 8). A major focus is placed on Text Categorisation and Sentiment Analysis, detailing methods like Bayes’ theorem and its application in Bayesian and Multinomial Naive Bayes classification (Weeks 9 and 10). Subsequent modules delve into structural analysis, introducing Syntax and Parsing (Weeks 11 and 12). The course then transitions into knowledge retrieval, exploring Information Extraction (Weeks 13 and 14) and Information Retrieval (Weeks 15 and 16). Advanced interaction systems are covered through the study of Chatbots and Dialogue Systems (Weeks 17 and 18). The latter phase of the course explores NLP in practice (Week 19), providing real-world application examples. Weeks 20 through 22 conclude the learning journey with a course summary, revision, and examination. The structured progression ensures deep understanding across foundational, statistical, and applied NLP domains.

---

### 05_Multinomial_naive_Bayes_Video_7_min

# Multinomial naive Bayes
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/pL0Q0/multinomial-naive-bayes

This discussion continues the topic of Bayesian classification by introducing a specialized variant: Multinomial Naive Bayes.
The previous Naive Bayes approach was based on a generative model, assuming features are generated by a model.
In that model, classification compares posterior probabilities for each label using Bayes' theorem.
This calculation involves multiplying the likelihood and the prior, then dividing by the probability of the evidence to yield the posterior probability.
Naive Bayes also relies on key assumptions, including feature independence and the equitable treatment of all features, which may not hold true in real-world data.
The Multinomial Naive Bayes variation fundamentally assumes that the features are generated from a multinomial distribution.
This approach focuses on the probability of observing counts across various categories, thus modeling by finding a best-fit multinomial distribution.
This method is highly suited for text classification tasks, such as categorizing a passage or blog post based on a topical scheme.
In this context, categories correspond to word types, meaning the multinomial distribution observes the counts across the entire vocabulary.
Since raw textual data cannot be directly processed, it must first be converted into a numerical form.
The simplest technique for this numerical conversion, reviewed previously, is the use of `TfidfVectorizer`.
For experimentation, the 20 newsgroups corpus is utilized, which is a collection of approximately 20,000 postings across 20 diverse topics.
The workflow involves setting up a data pipeline that integrates the `TfidfVectorizer` object and the `MultinomialNaiveBayes` model.
This pipeline is then fit using the training data and subsequently used to generate labels by calling the `predict` method on the test data.
A critical way to analyze the results of this classification process is through the confusion matrix.
The confusion matrix plots all pairwise possibilities, showing how true labels were classified against their predicted labels.
The diagonal elements of the confusion matrix represent correct classifications, where the predicted label matches the true label.
Off-diagonal elements reveal specific instances of misclassification, highlighting where the model made errors.
The lecture noted that some misclassifications are plausible, for instance, items for sale (`misc.forsale`) being predicted as recreational autos (`rec.autos`).
Another example pointed out that miscellaneous topics could plausibly be misclassified as talking about guns (`talk.politics.guns`).
The principles established allow the construction of a custom classifier function.
This function accepts a category, the trained model, and an arbitrary sentence to return a predicted label name.
Testing the custom function demonstrates accuracy, successfully classifying a sentence about politics as `talk.politics.misc`.
It was noted that classification difficulty increases when testing on categories not adequately covered during the training phase, such as Shakespearean text.

---

### 06_Naive_Bayes_classification_Reading_10_min

# Naive Bayes classification
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/mdsy3/naive-bayes-classification

VanderPlas, J. Python data science handbook: Essential tools for working with data . (California: O'Reilly Media, Inc., 2016), pp.382–390. Naive Bayes classification VanderPlas, J. Python data science handbook: Essential tools for working with data . (California: O'Reilly Media, Inc., 2016), pp.382–390. Mark as completed Dislike Report an issue

---

### 07_Naive_Bayes_and_sentiment_classification_Reading_1h

# Naive Bayes and sentiment classification
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ZroNC/naive-bayes-and-sentiment-classification

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 4. Also, refer to Appendix B on this online book version. If this link is broken, please let us know via the Student Portal . Naive Bayes and sentiment classification Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Chapter 4. Also, refer to Appendix B on this online book version. If this link is broken, please let us know via the Student Portal ....

---

