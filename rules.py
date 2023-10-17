import re 

class Rules:
    @staticmethod
    def regex_pattern(self) -> str:
        pass
    
    def match_token(self, content) -> str: 
        match = re.match(self.pattern, content)
        return f'<Token object; class="{self.token}" match="{match.group()}">'

    def __str__(self):
        return f'<Rule object; class="{self.token}" pattern="{self.pattern}">'  
    



class NumberConstantRule(Rules):
    token = "NUMERICAL"
    pattern = r'[0-9]+\.?[0.9]*'
    
    @staticmethod
    def regex_pattern() -> str:
        Pattern = re.compile(NumberConstantRule.pattern)
        return Pattern

class IdentifierRule(Rules):
    token = "IDENTIFIER"
    pattern = r'[a-zA-Z_][a-zA-Z0-9]*'

    @staticmethod
    def regex_pattern() -> str:
        Pattern = re.compile(IdentifierRule.pattern)
        return Pattern
        
class SymbolRule(Rules):
    token = "SYMBOL"
    pattern = r'[$&+,:;=?@#|<>.^*()%!-]'

    @staticmethod
    def regex_pattern() -> str:
        Pattern = re.compile(SymbolRule.pattern)
        return Pattern
