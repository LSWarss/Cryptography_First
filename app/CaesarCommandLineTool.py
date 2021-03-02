import click
from CaesarCoder import CaesarCoder
from CodeCracking import maunal_caesar_cracking, getTheLowestEntropy

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello, this is encoding and decoding CLI tool for Caesar code 📜")

@cli.command()
@click.option('--stride', default=2, help='Stride number for Caesar encoding')
@click.argument('text')
def encode(stride, text):
    coder = CaesarCoder(stride)
    click.echo(coder.encode(text))

@cli.command()
@click.option('--stride', default=2, help='Stride number for Caesar encoding')
@click.argument('text')
def decode(stride, text):
    coder = CaesarCoder(stride)
    click.echo(coder.decode(text))

@cli.command()
def maunal_cracking():
    maunal_caesar_cracking()
    
@cli.command()
@click.argument('text')
def automatic_cracking(text):
    getTheLowestEntropy(text)


if __name__ == '__main__':
    cli()