"""
======================
SAGA: Weighted samples
======================

Plot decision function of a weighted dataset, where the size of points
is proportional to its weight.

Adapted from scikit-learn's plot_sgd_weighted_samples.py
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from lightning.impl.sag import SAGAClassifier

# we create 20 points
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = np.array([1] * 10 + [-1] * 10)
sample_weight = 100 * np.abs(np.random.randn(20))
# and assign a bigger weight to the last 10 samples
sample_weight[:10] *= 10

# plot the weighted data points
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=sample_weight, alpha=0.9,
            cmap=plt.cm.bone)

# fit the unweighted model
clf = SAGAClassifier(alpha=0.01, loss='log')
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, levels=[0], linestyles=['solid'], colors="black")

# fit the weighted model
clf = SAGAClassifier(alpha=0.01, loss='log')
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, levels=[0], linestyles=['dashed'], colors="black")

# `QuadContourSet.collections` was removed in matplotlib 3.8, so the legend is
# built from explicit handles instead of from the contour artists.
plt.legend(
    handles=[
        Line2D([0], [0], color="black", linestyle="solid", label="no weights"),
        Line2D([0], [0], color="black", linestyle="dashed",
               label="with weights"),
    ],
    loc="lower left",
)

plt.xticks(())
plt.yticks(())
plt.show()