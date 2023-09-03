import click as ck
import pandas as pd
import matplotlib.pyplot as plt


ck.command()
ck.argument('input', 
    type=ck.Path(
        exists=True,
        file_okay=True,
        readable=True))
def qreport(input):
    """
    qreport generates a graph from the input CSV file
    """

if __name__ == "__main__":
    qreport()