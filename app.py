import streamlit as st
import pandas as pd
import itertools
import random
import re


# =====================================================
# ตั้งค่าหน้าเว็บไซต์
# =====================================================

st.set_page_config(
    page_title="Math Logic Learning & Solver",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# ธีมสีฟ้าพาสเทล
# =====================================================

st.markdown("""
<style>

/* ฟอนต์และพื้นหลัง */
.stApp {
    background: #F7FCFF;
    color: #20384F;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
}

/* หัวข้อ */
h1, h2, h3 {
    color: #245A81 !important;
}

/* แถบเมนูด้านซ้าย */
[data-testid="stSidebar"] {
    background: #E3F2FD;
    border-right: 3px solid #263B50;
}

/* ข้อความในเมนู */
[data-testid="stSidebar"] * {
    font-family: sans-serif;
}

/* หัวข้อในแถบเมนู */
[data-testid="stSidebar"] h1 {
    color: #245A81 !important;
    font-weight: 800;
}

[data-testid="stSidebar"] h3 {
    color: #245A81 !important;
    font-weight: 700;
}

/* ปุ่มเมนูด้านซ้าย */
[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 46px;
    background: #BDE0FE;
    color: #20384F;
    border: 2px solid #263B50;
    border-radius: 14px;
    box-shadow: 4px 4px 0 #263B50;
    font-size: 15px;
    font-weight: 600;
    text-align: left;
    justify-content: flex-start;
    margin-bottom: 9px;
    transition: 0.2s;
}

/* เมื่อชี้เมาส์ */
[data-testid="stSidebar"] .stButton > button:hover {
    background: #89C2F9;
    color: #20384F;
    border-color: #263B50;
    transform: translateY(-2px);
}

/* ปุ่มเมนูที่เลือก */
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: #89C2F9;
    color: #142F47;
    border: 2px solid #263B50;
    box-shadow: 4px 4px 0 #263B50;
}

/* กล่องขยายหัวข้อย่อย */
[data-testid="stSidebar"] [data-testid="stExpander"] {
    background: #D8EEFF;
    border: 1.5px solid #9CCCF2;
    border-radius: 14px;
    margin-bottom: 12px;
}

/* กล่องเนื้อหา */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 16px;
}

/* ปุ่มทั่วไป */
div.stButton > button {
    border-radius: 12px;
    font-weight: 600;
}

/* กล่องแจ้งเตือน */
[data-testid="stAlert"] {
    border-radius: 14px;
}

/* การ์ดคะแนน */
[data-testid="stMetric"] {
    background: #E3F2FD;
    padding: 16px;
    border-radius: 16px;
    border: 1px solid #B5D9F4;
}

/* เส้นคั่น */
hr {
    border-color: #B5D9F4;
}

/* รองรับโทรศัพท์ */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    h1 {
        font-size: 1.8rem !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# ระบบเก็บหน้าปัจจุบัน
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "หน้าแรก"


def change_page(page):
    st.session_state.page = page


def menu_button(label, page):
    selected = st.session_state.page == page

    st.sidebar.button(
        label,
        key=f"menu_{page}",
        use_container_width=True,
        type="primary" if selected else "secondary",
        on_click=change_page,
        args=(page,)
    )


# =====================================================
# ข้อมูลบทเรียน
# =====================================================

LESSONS = {

    "บทที่ 1 ความรู้เบื้องต้น": {

        "ความหมายของตรรกศาสตร์": {
            "content": """
ตรรกศาสตร์ (Logic) เป็นศาสตร์ที่ศึกษาเกี่ยวกับ
หลักการคิดอย่างมีเหตุผล การวิเคราะห์ข้ออ้าง
และการตรวจสอบว่าข้อสรุปเป็นไปตามเหตุที่กำหนดหรือไม่

ตรรกศาสตร์มีความสำคัญต่อการเรียนคณิตศาสตร์
เนื่องจากใช้เป็นพื้นฐานของการพิสูจน์และการให้เหตุผล
""",
            "example": "ถ้า p เป็นจริง และ p → q เป็นจริง จะสรุปได้ว่า q เป็นจริง"
        },

        "ประพจน์": {
            "content": """
ประพจน์ (Proposition) คือประโยคบอกเล่าที่สามารถ
ระบุค่าความจริงได้ว่าเป็นจริงหรือเป็นเท็จอย่างใดอย่างหนึ่ง

ตัวอย่างประพจน์
- 2 + 3 = 5
- 7 เป็นจำนวนคู่
- กรุงเทพมหานครเป็นเมืองหลวงของประเทศไทย

ประโยคคำถามและประโยคคำสั่งไม่ถือเป็นประพจน์
""",
            "example": "2 + 3 = 5 เป็นประพจน์ที่มีค่าความจริงเป็น T"
        },

        "ค่าความจริง": {
            "content": """
ค่าความจริงของประพจน์มี 2 ค่า ได้แก่

- T (True) หมายถึง จริง
- F (False) หมายถึง เท็จ

ในตรรกศาสตร์ประพจน์แบบดั้งเดิม
แต่ละประพจน์จะมีค่าความจริงเพียงค่าเดียว
""",
            "example": "5 > 3 มีค่าความจริงเป็น T"
        },

        "ตัวแปรประพจน์": {
            "content": """
ตัวแปรประพจน์ใช้แทนข้อความหรือประพจน์ต่าง ๆ

นิยมใช้อักษร p, q, r และ s

การใช้ตัวแปรช่วยให้สามารถเขียนประพจน์ที่ซับซ้อน
ให้อยู่ในรูปสัญลักษณ์ทางตรรกศาสตร์ได้
""",
            "example": "กำหนด p : วันนี้ฝนตก และ q : ถนนเปียก"
        }
    },

    "บทที่ 2 ตัวเชื่อมตรรกศาสตร์": {

        "นิเสธ (NOT)": {
            "content": """
นิเสธของประพจน์ p เขียนแทนด้วย ¬p

นิเสธมีค่าความจริงตรงข้ามกับประพจน์เดิม

| p | ¬p |
|---|---|
| T | F |
| F | T |
""",
            "example": "ถ้า p = T แล้ว ¬p = F"
        },

        "การเชื่อมแบบและ (AND)": {
            "content": """
การเชื่อมแบบและ เขียนแทนด้วย p ∧ q

จะเป็นจริงเมื่อประพจน์ทั้งสองเป็นจริงเท่านั้น

| p | q | p ∧ q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |
""",
            "example": "T ∧ F = F"
        },

        "การเชื่อมแบบหรือ (OR)": {
            "content": """
การเชื่อมแบบหรือ เขียนแทนด้วย p ∨ q

จะเป็นจริงเมื่อมีประพจน์อย่างน้อยหนึ่งประพจน์เป็นจริง

| p | q | p ∨ q |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |
""",
            "example": "T ∨ F = T"
        },

        "อิมพลิเคชัน (Implication)": {
            "content": """
อิมพลิเคชัน เขียนแทนด้วย p → q

อ่านว่า ถ้า p แล้ว q

เป็นเท็จเพียงกรณีเดียว คือ p เป็นจริง และ q เป็นเท็จ

| p | q | p → q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
""",
            "example": "T → F = F"
        },

        "สมมูลสองทาง (Biconditional)": {
            "content": """
สมมูลสองทาง เขียนแทนด้วย p ↔ q

อ่านว่า p ก็ต่อเมื่อ q

จะเป็นจริงเมื่อ p และ q มีค่าความจริงเหมือนกัน

| p | q | p ↔ q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |
""",
            "example": "T ↔ T = T"
        }
    },

    "บทที่ 3 สัจนิรันดร์และสมมูล": {

        "สัจนิรันดร์": {
            "content": """
สัจนิรันดร์ (Tautology) คือสูตรตรรกศาสตร์
ที่มีค่าความจริงเป็นจริงในทุกกรณี

ไม่ว่าจะกำหนดค่าความจริงของตัวแปรอย่างไร
สูตรนั้นก็ยังคงเป็นจริงเสมอ
""",
            "example": "p ∨ ¬p เป็นสัจนิรันดร์"
        },

        "ข้อขัดแย้ง": {
            "content": """
ข้อขัดแย้ง (Contradiction) คือสูตรตรรกศาสตร์
ที่มีค่าความจริงเป็นเท็จในทุกกรณี
""",
            "example": "p ∧ ¬p เป็นข้อขัดแย้ง"
        },

        "กรณีอื่น (Contingency)": {
            "content": """
Contingency คือสูตรตรรกศาสตร์ที่มีทั้งกรณีจริง
และกรณีเท็จ ขึ้นอยู่กับค่าความจริงของตัวแปร
""",
            "example": "p ∧ q เป็น Contingency"
        },

        "สมมูลทางตรรกศาสตร์": {
            "content": """
สูตรสองสูตรจะสมมูลทางตรรกศาสตร์กัน
เมื่อมีค่าความจริงเหมือนกันในทุกกรณี

ใช้สัญลักษณ์ ≡ แทนความสมมูล
""",
            "example": "p → q ≡ ¬p ∨ q"
        },

        "กฎของเดอมอร์แกน": {
            "content": """
กฎของเดอมอร์แกน (De Morgan's Laws)

1. ¬(p ∧ q) ≡ ¬p ∨ ¬q

2. ¬(p ∨ q) ≡ ¬p ∧ ¬q

ใช้สำหรับเปลี่ยนรูปนิเสธของประพจน์เชิงประกอบ
""",
            "example": "¬(p ∧ q) ≡ ¬p ∨ ¬q"
        }
    },

    "บทที่ 4 การอ้างเหตุผล": {

        "ความหมายของการอ้างเหตุผล": {
            "content": """
การอ้างเหตุผลประกอบด้วย

1. เหตุ (Premises)
2. ข้อสรุป (Conclusion)

การอ้างเหตุผลจะสมเหตุสมผลเมื่อไม่มีกรณีที่
เหตุทุกข้อเป็นจริงแต่ข้อสรุปเป็นเท็จ
""",
            "example": "p → q, p ∴ q"
        },

        "Modus Ponens": {
            "content": """
Modus Ponens เป็นรูปแบบการอ้างเหตุผลที่สมเหตุสมผล

รูปแบบ

p → q

p

∴ q
""",
            "example": "ถ้าฝนตก ถนนเปียก / ฝนตก / ดังนั้น ถนนเปียก"
        },

        "Modus Tollens": {
            "content": """
Modus Tollens เป็นรูปแบบการอ้างเหตุผลที่สมเหตุสมผล

รูปแบบ

p → q

¬q

∴ ¬p
""",
            "example": "p → q, ¬q ∴ ¬p"
        },

        "การตรวจความสมเหตุสมผล": {
            "content": """
สามารถตรวจสอบความสมเหตุสมผลได้ด้วยตารางค่าความจริง

พิจารณาว่ามีกรณีที่เหตุทุกข้อเป็นจริง
แต่ข้อสรุปเป็นเท็จหรือไม่

ถ้ามีกรณีดังกล่าว แสดงว่าการอ้างเหตุผลไม่สมเหตุสมผล
""",
            "example": "p → q, p ∴ q เป็นการอ้างเหตุผลที่สมเหตุสมผล"
        }
    },

    "บทที่ 5 ประโยคเปิดและตัวบ่งปริมาณ": {

        "ประโยคเปิด": {
            "content": """
ประโยคเปิดคือข้อความที่มีตัวแปร
ซึ่งค่าความจริงขึ้นอยู่กับค่าที่แทนตัวแปร

เมื่อกำหนดค่าตัวแปรแล้ว
จึงสามารถตรวจสอบค่าความจริงได้
""",
            "example": "x + 2 = 5 เป็นจริงเมื่อ x = 3"
        },

        "ตัวบ่งปริมาณสากล": {
            "content": """
ตัวบ่งปริมาณสากลใช้สัญลักษณ์ ∀

อ่านว่า สำหรับทุกตัว

ใช้ระบุว่าข้อความเป็นจริงสำหรับสมาชิกทุกตัว
ในขอบเขตที่กำหนด
""",
            "example": "∀x P(x)"
        },

        "ตัวบ่งปริมาณมีอยู่": {
            "content": """
ตัวบ่งปริมาณมีอยู่ใช้สัญลักษณ์ ∃

อ่านว่า มีอย่างน้อยหนึ่งตัว

ใช้ระบุว่ามีสมาชิกอย่างน้อยหนึ่งตัว
ที่ทำให้ข้อความเป็นจริง
""",
            "example": "∃x P(x)"
        },

        "นิเสธของตัวบ่งปริมาณ": {
            "content": """
สูตรสำคัญ

¬(∀x P(x)) ≡ ∃x ¬P(x)

¬(∃x P(x)) ≡ ∀x ¬P(x)
""",
            "example": "นิเสธของ 'ทุกคนผ่าน' คือ 'มีอย่างน้อยหนึ่งคนไม่ผ่าน'"
        }
    },

    "บทที่ 6 การให้เหตุผลและการพิสูจน์": {

        "การให้เหตุผลแบบนิรนัย": {
            "content": """
การให้เหตุผลแบบนิรนัย (Deductive Reasoning)
เป็นการให้เหตุผลจากหลักทั่วไปไปสู่ข้อสรุปเฉพาะ

หากเหตุเป็นจริงและรูปแบบการอ้างเหตุผลสมเหตุสมผล
ข้อสรุปจะเป็นจริง
""",
            "example": "จำนวนคู่ทุกจำนวนหารด้วย 2 ลงตัว และ 8 เป็นจำนวนคู่ ดังนั้น 8 หารด้วย 2 ลงตัว"
        },

        "การให้เหตุผลแบบอุปนัย": {
            "content": """
การให้เหตุผลแบบอุปนัย (Inductive Reasoning)
เป็นการใช้ข้อมูลหรือการสังเกตหลายกรณี
เพื่อคาดการณ์รูปแบบหรือข้อสรุปทั่วไป

ข้อสรุปจากอุปนัยอาจต้องตรวจสอบเพิ่มเติม
""",
            "example": "สังเกตรูปแบบของลำดับจำนวน แล้วคาดการณ์พจน์ถัดไป"
        },

        "การพิสูจน์ทางคณิตศาสตร์": {
            "content": """
การพิสูจน์ทางคณิตศาสตร์ใช้เหตุผล
นิยาม ทฤษฎีบท และกฎที่ยอมรับแล้ว
เพื่อแสดงว่าข้อความที่ต้องการพิสูจน์เป็นจริง
""",
            "example": "การพิสูจน์โดยตรง และการพิสูจน์โดยข้อขัดแย้ง"
        }
    }
}


# =====================================================
# ระบบคำนวณตรรกศาสตร์
# =====================================================

TOKEN_RE = re.compile(
    r"\s*(<->|<=>|->|=>|[()¬~!∧&∨|→↔]|[A-Za-z][A-Za-z0-9_]*)"
)


def tokenize(expr):
    tokens = []
    pos = 0

    while pos < len(expr):
        if expr[pos:].strip() == "":
            break

        match = TOKEN_RE.match(expr, pos)

        if not match:
            raise ValueError(
                "ไม่รู้จักสัญลักษณ์: " + expr[pos:]
            )

        token = match.group(1)
        pos = match.end()

        aliases = {
            "¬": "NOT",
            "~": "NOT",
            "!": "NOT",
            "∧": "AND",
            "&": "AND",
            "∨": "OR",
            "|": "OR",
            "→": "IMP",
            "->": "IMP",
            "=>": "IMP",
            "↔": "IFF",
            "<->": "IFF",
            "<=>": "IFF"
        }

        tokens.append(aliases.get(token, token))

    if not tokens:
        raise ValueError("กรุณากรอกสูตรตรรกศาสตร์")

    return tokens


class LogicParser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse(self):
        result = self.iff()

        if self.peek() is not None:
            raise ValueError("รูปแบบสูตรไม่ถูกต้อง")

        return result

    def iff(self):
        node = self.imp()

        while self.peek() == "IFF":
            self.eat()
            node = ("IFF", node, self.imp())

        return node

    def imp(self):
        node = self.or_expr()

        if self.peek() == "IMP":
            self.eat()
            node = ("IMP", node, self.imp())

        return node

    def or_expr(self):
        node = self.and_expr()

        while self.peek() == "OR":
            self.eat()
            node = ("OR", node, self.and_expr())

        return node

    def and_expr(self):
        node = self.unary()

        while self.peek() == "AND":
            self.eat()
            node = ("AND", node, self.unary())

        return node

    def unary(self):
        token = self.peek()

        if token == "NOT":
            self.eat()
            return ("NOT", self.unary())

        if token == "(":
            self.eat()
            node = self.iff()

            if self.peek() != ")":
                raise ValueError("วงเล็บไม่ครบ")

            self.eat()
            return node

        if token is None:
            raise ValueError("สูตรไม่สมบูรณ์")

        if token in ("AND", "OR", "IMP", "IFF", ")"):
            raise ValueError("ตำแหน่งตัวเชื่อมไม่ถูกต้อง")

        self.eat()

        if token.upper() in ("T", "TRUE"):
            return ("CONST", True)

        if token.upper() in ("F", "FALSE"):
            return ("CONST", False)

        return ("VAR", token)


def parse_logic(expr):
    return LogicParser(tokenize(expr)).parse()


def get_vars(node):
    if node[0] == "VAR":
        return {node[1]}

    if node[0] == "CONST":
        return set()

    if node[0] == "NOT":
        return get_vars(node[1])

    return get_vars(node[1]) | get_vars(node[2])


def evaluate(node, env):
    op = node[0]

    if op == "CONST":
        return node[1]

    if op == "VAR":
        return env[node[1]]

    if op == "NOT":
        return not evaluate(node[1], env)

    a = evaluate(node[1], env)
    b = evaluate(node[2], env)

    if op == "AND":
        return a and b

    if op == "OR":
        return a or b

    if op == "IMP":
        return (not a) or b

    if op == "IFF":
        return a == b

    raise ValueError("ตัวเชื่อมไม่ถูกต้อง")


def truth_table(expr):
    node = parse_logic(expr)
    variables = sorted(get_vars(node))

    if len(variables) > 10:
        raise ValueError("กรุณาใช้ตัวแปรไม่เกิน 10 ตัว")

    rows = []

    for values in itertools.product(
        [True, False],
        repeat=len(variables)
    ):
        env = dict(zip(variables, values))

        row = {
            var: "T" if env[var] else "F"
            for var in variables
        }

        row[expr] = (
            "T" if evaluate(node, env) else "F"
        )

        rows.append(row)

    return pd.DataFrame(rows), node


def classify_formula(expr):
    df, node = truth_table(expr)

    vars_list = sorted(get_vars(node))
    results = []

    for values in itertools.product(
        [True, False],
        repeat=len(vars_list)
    ):
        env = dict(zip(vars_list, values))
        results.append(evaluate(node, env))

    if all(results):
        return "สัจนิรันดร์ (Tautology)"

    if not any(results):
        return "ข้อขัดแย้ง (Contradiction)"

    return "กรณีอื่น (Contingency)"


def check_equivalence(expr1, expr2):
    node1 = parse_logic(expr1)
    node2 = parse_logic(expr2)

    vars_list = sorted(
        get_vars(node1) | get_vars(node2)
    )

    if len(vars_list) > 10:
        raise ValueError("กรุณาใช้ตัวแปรรวมไม่เกิน 10 ตัว")

    for values in itertools.product(
        [True, False],
        repeat=len(vars_list)
    ):
        env = dict(zip(vars_list, values))

        if evaluate(node1, env) != evaluate(node2, env):
            return False, env

    return True, None


def check_argument(premises, conclusion):
    premise_nodes = [parse_logic(p) for p in premises]
    conclusion_node = parse_logic(conclusion)

    vars_set = get_vars(conclusion_node)

    for node in premise_nodes:
        vars_set |= get_vars(node)

    vars_list = sorted(vars_set)

    if len(vars_list) > 10:
        raise ValueError("กรุณาใช้ตัวแปรรวมไม่เกิน 10 ตัว")

    for values in itertools.product(
        [True, False],
        repeat=len(vars_list)
    ):
        env = dict(zip(vars_list, values))

        premises_true = all(
            evaluate(node, env)
            for node in premise_nodes
        )

        conclusion_false = not evaluate(
            conclusion_node,
            env
        )

        if premises_true and conclusion_false:
            return False, env

    return True, None


# =====================================================
# แถบเมนูด้านซ้าย
# =====================================================

st.sidebar.title("🧠 MATH LOGIC")
st.sidebar.caption("Learning & Solver")
st.sidebar.markdown("---")

st.sidebar.subheader("ภาพรวมระบบ")

menu_button("🏠 หน้าหลัก", "หน้าแรก")
menu_button("📖 ภาพรวมบทเรียนและทฤษฎี", "ภาพรวมบทเรียน")

st.sidebar.markdown("---")
st.sidebar.subheader("โมดูลการเรียนรู้")

chapter_icons = [
    "📚", "🔗", "🧩", "🧠", "📐", "📘"
]

for index, (chapter, topics) in enumerate(LESSONS.items()):

    icon = chapter_icons[index]

    with st.sidebar.expander(
        f"{icon} {chapter}",
        expanded=st.session_state.page in topics
    ):
        for topic in topics:
            menu_button(
                f"↳ {topic}",
                topic
            )

st.sidebar.markdown("---")
st.sidebar.subheader("เครื่องมือและการประเมิน")

menu_button("🧮 เครื่องคำนวณตรรกศาสตร์", "เครื่องคำนวณ")
menu_button("📊 ตารางค่าความจริง", "ตารางค่าความจริง")
menu_button("🧠 ตรวจสอบสูตรตรรกศาสตร์", "ตรวจสอบสูตร")
menu_button("🔄 ตรวจสอบสมมูล", "ตรวจสอบสมมูล")
menu_button("⚖️ ตรวจสอบการอ้างเหตุผล", "ตรวจสอบเหตุผล")
menu_button("🌳 แผนภาพต้นไม้", "แผนภาพต้นไม้")
menu_button("📖 รวมสูตรตรรกศาสตร์", "รวมสูตร")
menu_button("📝 แบบฝึกหัด", "แบบฝึกหัด")
menu_button("🎮 เกมตรรกศาสตร์", "เกม")
menu_button("📋 แบบทดสอบ", "แบบทดสอบ")

st.sidebar.markdown("---")
st.sidebar.subheader("ข้อมูลโครงงาน")

menu_button("ℹ️ เกี่ยวกับเว็บไซต์", "เกี่ยวกับเว็บไซต์")


# =====================================================
# แสดงเนื้อหาตามหน้าที่เลือก
# =====================================================

page = st.session_state.page


# -----------------------------------------------------
# หน้าแรก
# -----------------------------------------------------

if page == "หน้าแรก":

    st.title("🧠 Math Logic Learning & Solver")

    st.subheader(
        "เว็บไซต์สื่อการเรียนรู้ตรรกศาสตร์ทางคณิตศาสตร์"
    )

    st.info(
        "เรียนรู้ • ฝึกคิด • ทดลองคำนวณ • ตรวจสอบคำตอบ"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("บทเรียน", len(LESSONS))

    col2.metric(
        "หัวข้อย่อย",
        sum(len(x) for x in LESSONS.values())
    )

    col3.metric("เครื่องมือและกิจกรรม", 10)

    st.markdown("## 🩵 ยินดีต้อนรับ")

    st.write("""
    เว็บไซต์นี้จัดทำขึ้นเพื่อส่งเสริมการเรียนรู้
    เรื่องตรรกศาสตร์ทางคณิตศาสตร์

    ผู้เรียนสามารถศึกษาเนื้อหา ทบทวนสูตร
    ทดลองสร้างตารางค่าความจริง
    และฝึกทำแบบฝึกหัดได้ด้วยตนเอง
    """)

    st.markdown("### วิธีใช้งาน")

    st.write("""
    1. เลือกบทเรียนจากแถบเมนูด้านซ้าย
    2. กดหัวข้อย่อยที่ต้องการศึกษา
    3. ทดลองใช้เครื่องคำนวณตรรกศาสตร์
    4. ทำแบบฝึกหัดและแบบทดสอบ
    """)


# -----------------------------------------------------
# ภาพรวมบทเรียน
# -----------------------------------------------------

elif page == "ภาพรวมบทเรียน":

    st.title("📖 ภาพรวมบทเรียนและทฤษฎี")

    for chapter, topics in LESSONS.items():

        with st.container(border=True):

            st.subheader(chapter)

            for topic in topics:
                st.write("📌", topic)


# -----------------------------------------------------
# เนื้อหาหัวข้อย่อย
# -----------------------------------------------------

elif any(
    page in topics
    for topics in LESSONS.values()
):

    for chapter, topics in LESSONS.items():

        if page in topics:

            lesson = topics[page]

            st.caption(chapter)
            st.title("📚 " + page)

            st.markdown("### ความรู้เบื้องต้น")

            with st.container(border=True):
                st.markdown(lesson["content"])

            st.markdown("### ตัวอย่าง")

            st.success(lesson["example"])

            st.markdown("### สรุปบทเรียน")

            st.info(
                "ศึกษาความหมายและตัวอย่างให้เข้าใจ "
                "จากนั้นสามารถทดลองทำโจทย์ในเมนูเครื่องมือได้"
            )

            break


# -----------------------------------------------------
# เครื่องคำนวณค่าความจริง
# -----------------------------------------------------

elif page == "เครื่องคำนวณ":

    st.title("🧮 เครื่องคำนวณตรรกศาสตร์")

    expr = st.text_input(
        "ป้อนสูตรตรรกศาสตร์",
        "p & q"
    )

    try:
        node = parse_logic(expr)
        vars_list = sorted(get_vars(node))

        if len(vars_list) > 10:
            st.warning("กรุณาใช้ตัวแปรไม่เกิน 10 ตัว")

        else:
            env = {}

            st.markdown("### กำหนดค่าความจริง")

            for var in vars_list:

                value = st.selectbox(
                    f"ค่าของ {var}",
                    ["T", "F"],
                    key=f"calc_{var}"
                )

                env[var] = value == "T"

            if st.button("คำนวณค่าความจริง"):

                result = evaluate(node, env)

                st.success(
                    "ผลลัพธ์ = "
                    + ("T (จริง)" if result else "F (เท็จ)")
                )

    except ValueError as e:
        st.error(str(e))


# -----------------------------------------------------
# ตารางค่าความจริง
# -----------------------------------------------------

elif page == "ตารางค่าความจริง":

    st.title("📊 ตารางค่าความจริง")

    expr = st.text_input(
        "ป้อนสูตร",
        "(p & q) -> r"
    )

    if st.button("สร้างตารางค่าความจริง"):

        try:
            df, node = truth_table(expr)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.success(
                f"จำนวนกรณีทั้งหมด {len(df)} กรณี"
            )

        except ValueError as e:
            st.error(str(e))


# -----------------------------------------------------
# ตรวจสอบประเภทสูตร
# -----------------------------------------------------

elif page == "ตรวจสอบสูตร":

    st.title("🧠 ตรวจสอบสูตรตรรกศาสตร์")

    expr = st.text_input(
        "ป้อนสูตรที่ต้องการตรวจสอบ",
        "p | ~p"
    )

    if st.button("ตรวจสอบสูตร"):

        try:
            result = classify_formula(expr)

            st.success(result)

            df, node = truth_table(expr)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        except ValueError as e:
            st.error(str(e))


# -----------------------------------------------------
# ตรวจสอบสมมูล
# -----------------------------------------------------

elif page == "ตรวจสอบสมมูล":

    st.title("🔄 ตรวจสอบสมมูลทางตรรกศาสตร์")

    expr1 = st.text_input(
        "สูตรที่ 1",
        "p -> q"
    )

    expr2 = st.text_input(
        "สูตรที่ 2",
        "~p | q"
    )

    if st.button("ตรวจสอบสมมูล"):

        try:
            same, counterexample = check_equivalence(
                expr1,
                expr2
            )

            if same:
                st.success(
                    "สูตรทั้งสองสมมูลกัน"
                )

            else:
                st.error(
                    "สูตรทั้งสองไม่สมมูลกัน"
                )

                st.write(
                    "ตัวอย่างค่าความจริงที่ทำให้ต่างกัน:",
                    counterexample
                )

        except ValueError as e:
            st.error(str(e))


# -----------------------------------------------------
# ตรวจสอบการอ้างเหตุผล
# -----------------------------------------------------

elif page == "ตรวจสอบเหตุผล":

    st.title("⚖️ ตรวจสอบการอ้างเหตุผล")

    premises_text = st.text_area(
        "เหตุ (หนึ่งสูตรต่อหนึ่งบรรทัด)",
        "p -> q\np"
    )

    conclusion = st.text_input(
        "ข้อสรุป",
        "q"
    )

    if st.button("ตรวจสอบความสมเหตุสมผล"):

        try:
            premises = [
                line.strip()
                for line in premises_text.splitlines()
                if line.strip()
            ]

            if not premises:
                st.warning("กรุณากรอกเหตุ")
            else:
                valid, counterexample = check_argument(
                    premises,
                    conclusion
                )

                if valid:
                    st.success(
                        "การอ้างเหตุผลสมเหตุสมผล"
                    )

                else:
                    st.error(
                        "การอ้างเหตุผลไม่สมเหตุสมผล"
                    )

                    st.write(
                        "ตัวอย่างค้าน:",
                        counterexample
                    )

        except ValueError as e:
            st.error(str(e))


# -----------------------------------------------------
# แผนภาพต้นไม้
# -----------------------------------------------------

elif page == "แผนภาพต้นไม้":

    st.title("🌳 แผนภาพต้นไม้")

    st.write(
        "แผนภาพต้นไม้ (Truth Tree) "
        "เป็นวิธีหนึ่งที่ใช้วิเคราะห์สูตรตรรกศาสตร์"
    )

    st.markdown("### ตัวอย่าง: p ∨ ¬p")

    st.write(
        "การตรวจสอบสัจนิรันดร์เริ่มจากสมมติให้สูตรเป็นเท็จ"
    )

    st.graphviz_chart("""
    digraph G {
        rankdir=TB;

        node [
            shape=box,
            style="rounded,filled",
            fillcolor="#D8EEFF",
            color="#245A81"
        ];

        A [label="F(p ∨ ¬p)"];
        B [label="Fp, F¬p"];
        C [label="Fp, Tp"];
        D [label="× ปิดกิ่ง"];

        A -> B;
        B -> C;
        C -> D;
    }
    """)

    st.success(
        "ทุกกิ่งปิด จึงสรุปว่า p ∨ ¬p เป็นสัจนิรันดร์"
    )

    st.caption(
        "หน้านี้เป็นตัวอย่างแผนภาพต้นไม้ "
        "ยังไม่ใช่ระบบสร้างต้นไม้จากสูตรใด ๆ โดยอัตโนมัติ"
    )


# -----------------------------------------------------
# รวมสูตรตรรกศาสตร์
# -----------------------------------------------------

elif page == "รวมสูตร":

    st.title("📖 รวมสูตรตรรกศาสตร์")

    formulas = {

        "กฎนิเสธ": [
            "¬(¬p) ≡ p",
            "p ∨ ¬p ≡ T",
            "p ∧ ¬p ≡ F"
        ],

        "กฎของเดอมอร์แกน": [
            "¬(p ∧ q) ≡ ¬p ∨ ¬q",
            "¬(p ∨ q) ≡ ¬p ∧ ¬q"
        ],

        "กฎการสลับที่": [
            "p ∧ q ≡ q ∧ p",
            "p ∨ q ≡ q ∨ p"
        ],

        "กฎการเปลี่ยนหมู่": [
            "(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)",
            "(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)"
        ],

        "กฎการแจกแจง": [
            "p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)",
            "p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)"
        ],

        "กฎอิมพลิเคชัน": [
            "p → q ≡ ¬p ∨ q",
            "p → q ≡ ¬q → ¬p"
        ],

        "กฎสมมูลสองทาง": [
            "p ↔ q ≡ (p → q) ∧ (q → p)"
        ],

        "กฎตัวบ่งปริมาณ": [
            "¬(∀x P(x)) ≡ ∃x ¬P(x)",
            "¬(∃x P(x)) ≡ ∀x ¬P(x)"
        ]
    }

    for category, items in formulas.items():

        with st.expander(category):

            for formula in items:
                st.code(formula, language=None)


# -----------------------------------------------------
# คำถามสำหรับแบบฝึกหัดและแบบทดสอบ
# -----------------------------------------------------

QUESTIONS = [

    (
        "T ∧ F มีค่าความจริงเป็นอะไร?",
        ["T", "F"],
        "F",
        "การเชื่อมแบบและต้องจริงทั้งสองข้าง"
    ),

    (
        "T ∨ F มีค่าความจริงเป็นอะไร?",
        ["T", "F"],
        "T",
        "การเชื่อมแบบหรือเป็นจริงเมื่อมีอย่างน้อยหนึ่งข้างจริง"
    ),

    (
        "¬T มีค่าความจริงเป็นอะไร?",
        ["T", "F"],
        "F",
        "นิเสธมีค่าตรงข้ามกับประพจน์เดิม"
    ),

    (
        "p ∨ ¬p เป็นสูตรประเภทใด?",
        ["สัจนิรันดร์", "ข้อขัดแย้ง", "กรณีอื่น"],
        "สัจนิรันดร์",
        "สูตรนี้เป็นจริงทุกกรณี"
    ),

    (
        "p ∧ ¬p เป็นสูตรประเภทใด?",
        ["สัจนิรันดร์", "ข้อขัดแย้ง", "กรณีอื่น"],
        "ข้อขัดแย้ง",
        "สูตรนี้เป็นเท็จทุกกรณี"
    ),

    (
        "T → F มีค่าความจริงเป็นอะไร?",
        ["T", "F"],
        "F",
        "อิมพลิเคชันเป็นเท็จเมื่อเหตุจริงแต่ผลเท็จ"
    )
]


# -----------------------------------------------------
# แบบฝึกหัด
# -----------------------------------------------------

elif page == "แบบฝึกหัด":

    st.title("📝 แบบฝึกหัดตรรกศาสตร์")

    for i, question in enumerate(QUESTIONS):

        text, options, correct, explanation = question

        with st.container(border=True):

            st.markdown(
                f"### ข้อ {i + 1}. {text}"
            )

            answer = st.radio(
                "เลือกคำตอบ",
                options,
                index=None,
                key=f"practice_{i}"
            )

            if st.button(
                "ตรวจคำตอบ",
                key=f"check_{i}"
            ):

                if answer is None:
                    st.warning("กรุณาเลือกคำตอบ")

                elif answer == correct:
                    st.success("ถูกต้อง!")
                    st.info(explanation)

                else:
                    st.error(
                        f"คำตอบที่ถูกคือ {correct}"
                    )
                    st.info(explanation)


# -----------------------------------------------------
# เกมตรรกศาสตร์
# -----------------------------------------------------

elif page == "เกม":

    st.title("🎮 เกมทายค่าความจริง")

    if "game" not in st.session_state:

        st.session_state.game = (
            random.choice([True, False]),
            random.choice([True, False]),
            random.choice(["AND", "OR", "IMP"])
        )

    p, q, op = st.session_state.game

    symbols = {
        "AND": "∧",
        "OR": "∨",
        "IMP": "→"
    }

    results = {
        "AND": p and q,
        "OR": p or q,
        "IMP": (not p) or q
    }

    st.markdown(
        f"### p = {'T' if p else 'F'} "
        f"และ q = {'T' if q else 'F'}"
    )

    st.markdown(
        f"### จงหาค่าของ p {symbols[op]} q"
    )

    answer = st.radio(
        "คำตอบ",
        ["T", "F"],
        index=None,
        key="game_answer"
    )

    col1, col2 = st.columns(2)

    if col1.button("ตรวจคำตอบ"):

        expected = "T" if results[op] else "F"

        if answer is None:
            st.warning("กรุณาเลือกคำตอบ")

        elif answer == expected:
            st.success("ถูกต้อง!")

        else:
            st.error(
                f"คำตอบที่ถูกคือ {expected}"
            )

    if col2.button("สุ่มโจทย์ใหม่"):

        st.session_state.game = (
            random.choice([True, False]),
            random.choice([True, False]),
            random.choice(["AND", "OR", "IMP"])
        )

        st.session_state.pop("game_answer", None)

        st.rerun()


# -----------------------------------------------------
# แบบทดสอบ
# -----------------------------------------------------

elif page == "แบบทดสอบ":

    st.title("📋 แบบทดสอบตรรกศาสตร์")

    answers = []

    for i, question in enumerate(QUESTIONS):

        text, options, correct, explanation = question

        answer = st.radio(
            f"ข้อ {i + 1}. {text}",
            options,
            index=None,
            key=f"quiz_{i}"
        )

        answers.append(answer)

    if st.button("ส่งแบบทดสอบ"):

        if any(answer is None for answer in answers):

            st.warning("กรุณาตอบให้ครบทุกข้อ")

        else:

            score = sum(
                answers[i] == QUESTIONS[i][2]
                for i in range(len(QUESTIONS))
            )

            st.metric(
                "คะแนนที่ได้",
                f"{score}/{len(QUESTIONS)}"
            )

            st.progress(score / len(QUESTIONS))

            with st.expander("ดูเฉลย"):

                for i, question in enumerate(QUESTIONS):

                    st.write(
                        f"ข้อ {i + 1}: {question[2]}"
                    )

                    st.caption(question[3])


# -----------------------------------------------------
# เกี่ยวกับเว็บไซต์
# -----------------------------------------------------

elif page == "เกี่ยวกับเว็บไซต์":

    st.title("ℹ️ เกี่ยวกับเว็บไซต์")

    st.markdown("""
    ## Math Logic Learning & Solver

    เว็บไซต์สื่อการเรียนรู้ตรรกศาสตร์ทางคณิตศาสตร์

    ### วัตถุประสงค์

    1. เพื่อส่งเสริมการเรียนรู้เรื่องตรรกศาสตร์
    2. เพื่อช่วยให้ผู้เรียนเข้าใจตัวเชื่อมตรรกศาสตร์
    3. เพื่อพัฒนาทักษะการคิดอย่างมีเหตุผล
    4. เพื่อให้ผู้เรียนฝึกสร้างตารางค่าความจริง
    5. เพื่อให้ผู้เรียนสามารถตรวจสอบสูตรตรรกศาสตร์

    ### เครื่องมือภายในเว็บไซต์

    - บทเรียนและทฤษฎี
    - เครื่องคำนวณตรรกศาสตร์
    - ตารางค่าความจริง
    - การตรวจสอบสูตร
    - การตรวจสอบสมมูล
    - การตรวจสอบการอ้างเหตุผล
    - ตัวอย่างแผนภาพต้นไม้
    - รวมสูตรตรรกศาสตร์
    - แบบฝึกหัด
    - เกมตรรกศาสตร์
    - แบบทดสอบ

    ### ข้อจำกัด

    เครื่องคำนวณรองรับตรรกศาสตร์ประพจน์
    แต่ยังไม่รองรับการคำนวณตัวบ่งปริมาณ
    และการสร้างแผนภาพต้นไม้อัตโนมัติ
    """)


# =====================================================
# ส่วนท้ายเว็บไซต์
# =====================================================

st.markdown("---")

st.caption(
    "🩵 Math Logic Learning & Solver | "
    "เว็บไซต์สื่อการเรียนรู้ตรรกศาสตร์ทางคณิตศาสตร์"
)
