import re as regex


class Token:

    type: str
    value: str
    full_match: str
    start: int
    end: int

    def __init__(self, type: str, value: str, full_match: regex.Match, start: int, end: int):
        self.type = type
        self.value = value
        self.full_match = full_match
        self.start = start
        self.end = end

    def __str__(self):
        return f"Token[ type = {self.type}, value = {self.value}, start = {self.start}, end = {self.end} ]"


class TokenIdentifier:

    regex: str
    group: int
    type: str

    def __init__(self, token_type, regex, group = 0, has_sub_tokens = False):
        self.regex = regex if regex.startswith("^") else f"^{regex}"
        self.type = token_type
        self.group = group
        

class TokenizableLanguage:

    identifiers: list[TokenIdentifier]
    default_identifiers = [
        TokenIdentifier("left parentheses", r"^\("),
        TokenIdentifier("right parentheses", r"^\)"),
        TokenIdentifier("left brace", r"^\{"),
        TokenIdentifier("right brace", r"^\}"),
        TokenIdentifier("semicolon", r"^;"),
        TokenIdentifier("left bracket", r"^\["),
        TokenIdentifier("right bracket", r"^\]"),
        TokenIdentifier("dot", r"^\."),
        TokenIdentifier("colon", r"^:"),
        TokenIdentifier("number", r"^-?\d+(\.\d+)?"),
        TokenIdentifier("operation", r"^(=(==?)?\+|-|\*|/|%|&&?|\|\|?|!)", 1),
        TokenIdentifier("string", r'^"([^"]|\\")*"'),
        TokenIdentifier("constant", r"^[A-Z]+\b"),
        TokenIdentifier("class name", r"^[A-Z](\w)*\b"),
        TokenIdentifier("function", r"^([A-Za-z_]\w*)\s*\(", 1),
        TokenIdentifier("identifier", r"^[a-z_]\w*\b"),
        TokenIdentifier("whitespace", r"^\s+"),
        TokenIdentifier("newline", r"^\n+"),
        TokenIdentifier("comment", r"^//[^\n]*"),
        TokenIdentifier("star", r"^\*"),
        TokenIdentifier("spread", "...")
    ]

    def __init__(self, identifiers: list[TokenIdentifier]):
        id_dict = {}
        for default_identifier in TokenizableLanguage.default_identifiers:
            id_dict[default_identifier.type] = default_identifier
        for identifier in identifiers:
            id_dict[identifier.type] = identifier
        self.identifiers = list(id_dict.values()).reverse()
                    

    def tokenize(self, code) -> list[Token]:
        tokens = []
        pos = 0
        while(code):
            match_found = False
            while(code.startswith("\n")):
                code = code[1:]
            for identifier in self.identifiers + TokenizableLanguage.default_identifiers:
                match = regex.match(identifier.regex, code)
                if (match):
                    str_match = match.group(identifier.group)
                    token = Token(
                        type = identifier.type, 
                        value = match.group(identifier.group),
                        full_match = match,
                        start = pos,
                        end = pos + len(str_match)
                    )
                    code = code[len(str_match):]
                    pos += len(str_match)
                    tokens.append(token)
                    match_found = True
                    break
            if not match_found: raise Exception("No match found: " + code)
        return tokens


# Assembly

C = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b"),
    ]
)

Cpp = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(alignas|alignof|and|and_eq|asm|atomic|cancel|atomic|commit|atomic|noexcept|auto|bitand|bitor|bool|break|case|catch|char|char8_t|char16_t|char32_t|class|compl|concept|const|consteval|constexpr|constinit|const_cast|continue|co_await|co_return|co_yield|decltype|default|delete|do|double|dynaimc_cast|else|enum|explicit|export|extern|false|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|noexcept|not|not_eq|nullptr|operator|or|or_eq|private|protected|public|reflexpr|register|reinterpret_cast|requires|return|short|signed|sizeof|static|static_assert|static_cast|struct|switch|synchronized|template|this|thread_local|throw|true|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|wchar_t|while|xor|xor_eq)\b"),
    ]
)

