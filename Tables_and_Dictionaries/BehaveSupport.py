"""
This set of functions extends default Behave table operations
in the way of transforming Table object into smth more native
"""


def context_variable_to_custom_layer(context, new_attribute, value, custom_layer='feature'):
    # identify stack layer
    layer = next(layer for layer in context._stack if layer['@layer'] == custom_layer)
    # push variable to layer
    layer[new_attribute] = value


def context_get_variable_from_custom_layer(context, attribute, custom_layer='feature'):
    # identify stack layer
    layer = next(layer for layer in context._stack if layer['@layer'] == custom_layer)
    # get variable from layer
    if attribute in layer:
        return layer[attribute]


def context_delete_variable_from_custom_layer(context, attribute, custom_layer='feature'):
    # identify stack layer
    layer = next(layer for layer in context._stack if layer['@layer'] == custom_layer)
    # delete variable if exists
    if attribute in layer:
        del layer[attribute]


def table_column_to_list(table, column_index=0):
    """
    return column as a flat list (['Head1', 'Cell1', 'Cell2',...])

    :param table:           context.table
    :param column_index:    optional arg to work on specific column
    """
    result = [table.headings[column_index]]
    for row in table.rows:
        result.append(row.cells[column_index])
    return result


def table_to_list_of_lists(table):
    """
    return rows as a list of lists ([['Head1', 'Head2', ...],
                                     ['Col1', 'Col2', ...],
                                     ['Col1', 'Col2', ...]])

    :param table:           context.table
    """
    result = [table.headings]
    for row in table.rows:
        result.append(row.cells)
    return result


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


def table_to_flat_dict(table):
    """
    return flat dict from first 2 columns

    {'Head1': 'Head2',
     'Cell1': 'Cell2',
     ...}
    """

    if len(table.headings) < 2:
        raise ValueError('Too few columns to construct flat dictionary. Expected 2')
    result = {table.headings[0]:table.headings[1]}
    for row in table.rows:
        result[row.cells[0]] = row.cells[1]
    return result


def item_in_context(context, item):
    """
    :return: Boolean based on presents of item in current context
    """
    behave_layered_vars = vars(context)['_stack']
    return any(item in layer.keys() for layer in behave_layered_vars)


def table_to_dict_with_lists(table):
    """
    return dict with lists with sorted values from 2 columns table
    List values divided by ';'

    {'Head1': ['Head2'],
     'Cell1': ['Cell2'],
     ...}
    """

    if len(table.headings) < 2:
        raise ValueError('Too few columns to construct flat dictionary. Expected 2')
    result = {table.headings[0]: sorted(table.headings[1].split('; '),  key=str.casefold)}
    for row in table.rows:
        result[row.cells[0]] = sorted(row.cells[1].split('; '),  key=str.casefold)
    return result


def table_to_flat_dict_without_headers(table):
    """
    returns dict from first 2 columns

    {'Cell1_1': 'Cell1_2',
     'Cell2_1': 'Cell2_2',
     ...}
    """
    if len(table.headings) < 2:
        raise ValueError('Too few columns to construct flat dictionary. Expected 2')
    result = {}
    for row in table.rows:
        result[row.cells[0]] = row.cells[1]
    return result


def table_to_nested_dict(table):
    """
    Table like this

    | key     | type   | status   |
    | Outlet  | button | disabled |
    | Daypart | input  | required |
    ...
    returns dict where values in first column are the keys
    and the rest goes into nested dict like:
    {'Outlet': {'type':'button', 'status':'disabled'},
     'Daypart': {'type':'input', 'status':'required'},
     ...}
    """
    if len(table.headings) < 2:
        raise ValueError('Too few columns to construct nested dictionary. Expected 2+')
    main, nested = {}, {}
    for row in table.rows:
        main[row[0]] = nested
        for cell_count, cell in enumerate(row):
            if cell_count == 0:
                continue
            nested.update({table.headings[cell_count]: cell})
        nested = {}
    return main


def replace_values_by_context(context, v):
    return getattr(context, v.split('.')[-1]) if 'context.' in v and hasattr(context, v.split('.')[-1]) else v


def get_context_vars(context, var_name):
    """triage between value and list of values to prep for replace_values_by_context method"""
    if isinstance(var_name, list):
        return [replace_values_by_context(context, val) for val in var_name]
    else:
        return replace_values_by_context(context, var_name)


def convert_context_variables_in_scenario_outline_example_tables(context, feature):
    for s in range(len(feature.scenarios)):
        if hasattr(feature.scenarios[s], 'examples'):
            for e in range(len(feature.scenarios[s].examples)):
                for r in range(len(feature.scenarios[s].examples[e].table.rows)):
                    feature.scenarios[s].examples[e].table.rows[r].cells = \
                        get_context_vars(context, feature.scenarios[s].examples[e].table.rows[r].cells)


