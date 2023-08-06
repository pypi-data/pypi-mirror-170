import re
from ..util import get_page_soup


def fb_match_lineups(pageSoup=None, url: str = None) -> dict:
    """Extracts matchday squad information (formation, starters, bench) for a given match

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        dict: squad information
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find lineup object
    lineup = pageSoup.find_all("div", {"class": "lineup"})

    # Home team
    lineup_x = lineup[0].find("table").find_all("tr")
    formation_x = lineup_x[0].text
    # generate empty lists
    squad_x = []
    bench_x = []
    role = "starter"

    # iterate through each player and store status and id
    for row in lineup_x[1:]:
        if row == lineup_x[12]:
            role = "bench"
            continue

        if role == "starter":
            squad_x.append(row.find("a", href=True)["href"])
        elif role == "bench":
            bench_x.append(row.find("a", href=True)["href"])

    # Away team
    lineup_y = lineup[1].find("table").find_all("tr")
    formation_y = lineup_y[0].text
    # generate empty lists
    squad_y = []
    bench_y = []
    role = "starter"

    # iterate through each player and store status and id
    for row in lineup_y[1:]:
        if row == lineup_y[12]:
            role = "bench"
            continue

        if role == "starter":
            squad_y.append(row.find("a", href=True)["href"])
        elif role == "bench":
            bench_y.append(row.find("a", href=True)["href"])

    # pattern to extract formation
    pattern = r"\(([^)]+)\)"

    # generate dictionary
    mydict = {
        "formation_x": re.search(pattern, formation_x).group(1),
        "formation_y": re.search(pattern, formation_y).group(1),
        "squad_x": squad_x,
        "bench_x": bench_x,
        "squad_y": squad_y,
        "bench_y": bench_y,
    }

    return mydict
