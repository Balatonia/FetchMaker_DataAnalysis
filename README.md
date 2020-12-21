# FetchMaker_DataAnalysis
The goal of FetchMaker is to classify different dog breeds to match them with possible future owners. I used SciPy and NumPy to analyze data and perform statistical tests.

The FetchMaker package provides data like weight, color, tail length of each dog. Dogs are grouped by breed (whippet, terrier, shihtzu, pitbull, rottweiler, poodle, chihuahua, and greyhound).

I used a binomial test to test whether whippets are more or less likely to be rescues compared to the overall average of 8%. It turned out that only 6% of whippets are rescues and the binomial test revealed that this difference is significant.

I used an ANOVA to compare the weights of whippets, terriers and pitbulls. Additionally, Tukey's range test revealed that there are significant differences between the average weights of pitbull and terriers as well as between whippets and terriers.

Furthermore, I did an Chi-Square contingency test to check the distribution of colors between poodles and shih tzus. 
