# 07_Evaluation_metrics_Video_5_min

# Evaluation metrics
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/ORIoC/evaluation-metrics

The provided material details the critical concepts of evaluation metrics within Natural Language Processing (NLP), arguing against the sole reliance on accuracy for performance measurement. The transcript introduces the limitations of accuracy, exemplified by a fictitious spam classifier operating on an unbalanced dataset. In such scenarios, high accuracy can be misleadingly achieved simply by predicting the majority class every time. A more compelling example involves a hospital system designed to predict cancerous tumors from medical scans. In this critical context, the classes—tumor and not tumor—are also unbalanced. The major issue is the differential cost of errors, where a False Negative (missing an actual tumor) is life-threatening. This serious disparity in error costs indicates that accuracy is an unsuitable primary metric.

To address this inadequacy, the concept of the Confusion Matrix is introduced as the foundational tool for comparison. This matrix compares the actual values, referred to as the ground truth, against the system's predicted values. The key components derived from this matrix are defined as True Positives (TP), False Positives (FP), False Negatives (FN), and True Negatives (TN).

The accuracy metric is initially defined as the proportion of correct predictions over all predictions, corresponding to the diagonal elements of the matrix divided by the total dataset size. However, the discussion pivots to two more robust metrics: Recall and Precision.

Recall, or sensitivity, is mathematically defined as the proportion of true positives over all actual positive cases (TP / (TP + FN)). Essentially, it measures how many of the actual tumors the system successfully detected. Conversely, Precision is calculated as the portion of true positives among all predicted positive cases (TP / (TP + FP)). Precision addresses the rate of correctness for the system’s positive predictions.

Fictitious examples demonstrate how these metrics provide a far more effective illustration of performance on unbalanced datasets than raw accuracy. By calculating Recall and Precision, researchers gain a principled baseline against which subsequent algorithmic iterations can be compared. This methodical approach is vital for improving system performance in fields like NLP.

The supplementary course outline contextualizes these concepts within a larger curriculum. The studies progress through various topics, starting with the Introduction to NLP and foundational Python/Jupyter environment skills. Subsequent modules cover Basic text processing, Language modelling, Lexical semantics, and Text categorisation and sentiment analysis. Core areas like Syntax and parsing, Information extraction, and Information retrieval are also covered over subsequent weeks. The dedicated evaluation section (Week 2, Topic 1.4) reinforces the importance of these specialized metrics. The overall structure provides a comprehensive framework for mastering advanced NLP methodologies.

