### Side-by-Side Box Plots
The difference in mean math scores for students at GP and MS was 0.64. How do we know whether this difference is considered small or large? To answer this question, we need to know something about the spread of the data.

One way to get a better sense of spread is by looking at a visual representation of the data. Side-by-side box plots are useful in visualizing mean and median differences because they allow us to visually estimate the variation in the data. This can help us determine if mean or median differences are “large” or “small”.

Let’s take a look at side by side boxplots of math scores at each school:

sns.boxplot(data = df, x = 'school', y = 'G3')
plt.show()



title

Looking at the plot, we can clearly see that there is a lot of overlap between the boxes (i.e. the middle 50% of the data). Therefore, we can be more confident that there is not much difference between the math scores of the two groups.

In contrast, suppose we saw the following plot:

title

In this version, the boxes barely overlap, demonstrating that the middle 50% of scores are different for the two schools. This would be evidence of a stronger association between school and math score.

import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
import seaborn as sns

students = pd.read_csv('students.csv')

#create the boxplot here:
sns.boxplot(data=students, x ='address',y='G3')

plt.show()


Inspecting Overlapping Histograms
=================================
Another way to explore the relationship between a quantitative and categorical variable in more detail is by inspecting overlapping histograms. In the code below, setting alpha = .5 ensures that the histograms are see-through enough that we can see both of them at once. We have also used normed=True make sure that the y-axis is a density rather than a frequency (note: the newest version of matplotlib renamed this parameter density instead of normed):

plt.hist(scores_GP , color="blue", label="GP", normed=True, alpha=0.5)
plt.hist(scores_MS , color="red", label="MS", normed=True, alpha=0.5)
plt.legend()
plt.show()



title

By inspecting this histogram, we can clearly see that the entire distribution of scores at GP (not just the mean or median) appears slightly shifted to the right (higher) compared to the scores at MS. However, there is also still a lot of overlap between the scores, suggesting that the association is relatively weak.

Note that there are only 46 students at MS, but there are 349 students at GP. If we hadn’t used normed = True, our histogram would have looked like this, making it impossible to compare the distributions fairly:

title

While overlapping histograms and side by side boxplots can convey similar information, histograms give us more detail and can be useful in spotting patterns that were not visible in a box plot (eg., a bimodal distribution). For example, the following set of box plots and overlapping histograms illustrate the same hypothetical data:

title

While the box plots and means/medians appear similar, the overlapping histograms illuminate the differences between these two distributions of scores.


import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt 
students = pd.read_csv('students.csv')

scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

#create the overlapping histograms here:
plt.hist(scores_urban, color="blue", label="Urban", normed=True, alpha=0.5)
plt.hist(scores_rural, color="red", label="Rural", normed=True, alpha=0.5)
plt.legend()
plt.show()
