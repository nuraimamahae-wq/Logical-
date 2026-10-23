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
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'score' not in st.session_state:
    st.session_state.score = 0

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
        "💡 ตัวอย่าง 3 ข้อพร้อมเฉลยละเอียด",
        "📝 แบบฝึกหัดและเฉลยท้ายบท",
        "📐 สรุปสูตรและสมมูลทั้งหมด",
        "⚡ เครื่องมือคำนวณอัจฉริยะ",
        "📚 เอกสารอ้างอิง"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 คะแนนสะสมของคุณ")
st.sidebar.metric(label="คะแนนแบบฝึกหัด", value=f"{st.session_state.score} คะแนน")

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
            <p>แอปพลิเคชันนี้พัฒนาขึ้นเพื่อรวบรวมเนื้อหาทางตรรกศาสตร์เชิงคณิตศาสตร์แบบจัดเต็ม ทั้งทฤษฎี ตัวอย่างการพิสูจน์เชิงลึก พร้อมตัวอย่างและโจทย์ฝึกหัดพร้อมเฉลย เพื่อเสริมสร้างกระบวนการคิดวิเคราะห์และการให้เหตุผลที่ถูกต้อง[cite: 7]</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. บทที่ 1
# ---------------------------------------------------------
elif main_menu == "📘 บทที่ 1: ประพจน์และการให้เหตุผล":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #2563EB, #1D4ED8);">📘 บทที่ 1: บทนำตรรกศาสตร์เชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง (True) หรือเท็จ (True/False) อย่างใดอย่างหนึ่งเท่านั้น ประพจน์ย่อยมักแทนด้วยตัวA-Z เช่น p, q, r, s[cite: 10]</p>
        <p><b>หลักการพิสูจน์เบื้องต้น:</b> การตรวจสอบความสมเหตุสมผลพิจารณาว่าข้อสรุปต้องเป็นจริงเสมอเมื่อเหตุทุกข้อเป็นจริง[cite: 10]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. บทที่ 2
# ---------------------------------------------------------
elif main_menu == "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p>ตัวเชื่อมทางตรรกศาสตร์หลักประกอบด้วย:</p>
        <ul>
            <li><b>นิเสธ (Negation $\\neg$):</b> กลับค่าความจริงของประพจน์[cite: 12]</li>
            <li><b>และ (Conjunction $\\wedge$):</b> เป็นจริงเฉพาะกรณีที่ประพจน์ย่อยเป็นจริงทั้งคู่[cite: 12]</li>
            <li><b>หรือ (Disjunction $\\vee$):</b> เป็นเท็จเฉพาะกรณีที่ประพจน์ย่อยเป็นเท็จทั้งคู่[cite: 12]</li>
            <li><b>การimplie (Implication $\\rightarrow$):</b> เป็นเท็จกรณีเดียวคือ หน้าจริง หลังเท็จ[cite: 12]</li>
            <li><b>สมมูล (Biconditional $\\leftrightarrow$):</b> เป็นจริงเมื่อประพจน์ทั้งสองมีค่าความจริงเหมือนกัน[cite: 12]</li>
        </ul>
        <p>ตารางค่าความจริงสำหรับประพจน์ $n$ ตัวจะมีทั้งหมด $2^n$ แถว[cite: 12]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. บทที่ 3
# ---------------------------------------------------------
elif main_menu == "📙 บทที่ 3: สัจนิรันดร์ (Tautologies)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์ (Tautologies)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็น <b>จริง (T) ทุกกรณี</b> ไม่ว่าประพจน์ย่อยจะมีค่าความจริงเป็นอย่างไร[cite: 16]</p>
        <p><b>วิธีการตรวจสอบ:</b> สามารถสร้างตารางค่าความจริงจนครบทุกกรณี หรือใช้วิธีสมมติให้ประพจน์เป็นเท็จเพื่อหาข้อขัดแย้ง (Countervaluation) หากเกิดข้อขัดแย้งแสดงว่าเป็นสัจนิรันดร์[cite: 16]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. บทที่ 4
# ---------------------------------------------------------
elif main_menu == "📕 บทที่ 4: การอ้างเหตุผล (Arguments)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p>การอ้างเหตุผลประกอบด้วย <b>เหตุ (Premises)</b> และ <b>ผลสรุป (Conclusion)</b> การอ้างเหตุผลจะ<b>สมเหตุสมผล (Valid)</b> ก็ต่อเมื่อกรณีที่เหตุทุกข้อเป็นจริง ผลสรุปต้องเป็นจริงด้วย[cite: 22]</p>
        <p><b>กฎสำคัญ:</b> Modus Ponens, Modus Tollens, Hypothetical Syllogism และ Disjunctive Syllogism[cite: 22]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. บทที่ 5
