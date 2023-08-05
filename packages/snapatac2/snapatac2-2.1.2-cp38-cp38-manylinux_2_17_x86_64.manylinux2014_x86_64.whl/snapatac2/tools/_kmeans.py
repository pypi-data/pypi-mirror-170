from typing import Optional, Union, Type
import numpy as np
import polars

from snapatac2._snapatac2 import AnnData, AnnDataSet
import snapatac2._snapatac2 as _snapatac2

def kmeans(
    adata: Union[AnnData, AnnDataSet, np.ndarray],
    n_clusters: int,
    n_iterations: int = -1,
    random_state: int = 0,
    use_rep: Optional[str] = None,
    key_added: str = 'kmeans',
    inplace: bool = True,
) -> None:
    """
    Cluster cells into subgroups using the K-means algorithm.

    Parameters
    ----------
    adata
        The annotated data matrix.
    n_clusters
        Number of clusters to return.
    n_iterations
        How many iterations of the kmeans clustering algorithm to perform.
        Positive values above 2 define the total number of iterations to perform,
        -1 has the algorithm run until it reaches its optimal clustering.
    random_state
        Change the initialization of the optimization.
    use_rep
        Which data in `adata.obsm` to use for clustering. Default is "X_spectral".
    key_added
        `adata.obs` key under which to add the cluster labels.

    Returns
    -------
    adds fields to `adata`:
    `adata.obs[key_added]`
        Array of dim (number of samples) that stores the subgroup id
        (`'0'`, `'1'`, ...) for each cell.
    `adata.uns['kmeans']['params']`
        A dict with the values for the parameters `n_clusters`, `random_state`,
        and `n_iterations`.
    """
    if use_rep is None: use_rep = "X_spectral"

    if isinstance(adata, AnnData) or isinstance(adata, AnnDataSet):
        data = adata.obsm[use_rep]
    else:
        data = adata
    groups = _snapatac2.kmeans(n_clusters, data)
    groups = np.array(groups, dtype=np.compat.unicode)
    if inplace:
        adata.obs[key_added] = polars.Series(
            groups,
            dtype=polars.datatypes.Categorical,
        )
        # store information on the clustering parameters
        #adata.uns['kmeans'] = {}
        #adata.uns['kmeans']['params'] = dict(
        #    n_clusters=n_clusters,
        #    random_state=random_state,
        #    n_iterations=n_iterations,
        #)

    else:
        return groups