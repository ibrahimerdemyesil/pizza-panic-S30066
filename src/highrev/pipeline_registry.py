"""Register the project's named pipelines."""

from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Session 05 base project: HighRev graphs are outside this exercise copy."""
    default = Pipeline([])
    return {"__default__": default}
