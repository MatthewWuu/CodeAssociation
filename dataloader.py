from ply import lex, yacc
import dataset
import torch.utils.data as data
import torch.utils

# CppDataset =


# 定义词法单元
tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()

# 定义语法规则
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    # 在这里处理标识符
    p[0] = p[1]

def p_error(p):
    print("Syntax error")

# 构建语法分析器
parser = yacc.yacc()

# 从本地文件读取 C++ 代码
file_path = './CodeNet_C++1000/p00000/s035670593.cpp'
with open(file_path, 'r') as file:
    cpp_code = file.read()

# 解析代码
lexer.input(cpp_code)
for tok in lexer:
    print(tok)

result = parser.parse(cpp_code)
print(result)
