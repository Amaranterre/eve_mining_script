def iter_result(result, selector, breaker=None, until=None):
    for feature in result:
        if (until is not None) and (not until(feature)):
                continue

        if selector(feature):
            return feature


        if (breaker is not None) and (breaker(feature)):
                break


def iter_resultset(result, selector, breaker=None, until=None):
    ans = []
    for feature in result:
        if (until is not None) and (not until(feature)):
                continue


        if selector(feature):
            ans.append(feature)

        if (breaker is not None) and (breaker(feature)):
                break

    return ans