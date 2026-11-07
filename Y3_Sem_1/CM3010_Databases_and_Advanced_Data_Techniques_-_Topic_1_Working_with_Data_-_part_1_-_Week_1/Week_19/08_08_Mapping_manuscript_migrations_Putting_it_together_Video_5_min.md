# 08_Mapping_manuscript_migrations_Putting_it_together_Video_5_min

# Mapping manuscript migrations: Putting it together?
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/j5zo0/mapping-manuscript-migrations-putting-it-together

The project's primary goal was to map manuscript migrations by integrating insights from three distinct and specialized databases. These databases—the Schoenberg Database, the Oxford database, and others—possess varied structures and aims. The confluence of these differences creates a rich and valuable composite dataset. The central research question driving the project was "how" to successfully combine the data from these divergent sources. The team firmly believed that asking questions across all three datasets would unlock research possibilities inaccessible to individual sources. The major technical challenge, therefore, involved developing a method to allow the systematic exploration of these three datasets simultaneously.

The first technical question concerned the method of data combination. Candidates included merging all data into an existing repository, such as stacking bottling data into the Schoenberg Database. Alternatively, the team considered creating a completely new union database encompassing all sources. A third complex option involved employing federated queries, which would send requests to all databases without creating a single, combined entity.

Another critical logistical hurdle was ensuring data integrity and consistency across the system. Specifically, the system needed a mechanism to guarantee that any updates made to the original client databases would successfully propagate throughout the combined dataset. A separate issue arose regarding the fate of auxiliary datasets, such as correction databases, and where they would reside long-term.

This challenge led to profound questions regarding the project's permanence and infrastructure. Since the project itself was short-lived, but the datasets are long-term institutional assets, durability is paramount. There is no guarantee of the permanent existence of the infrastructure, nor is there a permanent staffing commitment after the project concludes.

A crucial practical difficulty involves reconciling the diverse data models. The three sources operate using radically different approaches and levels of detail. For example, the Schoenberg Database provides strong observations of manuscripts but is notably hazy on manuscript existence. Conversely, the Oxford database is highly definite regarding manuscripts when they are known to be in the library. This difference in granularities presents a significant modeling problem.

The team had to determine how to reconcile these varying levels of detail while ensuring the solution scales efficiently to handle tens of thousands of records. The overall challenge requires solving issues spanning data architecture, system longevity, and semantic modeling. The project served as a practical exploration of these complex database management migrations. Ultimately, the study highlights the necessity of developing robust, scalable methods for integrating disparate, heterogeneous data. These challenges underscore the complexities inherent in modern data science and library management.

