import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling (เพิ่มลูกเล่นและสีสัน)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mathematical Logic Interactive App",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 36px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #4F46E5, #9333EA);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 20px;
        color: #374151;
        font-weight: 600;
        border-left: 5px solid #4F46E5;
        padding-left: 12px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .card-box {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation with Style
# ---------------------------------------------------------
st.sidebar.markdown("### 🧭 เมนูนำทางบทเรียน")
main_menu = st.sidebar.radio(
    "เลือกหัวข้อหลัก:",
    [
        "🏠 หน้าแรก & ข้อมูลรายงาน",
        "📘 Chapter 1: Introduction",
        "📗 Chapter 2: Connectives & Tables",
        "📙 Chapter 3: Tautologies",
        "📕 Chapter 4: Arguments",
        "purple Chapter 5: Quantifiers",
        "📓 Chapter 6: Inductive & Deductive",
        "📚 References (เอกสารอ้างอิง)"
    ]
)

# ---------------------------------------------------------
# 1. หน้าแรก & ข้อมูลรายงาน
# ---------------------------------------------------------
if main_menu == "🏠 หน้าแรก & ข้อมูลรายงาน":
    st.markdown('<div class="main-header">✨ Mathematical Logic Interactive Learning Hub ✨</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h3>📌 รายละเอียดรายงาน (Report Details)</h3>
            <p><b>วิชา:</b> English for Teaching Mathematics[cite: 9]</p>
            <p><b>ผู้จัดทำ:</b> Ms. Nur-aima Mahae (ID 671107068)[cite: 9]</p>
            <p><b>เสนอต่อ:</b> Assistant Professor Dr. litiwat Tocharoennirattisa[cite: 9]</p>
            <p><b>สังกัด:</b> Faculty of Education Mathematics Department, University Rajabhat Thonburi[cite: 9]</p>
            <p><b>ปีการศึกษา:</b> Semester 1 Academic Year 2026[cite: 9]</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h3>🎯 วัตถุประสงค์และภาพรวม</h3>
            <p>แอปพลิเคชันนี้พัฒนาขึ้นเพื่อรวบรวมเนื้อหา ทฤษฎี สูตร ตัวอย่างการพิสูจน์ และแบบฝึกหัดโต้ตอบ (Interactive Exercises) ทั้ง 6 บท ตามรายงานตรรกศาสตร์เชิงคณิตศาสตร์ เพื่อส่งเสริมการเรียนรู้ที่เข้าใจง่ายและสนุกสนานยิ่งขึ้น[cite: 10, 11]</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. Chapter 1
# ---------------------------------------------------------
elif main_menu == "📘 Chapter 1: Introduction":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #2563EB, #1D4ED8);">📘 Chapter 1: Introduction to Mathematical Logic</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["1.1 เนื้อหาและทฤษฎี", "1.2 สูตรและสัญลักษณ์", "1.3 ตัวอย่างการพิสูจน์", "1.4 แบบฝึกหัดทดสอบ"])
    
    if sub_menu == "1.1 เนื้อหาและทฤษฎี":
        st.info("Mathematical logic studies the formal structure of valid reasoning. A proposition has exactly one truth value, true or false.")[cite: 13]
    elif sub_menu == "1.2 สูตรและสัญลักษณ์":
        st.markdown("- **Atomic propositions:** $p, q, r, s$[cite: 12, 13]\n- **Modus Ponens:** จาก $p$ และ $p \\rightarrow q$ สรุป $q$[cite: 13]")
    elif sub_menu == "1.3 ตัวอย่างการพิสูจน์":
        st.success("**Proof 1.1:** Chained inference with four propositions ($p \\rightarrow q, q \\rightarrow r, r \\rightarrow s, p \\vdash s$)[cite: 13]")
    elif sub_menu == "1.4 แบบฝึกหัดทดสอบ":
        st.markdown('<p class="sub-header">📝 ทดสอบความเข้าใจ</p>', unsafe_allow_html=True)
        ans = st.radio("จากเหตุ $p \\rightarrow q$ และ $p$ สามารถสรุปผลเป็น $q$ ได้ตามกฎใด?", ["Modus Ponens", "Modus Tollens"])
        if st.button("ส่งคำตอบ Ch 1"):
            if ans == "Modus Ponens":
                st.balloons()
                st.success("🎉 ถูกต้องเยี่ยมมาก! เป็นกฎ Modus Ponens")
            else:
                st.error("❌ ยังไม่ถูกต้อง ลองใหม่อีกครั้งนะ")

# ---------------------------------------------------------
# 3. Chapter 2
# ---------------------------------------------------------
elif main_menu == "📗 Chapter 2: Connectives & Tables":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 Chapter 2: Logical Connectives and Truth Tables</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["2.1 เนื้อหาและทฤษฎี", "2.2 สูตรและสมมูล", "2.3 ตัวอย่างการสร้างตาราง", "2.4 เครื่องมือคำนวณ Truth Table"])
    
    if sub_menu == "2.1 เนื้อหาและทฤษฎี":
        st.info("Negation ($\\neg$) reverses truth. Conjunction ($p \\wedge q$) is true only when both are true. Disjunction ($p \\vee q$) is false only when both are false.")[cite: 15]
    elif sub_menu == "2.2 สูตรและสมมูล":
        st.markdown("- $A \\rightarrow B \\equiv \\neg A \\vee B$[cite: 15]\n- De Morgan's Laws: $\\neg(A \\wedge B) \\equiv \\neg A \\vee \\neg B$[cite: 15]")
    elif sub_menu == "2.3 ตัวอย่างการสร้างตาราง":
        st.success("A truth table for $n$ distinct atomic propositions contains $2^n$ rows.")[cite: 15]
    elif sub_menu == "2.4 เครื่องมือคำนวณ Truth Table":
        st.markdown('<p class="sub-header">⚡ โปรแกรมสร้างตารางค่าความจริงอัตโนมัติ</p>', unsafe_allow_html=True)
        expr_input = st.text_input("ป้อนประพจน์ (เช่น (p & q) >> r):", value="(p & q) >> r")
        if st.button("🚀 คำนวณตาราง"):
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
elif main_menu == "📙 Chapter 3: Tautologies":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 Chapter 3: Tautologies</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["3.1 เนื้อหาและทฤษฎี", "3.2 วิธีการตรวจสอบ", "3.3 ตัวอย่างโจทย์สัจนิรันดร์", "3.4 แบบฝึกหัดให้นักเรียนทำ"])
    
    if sub_menu == "3.1 เนื้อหาและทฤษฎี":
        st.info("A tautology is true under every truth assignment; a contradiction is false under every assignment.")[cite: 19]
    elif sub_menu == "3.2 วิธีการตรวจสอบ":
        st.markdown("Construct a full truth table or assume its negation and derive a contradiction.")[cite: 19]
    elif sub_menu == "3.3 ตัวอย่างโจทย์สัจนิรันดร์":
        st.success("Example: $[(p \\wedge q) \\rightarrow r] \\leftrightarrow [p \\rightarrow (q \\rightarrow r)]$ เป็นสัจนิรันดร์")[cite: 24]
    elif sub_menu == "3.4 แบบฝึกหัดให้นักเรียนทำ":
        st.markdown('<p class="sub-header">📝 ทดสอบความเข้าใจ</p>', unsafe_allow_html=True)
        ans3 = st.radio("ประพจน์ $p \\vee \\neg p$ เป็นสัจนิรันดร์หรือไม่?", ["เป็นสัจนิรันดร์", "ไม่เป็นสัจนิรันดร์"])
        if st.button("ส่งคำตอบ Ch 3"):
            if ans3 == "เป็นสัจนิรันดร์":
                st.balloons()
                st.success("🎉 ถูกต้อง! เป็น Law of Excluded Middle")
            else:
                st.error("❌ ผิดพลาด ลองใหม่อีกครั้ง")

