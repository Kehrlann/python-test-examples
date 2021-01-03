from tempfile import TemporaryDirectory
from lib.database import Database
from lib.report import generate_report
from os import path
from pathlib import Path


class TestSetupMethod():
    """
    Method setup and teardown:
    - Avant/après CHAQUE méthode de test
    - Utilisable dans toutes les méthodes de test
    - Pas de "pollution", vu que recréé à chaque fois

    Pour des opérations "courantes", peu coûteuses
    """

    def setup_method(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def teardown_method(self):
        self.test_dir.cleanup()

    def test_generate_report(self):
        report_path = self.test_path / 'report.txt'

        generate_report(self.test_path)

        assert path.isfile(report_path)
        with open(report_path, 'r') as f:
            content = f.read()
            assert "total: 1337" in content

    def test_no_logs(self):
        log_path = self.test_path / 'logs.txt'

        generate_report(self.test_path)

        assert not path.isfile(log_path)

    def test_logging_enabled(self):
        log_path = self.test_path / 'logs.txt'

        generate_report(self.test_path, enable_logs=True)

        assert path.isfile(log_path)
