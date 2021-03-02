import click
from VingenereCoder import VingenereCoder


@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello, this is encoding and decoding CLI tool for Vingenere cipher 📜")

@cli.command()
@click.option('--keyword', default="uekatowice", help='Keyword for the Vingenere cipher, default is: uekatowice')
@click.argument('text')
def encode(keyword, text):
    coder = VingenereCoder(keyword)
    click.echo(coder.encode(text))

@cli.command()
@click.option('--keyword', default="uekatowice", help='Keyword for the Vingenere cipher, default is: uekatowice')
@click.argument('text')
def decode(keyword, text):
    coder = VingenereCoder(keyword)
    click.echo(coder.decode(text))

if __name__ == '__main__':
    cli()