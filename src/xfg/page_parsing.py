import logging
from bs4 import BeautifulSoup
soup_parser = "html5lib"
try:
    import html5lib
except ImportError:
    soup_parser = "html.parser"


def parse_module_forms(form_soup):
    section = form_soup.select_one("h2").string
    logging.debug(f"Form Name: {section}")
    data = {}
    for row in form_soup.find_all("div", class_="form-row"):
        key = row.findChild("span", class_="readonlyLabel").string
        value = row.findChild("span", class_="value").string
        try:
            data[key] = value.strip()
        except AttributeError:
            logging.debug(f"Key: {key} has no value!")
            continue
    return {section: data}


def parse_module_tables(form_soup):
    data = []
    table = form_soup.select_one("table")
    try:
        table_header = table.select_one("thead > tr > td > div").string
    except AttributeError:
        table_header = table.select_one("thead > tr > td").string
    logging.debug(f"Table Header: {table_header}")
    headers = [header.text.strip() for header in table.select('th')]
    for ri, row in enumerate(table.select('tbody > tr')):
        for ci, cell in enumerate(row.select('td')):
            header = headers[ri]
            text = cell.get_text().strip()
            # If this is the first row we've come across, need to initialize our list of items
            # by appending our initial dict
            # After that we can just use the index to update the dict for this "column"
            if ri == 0:
                data.append({header:text})
            else:
                data[ci][header] = text
    return {table_header: data}


def parse_tables(html_content):
    soup = BeautifulSoup(html_content, soup_parser)
    stat_content = soup.select_one("#content")
    stats = {}

    for form in stat_content.select(".module"):
        classes = form.attrs.get("class", [])
        if not classes:
            continue
        logging.debug(f"Classes: {classes}")
        # For classes of "module forms", this is mostly static data
        # Generally uptime, addresses, versions, etc...
        if len(classes) == 2 and "forms" in classes:
            data =  parse_module_forms(form)
            if data:
                stats.update(data)
        # For classes of "modules" that just have tables of dynamic data
        # This is where power levels and such are
        if len(classes) == 1:
            data = parse_module_tables(form)
            if data:
                stats.update(data)
    return stats
