def check_int(string):
    return string.isdigit()


def try_parse_float(string):
    try:
        flt = float(string)
        return flt
    except ValueError:
        return False