def check_element_state(element, state: str) -> bool:
    state = state.lower()
    if any([e in state for e in ['selected', 'checked']]):
        result = element.is_selected()
    elif any([e in state for e in ['displayed', 'visible']]):
        result = element.is_displayed()
    elif any([e in state for e in ['enabled', 'disabled']]):
        result = element.is_enabled()
        if 'disabled' in state:
            if element.get_attribute('disabled') == 'true':
                result = True
            else:
                result = not result
    elif 'active' in state:
        # check for active/inactive using class attribute
        ele_class = element.get_attribute('class')
        if 'inactive' in state:
            result = 'inactive' in ele_class
        else:
            result = ('active' in ele_class) and ('inactive' not in ele_class)
    else:
        raise Exception(f'Unhandled state: {state}')
    if 'not' in state:
        result = not result
    return result