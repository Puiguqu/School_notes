# 02_Open,_Linked_and_Data_Video_6_min

# Open, Linked and Data
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/OiUL0/open-linked-and-data

The presentation introduces the concept of the Semantic Web of semantics, focusing specifically on Linked Data and Linked Open Data. While the Semantic Web is a broad concept, Linked Data requires a precise understanding of three foundational terms: data, open, and linked. Defining data is initially left vague but the concept of "openness" is crucial for the overall discussion. Generally, open data implies cost-free access and the removal of barriers to use.

Openness further requires that the data must be findable, accessible in various ways, and restriction-free for reuse, often governed by specific licenses. An increasingly important set of criteria is the FAIR principles, adopted by international governmental organizations. FAIR stands for Findable, Accessible, Interoperable, and Reusable, providing an additional layer of requirement beyond simple openness.

The speaker explicitly distinguishes between these terms: data can be closed; data can be open but not linked (e.g., a static spreadsheet); and data can be linked but not necessarily open. The ideal state is Linked Open Data.

Linked data fundamentally relies on web links, specifically URLs, which have been central to web architecture since Tim Berners-Lee’s 1989 proposal. Early hypertext systems struggled because link integrity was difficult to maintain, as there was no centralized coordination.

A key innovation of the URL is that linking is one-way and does not require permission or input from the organization being linked to. This decentralized approach makes the system "Wild West" in nature, meaning links can break.

However, in Linked Data, the expectation is that linking occurs specifically at the URL level. URLs possess guaranteed uniqueness globally, which is a significant advantage over traditional database keys. The maintenance responsibility is clearly tied to the registering individual or organization associated with the domain name.

The use of shared identifiers (URLs) offers immense advantages for shared, distributed, web-scale databases. Specifically, these identifiers are unlimited in number, independent of hardware and software, and universally applicable. This robustness makes URLs extremely useful as unique keys for distributed data systems. This entire framework allows for the construction of linked open data.

