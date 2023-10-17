import re 
from rules import *

# content = "The quick grey fox jumps over the lazy brown dog"
# content = "3.14" 
# content = "There is 3 turtles on the sea"
content = '52132 + )23(())))) - x * 3'

rules : list[Rules] = [
    NumberConstantRule, 
    IdentifierRule, 
    SymbolRule
]

parsing = True 
while parsing:
    for rule in rules:
        pattern = re.compile(rule.regex_pattern())

        match = pattern.match(content)

        if match == None:
            continue 

        while match:
            print(f'<Content object; string="{content}" remaing="{len(content)}">')
            print(content)
            print(match)
            print(rule.match_token(rule, content))
            endpos = match.end()

            content = content[endpos:].strip()
            match = pattern.match(content)
    if len(content) == 0:
        parsing = False