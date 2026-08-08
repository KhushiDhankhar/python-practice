import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url: str) -> None:
    """
    Fetches the published Google Doc at `doc_url`, parses the
    (x-coordinate, character, y-coordinate) table it contains, and
    prints the resulting 2D grid of characters.
    """
    points = _fetch_grid_points(doc_url)
    grid_text = _render_grid(points)
    print(grid_text)


def _fetch_grid_points(doc_url: str) -> dict:
    """
    Downloads the published doc's HTML and extracts a mapping of
    (x, y) -> character from its data table.
    """
    response = requests.get(doc_url, timeout=30)
    response.raise_for_status()
 
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if table is None:
        raise ValueError("No table found in the document.")
 
    points = {}
    rows = table.find_all("tr")
    for row in rows[1:]:  # skip the header row
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
 
        x_text = cells[0].get_text(strip=True)
        char = cells[1].get_text()  # keep as-is; don't strip whitespace chars
        y_text = cells[2].get_text(strip=True)
 
        if not x_text or not y_text:
            continue
 
        x = int(x_text)
        y = int(y_text)
        points[(x, y)] = char
 
    return points
 
 
def _render_grid(points: dict) -> str:
    """
    Builds the printable grid string from a {(x, y): char} mapping,
    filling unspecified positions with spaces.
    """
    if not points:
        return ""
 
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
 
    lines = []
    # Print from the highest y down to 0 so that y increases upward,
    # matching the orientation shown in the example document.
    for y in range(max_y, -1, -1):
        line_chars = [points.get((x, y), " ") for x in range(max_x + 1)]
        lines.append("".join(line_chars))
 
    return "\n".join(lines)
 
 
if __name__ == "__main__":
    example_url = (
        "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    )
    print_secret_message(example_url)
 