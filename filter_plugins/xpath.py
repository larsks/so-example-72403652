import lxml.etree
import xmltodict


def xpath_filter(v, expr):
    tree = lxml.etree.fromstring(v)
    res = tree.xpath(expr)
    return res


def xmltostring_filter(v):
    return lxml.etree.tostring(v)


def xmltodict_filter(v):
    return xmltodict.parse(v)


class FilterModule:
    def filters(self):
        return {
            "xpath": xpath_filter,
            "xmltostring": xmltostring_filter,
            "xmltodict": xmltodict_filter,
        }
