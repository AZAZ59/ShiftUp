from Utils.Table import Table


def get_short_result(result, limit=50):
    limit = min((len(result), limit))
    if limit == 0:
        return result
    else:
        result_type = result[0].get('type', None)
        if result_type is None:
            return result
        else:
            return result[:limit]