# ---------------------------------------------------------
elif main_menu == "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p><b>ประโยคเปิด $P(x)$</b> คือประโยคที่มีตัวแปรและจะยังบอกค่าความจริงไม่ได้จนกว่าจะแทนค่าหรือมีตัวบ่งปริมาณ[cite: 26]</p>
        <ul>
            <li><b>สำหรับทุกตัว ($\\forall x$):</b> เป็นจริงเมื่อทุกสมาชิกในเอกภพสัมพัทธ์ทำให้ $P(x)$ เป็นจริง[cite: 26]</li>
            <li><b>สำหรับบางตัว ($\\exists x$):</b> เป็นจริงเมื่อมีสมาชิกอย่างน้อยหนึ่งตัวทำให้ $P(x)$ เป็นจริง[cite: 26]</li>
        </ul>
        <p><b>กฎนิเสธ:</b> $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$ และ $\\neg \\exists x P(x) \\equiv \\forall x \\neg P(x)$[cite: 26]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. บทที่ 6
# ---------------------------------------------------------
elif main_menu == "📓 บทที่ 6: การอุปนัยและนิรนัย":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัย (Inductive & Deductive)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและทฤษฎีสำคัญ</h3>
        <p><b>การให้เหตุผลแบบอุปนัย (Inductive Reasoning)</b> ใช้ข้อสังเกตจากกรณีเฉพาะเพื่อสรุปเป็นกฎทั่วไป ส่วน<b>นิรนัย (Deductive Reasoning)</b> เป็นการอสรุปผลตามกฎเกณฑ์ตรรกะที่แน่นอน[cite: 29]</p>
        <p><b>การอุปนัยเชิงคณิตศาสตร์ (Mathematical Induction):</b> วิธีพิสูจน์สำหรับจำนวนเต็มบวก $n$ ประกอบด้วย 2 ขั้นตอนหลัก คือ พิสูจน์ว่าจริงที่ $n=1$ (Base case) และสมมติว่าจริงที่ $n=k$ แล้วพิสูจน์ให้ ัเห็นว่าจริงที่ $n=k+1$[cite: 29]</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. ตัวอย่าง 3 ข้อพร้อมเฉลยละเอียด
