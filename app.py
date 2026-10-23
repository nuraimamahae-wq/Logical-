import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mathematical Logic Interactive Learning App",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 32px;
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
        color: #1E3A8A;
        font-weight: 700;
        border-left: 5px solid #4F46E5;
        padding-left: 12px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .card-box {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 15px;
    }
    .solution-box {
        background-color: #ECFDF5;
        border: 1px solid #10B981;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.markdown("### 🧭 เมนูบทเรียนตรรกศาสตร์")
main_menu = st.sidebar.radio(
    "เลือกหัวข้อหลัก:",
    [
        "🏠 หน้าแรก & ข้อมูลรายงาน",
        "📘 บทที่ 1: ประพจน์และการให้เหตุผล",
        "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง",
        "📙 บทที่ 3: สัจนิรันดร์ (Tautologies)",
        "📕 บทที่ 4: การอ้างเหตุผล (Arguments)",
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ",
        "📓 บทที่ 6: การอุปนัยและนิรนัย",
        "📝 เฉลยแบบฝึกหัดท้ายบททั้งหมด",
        "📐 สรุปสูตรรวมทั้งหมด",
        "⚡ เครื่องมือคำนวณอัจฉริยะ",
        "📚 เอกสารอ้างอิง"
    ]
)

# ---------------------------------------------------------
# 1. หน้าแรก
# ---------------------------------------------------------
if main_menu == "🏠 หน้าแรก & ข้อมูลรายงาน":
    st.markdown('<div class="main-header">✨ สื่อการเรียนรู้ออนไลน์ วิชาตรรกศาสตร์เชิงคณิตศาสตร์ ✨</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h3>📌 รายละเอียดรายงาน</h3>
            <p><b>วิชา:</b> English for Teaching Mathematics[cite: 6]</p>
            <p><b>ผู้จัดทำ:</b> Ms. Nur-aima Mahae[cite: 6]</p>
            <p><b>เสนอต่อ:</b> Assistant Professor Dr. litiwat Tocharoennirattisa[cite: 6]</p>
            <p><b>สังกัด:</b> คณะครุศาสตร์ สาขาคณิตศาสตร์ มหาวิทยาลัยราชภัฏธนบุรี[cite: 6]</p>
            <p><b>ปีการศึกษา:</b> ภาคเรียนที่ 1 ปีการศึกษา 2026[cite: 6]</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h3>🎯 วัตถุประสงค์ของแอปพลิเคชัน</h3>
            <p>แอปพลิเคชันนี้รวบรวมเนื้อหาตรรกศาสตร์เชิงคณิตศาสตร์ทั้ง 6 บทแบบเจาะลึก พร้อมตัวอย่าง 3 ข้อพร้อมเฉลยในแต่ละบท, โจทย์ฝึกหัด 2 ข้อ, และสรุปสูตรประจำบทเพื่อเสริมสร้างความเข้าใจที่สมบูรณ์[cite: 7, 8]</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. บทที่ 1
# ---------------------------------------------------------
elif main_menu == "📘 บทที่ 1: ประพจน์และการให้เหตุผล":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #2563EB, #1D4ED8);">📘 บทที่ 1: บทนำตรรกศาสตร์เชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง (True) หรือเท็จ (False) อย่างใดอย่างหนึ่ง ประพจน์เชิงเดี่ยวแทนด้วยตัวอักษร $p, q, r, s$ ส่วนประพจน์เชิงซ้อนสร้างขึ้นผ่านตัวเชื่อมทางตรรกศาสตร์[cite: 10]</p>
        <p><b>หลักการพิสูจน์ (Syntax & Semantics):</b> การตรวจสอบความสมเหตุสมผลพิจารณาว่าข้อสรุปต้องเป็นจริงเสมอเมื่อเหตุทุกข้อเป็นจริง[cite: 10]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 1</h4>
        <ul>
            <li><b>Modus Ponens:</b> $p, p \rightarrow q \vdash q$[cite: 10]</li>
            <li><b>Modus Tollens:</b> $p \rightarrow q, \neg q \vdash \neg p$[cite: 14]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 1)")
    st.markdown("<b>ตัวอย่าง 1.1:</b> จงพิจารณาว่าประโยค 'กรุงเทพมหานครเป็นเมืองหลวงของประเทศไทย' เป็นประพจน์หรือไม่ และมีค่าความจริงเป็นอย่างไร?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นประพจน์ เพราะเป็นประโยคบอกเล่าที่มีค่าความจริงเป็น <b>จริง (True)</b>[cite: 10]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 1.2:</b> กำหนดให้ประพจน์ $p$ แทน 'ฝนตก' และ $q$ แทน 'ถนนเปียก' หากทราบว่า $p$ เป็นจริง และ $p \rightarrow q$ เป็นจริง จงหาค่าความจริงของ $q$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> จากกฎ Modus Ponens ($p$ และ $p \rightarrow q$ สรุป $q$) จะได้ว่า $q$ มีค่าความจริงเป็น <b>จริง (True)</b>[cite: 10]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 1.3:</b> กำหนดให้เหตุคือ $p \rightarrow q$ และ $\neg q$ จงหาข้อสรุปตามกฎการให้เหตุผล")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ใช้กฎ Modus Tollens จะสามารถสรุปผลได้ว่า <b>$\neg p$</b> (ไม่ใช่ $p$)[cite: 14]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 1)")
    st.markdown("1. ประโยค 'โปรดปิดประตูหน้าต่าง' เป็นประพจน์ทางตรรกศาสตร์หรือไม่ เพราะเหตุใด?")
    st.markdown("2. กำหนดเหตุ: $p \rightarrow r$ และ $p$ จงหาข้อสรุปที่สมเหตุสมผล")

