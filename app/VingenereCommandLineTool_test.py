from click.testing import CliRunner
import VingenereCommandLineTool as cli

runner = CliRunner()

def test_cli_hello():
    result = runner.invoke(cli.hello)
    assert result.output == "Hello, this is encoding and decoding CLI tool for Vingenere cipher 📜\n"
    assert result.exit_code == 0

def test_cli_encode():
    result = runner.invoke(cli.encode, ['The quick brown fox jumps over 13 lazy dogs.'])
    assert result.output == f'{str.upper("nloqnwysdviaxfhlfcotmsfekzwhahikc")}\n'
    assert result.exit_code == 0

def test_cli_decode():
    result = runner.invoke(cli.decode, [str.upper("nloqnwysdviaxfhlfcotmsfekzwhahikc")])
    assert result.output == f'{str.upper("thequickbrownfoxjumpsoverlazydogs")}\n'
    assert result.exit_code == 0