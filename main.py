import click
from dxd.tools.cli import dxd_cli
from dxc.tools.cli import dxc_cli
# Import other CLIs as they are created
# from dx.tools.cli import dx_cli
# from maths.tools.cli import maths_cli
# from vdx.tools.cli import vdx_cli

@click.group()
def main_cli():
    """
    🚀 Dexa Language Toolchain
    
    A unified CLI for compiling, rendering, and converting all Dexa formats.
    """
    pass

@main_cli.command()
@click.argument('source_file', type=click.Path(exists=True))
@click.option('--out', '-o', type=click.Path(), help="Output file path for the compiled .dex binary.")
def compile(source_file, out):
    """Compiles a .daxa file to the binary .dex format."""
    click.echo(f"Compiling {source_file}...")
    # TODO: Import and use the daxa.compiler
    click.echo("Compilation complete (simulation).")
    if out:
        click.echo(f"Output saved to {out}")

# Add sub-commands for each format
main_cli.add_command(dxd_cli, name="dxd")
main_cli.add_command(dxc_cli, name="dxc")
# main_cli.add_command(dx_cli, name="dx")
# main_cli.add_command(maths_cli, name="maths")
# main_cli.add_command(vdx_cli, name="vdx")


if __name__ == "__main__":
    main_cli()