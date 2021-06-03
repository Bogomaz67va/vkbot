import pytest
from model.keyboard.keyboard import button_bot, button_bot_age, button_bot_status


class TestKeyboard:
    @pytest.mark.parametrize("button_name", [
        "hello",
        "search",
        "test",
    ])
    def test_check_button_bot(self, button_name):
        assert button_bot(button_name), "error"
        assert button_bot(button_name, button_name), "error"
        assert button_bot(button_name, button_name, button_name), "error"

    @pytest.mark.parametrize("button_name_age", [
        "hello",
        "search",
        "test",
    ])
    def test_check_button_bot_age(self, button_name_age):
        assert button_bot_age(button_name_age, button_name_age, button_name_age, button_name_age,
                              button_name_age), "error"

    @pytest.mark.parametrize("button_name_status", [
        "hello",
        "search",
        "test",
    ])
    def test_check_button_bot_status(self, button_name_status):
        assert button_bot_status(button_name_status, button_name_status, button_name_status,
                                 button_name_status), "error"
