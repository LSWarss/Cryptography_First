from click.testing import CliRunner
import CaesarCommandLineTool as cli

runner = CliRunner()

def test_cli_hello():
    result = runner.invoke(cli.hello)
    assert result.output == "Hello, this is encoding and decoding CLI tool for Caesar code 📜\n"
    assert result.exit_code == 0

def test_cli_encode():
    result = runner.invoke(cli.encode, ['lukaszstachnik'])
    assert result.output == 'nwmcubuvcejpkm\n'
    assert result.exit_code == 0

def test_cli_decode():
    result = runner.invoke(cli.decode, ['nwmcubuvcejpkm'])
    assert result.output == 'lukaszstachnik\n'
    assert result.exit_code == 0