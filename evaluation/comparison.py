from evaluation.metrics import evaluate
import numpy as np

def paired_t_test(baseline_scores, personalized_scores):
    from scipy.stats import ttest_rel
    return ttest_rel(baseline_scores, personalized_scores)
