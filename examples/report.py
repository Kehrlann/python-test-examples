from datetime import datetime
from os import PathLike


def generate_report(report_dir: PathLike, enable_logs: bool = False) -> None:
    with open(report_dir / 'report.txt', 'w+') as f:
        f.writelines(
            [
                'Report content:',
                'Some gibberish',
                f"Date: {datetime.now()}",
                "total: 1337"
            ]
        )

    if enable_logs:
        with open(report_dir / 'logs.txt', 'w') as f:
            f.writelines(
                [
                    'logging stuff',
                    'bye bye'
                ]
            )