# ---------------------------------------------------------
# 3. บทที่ 2
# ---------------------------------------------------------
elif main_menu == "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p>ตัวเชื่อมทางตรรกศาสตร์หลัก: นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การimplie ($\rightarrow$), และสมมูล ($\leftrightarrow$) ตารางค่าความจริงของประพจน์ที่มี $n$ ตัวแปรจะมีทั้งหมด $2^n$ แถว[cite: 12]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 2</h4>
        <ul>
            <li><b>Implication Equivalence:</b> $A \rightarrow B \equiv \neg A \vee B$[cite: 12]</li>
            <li><b>De Morgan's Laws:</b> $\neg(A \wedge B) \equiv \neg A \vee \neg B$ และ $\neg(A \vee B) \equiv \neg A \wedge \neg B$[cite: 12]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 2)")
    st.markdown("<b>ตัวอย่าง 2.1:</b> กำหนดให้ $p$ เป็นจริง และ $q$ เป็นเท็จ จงหาค่าความจริงของ $p \wedge q$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ตัวเชื่อม และ ($\wedge$) จะเป็นจริงก็ต่อเมื่อประพจน์ย่อยเป็นจริงทั้งคู่ ดังนั้น $T \wedge F \equiv$ <b>เท็จ (False)</b>[cite: 12]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 2.2:</b> จงแปลงประพจน์ $p \rightarrow q$ ให้เป็นรูปdisjunction (หรือ)")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ใช้สูตรสมมูลการimplie จะได้ $\neg p \vee q$[cite: 12]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 2.3:</b> ประพจน์ $\neg(p \wedge q)$ สมมูลกับประพจน์ใดตามกฎเดอมอร์แกน")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมูลกับ $\neg p \vee \neg q$[cite: 12]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 2)")
    st.markdown("1. จงสร้างตารางค่าความจริงของประพจน์ $p \vee (q \wedge \neg p)$")
    st.markdown("2. จงหาประพจน์ที่สมมูลกับ $\neg(p \vee q)$")

