import pytest
import cli

url = 'postgres://bob@example.com:5432/db_one'

def test_pareser_without_driver():
    #without a specified driver the parser will exit
    with pytest.raises(SystemExit):
        parser = cli.create_pareser()
        parser.parse_args([url])

def test_parser_with_driver():
    #the parser will exit if it receieves a driver without a destination
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver_and_destination():
    #the parser will not exit if it receives a driver and destiination
    parser = cli.create_parser()

    args = parser.parse_args([url, '--driver', 'local', '/some/path'])
    assert args.driver == 'lcoal'