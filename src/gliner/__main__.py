"""Command-line interface."""
from typing import Any, List
import click
import argparse
from gliner.model import GLiNER



# @click.version_option results in "untyped decorator" error
# https://github.com/python/typeshed/issues/5642


@click.command()
@click.version_option()  # type: ignore[misc]
def main() -> List[Any]:
    """Gliner."""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="The text to predict entities from")
    parser.add_argument("labels", type=str, help="The labels to predict")
    args = parser.parse_args()
    # parse args and raise ValueError if not found
    if not args.text:
        raise ValueError("text is required")
    if not args.labels:
        raise ValueError("labels is required")
    text, labels = args.text, args.labels
    # load the model
    model = GLiNER.from_pretrained("urchade/gliner_multi")



    entities = model.predict_entities(text, labels)

    return entities


if __name__ == "__main__":
    main(prog_name="gliner")  # pragma: no cover
