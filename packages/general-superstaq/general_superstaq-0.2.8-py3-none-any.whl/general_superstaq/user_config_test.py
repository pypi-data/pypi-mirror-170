import os
import secrets
import tempfile
from unittest import mock

import pytest

import general_superstaq as gss


def test_service_get_balance() -> None:
    client = gss.superstaq_client._SuperstaQClient(
        remote_host="http://example.com", api_key="key", client_name="general_superstaq"
    )
    service = gss.user_config.UserConfig(client)
    mock_client = mock.MagicMock()
    mock_client.get_balance.return_value = {"balance": 12345.6789}
    service._client = mock_client

    assert service.get_balance() == "$12,345.68"
    assert service.get_balance(pretty_output=False) == 12345.6789


@mock.patch(
    "general_superstaq.superstaq_client._SuperstaQClient.ibmq_set_token",
    return_value={"status": "Your IBMQ account token has been updated"},
)
def test_ibmq_set_token(mock_ibmq: mock.MagicMock) -> None:
    client = gss.superstaq_client._SuperstaQClient(
        remote_host="http://example.com", api_key="key", client_name="general_superstaq"
    )
    service = gss.user_config.UserConfig(client)
    assert service.ibmq_set_token("valid token") == {
        "status": "Your IBMQ account token has been updated"
    }


@mock.patch(
    "general_superstaq.superstaq_client._SuperstaQClient.aqt_upload_configs",
    return_value={"status": "Your AQT configuration has been updated"},
)
def test_service_aqt_upload_configs(mock_aqt_compile: mock.MagicMock) -> None:
    client = gss.superstaq_client._SuperstaQClient(
        remote_host="http://example.com", api_key="key", client_name="general_superstaq"
    )
    service = gss.user_config.UserConfig(client)
    tempdir = tempfile.gettempdir()
    pulse = secrets.token_hex(nbytes=16)
    variable = secrets.token_hex(nbytes=16)
    with open(f"{tempdir}/{pulse}.yaml", "w") as pulses_file:
        pulses_file.write("Hello")
    with open(f"{tempdir}/{variable}.yaml", "w") as variables_file:
        variables_file.write("World")

    assert service.aqt_upload_configs(f"{tempdir}/{pulse}.yaml", f"{tempdir}/{variable}.yaml") == {
        "status": "Your AQT configuration has been updated"
    }
    os.remove(f"{tempdir}/{pulse}.yaml")
    os.remove(f"{tempdir}/{variable}.yaml")


@mock.patch(
    "general_superstaq.superstaq_client._SuperstaQClient.aqt_get_configs",
    return_value={"pulses": "Hello", "variables": "World"},
)
def test_service_aqt_get_configs(mock_aqt_compile: mock.MagicMock) -> None:
    client = gss.superstaq_client._SuperstaQClient(
        remote_host="http://example.com", api_key="key", client_name="general_superstaq"
    )
    service = gss.user_config.UserConfig(client)
    tempdir = tempfile.gettempdir()
    pulses_file = secrets.token_hex(nbytes=16)
    variables_file = secrets.token_hex(nbytes=16)

    service.aqt_download_configs(
        f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml"
    )

    with open(f"{tempdir}/{pulses_file}.yaml", "r") as file:
        assert file.read() == "Hello"

    with open(f"{tempdir}/{variables_file}.yaml", "r") as file:
        assert file.read() == "World"

    with pytest.raises(ValueError, match="exist"):
        service.aqt_download_configs(
            f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml"
        )

    service.aqt_download_configs(
        f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml", overwrite=True
    )

    with pytest.raises(ValueError, match="exists"):
        os.remove(f"{tempdir}/{pulses_file}.yaml")
        service.aqt_download_configs(
            f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml"
        )

    os.remove(f"{tempdir}/{variables_file}.yaml")

    with pytest.raises(ValueError, match="exists"):
        service.aqt_download_configs(
            f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml"
        )
        os.remove(f"{tempdir}/{variables_file}.yaml")
        service.aqt_download_configs(
            f"{tempdir}/{pulses_file}.yaml", f"{tempdir}/{variables_file}.yaml"
        )
