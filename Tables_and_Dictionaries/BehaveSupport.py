def table_column_to_list_of_dicts(table):
    """
    return list of table rows dicts

    [{'Head1': 'Cell1_1', 'Head2': 'Cell1_2'},
     {'Head1': 'Cell2_1', 'Head2': 'Cell2_2'}]
    """
    result = []
    for row in table.rows:
        result.append(dict(row.items()))
    return result