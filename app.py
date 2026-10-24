import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mathematical Logic Interactive App",
    page_icon="🧮",
    layout="wide"
)

st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; }
    .sub-title { font-size: 16px; color: #4B5563; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Main Navigation
# ---------------------------------------------------------
st.sidebar.title("📚 บทเรียนตรรกศาสตร์")
main_menu = st.sidebar.radio(
    "เลือกบทเรียนหลัก:",
    [
        "หน้าแรก & ข้อมูลรายงาน",
        "Chapter 1: Introduction to Logic",
        "Chapter 2: Connectives & Truth Tables",
        "Chapter 3: Tautologies",
        "Chapter 4: Arguments",
        "Chapter 5: Quantifiers",
        "Chapter 6: Inductive & Deductive",
        "References (เอกสารอ้างอิง)"
    ]
)

# ---------------------------------------------------------
# 1. หน้าแรก & ข้อมูลรายงาน (Cover & Overview)
# ---------------------------------------------------------
if main_menu == "หน้าแรก & ข้อมูลรายงาน":
    st.markdown('<p class="main-title">Mathematical Logic Interactive Learning App</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">สื่อการเรียนรู้ออนไลน์วิชาตรรกศาสตร์เชิงคณิตศาสตร์ (English for Teaching Mathematics)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **ผู้จัดทำรายงาน:**
        * Ms. Nur-aima Mahae (ID 671107068)[cite: 9]
        
        **เสนอต่อ:**
        * Assistant Professor Dr. litiwat Tocharoennirattisa[cite: 9]
        
        **สังกัด:**
        * Faculty of Education Mathematics Department, University Rajabhat Thonburi[cite: 9]
        * Semester 1 Academic Year 2026[cite: 9]
        """)
    with col2:
        st.success("""
        ### 🎯 Preface & Objectives
        This report was prepared to learn and better understand Mathematical Logic, focusing on logical thinking, correct reasoning, propositions, truth tables, rules of inference, and mathematical proofs[cite: 10].
        """)

# ---------------------------------------------------------
# 2. Chapter 1
# ---------------------------------------------------------
elif main_menu == "Chapter 1: Introduction to Logic":
    st.markdown("## 📘 Chapter 1: Introduction to Mathematical Logic")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 1):", ["1.1 เนื้อหาและทฤษฎี", "1.2 สูตรและสัญลักษณ์", "1.3 ตัวอย่างการพิสูจน์ (Worked Proofs)", "1.4 แบบฝึกหัดทดสอบความเข้าใจ"])
    
    if sub_menu == "1.1 เนื้อหาและทฤษฎี":
        st.write("Mathematical logic studies the formal structure of valid reasoning. A proposition has exactly one truth value, true or false[cite: 13].")
    elif sub_menu == "1.2 สูตรและสัญลักษณ์":
        st.markdown("- **Atomic propositions:** $p, q, r, s$[cite: 12, 13]\n- **Modus Ponens:** จาก $p$ และ $p \\rightarrow q$ สรุป $q$[cite: 13]")
    elif sub_menu == "1.3 ตัวอย่างการพิสูจน์ (Worked Proofs)":
        st.markdown("### Proof 1.1: Chained inference with four propositions")
        st.markdown("Premises: $p \\rightarrow q, q \\rightarrow r, r \\rightarrow s, p$ | Prove: $s$[cite: 13]")
        st.markdown("### Proof 1.2: Indirect proof using three atoms")
        st.markdown("Premises: $p \\vee q, p \\rightarrow r, q \\rightarrow r$ | Prove: $r$[cite: 14]")
    elif sub_menu == "1.4 แบบฝึกหัดทดสอบความเข้าใจ":
        st.write("📝 **โจทย์ฝึกหัด:** จากเหตุ $p \\rightarrow q$ และ $p$ สามารถสรุปผลเป็น $q$ ได้ตามกฎใด?")
        ans = st.radio("เลือกคำตอบ:", ["Modus Ponens", "Modus Tollens"])
        if st.button("ส่งคำตอบ Ch 1"):
            if ans == "Modus Ponens":
                st.success("ถูกต้อง! เป็นกฎ Modus Ponens")
            else:
                st.error("ลองใหม่อีกครั้ง")

# ---------------------------------------------------------
# 3. Chapter 2
# ---------------------------------------------------------
elif main_menu == "Chapter 2: Connectives & Truth Tables":
    st.markdown("## 📘 Chapter 2: Logical Connectives and Truth Tables")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 2):", ["2.1 เนื้อหาและทฤษฎี", "2.2 สูตรและสมมูล", "2.3 ตัวอย่างการสร้างตาราง", "2.4 เครื่องมือคำนวณ Truth Table"])
    
    if sub_menu == "2.1 เนื้อหาและทฤษฎี":
        st.write("Negation ($\\neg$) reverses truth. Conjunction ($p \\wedge q$) is true only when both are true. Disjunction ($p \\vee q$) is false only when both are false[cite: 15].")
    elif sub_menu == "2.2 สูตรและสมมูล":
        st.markdown("- $A \\rightarrow B \\equiv \\neg A \\vee B$[cite: 15]\n- De Morgan's Laws: $\\neg(A \\wedge B) \\equiv \\neg A \\vee \\neg B$[cite: 15]")
    elif sub_menu == "2.3 ตัวอย่างการสร้างตาราง":
        st.write("A truth table for $n$ distinct atomic propositions contains $2^n$ rows[cite: 15].")
    elif sub_menu == "2.4 เครื่องมือคำนวณ Truth Table":
        st.subheader("⚡ คำนวณตารางค่าความจริงอัตโนมัติ")
        expr_input = st.text_input("ป้อนประพจน์ (เช่น (p & q) >> r):", value="(p & q) >> r")
        if st.button("สร้างตาราง"):
            try:
                expr = sp.sympify(expr_input)
                v_list = sorted([str(s) for s in expr.free_symbols])
                combos = list(itertools.product([True, False], repeat=len(v_list)))
                res_rows = []
                for cb in combos:
                    v_map = dict(zip([sp.Symbol(v) for v in v_list], cb))
                    val = bool(expr.subs(v_map))
                    res_rows.append(list(cb) + [val])
                st.dataframe(pd.DataFrame(res_rows, columns=v_list + ["Result"]), use_container_width=True)
            except Exception as e:
                st.error(f"รูปแบบประพจน์ไม่ถูกต้อง: {e}")

# ---------------------------------------------------------
# 4. Chapter 3
# ---------------------------------------------------------
elif main_menu == "Chapter 3: Tautologies":
    st.markdown("## 📘 Chapter 3: Tautologies")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 3):", ["3.1 เนื้อหาและทฤษฎี", "3.2 วิธีการตรวจสอบ", "3.3 ตัวอย่างโจทย์สัจนิรันดร์", "3.4 แบบฝึกหัดให้นักเรียนทำ"])
    
    if sub_menu == "3.1 เนื้อหาและทฤษฎี":
        st.write("A tautology is true under every truth assignment; a contradiction is false under every assignment[cite: 19].")
    elif sub_menu == "3.2 วิธีการตรวจสอบ":
        st.write("Construct a full truth table or assume its negation and derive a contradiction[cite: 19].")
    elif sub_menu == "3.3 ตัวอย่างโจทย์สัจนิรันดร์":
        st.markdown("Example: $[(p \\wedge q) \\rightarrow r] \\leftrightarrow [p \\rightarrow (q \\rightarrow r)]$ เป็นสัจนิรันดร์[cite: 24]")
    elif sub_menu == "3.4 แบบฝึกหัดให้นักเรียนทำ":
        st.write("📝 **โจทย์ฝึกหัด:** ประพจน์ $p \\vee \\neg p$ เป็นสัจนิรันดร์หรือไม่?")
        ans3 = st.radio("เลือกคำตอบ:", ["เป็นสัจนิรันดร์", "ไม่เป็นสัจนิรันดร์"])
        if st.button("ตรวจคำตอบ Ch 3"):
            if ans3 == "เป็นสัจนิรันดร์":
                st.success("ถูกต้อง! เป็นสัจนิรันดร์ (Law of Excluded Middle)")
            else:
                st.error("ลองใหม่อีกครั้ง")

# ---------------------------------------------------------
# 5. Chapter 4
# ---------------------------------------------------------
elif main_menu == "Chapter 4: Arguments":
    st.markdown("## 📘 Chapter 4: Arguments")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 4):", ["4.1 เนื้อหาและทฤษฎี", "4.2 รูปแบบการอ้างเหตุผล", "4.3 ตัวอย่างการพิสูจน์", "4.4 โจทย์ฝึกหัดความสมเหตุสมผล"])
    
    if sub_menu == "4.1 เนื้อหาและทฤษฎี":
        st.write("An argument consists of premises and a conclusion. An argument is valid if every interpretation satisfying the premises also satisfies the conclusion[cite: 25].")
    elif sub_menu == "4.2 รูปแบบการอ้างเหตุผล":
        st.markdown("- **Modus Ponens:** $A \\rightarrow B, A \\vdash B$[cite: 25]\n- **Modus Tollens:** $A \\rightarrow B, \\neg B \\vdash \\neg A$[cite: 25]")
    elif sub_menu == "4.3 ตัวอย่างการพิสูจน์":
        st.write("Proof 4.1: Resolution with conditional branches[cite: 25]")
    elif sub_menu == "4.4 โจทย์ฝึกหัดความสมเหตุสมผล":
        st.write("📝 **โจทย์ฝึกหัด:** หากกำหนดเหตุคือ $p \\rightarrow q$ และ $\\neg q$ ถามว่าข้อสรุป $\\neg p$ สมเหตุสมผลตามกฎใด?")
        ans4 = st.selectbox("เลือกกฎ:", ["Modus Ponens", "Modus Tollens", "Hypothetical Syllogism"])
        if st.button("ส่งคำตอบ Ch 4"):
            if ans4 == "Modus Tollens":
                st.success("ถูกต้องเยี่ยมมาก! เป็นกฎ Modus Tollens")
            else:
                st.error("ยังไม่ถูกต้อง ลองทบทวนดูอีกครั้ง")

# ---------------------------------------------------------
# 6. Chapter 5
# ---------------------------------------------------------
elif main_menu == "Chapter 5: Quantifiers":
    st.markdown("## 📘 Chapter 5: Open Sentences and Quantifiers")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 5):", ["5.1 เนื้อหาและทฤษฎี", "5.2 นิเสธตัวบ่งปริมาณ", "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ", "5.4 โจทย์คำถามสำหรับนักเรียน"])
    
    if sub_menu == "5.1 เนื้อหาและทฤษฎี":
        st.write("An open sentence $P(x)$ has a free variable. Universal quantifier $\\forall x P(x)$ and existential quantifier $\\exists x P(x)$[cite: 29].")
    elif sub_menu == "5.2 นิเสธตัวบ่งปริมาณ":
        st.markdown("- $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$[cite: 29]\n- $\\neg \\exists x P(x) \\equiv \\forall x \\neg P(x)$[cite: 29]")
    elif sub_menu == "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ":
        st.write("Quantifier order matters: $\\forall x \\exists y R(x,y)$ generally differs from $\\exists y \\forall x R(x,y)$[cite: 29].")
    elif sub_menu == "5.4 โจทย์คำถามสำหรับนักเรียน":
        st.write("📝 **โจทย์ฝึกหัด:** นิเสธของข้อความ $\\forall x P(x)$ คือข้อใด?")
        ans5 = st.radio("เลือกข้อ:", ["$\\exists x \\neg P(x)$", "$\\forall x \\neg P(x)$"])
        if st.button("ตรวจคำตอบ Ch 5"):
            if ans5 == "$\\exists x \\neg P(x)$":
                st.success("ถูกต้องที่สุด!")
            else:
                st.error("ลองทบทวนใหม่อีกครั้ง")

# ---------------------------------------------------------
# 7. Chapter 6
# ---------------------------------------------------------
elif main_menu == "Chapter 6: Inductive & Deductive":
    st.markdown("## 📘 Chapter 6: Inductive and Deductive Reasoning")
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 6):", ["6.1 เนื้อหาและทฤษฎี", "6.2 หลักการอุปนัยเชิงคณิตศาสตร์", "6.3 ตัวอย่างการพิสูจน์สูตรกำลังสาม", "6.4 เครื่องมือคำนวณและทดลอง"])
    
    if sub_menu == "6.1 เนื้อหาและทฤษฎี":
        st.write("Inductive reasoning generalizes from observed cases, whereas deductive reasoning establishes conclusions that necessarily follow from stated premises[cite: 32].")
    elif sub_menu == "6.2 หลักการอุปนัยเชิงคณิตศาสตร์":
        st.write("Mathematical induction requires a base case and a step showing $P(k) \\rightarrow P(k+1)$[cite: 32].")
    elif sub_menu == "6.3 ตัวอย่างการพิสูจน์สูตรกำลังสาม":
        st.markdown("Claim: $1^3 + 2^3 + \\dots + n^3 = [\\frac{n(n+1)}{2}]^2$[cite: 37]")
    elif sub_menu == "6.4 เครื่องมือคำนวณและทดลอง":
        st.subheader("🔢 ตัวจำลองการคำนวณสูตรผลบวกกำลังสาม")
        n_val = st.slider("เลือกค่า n:", 1, 15, 4)
        lhs = sum([i**3 for i in range(1, n_val+1)])
        rhs = int((n_val * (n_val + 1) / 2) ** 2)
        st.write(f"ผลลัพธ์ฝั่งซ้าย (LHS): {lhs}")
        st.write(f"ผลลัพธ์ฝั่งขวา (RHS): {rhs}")
        if lhs == rhs:
            st.success("✅ สมการเป็นจริงสอดคล้องกับการพิสูจน์ทางอุปนัยเชิงคณิตศาสตร์!")

# ---------------------------------------------------------
# 8. References
# ---------------------------------------------------------
elif main_menu == "References (เอกสารอ้างอิง)":
    st.markdown("## 📖 References / เอกสารอ้างอิง")
    st.markdown("""
    * **Epp, S. S. (2011).** *Discrete Mathematics with Applications* (4th ed.). Brooks/Cole[cite: 40].
    * **Rosen, K. H. (2019).** *Discrete Mathematics and Its Applications* (8th ed.). McGraw-Hill Education[cite: 40].
    * **Enderton, H. B. (2001).** *A Mathematical Introduction to Logic* (2nd ed.). Academic Press[cite: 40].
    * **Velleman, D. J. (2019).** *How to Prove It: A Structured Approach* (3rd ed.). Cambridge University Press[cite: 40].
    """)
