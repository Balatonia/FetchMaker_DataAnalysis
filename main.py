import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(rottweiler_tl)
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippet_rescues = len(whippet_rescue)
num_whippets = np.size(whippet_rescue)

whippet_test = binom_test(num_whippet_rescues,num_whippets, p=0.08)
print(whippet_test)

whippet_weight = fetchmaker.get_weight("whippet")
terrier_weight= fetchmaker.get_weight("terrier")
pitbull_weight= fetchmaker.get_weight("pitbull")

dogs_anova_teststatistic, dogs_anova_pvalue = f_oneway(whippet_weight,terrier_weight, pitbull_weight)
print(dogs_anova_pvalue)

dogs_weights = np.concatenate([whippet_weight, terrier_weight, pitbull_weight])
labels = ['whippet'] * len(whippet_weight) + ['terrier'] * len(terrier_weight) + ['pitbull'] * len(pitbull_weight)
 
tukey_results = pairwise_tukeyhsd(dogs_weights, labels, 0.05)
print(tukey_results)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
dogs_color_table = [[np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")], 
[np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")], 
[np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")], 
[np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")], 
[np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]

color_test = chi2_contingency(dogs_color_table)
print(color_test[1])
