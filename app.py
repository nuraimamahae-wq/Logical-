import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="ระบบสื่อการเรียนรู้วิชาตรรกศาสตร์เชิงคณิตศาสตร์",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 32px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 20px;
        color: #1E3A8A;
        font-weight: 700;
        border-left: 5px solid #2563EB;
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
        "📘 บทที่ 1: บทนำตรรกศาสตร์เชิงคณิตศาสตร์",
        "📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง",
        "📙 บทที่ 3: สัจนิรันดร์",
        "📕 บทที่ 4: การอ้างเหตุผล",
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ",
        "📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์",
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
            <p><b>รายวิชา:</b> ภาษาอังกฤษสำหรับการสอนคณิตศาสตร์ (English for Teaching Mathematics)[cite: 4]</p>
            <p><b>ผู้จัดทำ:</b> Ms. Nur-aima Mahae (รหัสนักศึกษา: 671107068)[cite: 4]</p>
            <p><b>เสนอต่อ:</b> ผู้ช่วยศาสตราจารย์ ดร.อิติวัฒน์ โตเจริญนิรัติศัย[cite: 4]</p>
            <p><b>สังกัด:</b> คณะครุศาสตร์ สาขาวิชาคณิตศาสตร์ มหาวิทยาลัยราชภัฏธนบุรี[cite: 4]</p>
            <p><b>ปีการศึกษา:</b> ภาคเรียนที่ 1 ปีการศึกษา 2026[cite: 4]</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h3>🎯 วัตถุประสงค์ของแอปพลิเคชัน</h3>
            <p>แอปพลิเคชันนี้พัฒนาขึ้นเพื่อรวบรวมเนื้อหาตรรกศาสตร์เชิงคณิตศาสตร์ทั้ง 6 บทแบบเจาะลึก เป็นภาษาไทยทั้งหมด พร้อมเมนูย่อย ตัวอย่าง 3 ข้อพร้อมเฉลยในแต่ละบท, โจทย์ฝึกหัด 2 ข้อ, เฉลยท้ายบท, และสรุปสูตร เพื่อเสริมสร้างความเข้าใจเชิงลึกและการเรียนรู้ที่มีประสิทธิภาพ[cite: 5, 6]</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. บทที่ 1
