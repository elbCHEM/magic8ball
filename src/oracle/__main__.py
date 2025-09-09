import click
import random
from typing import Optional
from oracle.flow import main as app


@click.command()
@click.option('--seed', type=click.INT, default=None, help="Random seed")
def main(seed: Optional[int] = None) -> None:
    if seed is not None:
        random.seed(seed)
    app()


if __name__ == '__main__':
    main()
