import pytest
from model.vk_user.regular_expression import regular_search, PATTERNS_CITY


class TestRegular:

    @pytest.mark.parametrize("city_write_users", [
        "*Смоленск",
        "*Москва",
        "*Владимир",
        "*sdfsfd",
    ])
    def test_check_city(self, city_write_users):
        assert regular_search(PATTERNS_CITY, city_write_users), 'error'
