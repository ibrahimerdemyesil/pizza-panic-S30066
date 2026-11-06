"""Register the project's named pipelines."""

from kedro.pipeline import Pipeline

from highrev.pipelines.pizza_panic import pipeline as pizza_panic_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Session 05 base project plus the Pizza Panic bonus graph."""
    default = Pipeline([])
    return {
        "__default__": default,
        "pizza_panic": pizza_panic_pipeline.create_pipeline(),
    }