# ---------------------------------------------------------
elif main_menu == "📘 บทที่ 1: บทนำตรรกศาสตร์เชิงคณิตศาสตร์":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #2563EB, #1D4ED8);">📘 บทที่ 1: บทนำตรรกศาสตร์เชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    
    sub_ch1 = st.selectbox("เลือกเมนูย่อย (บทที่ 1):", ["1.1 บทนิยามและแนวคิดหลัก", "1.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "1.3 โจทย์ฝึกหัด (2 ข้อ)", "1.4 สรุปสูตรประจำบท"])
    
    if sub_ch1 == "1.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 1.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง ($\text{True}$) หรือเท็จ ($\text{False}$) อย่างใดอย่างหนึ่งเท่านั้น ประพจน์เชิงเดี่ยวแทนด้วยตัวอักษร $p, q, r, s$ ส่วนประพจน์เชิงซ้อนสร้างขึ้นผ่านตัวเชื่อมทางตรรกศาสตร์ ความสมเหตุสมผลพิจารณาว่าข้อสรุปต้องเป็นจริงเสมอเมื่อเหตุทุกข้อเป็นจริง[cite: 8]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch1 == "1.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 1.1")
        st.markdown("จงพิจารณาว่าประโยค 'ประเทศไทยมีพื้นที่ติดต่อกับมหาสมุทรแปซิฟิก' เป็นประพจน์หรือไม่ และมีค่าความจริงเป็นอย่างไร?")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นประพจน์ เพราะเป็นประโยคบอกเล่าที่มีค่าความจริงเป็น <b>เท็จ ($\text{False}$)</b>[cite: 8]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 1.2")
        st.markdown("กำหนดให้ $p$ และ $p \rightarrow q$ เป็นจริง จงหาค่าความจริงของ $q$ โดยใช้หลักการ Modus Ponens")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> จากกฎ Modus Ponens ($p, p \rightarrow q \vdash q$) จะได้ว่า $q$ มีค่าความจริงเป็น <b>จริง ($\text{True}$)</b>[cite: 8]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 1.3")
        st.markdown("กำหนดเหตุ $p \rightarrow r$ และข้อสรุป $\neg r$ จงหาข้อขัดแย้งตามหลักการพิสูจน์ทางอ้อม (Indirect Proof)")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> ตามกฎ Modus Tollens จะได้ผลสรุปคือ <b>$\neg p$</b>[cite: 8, 9]</div>', unsafe_allow_html=True)
    elif sub_ch1 == "1.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 1")
        st.markdown("1. ประโยค 'คุณกำลังศึกษาอยู่ที่คณะใด?' เป็นประพจน์ทางตรรกศาสตร์หรือไม่ เพราะเหตุใด?")
        st.markdown("2. กำหนดเหตุ: $p \rightarrow q$ และ $\neg q$ จงหาข้อสรุปที่สมเหตุสมผลตามกฎตรรกะ")
    elif sub_ch1 == "1.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 1</h3>
            <ul>
                <li><b>กฎการแยกแยะฝ่ายหน้า (Modus Ponens):</b> $p, p \rightarrow q \vdash q$[cite: 8]</li>
                <li><b>กฎการปฏิเสธฝ่ายหลัง (Modus Tollens):</b> $p \rightarrow q, \neg q \vdash \neg p$[cite: 9]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. บทที่ 2
# ---------------------------------------------------------
elif main_menu == "📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง</div>', unsafe_allow_html=True)
    
    sub_ch2 = st.selectbox("เลือกเมนูย่อย (บทที่ 2):", ["2.1 บทนิยามและแนวคิดหลัก", "2.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "2.3 โจทย์ฝึกหัด (2 ข้อ)", "2.4 สรุปสูตรประจำบท"])
    
    if sub_ch2 == "2.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 2.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p>ตัวเชื่อมหลักประกอบด้วย นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การimplie ($\rightarrow$), และสมมูล ($\leftrightarrow$) ตารางค่าความจริงสำหรับประพจน์ $n$ ตัวแปรจะมีทั้งหมด $2^n$ แถว[cite: 10]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch2 == "2.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 2.1")
        st.markdown("กำหนดให้ $p \equiv T$ และ $q \equiv F$ จงหาค่าความจริงของ $p \vee q$")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> ตัวเชื่อม หรือ ($\vee$) จะเป็นเท็จก็ต่อเมื่อเป็นเท็จทั้งคู่ ดังนั้น $T \vee F \equiv$ <b>จริง ($\text{True}$)</b>[cite: 10]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 2.2")
        st.markdown("จงแปลงประพจน์ $p \rightarrow q$ ให้เป็นรูปดิสจังชัน (Disjunction)")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมูลกับ $\neg p \vee q$[cite: 10]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 2.3")
        st.markdown("จงหานิเสธของประพจน์เชื่อม $p \wedge q$ ตามกฎเดอมอร์แกน")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> $\neg(p \wedge q) \equiv \neg p \vee \neg q$[cite: 10]</div>', unsafe_allow_html=True)
    elif sub_ch2 == "2.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 2")
        st.markdown("1. จงสร้างตารางค่าความจริงของประพจน์ $(p \wedge q) \rightarrow r$")
        st.markdown("2. จงหาประพจน์ที่สมมูลกับ $\neg(p \vee q)$")
    elif sub_ch2 == "2.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 2</h3>
            <ul>
                <li><b>สมมูลของการimplie:</b> $A \rightarrow B \equiv \neg A \vee B$[cite: 10]</li>
                <li><b>กฎเดอมอร์แกน (De Morgan's Laws):</b> $\neg(A \wedge B) \equiv \neg A \vee \neg B$ และ $\neg(A \vee B) \equiv \neg A \wedge \neg B$[cite: 10]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. บทที่ 3
# ---------------------------------------------------------
elif main_menu == "📙 บทที่ 3: สัจนิรันดร์":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์ (Tautologies)</div>', unsafe_allow_html=True)
    
    sub_ch3 = st.selectbox("เลือกเมนูย่อย (บทที่ 3):", ["3.1 บทนิยามและแนวคิดหลัก", "3.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "3.3 โจทย์ฝึกหัด (2 ข้อ)", "3.4 สรุปสูตรประจำบท"])
    
    if sub_ch3 == "3.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 3.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็นจริงทุกกรณี ตรวจสอบได้โดยการสร้างตารางค่าความจริงหรือสมมติให้เป็นเท็จเพื่อหาข้อขัดแย้ง[cite: 14]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch3 == "3.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 3.1")
        st.markdown("จงตรวจสอบว่า $p \vee \neg p$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> มีค่าความจริงเป็นจริงทุกกรณี ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 3.2")
        st.markdown("จงตรวจสอบว่า $(p \wedge q) \rightarrow p$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมติให้เป็นเท็จ จะได้ $p \wedge q \equiv T$ และ $p \equiv F$ ทำให้ $p$ เป็นจริงและเท็จพร้อมกัน เกิดข้อขัดแย้ง ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 3.3")
        st.markdown("จงตรวจสอบว่า $p \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นเท็จเมื่อ $p \equiv T$ และ $q \equiv F$ ดังนั้น <b>ไม่เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
    elif sub_ch3 == "3.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 3")
        st.markdown("1. จงตรวจสอบว่าประพจน์ $p \rightarrow (p \vee q)$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown("2. จงตรวจสอบว่าประพจน์ $(p \rightarrow q) \leftrightarrow (\neg p \vee q)$ เป็นสัจนิรันดร์หรือไม่")
    elif sub_ch3 == "3.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 3</h3>
            <ul>
                <li><b>กฎความเป็นจริงกึ่งกลาง (Law of Excluded Middle):</b> $p \vee \neg p \equiv T$</li>
                <li><b>ทฤษฎีบทการหักล้าง (Deduction Theorem):</b> $A_1, ..., A_n \models C \iff (A_1 \wedge ... \wedge A_n) \rightarrow C$ เป็นสัจนิรันดร์[cite: 14]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. บทที่ 4
# ---------------------------------------------------------
elif main_menu == "📕 บทที่ 4: การอ้างเหตุผล":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล</div>', unsafe_allow_html=True)
    
    sub_ch4 = st.selectbox("เลือกเมนูย่อย (บทที่ 4):", ["4.1 บทนิยามและแนวคิดหลัก", "4.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "4.3 โจทย์ฝึกหัด (2 ข้อ)", "4.4 สรุปสูตรประจำบท"])
    
    if sub_ch4 == "4.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 4.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p>การอ้างเหตุผลจะ<b>สมเหตุสมผล (Valid)</b> เมื่อกรณีที่เหตุทุกข้อเป็นจริง ผลสรุปต้องเป็นจริงด้วย โดยอิงตามกฎการอ้างเหตุผลสำคัญ[cite: 20]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch4 == "4.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 4.1")
        st.markdown("เหตุ: $p \rightarrow q, q \rightarrow r$ | ผลสรุป: $p \rightarrow r$ สมเหตุสมผลหรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Hypothetical Syllogism[cite: 20]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 4.2")
        st.markdown("เหตุ: $p \vee q, \neg p$ | ผลสรุป: $q$ สมเหตุสมผลหรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Disjunctive Syllogism[cite: 20]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 4.3")
        st.markdown("เหตุ: $p \rightarrow q, q$ | ผลสรุป: $p$ สมเหตุสมผลหรือไม่")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> ไม่สมเหตุสมผล (Fallacy: Affirming the consequent)[cite: 20]</div>', unsafe_allow_html=True)
    elif sub_ch4 == "4.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 4")
        st.markdown("1. ตรวจสอบความสมเหตุสมผลของเหตุ: $p \rightarrow q, \neg q$ ข้อสรุป: $\neg p$")
        st.markdown("2. ตรวจสอบความสมเหตุสมผลของเหตุ: $(p \vee q), p \rightarrow r, q \rightarrow r$ ข้อสรุป: $r$")
    elif sub_ch4 == "4.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 4</h3>
            <ul>
                <li><b>กฎฮิปปอเทติคัลซิลโลจิซึม (Hypothetical Syllogism):</b> $A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$[cite: 20]</li>
                <li><b>กฎคอนสตรัคทีฟไดเลมมา (Constructive Dilemma):</b> $(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$[cite: 16]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. บทที่ 5
# ---------------------------------------------------------
elif main_menu == "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)</div>', unsafe_allow_html=True)
    
    sub_ch5 = st.selectbox("เลือกเมนูย่อย (บทที่ 5):", ["5.1 บทนิยามและแนวคิดหลัก", "5.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "5.3 โจทย์ฝึกหัด (2 ข้อ)", "5.4 สรุปสูตรประจำบท"])
    
    if sub_ch5 == "5.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 5.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p>ประโยคเปิด $P(x)$ จะมีตัวแปรเสรี ตัวบ่งปริมาณประกอบด้วยสำหรับทุกตัว ($\forall x$) และสำหรับบางตัว ($\exists x$) ลำดับของตัวบ่งปริมาณส่งผลต่อค่าความจริง[cite: 24]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch5 == "5.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 5.1")
        st.markdown("จงหานิเสธของ $\forall x P(x)$")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> $\exists x \neg P(x)$[cite: 24]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 5.2")
        st.markdown("จงหานิเสธของ $\exists x \forall y Q(x, y)$")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> $\forall x \exists y \neg Q(x, y)$[cite: 24]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 5.3")
        st.markdown("บนเอกภพสัมพัทธ์จำนวนเต็ม ข้อความ $\forall x \exists y (x < y)$ เป็นจริงหรือเท็จ")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นจริง เพราะสำหรับทุกจำนวนเต็ม $x$ จะมี $y = x + 1$ เสมอ[cite: 24]</div>', unsafe_allow_html=True)
    elif sub_ch5 == "5.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 5")
        st.markdown("1. จงหานิเสธของประโยค: $\forall x (P(x) \rightarrow Q(x))$")
        st.markdown("2. อธิบายเหตุใดลำดับ $\forall x \exists y (x < y)$ จึงแตกต่างจาก $\exists y \forall x (x < y)$ บนจำนวนเต็ม")
    elif sub_ch5 == "5.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 5</h3>
            <ul>
                <li><b>นิเสธตัวบ่งปริมาณสากล:</b> $\neg \forall x P(x) \equiv \exists x \neg P(x)$[cite: 24]</li>
                <li><b>นิเสธตัวบ่งปริมาณเฉพาะตัว:</b> $\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 24]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. บทที่ 6
# ---------------------------------------------------------
elif main_menu == "📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    
    sub_ch6 = st.selectbox("เลือกเมนูย่อย (บทที่ 6):", ["6.1 บทนิยามและแนวคิดหลัก", "6.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)", "6.3 โจทย์ฝึกหัด (2 ข้อ)", "6.4 สรุปสูตรประจำบท"])
    
    if sub_ch6 == "6.1 บทนิยามและแนวคิดหลัก":
        st.markdown("""
        <div class="card-box">
            <h3>📖 6.1 บทนิยามและแนวคิดหลัก (Definitions and Central Ideas)</h3>
            <p>การอุปนัยเชิงคณิตศาสตร์ประกอบด้วย ขั้นฐาน ($\text{Base case}$ สำหรับ $n=1$) และขั้นอุปนัย ($\text{Inductive step}$ จาก $P(k) \rightarrow P(k+1)$) สำหรับพิสูจน์ประพจน์จำนวนเต็มบวก[cite: 27]</p>
        </div>
        """, unsafe_allow_html=True)
    elif sub_ch6 == "6.2 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)":
        st.markdown("### 💡 ตัวอย่างที่ 6.1")
        st.markdown("จงตรวจสอบสูตรผลบวกกำลังสาม $1^3 + 2^3 = [\frac{n(n+1)}{2}]^2$ เมื่อ $n=2$")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> ฝั่งซ้าย = $1 + 8 = 9$, ฝั่งขวา = $[\frac{2(3)}{2}]^2 = 3^2 = 9$ (เป็นจริง)[cite: 31]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 6.2")
        st.markdown("ขั้นตอนแรกของการพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์เรียกว่าอะไร?")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> ขั้นฐาน ($\text{Base Case}$) สำหรับ $n=1$[cite: 27]</div>', unsafe_allow_html=True)
        
        st.markdown("### 💡 ตัวอย่างที่ 6.3")
        st.markdown("สมมติฐานการอุปนัย ($\text{Inductive Hypothesis}$) คืออะไร?")
        st.markdown('<div class="solution-box"><b>เฉลย:</b> การสมมติให้ประพจน์เป็นจริงเมื่อ $n=k$[cite: 27, 31]</div>', unsafe_allow_html=True)
    elif sub_ch6 == "6.3 โจทย์ฝึกหัด (2 ข้อ)":
        st.markdown("### 📝 โจทย์ฝึกหัด บทที่ 6")
        st.markdown("1. จงพิสูจน์ว่า $1 + 3 + \dots + (2n-1) = n^2$ สำหรับทุก $n \ge 1$")
        st.markdown("2. จงอธิบายความแตกต่างระหว่างการอุปนัยและนิรนัย")
    elif sub_ch6 == "6.4 สรุปสูตรประจำบท":
        st.markdown("""
        <div class="card-box">
            <h3>📐 สรุปสูตรประจำบทที่ 6</h3>
            <ul>
                <li><b>ผลบวกจำนวนคี่ $n$ พจน์แรก:</b> $1 + 3 + \dots + (2n-1) = n^2$[cite: 27]</li>
                <li><b>ผลบวกกำลังสาม $n$ พจน์แรก:</b> $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 31]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. เฉลยแบบฝึกหัดท้ายบททั้งหมด
# ---------------------------------------------------------
elif main_menu == "📝 เฉลยแบบฝึกหัดท้ายบททั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 เฉลยแบบฝึกหัดท้ายบททั้งหมด (ครบทุกบท)</div>', unsafe_allow_html=True)
    
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 1"):
        st.markdown("1. ไม่เป็นประพจน์ เพราะเป็นประโยคคำถามซึ่งไม่มีค่าความจริง[cite: 8]<br>2. จากเหตุ $p \rightarrow q$ และ $\neg q$ สรุปผลได้คือ $\neg p$ ตามกฎ Modus Tollens[cite: 9]", unsafe_allow_html=True)
        
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 2"):
        st.markdown("1. ตารางค่าความจริงมี 8 แถว โดยผลลัพธ์ประพจน์ประเมินตามลำดับตัวเชื่อมในวงเล็บ[cite: 10]<br>2. สมมูลกับ $\neg p \wedge \neg q$ ตามกฎเดอมอร์แกน[cite: 10]", unsafe_allow_html=True)
        
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 3"):
        st.markdown("1. เป็นสัจนิรันดร์ เนื่องจากเมื่อสมมติให้เป็นเท็จจะเกิดข้อขัดแย้ง[cite: 14]<br>2. เป็นสัจนิรันดร์เพราะสมมูลกับรูปเงื่อนไขพื้นฐาน[cite: 14]", unsafe_allow_html=True)
        
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 4"):
        st.markdown("1. สมเหตุสมผลตามกฎ Modus Tollens[cite: 20]<br>2. สมเหตุสมผลตามกฎ Constructive Dilemma[cite: 16]", unsafe_allow_html=True)
        
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 5"):
        st.markdown("1. $\exists x (P(x) \wedge \neg Q(x))$[cite: 24]<br>2. ลำดับต่างกันเพราะขอบเขตและการผูกตัวแปรให้ผลลัพธ์ทางตรรกะต่างกันบนจำนวนเต็ม[cite: 24]", unsafe_allow_html=True)
        
    with st.expander("👉 เฉลยแบบฝึกหัด บทที่ 6"):
        st.markdown("1. พิสูจน์ขั้นฐาน $n=1$ และอุปนัยสเต็ปสำหรับ $n=k+1$ สำเร็จ[cite: 27]<br>2. อุปนัยสรุปจากกรณีเฉพาะสู่นามธรรมทั่วไป ส่วนนิรนัยใช้กฎตรรกะสืบทอดจากเหตุ[cite: 27]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 9. สรุปสูตรรวมทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 สรุปสูตรรวมทั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎทางตรรกศาสตร์รวมทุกบท</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📋 สรุปสูตรประจำทุกบทแบบรวบยอด</h3>
        <ul>
            <li><b>บทที่ 1 (Modus Ponens / Tollens):</b> $p, p \rightarrow q \vdash q$ และ $p \rightarrow q, \neg q \vdash \neg p$[cite: 8, 9]</li>
            <li><b>บทที่ 2 (Equivalences & De Morgan):</b> 
                <br>• $A \rightarrow B \equiv \neg A \vee B$[cite: 10]
                <br>• $\neg(A \wedge B) \equiv \neg A \vee \neg B$[cite: 10]
                <br>• $\neg(A \vee B) \equiv \neg A \wedge \neg B$[cite: 10]
            </li>
            <li><b>บทที่ 3 (Excluded Middle):</b> $p \vee \neg p \equiv T$[cite: 14]</li>
            <li><b>บทที่ 4 (Inference Rules):</b> 
                <br>• Hypothetical Syllogism: $A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$[cite: 20]
                <br>• Constructive Dilemma: $(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$[cite: 16]
            </li>
            <li><b>บทที่ 5 (Quantifier Negation):</b> $\neg \forall x P(x) \equiv \exists x \neg P(x)$ และ $\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 24]</li>
            <li><b>บทที่ 6 (Mathematical Induction):</b> 
                <br>• $1 + 3 + \dots + (2n-1) = n^2$[cite: 27]
                <br>• $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 31]
            </li>
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
            <li><b>Epp, S. S. (2011).</b> <i>Discrete Mathematics with Applications</i> (4th ed.). Brooks/Cole.</li>
            <li><b>Rosen, K. H. (2019).</b> <i>Discrete Mathematics and Its Applications</i> (8th ed.). McGraw-Hill Education.</li>
            <li><b>Enderton, H. B. (2001).</b> <i>A Mathematical Introduction to Logic</i> (2nd ed.). Academic Press.</li>
            <li><b>Velleman, D. J. (2019).</b> <i>How to Prove It: A Structured Approach</i> (3rd ed.). Cambridge University Press.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