# ---------------------------------------------------------
# 4. บทที่ 3
# ---------------------------------------------------------
elif main_menu == "📙 บทที่ 3: สัจนิรันดร์ (Tautologies)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์ (Tautologies)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็น <b>จริง (True) ทุกกรณี</b> ส่วนข้อขัดแย้ง (Contradiction) เป็นเท็จทุกกรณี ตรวจสอบได้โดยการสร้างตารางค่าความจริงหรือใช้วิธีหาข้อขัดแย้ง[cite: 16]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 3</h4>
        <ul>
            <li><b>Law of Excluded Middle:</b> $p \vee \neg p$ เป็นสัจนิรันดร์ हमेशा</li>
            <li><b>Deduction Theorem:</b> ประพจน์ $A_1, ..., A_n \models C$ สมมูลกับการเป็นสัจนิรันดร์ของ $(A_1 \wedge ... \wedge A_n) \rightarrow C$[cite: 16]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 3)")
    st.markdown("<b>ตัวอย่าง 3.1:</b> จงตรวจสอบว่าประพจน์ $p \vee \neg p$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เมื่อสร้างตารางค่าความจริง จะได้ผลลัพธ์เป็น T ทุกแถว ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 3.2:</b> จงตรวจสอบว่าประพจน์ $p \rightarrow (p \vee q)$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมติให้เป็นเท็จ จะได้ $p \equiv T$ และ $p \vee q \equiv F$ ซึ่งทำให้ $p \equiv F$ เกิดข้อขัดแย้ง ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 3.3:</b> ประพจน์ $p \wedge \neg p$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> มีค่าความจริงเป็นเท็จทุกกรณี จึงเป็นข้อขัดแย้ง <b>ไม่เป็นสัจนิรันดร์</b>[cite: 16]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 3)")
    st.markdown("1. จงตรวจสอบว่าประพจน์ $(p \wedge q) \rightarrow p$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown("2. จงตรวจสอบว่าประพจน์ $p \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")

# ---------------------------------------------------------
# 5. บทที่ 4
# ---------------------------------------------------------
elif main_menu == "📕 บทที่ 4: การอ้างเหตุผล (Arguments)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p>การอ้างเหตุผลประกอบด้วยเหตุและผลสรุป จะ<b>สมเหตุสมผล (Valid)</b> เมื่อกรณีที่เหตุทุกข้อเป็นจริง ผลสรุปต้องเป็นจริงด้วย[cite: 22]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 4</h4>
        <ul>
            <li><b>Hypothetical Syllogism:</b> $A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$[cite: 22]</li>
            <li><b>Constructive Dilemma:</b> $(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$[cite: 17]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 4)")
    st.markdown("<b>ตัวอย่าง 4.1:</b> เหตุ $p \rightarrow q$ และ $q \rightarrow r$ ผลสรุป $p \rightarrow r$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Hypothetical Syllogism[cite: 22]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 4.2:</b> เหตุ $p \rightarrow q$ และ $q$ ผลสรุป $p$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ไม่สมเหตุสมผล (เข้าข่าย Fallacy: Affirming the consequent)[cite: 22]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 4.3:</b> เหตุ $p \vee q, \neg p$ ผลสรุป $q$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Disjunctive Syllogism[cite: 14]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 4)")
    st.markdown("1. ตรวจสอบความสมเหตุสมผลของเหตุ: $p \rightarrow q, \neg q$ ข้อสรุป: $\neg p$")
    st.markdown("2. ตรวจสอบความสมเหตุสมผลของเหตุ: $p \vee q, p \rightarrow r, q \rightarrow s$ ข้อสรุป: $r \vee s$")

# ---------------------------------------------------------
# 6. บทที่ 5
# ---------------------------------------------------------
elif main_menu == "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p>ตัวบ่งปริมาณประกอบด้วย สำหรับทุกตัว ($\forall x$) และสำหรับบางตัว ($\exists x$) ลำดับของตัวบ่งปริมาณมีความสำคัญมาก[cite: 26]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 5</h4>
        <ul>
            <li><b>Quantifier Negation 1:</b> $\neg \forall x P(x) \equiv \exists x \neg P(x)$[cite: 26]</li>
            <li><b>Quantifier Negation 2:</b> $\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 26]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 5)")
    st.markdown("<b>ตัวอย่าง 5.1:</b> จงหานิเสธของ $\forall x P(x)$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> $\exists x \neg P(x)$[cite: 26]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 5.2:</b> จงหานิเสธของ $\exists x \forall y Q(x, y)$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> $\forall x \exists y \neg Q(x, y)$[cite: 26]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 5.3:</b> พิจารณาเอกภพสัมพัทธ์เป็นจำนวนเต็ม ข้อความ $\forall x \exists y (x < y)$ เป็นจริงหรือเท็จ")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นจริง เพราะสำหรับทุกจำนวนเต็ม $x$ สามารถเลือก $y = x + 1$ ได้เสมอ[cite: 26]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 5)")
    st.markdown("1. จงหานิเสธของข้อความ: $\forall x (P(x) \rightarrow Q(x))$")
    st.markdown("2. อธิบายว่าเหตุใดลำดับของตัวบ่งปริมาณใน $\forall x \exists y (x < y)$ จึงไม่สมมูลกับ $\exists y \forall x (x < y)$ บนจำนวนเต็ม")

