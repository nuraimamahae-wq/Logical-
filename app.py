import streamlit as st
import pandas as pd
import itertools
import re

# ==================================================
# ตั้งค่าหน้าเว็บไซต์
# ==================================================
st.set_page_config(
    page_title="Math Logic Learning & Solver",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# ธีมสีฟ้าพาสเทล
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Prompt', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f4f9ff, #e8f3ff);
    color: #25415e;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #d9ecff, #bddcff);
    border-right: 2px solid #6597c8;
}

h1, h2, h3 {
    color: #245783;
}

div.stButton > button {
    background-color: #f7fbff;
    color: #245783;
    border: 1.5px solid #6597c8;
    border-radius: 12px;
    box-shadow: 3px 3px 0px #a7c8e9;
    font-weight: 500;
}

div.stButton > button:hover {
    background-color: #d9ecff;
    border-color: #3479b8;
    color: #17436b;
}

.logic-card {
    background-color: white;
    border: 1px solid #c4def7;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(70, 120, 170, 0.10);
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #c4def7;
    border-radius: 14px;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# ระบบประมวลผลตรรกศาสตร์
# ==================================================

OPERATORS = {
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
    "<=>": "IFF",
}

TOKEN_PATTERN = re.compile(
    r"<->|<=>|->|=>|[()¬~!∧&∨|→↔]|[A-Za-z][A-Za-z0-9_]*"
)


class LogicError(Exception):
    pass


def tokenize(formula):
    tokens = TOKEN_PATTERN.findall(formula)
    cleaned = re.sub(r"\s+", "", formula)

    if "".join(tokens).lower() != cleaned.lower():
        raise LogicError(
            "สูตรมีสัญลักษณ์ที่ไม่รองรับ "
            "กรุณาใช้ p, q, r และสัญลักษณ์ ¬ ∧ ∨ → ↔"
        )

    result = []

    for token in tokens:
        if token in OPERATORS:
            result.append(OPERATORS[token])
        elif token == "(" or token == ")":
            result.append(token)
        else:
            result.append(token)

    if not result:
        raise LogicError("กรุณาป้อนสูตรตรรกศาสตร์")

    return result


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def take(self):
        token = self.peek()
        if token is not None:
            self.position += 1
        return token

    def parse(self):
        node = self.parse_iff()

        if self.peek() is not None:
            raise LogicError(
                f"ไม่สามารถอ่านสัญลักษณ์ {self.peek()} ได้"
            )

        return node

    def parse_iff(self):
        node = self.parse_imp()

        while self.peek() == "IFF":
            self.take()
            node = ("IFF", node, self.parse_imp())

        return node

    def parse_imp(self):
        node = self.parse_or()

        if self.peek() == "IMP":
            self.take()
            node = ("IMP", node, self.parse_imp())

        return node

    def parse_or(self):
        node = self.parse_and()

        while self.peek() == "OR":
            self.take()
            node = ("OR", node, self.parse_and())

        return node

    def parse_and(self):
        node = self.parse_not()

        while self.peek() == "AND":
            self.take()
            node = ("AND", node, self.parse_not())

        return node

    def parse_not(self):
        if self.peek() == "NOT":
            self.take()
            return ("NOT", self.parse_not())

        return self.parse_atom()

    def parse_atom(self):
        token = self.take()

        if token is None:
            raise LogicError("สูตรไม่สมบูรณ์")

        if token == "(":
            node = self.parse_iff()

            if self.take() != ")":
                raise LogicError("วงเล็บเปิดและปิดไม่ครบ")

            return node

        if token in (")", "AND", "OR", "IMP", "IFF", "NOT"):
            raise LogicError("ตำแหน่งตัวดำเนินการไม่ถูกต้อง")

        return ("VAR", token)


def parse_formula(formula):
    return Parser(tokenize(formula)).parse()


def get_variables(node):
    if node[0] == "VAR":
        return {node[1]}

    if node[0] == "NOT":
        return get_variables(node[1])

    return get_variables(node[1]) | get_variables(node[2])


def evaluate(node, values):
    kind = node[0]

    if kind == "VAR":
        return values[node[1]]

    if kind == "NOT":
        return not evaluate(node[1], values)

    left = evaluate(node[1], values)
    right = evaluate(node[2], values)

    if kind == "AND":
        return left and right

    if kind == "OR":
        return left or right

    if kind == "IMP":
        return (not left) or right

    if kind == "IFF":
        return left == right

    raise LogicError("ไม่รู้จักตัวดำเนินการ")


def truth_table(nodes):
    variables = sorted(
        set().union(*(get_variables(node) for node in nodes))
    )

    if len(variables) > 8:
        raise LogicError("รองรับตัวแปรไม่เกิน 8 ตัว")

    rows = []

    for combination in itertools.product(
        [True, False], repeat=len(variables)
    ):
        values = dict(zip(variables, combination))

        row = {
            variable: "T" if values[variable] else "F"
            for variable in variables
        }

        for index, node in enumerate(nodes):
            result = evaluate(node, values)
            row[f"ผลลัพธ์ {index + 1}"] = (
                "T" if result else "F"
            )

        rows.append(row)

    return variables, rows


def classify_formula(node):
    _, rows = truth_table([node])

    results = [row["ผลลัพธ์ 1"] for row in rows]

    if all(value == "T" for value in results):
        return "สัจนิรันดร์ (Tautology)"

    if all(value == "F" for value in results):
        return "ข้อขัดแย้ง (Contradiction)"

    return "ประพจน์ไม่แน่นอน (Contingency)"


# ==================================================
# เนื้อหาบทเรียน
# ==================================================

LESSONS = {
    "บทที่ 1 ประพจน์": {
        "ความหมายของประพจน์":
            "ประพจน์คือประโยคบอกเล่าที่ระบุได้ว่าเป็นจริงหรือเป็นเท็จ",
        "ค่าความจริง":
            "ค่าความจริงมี 2 ค่า คือ จริง (T) และเท็จ (F)",
        "ตัวแปรประพจน์":
            "นิยมใช้ p, q, r แทนประพจน์ต่าง ๆ"
    },

    "บทที่ 2 ตัวดำเนินการทางตรรกศาสตร์": {
        "นิเสธ":
            "¬p มีค่าความจริงตรงข้ามกับ p",
        "ตัวเชื่อมและ":
            "p ∧ q เป็นจริงเมื่อ p และ q เป็นจริงทั้งคู่",
        "ตัวเชื่อมหรือ":
            "p ∨ q เป็นเท็จเมื่อ p และ q เป็นเท็จทั้งคู่",
        "อิมพลิเคชัน":
            "p → q เป็นเท็จเฉพาะกรณี p เป็นจริงและ q เป็นเท็จ",
        "สมมูล":
            "p ↔ q เป็นจริงเมื่อ p และ q มีค่าความจริงเหมือนกัน"
    },

    "บทที่ 3 ตารางค่าความจริง": {
        "การสร้างตาราง":
            "ถ้ามีตัวแปร n ตัว จะมีชุดค่าความจริงทั้งหมด 2ⁿ แถว",
        "การคำนวณ":
            "คำนวณตามวงเล็บและตัวดำเนินการทางตรรกศาสตร์"
    },

    "บทที่ 4 สัจนิรันดร์และความสมมูล": {
        "สัจนิรันดร์":
            "สูตรที่เป็นจริงทุกแถวเรียกว่าสัจนิรันดร์",
        "ข้อขัดแย้ง":
            "สูตรที่เป็นเท็จทุกแถวเรียกว่าข้อขัดแย้ง",
        "ความสมมูล":
            "สูตรสองสูตรสมมูลกันเมื่อผลลัพธ์ตรงกันทุกแถว"
    },

    "บทที่ 5 การอ้างเหตุผล": {
        "ความสมเหตุสมผล":
            "การอ้างเหตุผลสมเหตุสมผลเมื่อไม่มีกรณีที่เหตุทุกข้อจริงแต่ข้อสรุปเท็จ",
        "Modus Ponens":
            "รูปแบบ p → q, p ดังนั้น q",
        "Modus Tollens":
            "รูปแบบ p → q, ¬q ดังนั้น ¬p"
    },

    "บทที่ 6 ต้นไม้ความจริง": {
        "แนวคิด":
            "ต้นไม้ความจริงใช้แยกสูตรออกเป็นเงื่อนไขย่อยเพื่อตรวจสอบความเป็นไปได้",
        "การปิดกิ่ง":
            "กิ่งที่มีทั้ง p และ ¬p ถือว่าขัดแย้งและปิดกิ่ง"
    }
}


# ==================================================
# คลังคำถาม
# ประกาศไว้นอก if/elif เพื่อป้องกัน SyntaxError
# ==================================================

QUESTIONS = [
    {
        "question": "ถ้า p เป็นจริง แล้ว ¬p มีค่าใด",
        "choices": ["T", "F"],
        "answer": "F",
        "explanation": "นิเสธมีค่าความจริงตรงข้ามกับประพจน์เดิม"
    },
    {
        "question": "p ∧ q เป็นจริงเมื่อใด",
        "choices": [
            "เมื่อ p จริงเท่านั้น",
            "เมื่อทั้ง p และ q จริง",
            "เมื่อทั้งคู่เท็จ"
        ],
        "answer": "เมื่อทั้ง p และ q จริง",
        "explanation": "ตัวเชื่อม AND ต้องจริงทั้งสองด้าน"
    },
    {
        "question": "p → q เป็นเท็จในกรณีใด",
        "choices": ["T → T", "T → F", "F → T", "F → F"],
        "answer": "T → F",
        "explanation": "อิมพลิเคชันเป็นเท็จเฉพาะกรณี T → F"
    },
    {
        "question": "ถ้ามีตัวแปร 3 ตัว จะมีตารางกี่แถว",
        "choices": ["3", "6", "8", "9"],
        "answer": "8",
        "explanation": "จำนวนแถวคือ 2³ = 8"
    },
    {
        "question": "p ∨ ¬p เป็นสูตรประเภทใด",
        "choices": [
            "สัจนิรันดร์",
            "ข้อขัดแย้ง",
            "ประพจน์ไม่แน่นอน"
        ],
        "answer": "สัจนิรันดร์",
        "explanation": "ไม่ว่า p จะเป็นจริงหรือเท็จ สูตรนี้เป็นจริงเสมอ"
    }
]


# ==================================================
# เมนูด้านซ้าย
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "หน้าแรก"

with st.sidebar:
    st.title("🧠 Math Logic")
    st.caption("Learning & Solver")
    st.markdown("---")

    if st.button("🏠 หน้าแรก", use_container_width=True):
        st.session_state.page = "หน้าแรก"

    with st.expander("📘 บทเรียน", expanded=True):
        for chapter, topics in LESSONS.items():
            with st.expander(chapter):
                for topic in topics:
                    if st.button(
                        topic,
                        key=f"{chapter}_{topic}",
                        use_container_width=True
                    ):
                        st.session_state.page = (
                            f"lesson::{chapter}::{topic}"
                        )

    with st.expander("🧮 เครื่องมือคำนวณ"):
        for name in [
            "คำนวณค่าความจริง",
            "ตารางค่าความจริง",
            "ตรวจประเภทสูตร",
            "ตรวจความสมมูล",
            "ตรวจการอ้างเหตุผล"
        ]:
            if st.button(name, key=f"tool_{name}", use_container_width=True):
                st.session_state.page = name

    with st.expander("🎮 แบบฝึกฝน"):
        for name in [
            "แบบฝึกหัด",
            "เกมจับคู่",
            "แบบทดสอบ",
            "ตัวอย่างต้นไม้ความจริง"
        ]:
            if st.button(name, key=f"practice_{name}", use_container_width=True):
                st.session_state.page = name

    with st.expander("📚 คลังความรู้"):
        if st.button("รวมสูตรตรรกศาสตร์", use_container_width=True):
            st.session_state.page = "รวมสูตรตรรกศาสตร์"

        if st.button("เกี่ยวกับเว็บไซต์", use_container_width=True):
            st.session_state.page = "เกี่ยวกับเว็บไซต์"

page = st.session_state.page


# ==================================================
# หน้าแรก
# ==================================================

if page == "หน้าแรก":
    st.markdown("""
    <div class="logic-card">
        <h1>🧠 Math Logic Learning & Solver</h1>
        <h3>เรียนรู้ตรรกศาสตร์ให้เข้าใจง่ายขึ้น</h3>
        <p>เว็บไซต์บทเรียน เครื่องมือคำนวณ และแบบฝึกหัด
        สำหรับการเรียนตรรกศาสตร์คณิตศาสตร์</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="logic-card">
        <h3>📘 บทเรียน</h3>
        <p>เรียนรู้แนวคิดพื้นฐานและตัวดำเนินการ</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="logic-card">
        <h3>📊 ตารางค่าความจริง</h3>
        <p>สร้างและตรวจสอบผลลัพธ์ของสูตร</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="logic-card">
        <h3>🎮 ฝึกฝน</h3>
        <p>ทำแบบฝึกหัดและแบบทดสอบ</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("สัญลักษณ์ตรรกศาสตร์ที่ควรรู้")

    st.dataframe(
        pd.DataFrame([
            ["¬p", "นิเสธ", "ไม่ p"],
            ["p ∧ q", "และ", "จริงเมื่อทั้งคู่จริง"],
            ["p ∨ q", "หรือ", "เท็จเมื่อทั้งคู่เท็จ"],
            ["p → q", "ถ้า...แล้ว", "เท็จเฉพาะ T → F"],
            ["p ↔ q", "ก็ต่อเมื่อ", "จริงเมื่อค่าตรงกัน"]
        ], columns=["สัญลักษณ์", "ชื่อ", "ความหมาย"]),
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# หน้าเรียนบทเรียน
# ==================================================

elif page.startswith("lesson::"):
    _, chapter, topic = page.split("::", 2)

    st.title(chapter)
    st.subheader(topic)

    st.markdown(
        f'<div class="logic-card">{LESSONS[chapter][topic]}</div>',
        unsafe_allow_html=True
    )

    if st.button("กลับหน้าแรก"):
        st.session_state.page = "หน้าแรก"
        st.rerun()


# ==================================================
# คำนวณค่าความจริง
# ==================================================

elif page == "คำนวณค่าความจริง":
    st.title("🧮 คำนวณค่าความจริง")

    formula = st.text_input(
        "ใส่สูตรตรรกศาสตร์",
        value="(p ∧ q) → ¬r"
    )

    try:
        node = parse_formula(formula)
        vars_ = sorted(get_variables(node))
        values = {}

        st.write("กำหนดค่าความจริง")

        columns = st.columns(max(1, len(vars_)))

        for i, variable in enumerate(vars_):
            with columns[i]:
                choice = st.selectbox(
                    f"ค่า {variable}",
                    ["T (จริง)", "F (เท็จ)"],
                    key=f"value_{variable}"
                )
                values[variable] = choice == "T (จริง)"

        if st.button("คำนวณ", type="primary"):
            result = evaluate(node, values)
            st.success(
                "ผลลัพธ์: " + ("T (จริง)" if result else "F (เท็จ)")
            )

    except LogicError as error:
        st.error(str(error))


# ==================================================
# ตารางค่าความจริง
# ==================================================

elif page == "ตารางค่าความจริง":
    st.title("📊 ตารางค่าความจริง")

    formula = st.text_input("ใส่สูตร", value="p → q")

    if st.button("สร้างตาราง", type="primary"):
        try:
            node = parse_formula(formula)
            variables, rows = truth_table([node])

            st.write(f"ตัวแปร: {', '.join(variables)}")
            st.dataframe(
                pd.DataFrame(rows),
                use_container_width=True,
                hide_index=True
            )

        except LogicError as error:
            st.error(str(error))


# ==================================================
# ตรวจประเภทสูตร
# ==================================================

elif page == "ตรวจประเภทสูตร":
    st.title("🔎 ตรวจประเภทสูตร")

    formula = st.text_input("สูตรที่ต้องการตรวจ", value="p ∨ ¬p")

    if st.button("ตรวจสอบ", type="primary"):
        try:
            node = parse_formula(formula)
            result = classify_formula(node)

            st.success(result)

            _, rows = truth_table([node])
            st.dataframe(
                pd.DataFrame(rows),
                use_container_width=True,
                hide_index=True
            )

        except LogicError as error:
            st.error(str(error))


# ==================================================
# ตรวจความสมมูล
# ==================================================

elif page == "ตรวจความสมมูล":
    st.title("⚖️ ตรวจสอบความสมมูล")

    formula1 = st.text_input("สูตรที่ 1", value="p → q")
    formula2 = st.text_input("สูตรที่ 2", value="¬p ∨ q")

    if st.button("เปรียบเทียบ", type="primary"):
        try:
            node1 = parse_formula(formula1)
            node2 = parse_formula(formula2)

            _, rows = truth_table([node1, node2])

            equivalent = all(
                row["ผลลัพธ์ 1"] == row["ผลลัพธ์ 2"]
                for row in rows
            )

            if equivalent:
                st.success("สูตรทั้งสองสมมูลกัน")
            else:
                st.error("สูตรทั้งสองไม่สมมูลกัน")

            st.dataframe(
                pd.DataFrame(rows),
                use_container_width=True,
                hide_index=True
            )

        except LogicError as error:
            st.error(str(error))


# ==================================================
# ตรวจการอ้างเหตุผล
# ==================================================

elif page == "ตรวจการอ้างเหตุผล":
    st.title("🧩 ตรวจสอบการอ้างเหตุผล")

    premises_text = st.text_area(
        "เหตุ (หนึ่งสูตรต่อหนึ่งบรรทัด)",
        value="p → q\np"
    )

    conclusion = st.text_input("ข้อสรุป", value="q")

    if st.button("ตรวจสอบ", type="primary"):
        try:
            premises = [
                line.strip()
                for line in premises_text.splitlines()
                if line.strip()
            ]

            premise_nodes = [
                parse_formula(item) for item in premises
            ]
            conclusion_node = parse_formula(conclusion)

            nodes = premise_nodes + [conclusion_node]
            _, rows = truth_table(nodes)

            counterexamples = []

            for row in rows:
                all_premises_true = all(
                    row[f"ผลลัพธ์ {i+1}"] == "T"
                    for i in range(len(premise_nodes))
                )

                conclusion_false = (
                    row[f"ผลลัพธ์ {len(nodes)}"] == "F"
                )

                if all_premises_true and conclusion_false:
                    counterexamples.append(row)

            if counterexamples:
                st.error("การอ้างเหตุผลไม่สมเหตุสมผล")
                st.write("พบกรณีโต้แย้งดังนี้")
                st.dataframe(
                    pd.DataFrame(counterexamples),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.success("การอ้างเหตุผลสมเหตุสมผล")

            with st.expander("ดูตารางค่าความจริงทั้งหมด"):
                st.dataframe(
                    pd.DataFrame(rows),
                    use_container_width=True,
                    hide_index=True
                )

        except LogicError as error:
            st.error(str(error))


# ==================================================
# แบบฝึกหัด
# ==================================================

elif page == "แบบฝึกหัด":
    st.title("✍️ แบบฝึกหัดตรรกศาสตร์")

    exercise = st.selectbox(
        "เลือกข้อ",
        [
            "ข้อ 1: นิเสธ",
            "ข้อ 2: ตัวเชื่อม AND",
            "ข้อ 3: อิมพลิเคชัน",
            "ข้อ 4: จำนวนแถว",
            "ข้อ 5: สัจนิรันดร์"
        ]
    )

    exercises = {
        "ข้อ 1: นิเสธ": (
            "ถ้า p เป็น F แล้ว ¬p เป็นอะไร",
            ["T", "F"],
            "T",
            "นิเสธมีค่าตรงข้ามกับ p"
        ),
        "ข้อ 2: ตัวเชื่อม AND": (
            "T ∧ F มีค่าเท่าใด",
            ["T", "F"],
            "F",
            "AND จะจริงเมื่อทั้งสองส่วนจริงเท่านั้น"
        ),
        "ข้อ 3: อิมพลิเคชัน": (
            "F → F มีค่าเท่าใด",
            ["T", "F"],
            "T",
            "อิมพลิเคชันเป็นเท็จเฉพาะ T → F"
        ),
        "ข้อ 4: จำนวนแถว": (
            "มีตัวแปร 4 ตัว ตารางมีกี่แถว",
            ["4", "8", "16", "32"],
            "16",
            "จำนวนแถวคือ 2⁴ = 16"
        ),
        "ข้อ 5: สัจนิรันดร์": (
            "สูตรใดเป็นสัจนิรันดร์",
            ["p ∧ ¬p", "p ∨ ¬p", "p ∧ q"],
            "p ∨ ¬p",
            "p ∨ ¬p เป็นจริงเสมอ"
        )
    }

    question, choices, answer, explanation = exercises[exercise]

    st.subheader(question)

    response = st.radio(
        "เลือกคำตอบ",
        choices,
        key="exercise_response"
    )

    if st.button("ตรวจคำตอบ", type="primary"):
        if response == answer:
            st.success("ถูกต้อง! 🎉")
        else:
            st.error(f"คำตอบที่ถูกต้องคือ {answer}")

        st.info(explanation)


# ==================================================
# เกมจับคู่
# ==================================================

elif page == "เกมจับคู่":
    st.title("🎮 เกมจับคู่ตัวดำเนินการ")

    pairs = {
        "¬": "นิเสธ",
        "∧": "และ",
        "∨": "หรือ",
        "→": "ถ้า...แล้ว",
        "↔": "ก็ต่อเมื่อ"
    }

    symbol = st.selectbox("เลือกสัญลักษณ์", list(pairs.keys()))

    meaning = st.radio(
        "เลือกความหมาย",
        ["นิเสธ", "และ", "หรือ", "ถ้า...แล้ว", "ก็ต่อเมื่อ"]
    )

    if st.button("ตรวจคำตอบ", type="primary"):
        if pairs[symbol] == meaning:
            st.success("จับคู่ถูกต้อง! ⭐")
        else:
            st.error(f"{symbol} หมายถึง {pairs[symbol]}")


# ==================================================
# แบบทดสอบ
# ==================================================

elif page == "แบบทดสอบ":
    st.title("📝 แบบทดสอบตรรกศาสตร์")

    answers = []

    for index, question in enumerate(QUESTIONS):
        st.markdown(f"**ข้อ {index + 1}. {question['question']}**")

        answer = st.radio(
            "เลือกคำตอบ",
            question["choices"],
            key=f"quiz_{index}"
        )

        answers.append(answer)

    if st.button("ส่งคำตอบ", type="primary"):
        score = 0

        for index, question in enumerate(QUESTIONS):
            if answers[index] == question["answer"]:
                score += 1

        st.metric("คะแนน", f"{score} / {len(QUESTIONS)}")

        for index, question in enumerate(QUESTIONS):
            if answers[index] == question["answer"]:
                st.success(f"ข้อ {index + 1}: ถูกต้อง")
            else:
                st.error(
                    f"ข้อ {index + 1}: "
                    f"คำตอบคือ {question['answer']}"
                )

            st.caption(question["explanation"])


# ==================================================
# ตัวอย่างต้นไม้ความจริง
# ==================================================

elif page == "ตัวอย่างต้นไม้ความจริง":
    st.title("🌳 ตัวอย่างต้นไม้ความจริง")

    st.markdown("""
    <div class="logic-card">
        <h3>ตัวอย่าง: p ∧ ¬p</h3>
        <p>1. เริ่มจากสูตร p ∧ ¬p</p>
        <p>2. ตัวเชื่อม ∧ กำหนดให้ทั้ง p และ ¬p ต้องเป็นจริง</p>
        <p>3. จะได้ p และ ¬p อยู่ในกิ่งเดียวกัน</p>
        <p>4. ทั้งสองข้อความขัดแย้งกัน กิ่งจึงปิด</p>
        <h3>สรุป: p ∧ ¬p เป็นข้อขัดแย้ง</h3>
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# รวมสูตร
# ==================================================

elif page == "รวมสูตรตรรกศาสตร์":
    st.title("📚 รวมสูตรตรรกศาสตร์")

    formula_groups = {
        "ตัวดำเนินการ": [
            "¬p : นิเสธของ p",
            "p ∧ q : p และ q",
            "p ∨ q : p หรือ q",
            "p → q : ถ้า p แล้ว q",
            "p ↔ q : p ก็ต่อเมื่อ q"
        ],

        "สมมูลพื้นฐาน": [
            "p → q ≡ ¬p ∨ q",
            "p ↔ q ≡ (p → q) ∧ (q → p)",
            "¬(p ∧ q) ≡ ¬p ∨ ¬q",
            "¬(p ∨ q) ≡ ¬p ∧ ¬q"
        ],

        "กฎสำคัญ": [
            "p ∧ T ≡ p",
            "p ∨ F ≡ p",
            "p ∧ F ≡ F",
            "p ∨ T ≡ T",
            "p ∨ ¬p ≡ T",
            "p ∧ ¬p ≡ F"
        ],

        "กฎการอ้างเหตุผล": [
            "Modus Ponens: p → q, p ∴ q",
            "Modus Tollens: p → q, ¬q ∴ ¬p"
        ]
    }

    for category, formulas in formula_groups.items():
        with st.expander(category, expanded=True):
            for formula in formulas:
                st.code(formula)


# ==================================================
# เกี่ยวกับเว็บไซต์
# ==================================================

elif page == "เกี่ยวกับเว็บไซต์":
    st.title("ℹ️ เกี่ยวกับเว็บไซต์")

    st.markdown("""
    <div class="logic-card">
        <h3>Math Logic Learning & Solver</h3>
        <p>เว็บไซต์สำหรับเรียนรู้และทบทวนตรรกศาสตร์คณิตศาสตร์</p>
        <p><b>เครื่องมือ:</b> Python, Streamlit และ Pandas</p>
        <p><b>ธีม:</b> Pastel Blue</p>
        <p><b>เนื้อหา:</b> ประพจน์ ตัวดำเนินการ ตารางค่าความจริง
        สัจนิรันดร์ ความสมมูล และการอ้างเหตุผล</p>
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# หน้าสำรอง
# ==================================================

else:
    st.warning("ไม่พบหน้าที่เลือก กรุณาเลือกเมนูจากแถบด้านซ้าย")

st.markdown("---")
st.caption("Math Logic Learning & Solver | Pastel Blue Edition")
