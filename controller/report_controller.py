import os
import pandas as pd


def generate_csv_report(results):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    df = pd.DataFrame(results)

    df.to_csv(
        "reports/document_summary_report.csv",
        index=False
    )