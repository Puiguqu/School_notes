# 04_Exotic_distance_measures_Reading_1h

# Exotic distance measures
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/cCeml/exotic-distance-measures

Many applications succeed using traditional metrics like Euclidean or Manhattan distance. However, certain fields, such as music notation, demand sophisticated methods for measuring similarity. Earth Movers distance, also known as Transportation Distance, is a specialized form of edit distance designed to address this complexity. Technically, it is characterized by its ability to apply different weights to varying points. This means the computational cost of a change is not uniform but varies depending on its location within the data structure. The Dutch Song Database specifically employs the Earth Movers distance metric for its analyses. This method is founded upon research and development conducted by Rainer Typke and his colleagues. Specifically, the seminal work was published in the 4th International Conference on Music Information Retrieval in 2003. The primary citation for this foundational work is Typke, R., Giannopoulos, P., Veltkamp, R. C., Wiering, F., and van Oostrum, R. These specialized measures have been further evaluated using the Dutch Song Database. Recent comparative studies contrasted Earth Movers distance with other measures, including the common Euclidean distance. The key finding of these later evaluations was that while Euclidean distance is functional, the specialist distance measures significantly outperform it. This is supported by research from Janssen, B., van Kranenburg, P., and Volk, A.

