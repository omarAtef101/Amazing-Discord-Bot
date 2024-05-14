from typing import TypedDict

class Tokens(TypedDict):
    discord: str

class Options(TypedDict):
    prefixes: str
    logging: int
    
class Ides(TypedDict):
    owner_userid: int
    
class Config(TypedDict):
    TOKENS: Tokens
    OPTIONS: Options
    IDES: Ides