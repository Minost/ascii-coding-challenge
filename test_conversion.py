from main import convert_ascii_character


class TestConversion:
    def test_convert_ascii_character_valid(self):
        assert convert_ascii_character('g') == 1030

    def test_convert_ascii_character_limit(self):
        assert convert_ascii_character('h') == 0

    def test_convert_ascii_character_invalid(self):
        assert convert_ascii_character('i') == 0

    def test_convert_ascii_character_special(self):
        assert convert_ascii_character('@') == 640
