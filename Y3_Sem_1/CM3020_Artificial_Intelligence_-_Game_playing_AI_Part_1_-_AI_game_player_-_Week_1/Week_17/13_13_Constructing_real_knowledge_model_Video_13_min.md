# 13_Constructing_real_knowledge_model_Video_13_min

# Constructing real knowledge model
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/f09GE/constructing-real-knowledge-model

This lecture addresses how data and knowledge are incorporated into real AI systems, focusing specifically on drug design applications. The speaker introduces the necessity of using external data and knowledge representations for the "robot scientist" agent. The demonstration begins with a simple toy domain model containing chemical entities and basic biological properties, acknowledging that real-world sources are significantly more complex.

A primary external resource discussed is CHEMBL, described as an ontology of chemical entities of biological interest containing over 150,000 classes. CHEMBL allows users to retrieve extensive information on specific compounds, such as morphine, including synonyms, various names, and molecular properties. The use of Unique Resource Identifiers (IDs) is critical to ensure that diverse resources accurately refer to the same chemical entity.

Another vital source is DrugBank, which functions as a comprehensive database rather than an ontology. DrugBank provides detailed information on substances, including brand names, genetic names, mechanism of action, volume of distribution, and adverse effects. It also contains critical data regarding potential drug-drug and food interactions, such as interactions involving alcohol.

CHEMBL is highlighted as especially relevant to the drug design case study because it is a collaborative database populated by researchers analyzing scientific literature. For compounds like morphine, CHEMBL provides data on clinical trial stages, approved uses, synonyms, and structural information.

Crucially, CHEMBL incorporates molecular features, such as the Lipinski rules (or Rule of Five), which help assess whether a small molecule is likely to be a drug. CHEMBL thus provides extensive experimental and clinical data used by the robotic agent.

In the project, the toy robot scientist extensively utilized these external sources, combining its own derived data with information from resources like CHEMBL. The process of integrating data and knowledge from diverse resources is referred to as knowledge and data integration, a difficult task due to inconsistent or varied textual information.

This integrated data is then unified into a machine-accessible, structured format, represented by the lab project's internal ontologies. These ontologies were largely imported from other sources, particularly those related to systems biology and biological entities. The architecture ensures that all necessary entities and information are consolidated for the robot scientist to reason over.

The underlying structure utilizes an upper-level ontology, which is foundational in systems biology and ensures essential interoperability between different data sets. This unified structure is characteristic of how real knowledge models are constructed. Although some external sources possess strict logical structures, this effort is challenging because all available information must be combined, harmonized, and encoded. The final goal is to provide a logically consistent dataset that the AI system can effectively reason with.