# ---------------------------------------------------------
# 7. บทที่ 6
# ---------------------------------------------------------
elif main_menu == "📓 บทที่ 6: การอุปนัยและนิรนัย":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัย (Inductive & Deductive)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎี (Definitions and Central Ideas)</h3>
        <p>การอุปนัยสรุปจากกรณีเฉพาะ ส่วนนิรนัยสรุปตามกฎตรรกะ การอุปนัยเชิงคณิตศาสตร์ประกอบด้วย Base case ($n=1$) และ Inductive step ($P(k) \rightarrow P(k+1)$)[cite: 29]</p>
        
        <h4>📐 สรุปสูตรประจำบทที่ 6</h4>
        <ul>
            <li><b>Sum of First $n$ Cubes:</b> $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 34]</li>
            <li><b>Sum of First $n$ Odd Integers:</b> $1 + 3 + \dots + (2n-1) = n^2$[cite: 29]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 ตัวอย่าง 3 ข้อพร้อมเฉลย (บทที่ 6)")
    st.markdown("<b>ตัวอย่าง 6.1:</b> จงตรวจสอบสูตรผลบวกกำลังสามเมื่อ $n=2$ จากสูตร $1^3 + 2^3 = [\frac{n(n+1)}{2}]^2$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ฝั่งซ้าย = $1 + 8 = 9$ , ฝั่งขวา = $[\frac{2(3)}{2}]^2 = 3^2 = 9$ (เท่ากันและเป็นจริง)[cite: 34]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 6.2:</b> ขั้นตอนแรกของการอุปนัยเชิงคณิตศาสตร์คืออะไร?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> การพิสูจน์ขั้นฐาน (Base Case) ว่าเป็นจริงเมื่อ $n=1$[cite: 29]</div>', unsafe_allow_html=True)
    
    st.markdown("<b>ตัวอย่าง 6.3:</b> สมมติฐานในการอุปนัย (Inductive Hypothesis) คือข้อสมมติใด?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมติให้ประพจน์เป็นจริงเมื่อ $n=k$ เพื่อนำไปพิสูจน์ต่อที่ $n=k+1$[cite: 29, 34]</div>', unsafe_allow_html=True)

    st.markdown("### 📝 โจทย์ฝึกหัด 2 ข้อ (บทที่ 6)")
    st.markdown("1. จงใช้การอุปนัยเชิงคณิตศาสตร์พิสูจน์ว่า $1 + 3 + \dots + (2n-1) = n^2$ สำหรับทุก $n \ge 1$")
    st.markdown("2. จงอธิบายความแตกต่างระหว่างการให้เหตุผลแบบอุปนัยและแบบนิรนัย")

# ---------------------------------------------------------
# 8. เฉลยแบบฝึกหัดท้ายบททั้งหมด
# ---------------------------------------------------------
elif main_menu == "📝 เฉลยแบบฝึกหัดท้ายบททั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 เฉลยแบบฝึกหัดท้ายบททั้งหมด (ครบทั้ง 6 บท)</div>', unsafe_allow_html=True)
    
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 1"):
        st.markdown("""
        * **ข้อ 1:** ไม่เป็นประพจน์ เพราะเป็นประโยคคำสั่ง (Imperative sentence) ซึ่งไม่มีค่าความจริงเป็นจริงหรือเท็จ
        * **ข้อ 2:** จากเหตุ $p \rightarrow r$ และ $p$ สามารถสรุปผลเป็น **$r$** ได้ตามกฎ Modus Ponens[cite: 10]
        """)
        
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 2"):
        st.markdown("""
        * **ข้อ 1:** ตารางค่าความจริงของ $p \vee (q \wedge \neg p)$ จะให้ผลลัพธ์สมมูลกับ $p \vee q$
        * **ข้อ 2:** ตามกฎเดอมอร์แกน $\neg(p \vee q) \equiv$ **$\neg p \wedge \neg q$**[cite: 12]
        """)
        
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 3"):
        st.markdown("""
        * **ข้อ 1:** $(p \wedge q) \rightarrow p$ **เป็นสัจนิรันดร์** เพราะหากสมมติให้เป็นเท็จ จะได้หน้าจริงหลังเท็จ ($p \wedge q \equiv T$ และ $p \equiv F$) ซึ่งทำให้ $p$ เป็นจริงและเท็จพร้อมกัน เกิดข้อขัดแย้ง
        * **ข้อ 2:** $p \rightarrow q$ **ไม่เป็นสัจนิรันดร์** (เป็นแบบสมนัย/คอนจังก์ชันธรรมดา) เพราะเป็นเท็จเมื่อ $p$ เป็นจริงและ $q$ เป็นเท็จ[cite: 12]
        """)
        
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 4"):
        st.markdown("""
        * **ข้อ 1:** สมเหตุสมผลตามกฎ Modus Tollens[cite: 14]
        * **ข้อ 2:** สมเหตุสมผลตามกฎ Constructive Dilemma[cite: 17]
        """)
        
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 5"):
        st.markdown("""
        * **ข้อ 1:** $\exists x (P(x) \wedge \neg Q(x))$ (เนื่องจากนิเสธของ $A \rightarrow B$ คือ $A \wedge \neg B$)
        * **ข้อ 2:** เพราะ $\forall x \exists y (x < y)$ หมายถึงทุกจำนวนมีตัวที่มากกว่า ซึ่งเป็นจริง แต่ $\exists y \forall x (x < y)$ หมายถึงมีจำนวนเต็มตัวหนึ่งที่มากกว่าทุกจำนวน ซึ่งไม่มีอยู่จริงบนจำนวนเต็ม[cite: 26]
        """)
        
    with st.expander("👉 คลิกเพื่อดูเฉลย บทที่ 6"):
        st.markdown("""
        * **ข้อ 1:** พิสูจน์ $n=1$ ได้ $1 = 1^2$ (จริง) สมมติจริงที่ $k$ แล้วพิสูจน์ที่ $k+1$ จะได้ผลรวมเป็น $(k+1)^2$ ตามหลักอุปนัย[cite: 29]
        * **ข้อ 2:** อุปนัยเป็นการสรุปจากกรณีเฉพาะไปสู่ทั่วไป ส่วนนิรนัยเป็นการอ้างผลตามกฎตรรกะที่แน่นอนตายตัว[cite: 29]
        """)

# ---------------------------------------------------------
# 9. สรุปสูตรรวมทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 สรุปสูตรรวมทั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎทางตรรกศาสตร์ทั้งหมด (รวมทุกบท)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📋 1. กฎและสมมูลสำคัญทางตรรกศาสตร์</h3>
        <ul>
            <li><b>การแปลง Implication:</b> $A \rightarrow B \equiv \neg A \vee B$[cite: 12]</li>
            <li><b>De Morgan's Laws:</b> 
                <br>• $\neg(A \wedge B) \equiv \neg A \vee \neg B$[cite: 12]
                <br>• $\neg(A \vee B) \equiv \neg A \wedge \neg B$[cite: 12]
            </li>
            <li><b>Double Negation:</b> $\neg(\neg A) \equiv A$</li>
            <li><b>Law of Excluded Middle:</b> $p \vee \neg p \equiv T$</li>
        </ul>
        
        <h3>📋 2. กฎการอ้างเหตุผลหลัก (Inference Rules)</h3>
        <ul>
            <li><b>Modus Ponens:</b> $p, p \rightarrow q \vdash q$[cite: 10]</li>
            <li><b>Modus Tollens:</b> $p \rightarrow q, \neg q \vdash \neg p$[cite: 14]</li>
            <li><b>Hypothetical Syllogism:</b> $p \rightarrow q, q \rightarrow r \vdash p \rightarrow r$[cite: 22]</li>
            <li><b>Disjunctive Syllogism:</b> $p \vee q, \neg p \vdash q$[cite: 14]</li>
            <li><b>Constructive Dilemma:</b> $(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$[cite: 17]</li>
        </ul>

        <h3>📋 3. กฎตัวบ่งปริมาณ (Quantifier Rules)</h3>
        <ul>
            <li>$\neg \forall x P(x) \equiv \exists x \neg P(x)$[cite: 26]</li>
            <li>$\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 26]</li>
        </ul>

        <h3>📋 4. สูตรการอุปนัยเชิงคณิตศาสตร์ (Mathematical Induction)</h3>
        <ul>
            <li><b>ผลบวกเลขคี่:</b> $1 + 3 + \dots + (2n-1) = n^2$[cite: 29]</li>
            <li><b>ผลบวกกำลังสาม:</b> $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 34]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 10. เครื่องมือคำนวณอัจฉริยะ
# ---------------------------------------------------------
elif main_menu == "⚡ เครื่องมือคำนวณอัจฉริยะ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #F59E0B, #D97706);">⚡ เครื่องมือตรวจสอบสัจนิรันดร์อัตโนมัติ</div>', unsafe_allow_html=True)
    
    user_expr = st.text_input("ป้อนประพจน์ที่ต้องการตรวจสอบ (เช่น (p >> q) | (q >> p)):", value="(p >> q) | (q >> p)")
    if st.button("🚀 ตรวจสอบความเป็นสัจนิรันดร์"):
        try:
            expr = sp.sympify(user_expr)
            syms = sorted([str(s) for s in expr.free_symbols])
            combos = list(itertools.product([True, False], repeat=len(syms)))
            is_tautology = True
            for cb in combos:
                mapping = dict(zip([sp.Symbol(s) for s in syms], cb))
                if not bool(expr.subs(mapping)):
                    is_tautology = False
                    break
            if is_tautology:
                st.success("🎉 ผลลัพธ์: ประพจน์นี้ **เป็นสัจนิรันดร์ (Tautology)** (เป็นจริงในทุกกรณี)")
            else:
                st.warning("⚠️ ผลลัพธ์: ประพจน์นี้ **ไม่เป็นสัจนิรันดร์** (มีบางกรณีที่มีค่าความจริงเป็นเท็จ)")
        except Exception as e:
            st.error(f"รูปแบบประพจน์ไม่ถูกต้อง: {e}")

# ---------------------------------------------------------
# 11. เอกสารอ้างอิง
# ---------------------------------------------------------
elif main_menu == "📚 เอกสารอ้างอิง":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #475569, #334155);">📚 เอกสารอ้างอิง (References)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <ul>
            <li><b>Epp, S. S. (2011).</b> <i>Discrete Mathematics with Applications</i> (4th ed.). Brooks/Cole[cite: 37].</li>
            <li><b>Rosen, K. H. (2019).</b> <i>Discrete Mathematics and Its Applications</i> (8th ed.). McGraw-Hill Education[cite: 37].</li>
            <li><b>Enderton, H. B. (2001).</b> <i>A Mathematical Introduction to Logic</i> (2nd ed.). Academic Press[cite: 37].</li>
            <li><b>Velleman, D. J. (2019).</b> <i>How to Prove It: A Structured Approach</i> (3rd ed.). Cambridge University Press[cite: 37].</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
