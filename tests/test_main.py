"""Test cases for the __main__ module."""
from typing import List
import pytest
from click.testing import CliRunner

from gliner import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def text() -> str:
    return """
        Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
    """
    
@pytest.fixture
def labels() -> List[str]:
    return ["person", "award", "date", "competitions", "teams"]

def test_main_succeeds(runner: CliRunner, text: str, labels: List[str]) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main, args=[text, labels])
    raise ValueError(result)
    assert result.exit_code == 0
