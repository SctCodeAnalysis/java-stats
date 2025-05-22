"""Entry point for the Java Stats CLI."""

import click

from java_stats import JavaStats


@click.command()
@click.argument("repo_path", type=click.Path(exists=True))
@click.option("--report", default="report.xml", help="Path to the output XML file")
def main(repo_path: str, report: str):
    """
    Main function that calculates metrics for a given Java
    repository and creates report as XML file.
    """
    stats = JavaStats(repo_path)

    with open(report, "w", encoding="utf-8") as file:
        click.echo(stats.as_xml(), file=file)


if __name__ == "__main__":
    # pylint: disable=E1120
    main()
