from typing import TypedDict

class Tokens(TypedDict):
    discord: str

class Options(TypedDict):
    prefixes: str
    
class Ides(TypedDict):
    owner_userid: int
    
class Config(TypedDict):
    TOKENS: Tokens
    OPTIONS: Options
    IDES: Ides