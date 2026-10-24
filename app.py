import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="สื่อการเรียนรู้วิชาตรรกศาสตร์เชิงคณิตศาสตร์ขั้นสูง",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 26px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 18px;
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
# Sidebar Navigation (Granular Submenu Structure)
# ---------------------------------------------------------
st.sidebar.markdown("### 🧭 เมนูบทเรียนและเมนูย่อย")
main_menu = st.sidebar.selectbox(
    "เลือกเมนูหัวข้อหลักและเมนูย่อยต่อบท:", [
        # บทที่ 1
        "📘 บทที่ 1: 1.1 เนื้อหาและแนวคิดหลัก",
        "📘 บทที่ 1: 1.2 สูตรและสัญลักษณ์ประจำบท",
        "📘 บทที่ 1: 1.3 ตัวอย่างพร้อมวิธีทำ",
        "📘 บทที่ 1: 1.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # บทที่ 2
        "📗 บทที่ 2: 2.1 เนื้อหาและแนวคิดหลัก",
        "📗 บทที่ 2: 2.2 สูตรและสัญลักษณ์ประจำบท",
        "📗 บทที่ 2: 2.3 ตัวอย่างพร้อมวิธีทำ",
        "📗 บทที่ 2: 2.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # บทที่ 3
        "📙 บทที่ 3: 3.1 เนื้อหาและแนวคิดหลัก",
        "📙 บทที่ 3: 3.2 สูตรและสัญลักษณ์ประจำบท",
        "📙 บทที่ 3: 3.3 ตัวอย่างพร้อมวิธีทำ",
        "📙 บทที่ 3: 3.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # บทที่ 4
        "📕 บทที่ 4: 4.1 เนื้อหาและแนวคิดหลัก",
        "📕 บทที่ 4: 4.2 สูตรและสัญลักษณ์ประจำบท",
        "📕 บทที่ 4: 4.3 ตัวอย่างพร้อมวิธีทำ",
        "📕 บทที่ 4: 4.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # บทที่ 5
        "🟣 บทที่ 5: 5.1 เนื้อหาและแนวคิดหลัก",
        "🟣 บทที่ 5: 5.2 สูตรและสัญลักษณ์ประจำบท",
        "🟣 บทที่ 5: 5.3 ตัวอย่างพร้อมวิธีทำ",
        "🟣 บทที่ 5: 5.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # บทที่ 6
        "📓 บทที่ 6: 6.1 เนื้อหาและแนวคิดหลัก",
        "📓 บทที่ 6: 6.2 สูตรและสัญลักษณ์ประจำบท",
        "📓 บทที่ 6: 6.3 ตัวอย่างพร้อมวิธีทำ",
        "📓 บทที่ 6: 6.4 โจทย์ฝึกหัดพร้อมเฉลย",
        
        # เมนูเสริม
        "📐 เมนูสรุปสูตรทั้งหมด (รวมทุกบท)",
        "📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ",
        "⚡ เครื่องมือคำนวณอัจฉริยะ"
    ]
)

# Sidebar Progress & Utilities
st.sidebar.markdown("---")
st.sidebar.markdown("📊 **สถานะการอ่านบทเรียน**")
st.sidebar.progress(100)
st.sidebar.caption("โหลดเนื้อหาครบถ้วน 6 บท พร้อมแบบทดสอบ")

if st.sidebar.button("⬆️ กลับไปด้านบนสุด"):
    st.rerun()

