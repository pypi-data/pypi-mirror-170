"""Plotting Utilities for the factor analysis module."""

import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def scree_plot(eigenvalues, axes) -> None:
    """
    Plot the scree plot of the eigenvalues onto the given axes.

    Parameters
    ----------
    eigenvalues : array_like
        The eigenvalues to plot.
    axes : matplotlib.axes.Axes
        The Axes to plot onto.

    Returns
    -------
    None
    """
    x = np.arange(len(eigenvalues)) + 1
    axes.plot(x, eigenvalues, "bo-", linewidth=2)
    axes.axhline(1, c="g")
    axes.set_title("Scree Plot")
    axes.set_xlabel("Factor")
    axes.set_ylabel("Eigenvalue")


def create_loadings_heatmaps(
    X, methods, figsize=(10, 8), fa_params=None, annotate=True
):
    """Plot the loadings heatmap of multiple unfitted FactorAnalysis instances.

    The Instances will be fitted using the data `X`.
    Red Values indicate large positive loadings and blue indicate large
    negative values. Since there is no colorbar, if you want This
    to show up in the plot, use the `annotate` keyword argument to
    display the values of the loadings in the heatmap.

    This is useful for comparing different variants of factor analysis models for
    different parameters. The n_factors parameter has to be set, other parameters
    of the factor analysis instances can be set using the other_params dict.

    Parameters
    ----------
    X : array-like, shape (n_samples, n_features)
        Data that is used in the fit method.
    methods : array_like of tuples (str, FactorAnalysis)
        This contains the variants of factor analysis instances. Each element
        is a tuple (str, FactorAnalysis) where the first element is a short description
        and the second element is the unfitted FactorAnalysis instance.
        You only need to specify the type of algorithm used in each instance.
        The other parameters can be set using the fa_params dict containing
        key-value pairs, e.g. `fa_params={'n_factors': 2}`.
    figsize : tuple of int
        The size of the figure.
    fa_params : dict
        This is used to batch-set the parameters of the factor analysis instances.
    annotate : bool, default=True
        If True, then annotate the heatmap with the corresponding
        values of the loading matrix.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object containing all heatmaps.
    """
    if fa_params is None:
        fa_params = {}
    fig, axes = plt.subplots(ncols=len(methods), figsize=figsize)
    if len(methods) == 1:
        # make it iterable
        axes = [axes]
    for ax, (method, fa) in zip(axes, methods):
        fa.set_params(**fa_params)
        fa.fit(X)
        feature_names = getattr(
            fa, "feature_names_in_", [f"X{i}" for i in range(1, X.shape[1] + 1)]
        )
        loadings = fa.loadings_
        vmax = np.abs(loadings).max()
        im = ax.imshow(loadings, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
        if annotate:
            _annotate_heatmap(im, valfmt="{x:.2f}", threshold=0.2)
        ax.set_yticks(np.arange(len(feature_names)))
        if ax.get_subplotspec().is_first_col():
            ax.set_yticklabels(feature_names)
        else:
            ax.set_yticklabels([])
        ax.set_title(str(method))
        ax.set_xticks(range(fa.n_factors))
        ax.set_xticklabels(
            [f"Factor {i}" for i in range(1, fa.n_factors + 1)], rotation=45
        )
    fig.suptitle("Loadings-matrix")
    plt.tight_layout()
    return axes


def create_corr_heatmap(X, triangular=False, is_corr_mtx=False, annotate=True):
    """
    Plot the correlation matrix of `X` as a heatmap.

    Parameters
    ----------
    X : array_like, shape (n_samples, n_features) or (n_features, n_features)
        The samples from which the correlation matrix is calculated or
        the correlation matrix itself if `is_corr_mtx=True`
    triangular : bool, default=False
        If True, then only plot the lower-triangular part of the correlation
        matrix.
    annotate: bool, default=True
        If True, then annotate the heatmap with the corresponding correlations.
    is_corr_mtx : bool, default=False
        If set to True, then X is treated as a correlation matrix.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object with the heatmap.
    """
    X = pd.DataFrame(X)
    if not is_corr_mtx:
        corr = X.corr()
    else:
        corr = X
    if triangular:
        mask = np.ones_like(corr)
        mask = np.triu(mask)
    else:
        mask = np.zeros_like(corr)
    hm = sns.heatmap(
        data=corr, vmax=1, vmin=-1, cmap="RdBu_r", mask=mask, annot=annotate
    )
    return hm


def _annotate_heatmap(
    im,
    data=None,
    valfmt="{x:.2f}",
    textcolors=("black", "white"),
    threshold=None,
    **textkw,
):
    """Annotate the given heatmap.

    Note: This function has been copied (with a minor modification) from
    https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt : string, default="{x:.2f}"
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors : 2-tuple of color, default: ("black", "white")
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold: float, default: None
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    kwargs: Any
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max()) / 2.0

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(np.abs(data[i, j])) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