CSharp = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(abstract|as|base|bool|break|byte|case|catch|char|checked|class|const|continue|decimal|default|delegate|do|double|else|enum|event|explicit|extern|false|finally|fixed|float|for|foreach|goto|if|implicit|in|int|interface|internal|is|lock|long|namespace|new|null|object|operator|out|override|params|private|protected|public|readonly|ref|return|sbyte|sealed|short|sizeof|stackalloc|static|string|struct|switch|this|throw|true|try|typeof|uint|ulong|unchecked|unsafe|ushort|using|using|static|void|volatile|while)\b"),
    ]
)

Go = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(break|case|chan|const|continue|default|defer|else|fallthrough|for|func|go|goto|if|import|interface|map|package|range|return|select|struct|switch|type|var)\b"),
    ]
)

Haskell = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(case|class|data|default|deriving|do|else|forall|if|import|in|infix|infixl|infixr|instance|let|module|newtype|of|qualified|then|type|where|_|foreign|ccall|as|safe|unsafe`)\b")
    ]
)

Java = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(abstract|assert|boolean|break|byte|case|catch|char|class|continue|default|do|double|else|enum|extends|final|finally|float|for|if|implements|import|instanceof|int|interface|long|native|new|null|package|public|return|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|void|volative|while)\b", 1),
    ]
)

JavaScript = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(as|break|case|catch|class|const|constructor|continue|debugger|default|delete|do|else|enum|export|extends|false|finally|for|from|function|get|if|import|in|instanceof|new|let|module|null|of|return|set|super|static|string|switch|this|throw|true|try|var|while|with|yield)\b"),
    ]
)

Lua = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(and|break|do|else|elseif|end|false|for|function|if|in|local|nil|not|or|repeat|return|then|true|until|while)\b")
    ]
)

Python = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b"),
        TokenIdentifier("comment", r"#[^\n]*"),
    ]
)

Ruby = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(__ENCODING__|__LINE|__FILE__|BEGIN|END|alias|and|begin|break|case|class|def|defined|do|else|elsif|end|ensure|false|for|if|in|module|next|nil|not|or|redo|rescue|retry|return|self|super|then|trueundef|unless|until|when|while|yield)\b")
    ]
)

Rust = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(as|async|await|break|consts|continue|crate|dyn|else|enum|extern|false|fn|for|if|impl|in|let|loop|match|mod|move|mut|pub|ref|return|self|Self|static|struct|super|trait|true|type|unsafe|use|where|while)\b")
    ]
)

SQL = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(ADD|ALL|ALTER|AND|ANY|AS|ASC|BACKUP|BETWEEN|CASE|CHECK|COLUMN|CONSTRAINT|CREATE|DATABASE|INDEX|OR|REPLACE|VIEW|TABLE|PROCEDURE|UNIQUE|INDEX|DEFAULT|DELETE|DESC|DISTINCT|DROP|EXEC|EXISTS|FOREIGN|KEY|FROM|FULL|OUTER|JOIN|GROUP|BY|HAVING|IN|INNER|JOIN|INSERT|INTO|SELECT|IS|NULL|NOT|LEFT|LIKE|LIMIT|NOT|OR|ORDER|OUTER|PRIMARY|PROCEDURE|RIGHT|ROWNUM|INTO|TOP|SET|TABLE|TOP|TRUNCATE|UNION|ALL|UPDATE|VALUES|WHERE)\b")
    ]
)

TypeScript = TokenizableLanguage(
    identifiers = [
        TokenIdentifier("keyword", r"(any|as|boolean|break|case|catch|class|const|constructor|continue|debugger|declare|default|delete|do|else|enum|export|extends|false|finally|for|from|function|get|if|implements|import|in|instanceof|interface|new|let|module|null|number|of|private|protected|public|require|return|set|super|static|string|switch|symbol|this|throw|true|try|type|typeof|var|void|while|with|yield)\b"),
    ]
)

# XML