# ---------------------------------------------------------
# บทที่ 1: ประพจน์และการให้เหตุผล
# ---------------------------------------------------------
if "บทที่ 1" in main_menu:
    if "1.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง ($\text{True}$) หรือเท็จ ($\text{False}$) อย่างใดอย่างหนึ่งเท่านั้น ประพจน์เชิงเดี่ยว (Atomic propositions) มักแทนด้วยตัวอักษร $p, q, r, s$ ส่วนประพจน์เชิงซ้อนสร้างขึ้นผ่านตัวเชื่อมทางตรรกศาสตร์ ความสมเหตุสมผลพิจารณาว่าข้อสรุปต้องเป็นจริงเสมอเมื่อเหตุทุกข้อเป็นจริง</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "1.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 1</div>', unsafe_allow_html=True)
        st.markdown(r"* **Modus Ponens:** $$p, p \rightarrow q \vdash q$$")
        st.markdown(r"* **Modus Tollens:** $$p \rightarrow q, \neg q \vdash \neg p$$")

    elif "1.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 1.1: การวิเคราะห์ค่าความจริงของประพจน์เงื่อนไขซับซ้อน"):
            st.markdown(r"<b>โจทย์:</b> จงพิจารณาว่าประโยค 'ถ้า $x^2 < 0$ แล้ว $x$ เป็นจำนวนจริง' มีค่าความจริงเป็นอย่างไร?")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. แยกประพจน์ย่อย: ให้ $p$ คือ $x^2 < 0$ และ $q$ คือ $x$ เป็นจำนวนจริง<br>2. ประพจน์เหตุ $p$ ($x^2 < 0$) มีค่าความจริงเป็นเท็จ ($\text{False}$) เสมอในระบบจำนวนจริง<br>3. ประพจน์ผล $q$ ($x$ เป็นจำนวนจริง) มีค่าความจริงเป็นจริง ($\text{True}$)<br>4. ตามนิยามของประพจน์เงื่อนไข $F \rightarrow T$ จะได้ค่าความจริงรวมเป็น <b>จริง ($\text{True}$)</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 1.2: การประยุกต์ใช้กฎ Modus Ponens ขั้นสูง"):
            st.markdown(r"<b>โจทย์:</b> กำหนดเหตุ: 1) $(p \wedge q) \rightarrow r$ และ 2) $(p \wedge q)$ จงหาค่าความจริงของ $r$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. ให้ตัวแปรเสริม $A = (p \wedge q)$<br>2. จัดรูปเหตุใหม่จะได้ $A \rightarrow r$ และ $A$<br>3. ใช้กฎ Modus Ponens สรุปผลลัพธ์จะได้ $r \equiv \text{True}$ (จริง)</div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 1.3: การพิสูจน์ทางอ้อม (Indirect Proof)"):
            st.markdown(r"<b>โจทย์:</b> กำหนดเหตุ $p \rightarrow (q \rightarrow r)$ และสมมติให้ $\neg r \wedge q$ เป็นจริง จงหาค่าความจริงของ $p$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. จาก $\neg r \wedge q \equiv T$ จะได้ $q \equiv T$ และ $r \equiv F$<br>2. แทนค่า $r \equiv F$ ในวงเล็บหลัง $q \rightarrow r$ จะได้ $T \rightarrow F \equiv F$<br>3. เมื่อเหตุทั้งหมดเป็นจริง จะได้ $p \rightarrow F \equiv T$ บังคับให้ $p$ ต้องเป็น <b>เท็จ ($\text{False}$)</b></div>', unsafe_allow_html=True)

    elif "1.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 1</div>', unsafe_allow_html=True)
        st.markdown("1. ประโยค 'สำหรับทุกจำนวนจริง $x$ ถ้า $x > 2$ แล้ว $x^2 > 4$' เป็นประพจน์หรือไม่?")
        st.markdown("2. กำหนดเหตุ: $p \rightarrow (q \rightarrow r)$, $p$, และ $q$ จงหาข้อสรุปที่สมเหตุสมผล")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 1"):
            st.markdown("1. เป็นประพจน์ เพราะมีค่าความจริงเป็นจริงแน่นอนบนโดเมนจำนวนจริง<br>2. ข้อสรุปคือ $r$ โดยใช้กฎ Modus Ponens ซ้อนกันสองครั้ง", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 2: ตัวเชื่อมและตารางค่าความจริง
# ---------------------------------------------------------
elif "บทที่ 2" in main_menu:
    if "2.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p>ตัวเชื่อมหลักประกอบด้วย นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การimplie ($\rightarrow$), และสมมูล ($\leftrightarrow$) ตารางค่าความจริง (Truth Table) สำหรับประพจน์ที่มี $n$ ตัวแปรที่แตกต่างกัน จะมีจำนวนแถวทั้งหมดเท่ากับ $2^n$ แถว การประเมินค่าความจริงต้องทำจากวงเล็บชั้นในสุดออกสู่ภายนอก</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "2.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 2</div>', unsafe_allow_html=True)
        st.markdown(r"* **สมมูลของประพจน์เงื่อนไข:** $$A \rightarrow B \equiv \neg A \vee B$$")
        st.markdown(r"* **กฎเดอมอร์แกน (De Morgan's Laws):** $$\neg(A \wedge B) \equiv \neg A \vee \neg B$$ และ $$\neg(A \vee B) \equiv \neg A \wedge \neg B$$")

    elif "2.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 2.1: การสร้างตารางค่าความจริง 3 ตัวแปร"):
            st.markdown(r"<b>โจทย์:</b> จงสร้างตารางค่าความจริงเพื่อตรวจสอบประพจน์ $(p \wedge q) \rightarrow r$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. มี 3 ตัวแปร ($p, q, r$) ตารางจะมีทั้งหมด $2^3 = 8$ แถว<br>2. ประเมินค่า $p \wedge q$ ก่อน แล้วจึงนำไปเชื่อมด้วย $\rightarrow r$<br>3. ผลลัพธ์จะเป็นเท็จ ($\text{False}$) เพียงกรณีเดียวคือเมื่อ $p \equiv T, q \equiv T$ และ $r \equiv F$</div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 2.2: การจัดรูปประพจน์ซับซ้อนด้วยกฎสมมูล"):
            st.markdown(r"<b>โจทย์:</b> จงลดรูปประพจน์ $\neg(p \rightarrow \neg q)$ ให้เหลือเฉพาะตัวเชื่อมพื้นฐาน")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. แปลงเงื่อนไขในวงเล็บ: $(p \rightarrow \neg q) \equiv \neg p \vee \neg q$<br>2. ใส่เครื่องหมายนิเสธภายนอก: $\neg(\neg p \vee \neg q)$<br>3. ใช้กฎเดอมอร์แกน: $(\neg \neg p \wedge \neg \neg q)$<br>4. ใช้กฎนิเสธซ้อนจะได้คำตอบ: <b>$p \wedge q$</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 2.3: การตรวจสอบสมมูลเชิงตรรกะของประพจน์"):
            st.markdown(r"<b>โจทย์:</b> จงพิสูจน์ว่า $p \leftrightarrow q$ สมมูลกับ $(p \rightarrow q) \wedge (q \rightarrow p)$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. สร้างตารางค่าความจริงเปรียบเทียบระหว่างสองฝั่ง<br>2. สังเกตว่าคอลัมน์ผลลัพธ์สุดท้ายมีค่าความจริงตรงกันในทุกๆ แถว (ทุกกรณี)<br>3. ดังนั้น ประพจน์ทั้งสองจึง <b>สมมูลกันเชิงตรรกะ</b></div>', unsafe_allow_html=True)

    elif "2.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 2</div>', unsafe_allow_html=True)
        st.markdown("1. จงหาประพจน์ที่สมมูลกับ $\neg(p \leftrightarrow q)$ โดยใช้เฉพาะตัวเชื่อม $\neg, \wedge, \vee$")
        st.markdown("2. สร้างตารางค่าความจริงของประพจน์ $[p \wedge (q \vee r)] \leftrightarrow [(p \wedge q) \vee (p \wedge r)]$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 2"):
            st.markdown("1. $(p \wedge \neg q) \vee (\neg p \wedge q)<br>2. เป็นสัจนิรันดร์ (กฎการแจกแจง Distributive Law)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง
# ---------------------------------------------------------
elif "บทที่ 3" in main_menu:
    if "3.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็นจริง ($\text{True}$) ทุกกรณีภายใต้ทุกการกำหนดค่าความจริง ส่วน <b>ข้อขัดแย้ง (Contradiction)</b> คือประพจน์ที่เป็นเท็จทุกกรณี การตรวจสอบทำได้โดยการสร้างตารางค่าความจริงหรือใช้วิธีสมมติให้ประพจน์เป็นเท็จเพื่อหาข้อขัดแย้ง (Countervaluation)</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "3.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 3</div>', unsafe_allow_html=True)
        st.markdown(r"* **กฎความเป็นจริงกึ่งกลาง:** $$p \vee \neg p \equiv T$$")
        st.markdown(r"* **ทฤษฎีบทการหักล้าง (Deduction Theorem):** $$A_1, ..., A_n \models C \iff (A_1 \wedge ... \wedge A_n) \rightarrow C \text{ เป็นสัจนิรันดร์}$$")

    elif "3.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 3.1: การพิสูจน์สัจนิรันดร์โดยวิธีหาข้อขัดแย้ง"):
            st.markdown(r"<b>โจทย์:</b> จงตรวจสอบว่าประพจน์ $[(p \rightarrow q) \wedge p] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. สมมติให้ประพจน์เป็นเท็จ ($\equiv F$) จะได้เหตุเป็นจริงและผลเป็นเท็จ: $[(p \rightarrow q) \wedge p] \equiv T$ และ $q \equiv F$<br>2. จากเหตุที่เป็นจริง จะได้ $p \equiv T$ และ $(p \rightarrow q) \equiv T$<br>3. แทนค่า $p \equiv T, q \equiv F$ ใน $p \rightarrow q$ จะได้ $T \rightarrow F \equiv F$ ซึ่งขัดแย้งกับข้อ 2<br>4. เกิดข้อขัดแย้ง ดังนั้นประพจน์นี้ <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 3.2: การตรวจสอบประพจน์เงื่อนไขซับซ้อน"):
            st.markdown(r"<b>โจทย์:</b> จงตรวจสอบว่า $[(p \rightarrow q) \wedge (q \rightarrow r)] \rightarrow (p \rightarrow r)$ เป็นสัจนิรันดร์หรือไม่")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. สมมติให้ประพจน์เป็นเท็จ จะได้ $p \rightarrow r \equiv F$ ซึ่งบังคับให้ $p \equiv T$ และ $r \equiv F$<br>2. นำไปตรวจสอบวงเล็บเหตุ: ต้องทำให้ $(p \rightarrow q) \wedge (q \rightarrow r) \equiv T$<br>3. จะได้ $p \rightarrow q \equiv T \implies q \equiv T$ และ $q \rightarrow r \equiv T \rightarrow F \equiv F$ ซึ่งขัดแย้ง<br>4. สรุปได้ว่า <b>เป็นสัจนิรันดร์</b> (กฎ Hypothetical Syllogism)</div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 3.3: การวิเคราะห์ประพจน์ข้อขัดแย้ง"):
            st.markdown(r"<b>โจทย์:</b> จงตรวจสอบว่า $(p \wedge q) \wedge \neg(p \vee q)$ เป็นข้อขัดแย้งหรือไม่")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. กระจายกฎเดอมอร์แกนที่พจน์หลังจะได้ $\neg p \wedge \neg q$<br>2. จัดรูปใหม่โดยสมบัติการเปลี่ยนกลุ่ม: $(p \wedge \neg p) \wedge (q \wedge \neg q)$<br>3. เนื่องจาก $p \wedge \neg p \equiv F$ จะได้ $F \wedge F \equiv F$ ทุกกรณี<br>4. ดังนั้นประพจน์นี้ <b>เป็นข้อขัดแย้ง</b></div>', unsafe_allow_html=True)

    elif "3.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 3</div>', unsafe_allow_html=True)
        st.markdown("1. จงตรวจสอบว่า $[p \wedge (p \rightarrow q)] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown("2. ตรวจสอบว่า $[(p \vee q) \wedge \neg p] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 3"):
            st.markdown("1. เป็นสัจนิรันดร์ (Modus Ponens)<br>2. เป็นสัจนิรันดร์ (Disjunctive Syllogism)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 4: การอ้างเหตุผล
# ---------------------------------------------------------
elif "บทที่ 4" in main_menu:
    if "4.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p>การอ้างเหตุผลประกอบด้วยชุดของประพจน์เหตุ (Premises) และประพจน์ผลสรุป (Conclusion) การอ้างเหตุผลจะ <b>สมเหตุสมผล (Valid)</b> ก็ต่อเมื่อ ทุกกรณีที่ประพจน์เหตุทุกข้อเป็นจริงพร้อมกัน จะบังคับให้ประพจน์ผลสรุปเป็นจริงตามไปด้วยเสมอ</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "4.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 4</div>', unsafe_allow_html=True)
        st.markdown(r"* **Hypothetical Syllogism:** $$A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$$")
        st.markdown(r"* **Constructive Dilemma:** $$(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$$")

    elif "4.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 4.1: การตรวจสอบการอ้างเหตุผลหลายบรรทัด"):
            st.markdown(r"<b>โจทย์:</b> เหตุ: 1) $p \rightarrow q$, 2) $q \rightarrow r$, 3) $\neg r$ | ผลสรุป: $\neg p$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. จากเหตุ (1) และ (2) ใช้กฎ Hypothetical Syllogism ได้ $p \rightarrow r$<br>2. นำผลลัพธ์ที่ได้ไปอ้างอิงร่วมกับเหตุ (3) คือ $\neg r$<br>3. ใช้กฎ Modus Tollens จะได้ข้อสรุปคือ $\neg p$ ตรงกับผลสรุปพอดี ดังนั้น <b>สมเหตุสมผล</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 4.2: การอ้างเหตุผลด้วยกฎ Constructive Dilemma"):
            st.markdown(r"<b>โจทย์:</b> เหตุ: 1) $p \rightarrow q$, 2) $r \rightarrow s$, 3) $p \vee r$ | ผลสรุป: $q \vee s$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b> ประพจน์ชุดนี้ตรงกับรูปมาตรฐานของกฎ Constructive Dilemma ทุกประการ ดังนั้นจึงสรุปได้ทันทีว่า <b>สมเหตุสมผล</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 4.3: การตรวจสอบความสมเหตุสมผลด้วยวิธีสมมติผลสรุปเป็นเท็จ"):
            st.markdown(r"<b>โจทย์:</b> เหตุ: 1) $p \vee q$, 2) $p \rightarrow r$, 3) $q \rightarrow s$ | ผลสรุป: $r \vee s$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. สมมติให้ผลสรุปเป็นเท็จ: $r \vee s \equiv F \implies r \equiv F$ และ $s \equiv F$<br>2. จากเหตุ (2) $p \rightarrow r \equiv F \implies p \equiv T$<br>3. จากเหตุ (3) $q \rightarrow s \equiv F \implies q \equiv T$<br>4. นำ $p \equiv T, q \equiv T$ ไปแทนในเหตุ (1) ได้ $T \vee T \equiv T$ ซึ่งไม่เกิดข้อขัดแย้งกับเหตุ<br>5. เกิดกรณีที่เหตุเป็นจริงแต่ผลเป็นเท็จ ดังนั้นการอ้างเหตุผลนี้ <b>ไม่สมเหตุสมผล (Invalid)</b></div>', unsafe_allow_html=True)

    elif "4.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 4</div>', unsafe_allow_html=True)
        st.markdown("1. เหตุ: $p \rightarrow (q \rightarrow r)$, $p$, $q$ | ผลสรุป: $r$ สมเหตุสมผลหรือไม่?")
        st.markdown("2. เหตุ: $p \vee q$, $p \rightarrow \neg r$, $q \rightarrow \neg s$ | ผลสรุป: $\neg r \vee \neg s$ สมเหตุสมผลหรือไม่?")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 4"):
            st.markdown("1. สมเหตุสมผล (Modus Ponens ซ้อน)<br>2. สมเหตุสมผล (Constructive Dilemma)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ
# ---------------------------------------------------------
elif "บทที่ 5" in main_menu:
    if "5.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p>ประโยคเปิด $P(x)$ คือประโยคที่มีตัวแปรเสรีซึ่งยังระบุค่าความจริงไม่ได้จนกว่าจะมีการแทนค่าหรือใช้ตัวบ่งปริมาณ (Quantifiers) ประกอบด้วยตัวบ่งปริมาณสากล สำหรับทุกตัว ($\forall x$) และตัวบ่งปริมาณเฉพาะตัว สำหรับบางตัว ($\exists x$) โดยลำดับของตัวบ่งปริมาณที่ต่างกันจะให้ความหมายและค่าความจริงที่แตกต่างกัน</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "5.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 5</div>', unsafe_allow_html=True)
        st.markdown(r"* **นิเสธตัวบ่งปริมาณสากล:** $$\neg \forall x P(x) \equiv \exists x \neg P(x)$$")
        st.markdown(r"* **นิเสธตัวบ่งปริมาณเฉพาะตัว:** $$\neg \exists x P(x) \equiv \forall x \neg P(x)$$")

    elif "5.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 5.1: การหานิเสธของตัวบ่งปริมาณซ้อน"):
            st.markdown(r"<b>โจทย์:</b> จงหานิเสธของประพจน์ $\forall x \exists y (x^2 + y^2 > 10)$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. ใส่เครื่องหมายนิเสธหน้าประพจน์: $\neg \forall x \exists y (x^2 + y^2 > 10)$<br>2. ดันนิเสธเข้าด้านในพร้อมเปลี่ยนตัวบ่งปริมาณ: $\exists x \forall y \neg(x^2 + y^2 > 10)$<br>3. เปลี่ยนเครื่องหมายอสมการ: <b>$\exists x \forall y (x^2 + y^2 \le 10)$</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 5.2: การวิเคราะห์ค่าความจริงของประพจน์ตัวบ่งปริมาณซ้อน"):
            st.markdown(r"<b>โจทย์:</b> บนเอกภพสัมพัทธ์จำนวนจริง ค่าความจริงของ $\forall x \exists y (x + y = 0)$ คืออะไร?")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. พิจารณาว่าสำหรับทุกจำนวนจริง $x$ จะมี $y$ ที่ทำให้สมการเป็นจริงหรือไม่<br>2. เมื่อเลือก $y = -x$ ซึ่งเป็นจำนวนจริงเสมอ จะได้สมการ $x + (-x) = 0$<br>3. ดังนั้น ค่าความจริงของประพจน์นี้จึงเป็น <b>จริง ($\text{True}$)</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 5.3: นิเสธของประพจน์เงื่อนไขที่มีตัวบ่งปริมาณ"):
            st.markdown(r"<b>โจทย์:</b> จงหานิเสธของประพจน์ $\forall x [P(x) \rightarrow Q(x)]$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. เปลี่ยน $\forall x$ เป็น $\exists x$ และใส่เครื่องหมายนิเสธในวงเล็บ: $\exists x \neg[P(x) \rightarrow Q(x)]$<br>2. ใช้สมการสมมูล $A \rightarrow B \equiv \neg A \vee B$ จะได้ $\neg[\neg P(x) \vee Q(x)]$<br>3. ใช้กฎเดอมอร์แกนจะได้คำตอบ: <b>$\exists x [P(x) \wedge \neg Q(x)]$</b></div>', unsafe_allow_html=True)

    elif "5.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 5</div>', unsafe_allow_html=True)
        st.markdown("1. จงหานิเสธของประพจน์ $\exists x \forall y [P(x) \leftrightarrow Q(y)]$")
        st.markdown("2. กำหนดเอกภพสัมพัทธ์เป็นเซตของจำนวนเต็ม จงหาค่าความจริงของ $\exists x \forall y (x \cdot y = y)$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 5"):
            st.markdown("1. $\forall x \exists y [(P(x) \wedge \neg Q(y)) \vee (\neg P(x) \wedge Q(y))]<br>2. เป็นจริง (เมื่อเลือก $x = 1$)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์
# ---------------------------------------------------------
elif "บทที่ 6" in main_menu:
    if "6.1 เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์ (เนื้อหา)</div>', unsafe_allow_html=True)
        st.markdown(r"""
        <div class="card-box">
            <p>การให้เหตุผลแบบนิรนัยเป็นการสรุปผลตามกฎเกณฑ์ตรรกะที่แน่นอน ส่วนการอุปนัยเชิงคณิตศาสตร์เป็นเทคนิคการพิสูจน์เชิง deductive สำหรับข้อความที่เกี่ยวกับจำนวนเต็มบวก $n$ โดยประกอบด้วย 2 ขั้นตอนหลัก ได้แก่ <b>ขั้นฐาน (Base Case)</b> สำหรับ $n=1$ และ <b>ขั้นอุปนัย (Inductive Step)</b> สำหรับการพิสูจน์ $P(k) \rightarrow P(k+1)$</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "6.2 สูตรและสัญลักษณ์ประจำบท" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์ (สูตร)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📐 สูตรและสัญลักษณ์ประจำบทที่ 6</div>', unsafe_allow_html=True)
        st.markdown(r"* **ผลบวกจำนวนคี่ $n$ พจน์แรก:** $$1 + 3 + \dots + (2n-1) = n^2$$")
        st.markdown(r"* **ผลบวกกำลังสาม $n$ พจน์แรก:** $$1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2$$")

    elif "6.3 ตัวอย่างพร้อมวิธีทำ" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์ (ตัวอย่าง)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">💡 ตัวอย่างพร้อมวิธีทำระดับสูง</div>', unsafe_allow_html=True)
        
        with st.expander("ตัวอย่าง 6.1: การตรวจสอบสูตรผลบวกเลขคี่"):
            st.markdown(r"<b>โจทย์:</b> จงแสดงว่าสูตร $1 + 3 + \dots + (2n-1) = n^2$ เป็นจริงเมื่อ $n = 4$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. แทนค่า $n = 4$ ในฝั่งซ้าย (บวกเลขคี่ 4 พจน์แรก): $1 + 3 + 5 + 7 = 16$<br>2. แทนค่า $n = 4$ ในฝั่งขวา: $4^2 = 16$<br>3. ฝั่งซ้ายเท่ากับฝั่งขวา ($16 = 16$) สมการจึงเป็นจริงสำหรับ $n = 4$</div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 6.2: การคำนวณผลบวกอนุกรมกำลังสาม"):
            st.markdown(r"<b>โจทย์:</b> จงหาผลบวกของอนุกรม $1^3 + 2^3 + 3^3 + 4^3 + 5^3$")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b><br>1. ใช้สูตรผลบวกกำลังสาม เมื่อ $n = 5$<br>2. คำนวณตามสูตร: $\left[\frac{5(5+1)}{2}\right]^2 = \left[\frac{30}{2}\right]^2 = [15]^2$<br>3. ผลลัพธ์สุดท้ายคือ <b>225</b></div>', unsafe_allow_html=True)

        with st.expander("ตัวอย่าง 6.3: หลักการสมมติฐานในการอุปนัย"):
            st.markdown(r"<b>โจทย์:</b> ในการพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์ หากผ่านขั้นตอน Base case แล้ว ขั้นตอนถัดไปต้องตั้งสมมติฐานอย่างไร?")
            st.markdown(r'<div class="solution-box"><b>วิธีทำ:</b> ต้องตั้งสมมติฐานว่าประพจน์เป็นจริงสำหรับ $n = k$ (เรียกว่า Inductive Hypothesis) แล้วนำไปใช้พิสูจน์ต่อให้เป็นจริงสำหรับ $n = k + 1$</div>', unsafe_allow_html=True)

    elif "6.4 โจทย์ฝึกหัดพร้อมเฉลย" in main_menu:
        st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์ (โจทย์ฝึกหัด)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดและเฉลยประจำบทที่ 6</div>', unsafe_allow_html=True)
        st.markdown("1. จงใช้การอุปนัยพิสูจน์ว่า $2 + 4 + 6 + \dots + 2n = n(n+1)$")
        st.markdown("2. จงหาผลบวกของ $1^3 + 2^3 + \dots + 10^3$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 6"):
            st.markdown("1. พิสูจน์สำเร็จตามหลักอุปนัยเชิงคณิตศาสตร์<br>2. คำตอบคือ 3,025", unsafe_allow_html=True)

# ---------------------------------------------------------
# เมนูสรุปสูตรทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 เมนูสรุปสูตรทั้งหมด (รวมทุกบท)":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎสำคัญทางตรรกศาสตร์ทั้งหมด (ทุกบท)</div>', unsafe_allow_html=True)
    
    st.markdown(r"""
    <div class="card-box">
        <h3>📋 หมวดหมู่ที่ 1: กฎการอ้างเหตุผลเบื้องต้น (บทที่ 1)</h3>
        <ul>
            <li><b>Modus Ponens:</b> $$p, p \rightarrow q \vdash q$$</li>
            <li><b>Modus Tollens:</b> $$p \rightarrow q, \neg q \vdash \neg p$$</li>
        </ul>

        <h3>📋 หมวดหมู่ที่ 2: กฎสมมูลและตัวเชื่อมตรรกศาสตร์ (บทที่ 2)</h3>
        <ul>
            <li><b>สมมูลของการimplie:</b> $$A \rightarrow B \equiv \neg A \vee B$$</li>
            <li><b>กฎเดอมอร์แกน:</b> $$\neg(A \wedge B) \equiv \neg A \vee \neg B$$ และ $$\neg(A \vee B) \equiv \neg A \wedge \neg B$$</li>
        </ul>

        <h3>📋 หมวดหมู่ที่ 3: กฎสัจนิรันดร์และข้อขัดแย้ง (บทที่ 3)</h3>
        <ul>
            <li><b>Law of Excluded Middle:</b> $$p \vee \neg p \equiv T$$</li>
            <li><b>Deduction Theorem:</b> $$A_1, ..., A_n \models C \iff (A_1 \wedge ... \wedge A_n) \rightarrow C \text{ เป็นสัจนิรันดร์}$$</li>
        </ul>

        <h3>📋 หมวดหมู่ที่ 4: กฎการอ้างเหตุผลขั้นสูง (บทที่ 4)</h3>
        <ul>
            <li><b>Hypothetical Syllogism:</b> $$A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$$</li>
            <li><b>Constructive Dilemma:</b> $$(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$$</li>
        </ul>

        <h3>📋 หมวดหมู่ที่ 5: กฎตัวบ่งปริมาณ (บทที่ 5)</h3>
        <ul>
            <li><b>นิเสธ Universal:</b> $$\neg \forall x P(x) \equiv \exists x \neg P(x)$$</li>
            <li><b>นิเสธ Existential:</b> $$\neg \exists x P(x) \equiv \forall x \neg P(x)$$</li>
        </ul>

        <h3>📋 หมวดหมู่ที่ 6: สูตรการอุปนัยเชิงคณิตศาสตร์ (บทที่ 6)</h3>
        <ul>
            <li><b>ผลบวกเลขคี่:</b> $$1 + 3 + \dots + (2n-1) = n^2$$</li>
            <li><b>ผลบวกกำลังสาม:</b> $$1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2$$</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# แบบทดสอบท้าทาย 10 ข้อ
# ---------------------------------------------------------
elif main_menu == "📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ (ระดับยากพิเศษ)</div>', unsafe_allow_html=True)
    st.markdown("คำชี้แจง: โปรดตอบคำถามทั้ง 10 ข้อด้านล่างนี้ ระบบจะนับคะแนนและอนุญาตให้เปิดดูเฉลยได้เมื่อคุณส่งคำตอบครบแล้วเท่านั้น")

    with st.form("quiz_form"):
        q1 = st.radio("1. ประพจน์ใดต่อไปนี้สมมูลกับ $p \rightarrow q$?", ["$\neg p \wedge q$", "$\neg p \vee q$", "$p \wedge \neg q$", "$p \leftrightarrow q$"], index=None)
        q2 = st.radio("2. นิเสธของประพจน์ $\forall x \exists y (x + y > 0)$ คือข้อใด?", ["$\exists x \forall y (x + y \le 0)$", "$\forall x \forall y (x + y \le 0)$", "$\exists x \exists y (x + y \le 0)$", "$\forall x \exists y (x + y \le 0)$"], index=None)
        q3 = st.radio("3. กฎการอ้างเหตุผล $p \rightarrow q, \neg q \vdash \neg p$ มีชื่อเรียกว่าอะไร?", ["Modus Ponens", "Modus Tollens", "Hypothetical Syllogism", "Constructive Dilemma"], index=None)
        q4 = st.radio("4. ประพจน์ $[(p \rightarrow q) \wedge p] \rightarrow q$ มีลักษณะทางตรรกศาสตร์อย่างไร?", ["เป็นสัจนิรันดร์", "เป็นข้อขัดแย้ง", "เป็นประพจน์กึ่งจริงกึ่งเท็จ", "สรุปไม่ได้"], index=None)
        q5 = st.radio("5. ผลบวกของอนุกรมกำลังสาม $1^3 + 2^3 + 3^3 + 4^3 + 5^3$ มีค่าเท่ากับเท่าใด?", ["225", "625", "100", "1,225"], index=None)
        q6 = st.radio("6. เหตุ: $p \rightarrow q, q \rightarrow r, \neg r$ ผลสรุปคือข้อใดจึงจะสมเหตุสมผล?", ["$p$", "$\neg p$", "$q$", "$\neg q$"], index=None)
        q7 = st.radio("7. ประพจน์ใดต่อไปนี้เป็นข้อขัดแย้ง (Contradiction)?", ["$p \vee \neg p$", "$p \rightarrow p$", "$p \wedge \neg p$", "$p \leftrightarrow p$"], index=None)
        q8 = st.radio("8. ข้อความใดกล่าวถูกต้องเกี่ยวกับการอุปนัยเชิงคณิตศาสตร์?", ["พิสูจน์เฉพาะกรณีเฉพาะ", "ต้องพิสูจน์ขั้น Base case และ Inductive step", "ใช้ตรวจสอบเฉพาะประพจน์เท็จ", "ไม่ต้องมีสมมติฐาน"], index=None)
        q9 = st.radio("9. นิเสธของ $\neg p \vee \neg q$ สมมูลกับประพจน์ใด?", ["$p \vee q$", "$p \wedge q$", "$\neg p \wedge \neg q$", "$\neg(p \vee q)$"], index=None)
        q10 = st.radio("10. เหตุใดลำดับของตัวบ่งปริมาณ $\forall x \exists y (x < y)$ จึงไม่สมมูลกับ $\exists y \forall x (x < y)$ บนจำนวนเต็ม?", ["เพราะขอบเขตตัวแปรต่างกัน", "ความหมายและการสลับตัวบ่งปริมาณทำให้ค่าความจริงเปลี่ยน", "ไม่มีผลต่างกัน", "นิเสธไม่เท่ากัน"], index=None)

        submitted = st.form_submit_button("📥 ส่งคำตอบทั้งหมด")

    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    answered_count = sum(1 for ans in answers if ans is not None)

    st.markdown(f"### 📊 สถานะการทำข้อสอบ: **{answered_count} / 10 ข้อ**")
    st.progress(answered_count / 10)

    if submitted:
        if answered_count < 10:
            st.warning("⚠️ กรุณาตอบคำถามให้ครบทั้ง 10 ข้อก่อนจึงจะสามารถส่งคำตอบและดูเฉลยได้!")
        else:
            correct_answers = [
                "$\neg p \vee q$",
                "$\exists x \forall y (x + y \le 0)$",
                "Modus Tollens",
                "เป็นสัจนิรันดร์",
                "225",
                "$\neg p$",
                "$p \wedge \neg p$",
                "ต้องพิสูจน์ขั้น Base case และ Inductive step",
                "$p \wedge q$",
                "ความหมายและการสลับตัวบ่งปริมาณทำให้ค่าความจริงเปลี่ยน"
            ]
            explanations = [
                "สมมูลของ $p \rightarrow q$ คือการแปลงเป็นดิสจังชันจะได้ $\neg p \vee q$",
                "นิเสธของ $\forall x \exists y$ จะเปลี่ยนเป็น $\exists x \forall y$ และเปลี่ยนเครื่องหมาย $>$ เป็น $\le$",
                "กฎ Modus Tollens คือ $p \rightarrow q, \neg q \vdash \neg p$",
                "ประพจน์นี้เป็นสัจนิรันดร์เพราะพิสูจน์แล้วเป็นจริงทุกกรณี (Modus Ponens)",
                "คำนวณจากสูตร $[\frac{5(6)}{2}]^2 = 15^2 = 225$",
                "ใช้กฎ Hypothetical Syllogism และ Modus Tollens ร่วมกันจะได้ $\neg p$",
                "ประพจน์ $p \wedge \neg p$ เป็นเท็จทุกกรณีจึงเป็นข้อขัดแย้ง",
                "การอุปนัยเชิงคณิตศาสตร์ต้องพิสูจน์ทั้ง Base case และ Inductive step",
                "ตามกฎเดอมอร์แกน $\neg(\neg p \vee \neg q) \equiv p \wedge q$",
                "การสลับลำดับตัวบ่งปริมาณในโดเมนจำนวนเต็มจะทำให้ขอบเขตการเลือกค่าเปลี่ยนและค่าความจริงเปลี่ยน"
            ]

            score = sum(1 for user_ans, correct in zip(answers, correct_answers) if user_ans == correct)
            st.success(f"🎉 ส่งคำตอบสำเร็จ! คะแนนที่คุณทำได้คือ: **{score} / 10 คะแนน**")
            
            st.markdown("---")
            st.markdown("## 🔑 เฉลยละเอียดพร้อมเหตุผลประกอบแต่ละข้อ")
            for i, (correct, exp) in enumerate(zip(correct_answers, explanations), 1):
                with st.expander(f"ดูเฉลยข้อที่ {i}"):
                    st.markdown(f"* **คำตอบที่ถูกต้อง:** `{correct}`")
                    st.markdown(f"* **คำอธิบาย / เหตุผล:** {exp}")

# ---------------------------------------------------------
# เครื่องมือคำนวณอัจฉริยะ
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