# ---------------------------------------------------------
elif main_menu == "💡 ตัวอย่าง 3 ข้อพร้อมเฉลยละเอียด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #10B981, #059669);">💡 ตัวอย่างโจทย์พร้อมวิธีทำอย่างละเอียด</div>', unsafe_allow_html=True)
    
    st.markdown("### ตัวอย่างที่ 1: การตรวจสอบสัจนิรันดร์")
    st.markdown("จงตรวจสอบว่าประพจน์ $[(p \\wedge q) \\rightarrow r] \\leftrightarrow [p \\rightarrow (q \\rightarrow r)]$ เป็นสัจนิรันดร์หรือไม่[cite: 21]")
    with st.container():
        st.markdown("""
        <div class="solution-box">
            <b>วิธีทำ (พิสูจน์โดยหาข้อขัดแย้ง):</b><br>
            1. สมมติให้ประพจน์หลักมีค่าความจริงเป็น <b>เท็จ ($\\equiv F$)</b>[cite: 21]<br>
            2. เนื่องจากเชื่อมด้วย $\\leftrightarrow$ และเป็น F แสดงว่าประพจน์ซ้ายและขวาต้องมีค่าความจริง<b>ตรงข้ามกัน</b> (กรณีหนึ่งเป็น T อีกกรณีเป็น F)[cite: 21]<br>
            3. หากสมมติกรณีที่ฝั่งซ้ายเป็น F และฝั่งขวาเป็น T จะพบว่า เมื่อแทนค่า $p \\equiv T, q \\equiv T, r \\equiv F$ จะเกิดข้อขัดแย้งกับเงื่อนไขเริ่มต้น[cite: 21]<br>
            4. ทำซ้ำในทุกกรณี จะพบว่าเกิดข้อขัดแย้งทั้งหมด ดังนั้นการสมมติให้เป็นเท็จจึงเป็นไปไม่ได้<br>
            <b>สรุป:</b> ประพจน์นี้<b>เป็นสัจนิรันดร์ (Tautology)</b>[cite: 21]
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### ตัวอย่างที่ 2: การตรวจสอบความสมเหตุสมผลของการอ้างเหตุผล")
    st.markdown("กำหนดเหตุ: 1) $p \\rightarrow (q \\vee r)$ , 2) $q \\rightarrow \\neg s$ , 3) $s$ <br>จงตรวจสอบว่าข้อสรุป $\\therefore p \\rightarrow r$ สมเหตุสมผลหรือไม่[cite: 35]", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="solution-box">
            <b>วิธีทำ:</b><br>
            1. สมมติให้การอ้างเหตุผล<b>ไม่สมเหตุสมผล</b> กล่าวคือ เหตุทุกข้อเป็น <b>จริง (T)</b> แต่ข้อสรุปเป็น <b>เท็จ (F)</b>[cite: 35]<br>
            2. จากข้อสรุป $p \\rightarrow r \\equiv F$ จะได้บังคับว่า $p \\equiv T$ และ $r \\equiv F$[cite: 35]<br>
            3. นำ $p \\equiv T$ ไปแทนในเหตุที่ 1 $[p \\rightarrow (q \\vee r)] \\equiv T$ จะได้ $T \\rightarrow (q \\vee F) \\equiv T$ ดังนั้น $q$ ต้องเป็น <b>เท็จ ($F$)</b>[cite: 36]<br>
            4. นำ $q \\equiv F$ ไปแทนในเหตุที่ 2 $[q \\rightarrow \\neg s] \\equiv T$ จะได้ $F \\rightarrow \\neg s \\equiv T$ ซึ่งสอดคล้อง[cite: 35]<br>
            5. ตรวจสอบเหตุที่ 3 คือ $s \\equiv T$ ซึ่งทำให้ $\\neg s \\equiv F$ จะเกิดข้อขัดแย้งกับการสมมติ<br>
            <b>สรุป:</b> การสมมติทำให้เกิดข้อขัดแย้ง ดังนั้นการอ้างเหตุผลนี้<b>สมเหตุสมผล (Valid)</b>[cite: 36]
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### ตัวอย่างที่ 3: การพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์")
    st.markdown("จงพิสูจน์ว่า $1^3 + 2^3 + 3^3 + \\dots + n^3 = [\\frac{n(n+1)}{2}]^2$ สำหรับทุกจำนวนเต็มบวก $n \\ge 1$[cite: 34]")
    with st.container():
        st.markdown("""
        <div class="solution-box">
            <b>วิธีทำ:</b><br>
            1. <b>ขั้นฐาน (Base Case):</b> เมื่อ $n = 1$<br>
            &nbsp;&nbsp;&nbsp;&nbsp;ฝั่งซ้าย = $1^3 = 1$ , ฝั่งขวา = $[\\frac{1(1+1)}{2}]^2 = 1^2 = 1$ (จริง)<br>
            2. <b>ขั้นอุปนัย (Inductive Step):</b> สมมติว่าสูตรเป็นจริงเมื่อ $n = k$ นั่นคือ $1^3 + \\dots + k^3 = [\\frac{k(k+1)}{2}]^2$[cite: 34]<br>
            3. พิสูจน์ว่าจริงสำหรับ $n = k+1$ โดยบวกพจน์ $(k+1)^3$ ทั้งสองข้าง แล้วจัดรูปทางพีชคณิตจะได้ผลลัพธ์เป็น $[\\frac{(k+1)(k+2)}{2}]^2$<br>
            <b>สรุป:</b> สมการนี้เป็นจริงสำหรับทุกจำนวนเต็มบวก $n \\ge 1$[cite: 34]
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 9. แบบฝึกหัดและเฉลยท้ายบท
# ---------------------------------------------------------
elif main_menu == "📝 แบบฝึกหัดและเฉลยท้ายบท":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 แบบฝึกหัดทดสอบความรู้พร้อมเฉลยท้ายสุด</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 โจทย์ข้อที่ 1")
    st.markdown("กำหนดให้ $p$ และ $q$ เป็นประพจน์ที่มีค่าความจริงเป็น **จริง (True)** และ $r$ มีค่าความจริงเป็น **เท็จ (False)** จงหาค่าความจริงของประพจน์: $[(p \\wedge \\neg q) \\vee r] \\rightarrow p$")
    
    ans_q1 = st.radio("เลือกคำตอบข้อ 1:", ["จริง (True)", "เท็จ (False)"], key="ex_q1")
    
    st.markdown("---")
    st.markdown("### 📋 โจทย์ข้อที่ 2")
    st.markdown("จงพิจารณาว่าข้อความใดต่อไปนี้เป็น **นิเสธ (Negation)** ที่ถูกต้องของประพจน์ $\\forall x \\exists y (x + y > 0)$")
    
    ans_q2 = st.radio("เลือกคำตอบข้อ 2:", [
        "$\\exists x \\forall y (x + y \\le 0)$",
        "$\\forall x \\forall y (x + y \\le 0)$",
        "$\\exists x \\exists y (x + y > 0)$"
    ], key="ex_q2")

    if st.button("ส่งคำตอบแบบฝึกหัดทั้งหมด"):
        score_count = 0
        if ans_q1 == "จริง (True)":
            score_count += 1
        if ans_q2 == "$\\exists x \\forall y (x + y \\le 0)$":
            score_count += 1
        st.session_state.score = score_count
        st.success(f"🎉 คุณทำคะแนนได้ {score_count} / 2 คะแนน! เลื่อนลงมาดูเฉลยละเอียดด้านล่างได้เลยครับ")

    st.markdown("---")
    st.markdown("## 🔑 เฉลยแบบฝึกหัดท้ายบท (ให้อ่านหลังทำเสร็จ)")
    with st.expander("👉 คลิกเพื่อดูเฉลยและวิธีทำอย่างละเอียด"):
        st.markdown("""
        ### เฉลยโจทย์ข้อที่ 1:
        * **โจทย์:** $[(p \\wedge \\neg q) \\vee r] \\rightarrow p$ โดยที่ $p \\equiv T, q \\equiv T, r \\equiv F$
        * **วิธีทำ:**
          1. แทนค่า $\\neg q \\equiv \\neg T \\equiv F$
          2. พิจารณาวงเล็บแรก $(p \\wedge \\neg q) \\equiv (T \\wedge F) \\equiv F$
          3. พิจารณาเชื่อมต่อด้วย $\\vee r$: $(F \\vee F) \\equiv F$
          4. นำไปแทนในประพจน์หลัก: $F \\rightarrow T$ ซึ่งมีค่าความจริงเป็น **จริง (True)**
        * **เฉลย:** **จริง (True)**

        ---

        ### เฉลยโจทย์ข้อที่ 2:
        * **โจทย์:** นิเสธของ $\\forall x \\exists y (x + y > 0)$
        * **วิธีทำ:** 
          1. ตามกฎการกระจายนิเสธของตัวบ่งปริมาณ: $\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$
          2. นิเสธของ $\\exists y$ จะเปลี่ยนเป็น $\\forall y$
          3. นิเสธของเครื่องหมาย $>$ คือ $\\le$
          4. ดังนั้นจะได้ $\\exists x \\forall y (x + y \\le 0)$
        * **เฉลย:** **$\\exists x \\forall y (x + y \\le 0)$**
        """)

# ---------------------------------------------------------
# 10. สรุปสูตรและสมมูลทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 สรุปสูตรและสมมูลทั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎสมมูลทางตรรกศาสตร์</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📋 กฎสมมูลที่สำคัญ (Logical Equivalences)</h3>
        <ul>
            <li><b>กฎการเปลี่ยนรูป Implication:</b> $A \\rightarrow B \\equiv \\neg A \\vee B$[cite: 12]</li>
            <li><b>กฎเดอมอร์แกน (De Morgan's Laws):</b> 
                <br>• $\\neg(A \\wedge B) \\equiv \\neg A \\vee \\neg B$[cite: 12]
                <br>• $\\neg(A \\vee B) \\equiv \\neg A \\wedge \\neg B$[cite: 12]
            </li>
            <li><b>กฎนิเสธซ้อน (Double Negation):</b> $\\neg(\\neg A) \\equiv A$</li>
            <li><b>กฎการสลับที่ (Commutative Laws):</b> $A \\vee B \\equiv B \\vee A$ และ $A \\wedge B \\equiv B \\wedge A$</li>
            <li><b>กฎการแจกแจง (Distributive Laws):</b> $A \\vee (B \\wedge C) \\equiv (A \\vee B) \\wedge (A \\vee C)$</li>
        </ul>
        
        <h3>📋 กฎนิเสธตัวบ่งปริมาณ (Quantifier Negation)</h3>
        <ul>
            <li>$\\neg \\forall x P(x) \\equiv \\exists x \\neg P(x)$[cite: 26]</li>
            <li>$\\neg \\exists x P(x) \\equiv \\forall x \\neg P(x)$[cite: 26]</li>
        </ul>
        
        <h3>📋 กฎการอ้างเหตุผลสำคัญ (Valid Inference Rules)</h3>
        <ul>
            <li><b>Modus Ponens:</b> $A \\rightarrow B, A \\vdash B$[cite: 22]</li>
            <li><b>Modus Tollens:</b> $A \\rightarrow B, \\neg B \\vdash \\neg A$[cite: 22]</li>
            <li><b>Hypothetical Syllogism:</b> $A \\rightarrow B, B \\rightarrow C \\vdash A \\rightarrow C$[cite: 22]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 11. เครื่องมือคำนวณอัจฉริยะ
# ---------------------------------------------------------
elif main_menu == "⚡ เครื่องมือคำนวณอัจฉริยะ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #F59E0B, #D97706);">⚡ เครื่องมือตรวจสอบสัจนิรันดร์อัตโนมัติ</div>', unsafe_allow_html=True)
    
    user_expr = st.text_input("ป้อนประพจน์ที่ต้องการตรวจสอบ (เช่น (p >> q) | (q >> p)):", value="(p >> q) | (q >> p)")
    if st.button("🚀 ตรวจสอบความ เป็นสัจนิรันดร์"):
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
# 12. เอกสารอ้างอิง
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
