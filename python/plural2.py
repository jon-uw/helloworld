# read plural rule from a file then return the plural format of a noun

import re

DEFAULT_RULE_FILE = 'plural_rules.txt' # space delemilated
# closure
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield (build_match_and_apply_functions(
                pattern, search, replace))      # this is magic


def plural(noun, rules_filename=DEFAULT_RULE_FILE):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('No matching rule for {0}'.format(noun))

print(plural('abc'))

