import tempfile
import unittest
from pathlib import Path
from main import pack_svgs

class SpritePackTests(unittest.TestCase):
    def test_packs_symbols(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"arrow-left.svg"
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5 12h14"/></svg>', encoding="utf-8")
            result = pack_svgs([path])
            self.assertIn('id="arrow-left"', result)
            self.assertIn("<path", result)

if __name__ == "__main__":
    unittest.main()
