"""Wire the supplied Pizza Panic functions into a Kedro graph."""

from kedro.pipeline import Pipeline, node

from .nodes import prepare_features, search_candidates, split_data


def create_pipeline(**kwargs) -> Pipeline:
    """Build three nodes using the contracts in INTEGRATION_TEMPLATE.md.

    Raw catalog inputs -> pizza_features -> pizza_split -> results + models.
    Pass configuration with params: inputs; do not call the functions here.
    Give every node a descriptive unique name.
    """
    return Pipeline(
        [
            node(
                func=prepare_features,
                inputs=["pizza_orders", "pizza_restaurants"],
                outputs="pizza_features",
                name="pizza_prepare_features_node",
            ),
            node(
                func=split_data,
                inputs=["pizza_features", "params:pizza_settings"],
                outputs="pizza_split",
                name="pizza_split_data_node",
            ),
            node(
                func=search_candidates,
                inputs=["pizza_split", "params:pizza_settings", "params:pizza_selection"],
                outputs=["pizza_results", "pizza_models"],
                name="pizza_search_candidates_node",
            ),
        ]
    )