# ---------------------------------------------------------
# 5. Chapter 4
# ---------------------------------------------------------
elif main_menu == "📕 Chapter 4: Arguments":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 Chapter 4: Arguments</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["4.1 เนื้อหาและทฤษฎี", "4.2 รูปแบบการอ้างเหตุผล", "4.3 ตัวอย่างการพิสูจน์", "4.4 โจทย์ฝึกหัดความสมเหตุสมผล"])
    
    if sub_menu == "4.1 เนื้อหาและทฤษฎี":
        st.info("An argument consists of premises and a conclusion. An argument is valid if every interpretation satisfying the premises also satisfies the conclusion.")[cite: 25]
    elif sub_menu == "4.2 รูปแบบการอ้างเหตุผล":
        st.markdown("- **Modus Ponens:** $A \\rightarrow B, A \\vdash B$[cite: 25]\n- **Modus Tollens:** $A \\rightarrow B, \\neg B \\vdash \\neg A$[cite: 25]")
    elif sub_menu == "4.3 ตัวอย่างการพิสูจน์":
        st.success("Proof 4.1: Resolution with conditional branches")[cite: 25]
    elif sub_menu == "4.4 โจทย์ฝึกหัดความสมเหตุสมผล":
        st.markdown('<p class="sub-header">📝 ทดสอบความเข้าใจ</p>', unsafe_allow_html=True)
        ans4 = st.selectbox("หากกำหนดเหตุคือ $p \\rightarrow q$ และ $\\neg q$ ถามว่าข้อสรุป $\\neg p$ สมเหตุสมผลตามกฎใด?", ["Modus Ponens", "Modus Tollens", "Hypothetical Syllogism"])
        if st.button("ส่งคำตอบ Ch 4"):
            if ans4 == "Modus Tollens":
                st.balloons()
                st.success("🎉 ถูกต้องเยี่ยมมาก! นี่ือกฎ Modus Tollens")
            else:
                st.error("❌ ยังไม่ถูกต้อง ลองทบทวนดูอีกครั้งนะ")

