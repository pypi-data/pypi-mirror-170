#!/usr/bin/env python
""" Tests covering the command-line code.
"""

from unittest import mock

from click.testing import CliRunner

import nf_core.__main__


@mock.patch("nf_core.__main__.nf_core_cli")
def test_header(mock_cli):
    """Just try to execute the header function"""
    nf_core.__main__.run_nf_core()


def test_cli_help():
    """Test the main launch function with --help"""
    runner = CliRunner()
    result = runner.invoke(nf_core.__main__.nf_core_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show the version and exit." in result.output


def test_cli_bad_subcommand():
    """Test the main launch function with verbose flag and an unrecognised argument"""
    runner = CliRunner()
    result = runner.invoke(nf_core.__main__.nf_core_cli, ["-v", "foo"])
    assert result.exit_code == 2
    # Checks that -v was considered valid
    assert "No such command" in result.output
