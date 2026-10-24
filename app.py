import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="สื่อการเรียนรู้วิชาตรรกศาสตร์เชิงคณิตศาสตร์",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 30px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 20px;
        color: #1E3A8A;
        font-weight: 700;
        border-left: 5px solid #2563EB;
        padding-left: 10px;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .card-box {
        background-color: #F8FAFC;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        margin-bottom: 15px;
    }
    .solution-box {
        background-color: #ECFDF5;
        border: 1px solid #10B981;
        padding: 12px;
        border-radius: 8px;
        margin-top: 8px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.markdown("### 🧭 เมนูบทเรียนตรรกศาสตร์")
main_menu = st.sidebar.radio(
    "เลือกบทเรียน:",
    [
        "📘 บทที่ 1: ประพจน์และการให้เหตุผล",
        "📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง",
        "📙 บทที่ 3: สัจนิรันดร์",
        "📕 บทที่ 4: การอ้างเหตุผล",
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ",
        "📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์",
        "📐 สรุปสูตรทั้งหมด",
        "📝 แบบฝึกหัดท้าทาย 10 ข้อพร้อมเฉลย",
        "⚡ เครื่องมือคำนวณอัจฉริยะ"
    ]
)

# ---------------------------------------------------------
# 1. บทที่ 1
# ---------------------------------------------------------
if main_menu == "📘 บทที่ 1: ประพจน์และการให้เหตุผล":
    st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง ($\text{True}$) หรือเท็จ ($\text{False}$) อย่างใดอย่างหนึ่งเท่านั้น ประพจน์เชิงเดี่ยวแทนด้วยตัวอักษร $p, q, r, s$ ส่วนประพจน์เชิงซ้อนสร้างขึ้นผ่านตัวเชื่อมทางตรรกศาสตร์ ความสมเหตุสมผลพิจารณาว่าข้อสรุปต้องเป็นจริงเสมอเมื่อเหตุทุกข้อเป็นจริง[cite: 8]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 1</div>', unsafe_allow_html=True)
    st.markdown("""
    * **กฎการแยกแยะฝ่ายหน้า (Modus Ponens):** $p, p \rightarrow q \vdash q$[cite: 8]
    * **กฎการปฏิเสธฝ่ายหลัง (Modus Tollens):** $p \rightarrow q, \neg q \vdash \neg p$[cite: 9]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 1.1:** จงพิจารณาว่าประโยค 'ประเทศไทยมีพื้นที่ติดต่อกับมหาสมุทรแปซิฟิก' เป็นประพจน์หรือไม่ และมีค่าความจริงเป็นอย่างไร?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นประพจน์ เพราะเป็นประโยคบอกเล่าที่มีค่าความจริงเป็น <b>เท็จ ($\text{False}$)</b>[cite: 8]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 1.2:** กำหนดให้ $p$ และ $p \rightarrow q$ เป็นจริง จงหาค่าความจริงของ $q$ โดยใช้หลักการ Modus Ponens")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> จากกฎ Modus Ponens ($p, p \rightarrow q \vdash q$) จะได้ว่า $q$ มีค่าความจริงเป็น <b>จริง ($\text{True}$)</b>[cite: 8]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 1.3:** กำหนดเหตุ $p \rightarrow r$ และข้อสรุป $\neg r$ จงหาข้อขัดแย้งตามหลักการพิสูจน์ทางอ้อม (Indirect Proof)")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ตามกฎ Modus Tollens จะได้ผลสรุปคือ <b>$\neg p$</b>[cite: 8, 9]</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 1 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. ประโยค 'คุณกำลังศึกษาอยู่ที่คณะใด?' เป็นประพจน์ทางตรรกศาสตร์หรือไม่ เพราะเหตุใด?")
    st.markdown("2. กำหนดเหตุ: $p \rightarrow q$ และ $\neg q$ จงหาข้อสรุปที่สมเหตุสมผลตามกฎตรรกะ")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 1"):
        st.markdown("1. ไม่เป็นประพจน์ เพราะเป็นประโยคคำถามซึ่งไม่มีค่าความจริง[cite: 8]<br>2. จากเหตุ $p \rightarrow q$ และ $\neg q$ สรุปผลได้คือ $\neg p$ ตามกฎ Modus Tollens[cite: 9]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. บทที่ 2
# ---------------------------------------------------------
elif main_menu == "📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมทางตรรกศาสตร์และตารางค่าความจริง</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p>ตัวเชื่อมหลักประกอบด้วย นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การimplie ($\rightarrow$), และสมมูล ($\leftrightarrow$) ตารางค่าความจริงสำหรับประพจน์ $n$ ตัวแปรจะมีทั้งหมด $2^n$ แถว[cite: 10]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 2</div>', unsafe_allow_html=True)
    st.markdown("""
    * **สมมูลของการimplie:** $A \rightarrow B \equiv \neg A \vee B$[cite: 10]
    * **กฎเดอมอร์แกน (De Morgan's Laws):** $\neg(A \wedge B) \equiv \neg A \vee \neg B$ และ $\neg(A \vee B) \equiv \neg A \wedge \neg B$[cite: 10]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 2.1:** กำหนดให้ประพจน์ $p \equiv T$ และ $q \equiv F$ จงหาค่าความจริงของ $p \vee q$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ตัวเชื่อม หรือ ($\vee$) จะเป็นเท็จก็ต่อเมื่อเป็นเท็จทั้งคู่ ดังนั้น $T \vee F \equiv$ <b>จริง ($\text{True}$)</b>[cite: 10]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 2.2:** จงแปลงประพจน์ $p \rightarrow q$ ให้เป็นรูปดิสจังชัน (Disjunction)")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมูลกับ $\neg p \vee q$[cite: 10]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 2.3:** จงหานิเสธของประพจน์เชื่อม $p \wedge q$ ตามกฎเดอมอร์แกน")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> $\neg(p \wedge q) \equiv \neg p \vee \neg q$[cite: 10]</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 2 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. จงสร้างตารางค่าความจริงของประพจน์ $(p \wedge q) \rightarrow r$")
    st.markdown("2. จงหาประพจน์ที่สมมูลกับ $\neg(p \vee q)$")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 2"):
        st.markdown("1. ตารางค่าความจริงมี 8 แถว โดยผลลัพธ์ประพจน์ประเมินตามลำดับตัวเชื่อมในวงเล็บ[cite: 10]<br>2. สมมูลกับ $\neg p \wedge \neg q$ ตามกฎเดอมอร์แกน[cite: 10]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. บทที่ 3
# ---------------------------------------------------------
elif main_menu == "📙 บทที่ 3: สัจนิรันดร์":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์ (Tautologies)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็นจริงทุกกรณี ตรวจสอบได้โดยการสร้างตารางค่าความจริงหรือสมมติให้เป็นเท็จเพื่อหาข้อขัดแย้ง[cite: 14]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 3</div>', unsafe_allow_html=True)
    st.markdown("""
    * **กฎความเป็นจริงกึ่งกลาง (Law of Excluded Middle):** $p \vee \neg p \equiv T$
    * **ทฤษฎีบทการหักล้าง (Deduction Theorem):** $A_1, ..., A_n \models C \iff (A_1 \wedge ... \wedge A_n) \rightarrow C$ เป็นสัจนิรันดร์[cite: 14]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 3.1:** จงตรวจสอบว่า $p \vee \neg p$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> มีค่าความจริงเป็นจริงทุกกรณี ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 3.2:** จงตรวจสอบว่า $(p \wedge q) \rightarrow p$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมมติให้เป็นเท็จ จะได้ $p \wedge q \equiv T$ และ $p \equiv F$ ทำให้ $p$ เป็นจริงและเท็จพร้อมกัน เกิดข้อขัดแย้ง ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 3.3:** จงตรวจสอบว่า $p \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นเท็จเมื่อ $p \equiv T$ และ $q \equiv F$ ดังนั้น <b>ไม่เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 3 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. จงตรวจสอบว่าประพจน์ $p \rightarrow (p \vee q)$ เป็นสัจนิรันดร์หรือไม่")
    st.markdown("2. จงตรวจสอบว่าประพจน์ $(p \rightarrow q) \leftrightarrow (\neg p \vee q)$ เป็นสัจนิรันดร์หรือไม่")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 3"):
        st.markdown("1. เป็นสัจนิรันดร์ เนื่องจากเมื่อสมมติให้เป็นเท็จจะเกิดข้อขัดแย้ง[cite: 14]<br>2. เป็นสัจนิรันดร์เพราะสมมูลกับรูปเงื่อนไขพื้นฐาน[cite: 14]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. บทที่ 4
# ---------------------------------------------------------
elif main_menu == "📕 บทที่ 4: การอ้างเหตุผล":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p>การอ้างเหตุผลจะ<b>สมเหตุสมผล (Valid)</b> เมื่อกรณีที่เหตุทุกข้อเป็นจริง ผลสรุปต้องเป็นจริงด้วย โดยอิงตามกฎการอ้างเหตุผลสำคัญ[cite: 20]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 4</div>', unsafe_allow_html=True)
    st.markdown("""
    * **กฎฮิปปอเทติคัลซิลโลจิซึม (Hypothetical Syllogism):** $A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$[cite: 20]
    * **กฎคอนสตรัคทีฟไดเลมมา (Constructive Dilemma):** $(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$[cite: 16]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 4.1:** เหตุ: $p \rightarrow q, q \rightarrow r$ | ผลสรุป: $p \rightarrow r$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Hypothetical Syllogism[cite: 20]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 4.2:** เหตุ: $p \vee q, \neg p$ | ผลสรุป: $q$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> สมเหตุสมผลตามกฎ Disjunctive Syllogism[cite: 20]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 4.3:** เหตุ: $p \rightarrow q, q$ | ผลสรุป: $p$ สมเหตุสมผลหรือไม่")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ไม่สมเหตุสมผล (Fallacy: Affirming the consequent)[cite: 20]</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 4 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. ตรวจสอบความสมเหตุสมผลของเหตุ: $p \rightarrow q, \neg q$ ข้อสรุป: $\neg p$")
    st.markdown("2. ตรวจสอบความสมเหตุสมผลของเหตุ: $(p \vee q), p \rightarrow r, q \rightarrow r$ ข้อสรุป: $r$")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 4"):
        st.markdown("1. สมเหตุสมผลตามกฎ Modus Tollens[cite: 20]<br>2. สมเหตุสมผลตามกฎ Constructive Dilemma[cite: 16]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. บทที่ 5
# ---------------------------------------------------------
elif main_menu == "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p>ประโยคเปิด $P(x)$ จะมีตัวแปรเสรี ตัวบ่งปริมาณประกอบด้วยสำหรับทุกตัว ($\forall x$) และสำหรับบางตัว ($\exists x$) ลำดับของตัวบ่งปริมาณส่งผลต่อค่าความจริง[cite: 24]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 5</div>', unsafe_allow_html=True)
    st.markdown("""
    * **นิเสธตัวบ่งปริมาณสากล:** $\neg \forall x P(x) \equiv \exists x \neg P(x)$[cite: 24]
    * **นิเสธตัวบ่งปริมาณเฉพาะตัว:** $\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 24]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 5.1:** จงหานิเสธของ $\forall x P(x)$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> $\exists x \neg P(x)$[cite: 24]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 5.2:** จงหานิเสธของ $\exists x \forall y Q(x, y)$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> $\forall x \exists y \neg Q(x, y)$[cite: 24]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 5.3:** บนเอกภพสัมพัทธ์จำนวนเต็ม ข้อความ $\forall x \exists y (x < y)$ เป็นจริงหรือเท็จ")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> เป็นจริง เพราะสำหรับทุกจำนวนเต็ม $x$ จะมี $y = x + 1$ เสมอ[cite: 24]</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 5 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. จงหานิเสธของประโยค: $\forall x (P(x) \rightarrow Q(x))$")
    st.markdown("2. อธิบายเหตุใดลำดับ $\forall x \exists y (x < y)$ จึงแตกต่างจาก $\exists y \forall x (x < y)$ บนจำนวนเต็ม")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 5"):
        st.markdown("1. $\exists x (P(x) \wedge \neg Q(x))$[cite: 24]<br>2. ลำดับต่างกันเพราะขอบเขตและการผูกตัวแปรให้ผลลัพธ์ทางตรรกะต่างกันบนจำนวนเต็ม[cite: 24]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. บทที่ 6
# ---------------------------------------------------------
elif main_menu == "📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
        <p>การอุปนัยเชิงคณิตศาสตร์ประกอบด้วย ขั้นฐาน ($\text{Base case}$ สำหรับ $n=1$) และขั้นอุปนัย ($\text{Inductive step}$ จาก $P(k) \rightarrow P(k+1)$) สำหรับพิสูจน์ประพจน์จำนวนเต็มบวก[cite: 27]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">📐 สรุปสูตรประจำบทที่ 6</div>', unsafe_allow_html=True)
    st.markdown("""
    * **ผลบวกจำนวนคี่ $n$ พจน์แรก:** $1 + 3 + \dots + (2n-1) = n^2$[cite: 27]
    * **ผลบวกกำลังสาม $n$ พจน์แรก:** $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 31]
    """)

    st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำ (3 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("**ตัวอย่าง 6.1:** จงตรวจสอบสูตรผลบวกกำลังสาม $1^3 + 2^3 = [\frac{n(n+1)}{2}]^2$ เมื่อ $n=2$")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ฝั่งซ้าย = $1 + 8 = 9$, ฝั่งขวา = $[\frac{2(3)}{2}]^2 = 3^2 = 9$ (เป็นจริง)[cite: 31]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 6.2:** ขั้นตอนแรกของการพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์เรียกว่าอะไร?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> ขั้นฐาน ($\text{Base Case}$) สำหรับ $n=1$[cite: 27]</div>', unsafe_allow_html=True)
    
    st.markdown("**ตัวอย่าง 6.3:** สมมติฐานการอุปนัย ($\text{Inductive Hypothesis}$) คืออะไร?")
    st.markdown('<div class="solution-box"><b>เฉลย:</b> การสมมติให้ประพจน์เป็นจริงเมื่อ $n=k$[cite: 27, 31]</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดประจำบทที่ 6 (2 ข้อ)</div>', unsafe_allow_html=True)
    st.markdown("1. จงพิสูจน์ว่า $1 + 3 + \dots + (2n-1) = n^2$ สำหรับทุก $n \ge 1$")
    st.markdown("2. จงอธิบายความแตกต่างระหว่างการอุปนัยและนิรนัย")
    
    with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 6"):
        st.markdown("1. พิสูจน์ขั้นฐาน $n=1$ และอุปนัยสเต็ปสำหรับ $n=k+1$ สำเร็จ[cite: 27]<br>2. อุปนัยสรุปจากกรณีเฉพาะสู่นามธรรมทั่วไป ส่วนนิรนัยใช้กฎตรรกะสืบทอดจากเหตุ[cite: 27]", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. สรุปสูตรทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 สรุปสูตรทั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎทางตรรกศาสตร์ทั้งหมด</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📋 รวมสูตรสำคัญทุกบท</h3>
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
# 8. แบบฝึกหัดท้าทาย 10 ข้อพร้อมเฉลย
# ---------------------------------------------------------
elif main_menu == "📝 แบบฝึกหัดท้าทาย 10 ข้อพร้อมเฉลย":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 แบบฝึกหัดท้าทายรวม 10 ข้อ (ทำก่อนดูเฉลย)</div>', unsafe_allow_html=True)
    st.markdown("คำชี้แจง: ให้ผู้เล่นทำแบบฝึกหัดด้านล่างนี้ทีละข้อ จากนั้นสามารถกดเปิดดูเฉลยที่ด้านล่างสุดได้ครับ")

    q_answers = []
    
    st.markdown("---")
    st.markdown("**ข้อ 1:** ประโยค 'ขอให้ทุกคนโชคดีกับการสอบ' เป็นประพจน์ทางตรรกศาสตร์หรือไม่?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 1:", ["เป็นประพจน์", "ไม่เป็นประพจน์"], key="quiz1"))

    st.markdown("---")
    st.markdown("**ข้อ 2:** กำหนดให้ $p \equiv F, q \equiv T$ ค่าความจริงของ $p \wedge q$ คือข้อใด?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 2:", ["จริง (True)", "เท็จ (False)"], key="quiz2"))

    st.markdown("---")
    st.markdown("**ข้อ 3:** ประพจน์ $p \rightarrow q$ สมมูลกับประพจน์ใด?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 3:", ["$\neg p \vee q$", "$\neg p \wedge q$", "$p \vee \neg q$"], key="quiz3"))

    st.markdown("---")
    st.markdown("**ข้อ 4:** นิเสธของประพจน์ $\neg(p \wedge q)$ ตามกฎเดอมอร์แกนคือข้อใด?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 4:", ["$\neg p \wedge \neg q$", "$\neg p \vee \neg q$", "$p \vee q$"], key="quiz4"))

    st.markdown("---")
    st.markdown("**ข้อ 5:** ประพจน์ $p \vee \neg p$ มีชื่อเรียกว่าอะไร?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 5:", ["สัจนิรันดร์ (Tautology)", "ข้อขัดแย้ง (Contradiction)"], key="quiz5"))

    st.markdown("---")
    st.markdown("**ข้อ 6:** กฎการอ้างเหตุผล $p, p \rightarrow q \vdash q$ มีชื่อเรียกว่าอะไร?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 6:", ["Modus Ponens", "Modus Tollens"], key="quiz6"))

    st.markdown("---")
    st.markdown("**ข้อ 7:** ข้อสรุปจากเหตุ $p \rightarrow q$ และ $\neg q$ คือข้อใดตามกฎ Modus Tollens?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 7:", ["$\neg p$", "$p$", "$q$"], key="quiz7"))

    st.markdown("---")
    st.markdown("**ข้อ 8:** นิเสธของข้อความ $\forall x P(x)$ คือข้อใด?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 8:", ["$\exists x \neg P(x)$", "$\forall x \neg P(x)$"], key="quiz8"))

    st.markdown("---")
    st.markdown("**ข้อ 9:** ขั้นตอนแรกของการพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์คืออะไร?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 9:", ["ขั้นฐาน (Base Case สำหรับ $n=1$)", "ขั้นอุปนัย (Inductive step)"], key="quiz9"))

    st.markdown("---")
    st.markdown("**ข้อ 10:** สูตรผลบวกกำลังสาม $1^3 + 2^3 + \dots + n^3$ มีค่าเท่ากับข้อใด?")
    q_answers.append(st.radio("เลือกคำตอบ ข้อ 10:", ["$[\frac{n(n+1)}{2}]^2$", "$n^2$", "$\frac{n(n+1)(2n+1)}{6}$"], key="quiz10"))

    st.markdown("---")
    if st.button("📥 ตรวจคำตอบทั้งหมด"):
        st.success("ทำแบบฝึกหัดครบแล้ว! เลื่อนลงไปดูเฉลยละเอียดด้านล่างได้เลยครับ")

    st.markdown("---")
    st.markdown("## 🔑 เฉลยแบบฝึกหัดท้าทาย 10 ข้อ")
    with st.expander("👉 คลิกเพื่อเปิดดูเฉลยครบทั้ง 10 ข้อ"):
        st.markdown("""
        * **ข้อ 1 เฉลย:** **ไม่เป็นประพจน์** (เพราะเป็นประโยคขอร้อง/อวยพร ไม่มีค่าความจริง)[cite: 8]
        * **ข้อ 2 เฉลย:** **เท็จ (False)** (เนื่องจากตัวเชื่อม $\wedge$ เป็นเท็จเมื่อมีตัวใดตัวหนึ่งเป็นเท็จ)[cite: 10]
        * **ข้อ 3 เฉลย:** **$\neg p \vee q$** (สมมูลของการimplie)[cite: 10]
        * **ข้อ 4 เฉลย:** **$\neg p \vee \neg q$** (กฎเดอมอร์แกน)[cite: 10]
        * **ข้อ 5 เฉลย:** **สัจนิรันดร์ (Tautology)** (เป็นจริงทุกกรณี)[cite: 14]
        * **ข้อ 6 เฉลย:** **Modus Ponens**[cite: 8]
        * **ข้อ 7 เฉลย:** **$\neg p$** (Modus Tollens)[cite: 9]
        * **ข้อ 8 เฉลย:** **$\exists x \neg P(x)$**[cite: 24]
        * **ข้อ 9 เฉลย:** **ขั้นฐาน (Base Case สำหรับ $n=1$)**[cite: 27]
        * **ข้อ 10 เฉลย:** **$[\frac{n(n+1)}{2}]^2$**[cite: 31]
        """)

# ---------------------------------------------------------
# 9. เครื่องมือคำนวณอัจฉริยะ
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