# ---------------------------------------------------------
# 6. Chapter 5
# ---------------------------------------------------------
elif main_menu == "purple Chapter 5: Quantifiers":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 Chapter 5: Open Sentences and Quantifiers</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["5.1 เนื้อหาและทฤษฎี", "5.2 นิเสธตัวบ่งปริมาณ", "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ", "5.4 โจทย์คำถามสำหรับนักเรียน"])
    
    if sub_menu == "5.1 เนื้อหาและทฤษฎี":
        st.info("An open sentence $P(x)$ has a free variable. Universal quantifier $\\forall x P(x)$ and existential quantifier $\\exists x P(x)$.")[cite: 29]
    elif sub_menu == "5.2 นิเสธตัวบ่งปริมาณ":
        st.markdown("- $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$[cite: 29]\n- $\\neg \\exists x P(x) \\equiv \\forall x \\neg P(x)$[cite: 29]")
    elif sub_menu == "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ":
        st.success("Quantifier order matters: $\\forall x \\exists y R(x,y)$ generally differs from $\\exists y \\forall x R(x,y)$.")[cite: 29]
    elif sub_menu == "5.4 โจทย์คำถามสำหรับนักเรียน":
        st.markdown('<p class="sub-header">📝 ทดสอบความเข้าใจ</p>', unsafe_allow_html=True)
        ans5 = st.radio("นิเสธของข้อความ $\\forall x P(x)$ คือข้อใด?", ["$\\exists x \\neg P(x)$", "$\\forall x \\neg P(x)$"])
        if st.button("ส่งคำตอบ Ch 5"):
            if ans5 == "$\\exists x \\neg P(x)$":
                st.balloons()
                st.success("🎉 ถูกต้องที่สุด!")
            else:
                st.error("❌ ลองทบทวนใหม่อีกครั้ง")

# ---------------------------------------------------------
# 7. Chapter 6
# ---------------------------------------------------------
elif main_menu == "📓 Chapter 6: Inductive & Deductive":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 Chapter 6: Inductive and Deductive Reasoning</div>', unsafe_allow_html=True)
    sub_menu = st.selectbox("📌 เลือกหัวข้อย่อย:", ["6.1 เนื้อหาและทฤษฎี", "6.2 หลักการอุปนัยเชิงคณิตศาสตร์", "6.3 ตัวอย่างการพิสูจน์สูตรกำลังสาม", "6.4 เครื่องมือคำนวณและทดลอง"])
    
    if sub_menu == "6.1 เนื้อหาและทฤษฎี":
        st.info("Inductive reasoning generalizes from observed cases, whereas deductive reasoning establishes conclusions that necessarily follow from stated premises.")[cite: 32]
    elif sub_menu == "6.2 หลักการอุปนัยเชิงคณิตศาสตร์":
        st.markdown("Mathematical induction requires a base case and a step showing $P(k) \\rightarrow P(k+1)$.")[cite: 32]
    elif sub_menu == "6.3 ตัวอย่างการพิสูจน์สูตรกำลังสาม":
        st.success("Claim: $1^3 + 2^3 + \\dots + n^3 = [\\frac{n(n+1)}{2}]^2$")[cite: 37]
    elif sub_menu == "6.4 เครื่องมือคำนวณและทดลอง":
        st.markdown('<p class="sub-header">🔢 ตัวจำลองการคำนวณสูตรผลบวกกำลังสาม</p>', unsafe_allow_html=True)
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
elif main_menu == "📚 References (เอกสารอ้างอิง)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #475569, #334155);">📚 References / เอกสารอ้างอิง</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <ul>
            <li><b>Epp, S. S. (2011).</b> <i>Discrete Mathematics with Applications</i> (4th ed.). Brooks/Cole.[cite: 40]</li>
            <li><b>Rosen, K. H. (2019).</b> <i>Discrete Mathematics and Its Applications</i> (8th ed.). McGraw-Hill Education.[cite: 40]</li>
            <li><b>Enderton, H. B. (2001).</b> <i>A Mathematical Introduction to Logic</i> (2nd ed.). Academic Press.[cite: 40]</li>
            <li><b>Velleman, D. J. (2019).</b> <i>How to Prove It: A Structured Approach</i> (3rd ed.). Cambridge University Press.[cite: 40]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
