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
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 18px;
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
# Sidebar Navigation with Submenus
# ---------------------------------------------------------
st.sidebar.markdown("### 🧭 เมนูบทเรียนตรรกศาสตร์")
main_menu = st.sidebar.selectbox(
    "เลือกหัวข้อหลักและเมนูย่อย:",
    [
        "📘 บทที่ 1: ประพจน์และการให้เหตุผล (เนื้อหาและแนวคิดหลัก)",
        "📘 บทที่ 1: ประพจน์และการให้เหตุผล (สูตรและตัวอย่างขั้นสูง)",
        "📘 บทที่ 1: ประพจน์และการให้เหตุผล (โจทย์ฝึกหัดและเฉลย)",
        
        "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (เนื้อหาและแนวคิดหลัก)",
        "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (สูตรและตัวอย่างขั้นสูง)",
        "📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง (โจทย์ฝึกหัดและเฉลย)",
        
        "📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (เนื้อหาและแนวคิดหลัก)",
        "📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (สูตรและตัวอย่างขั้นสูง)",
        "📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง (โจทย์ฝึกหัดและเฉลย)",
        
        "📕 บทที่ 4: การอ้างเหตุผล (เนื้อหาและแนวคิดหลัก)",
        "📕 บทที่ 4: การอ้างเหตุผล (สูตรและตัวอย่างขั้นสูง)",
        "📕 บทที่ 4: การอ้างเหตุผล (โจทย์ฝึกหัดและเฉลย)",
        
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (เนื้อหาและแนวคิดหลัก)",
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (สูตรและตัวอย่างขั้นสูง)",
        "🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (โจทย์ฝึกหัดและเฉลย)",
        
        "📓 บทที่ 6: การอุปนัยและนิรนัย (เนื้อหาและแนวคิดหลัก)",
        "📓 บทที่ 6: การอุปนัยและนิรนัย (สูตรและตัวอย่างขั้นสูง)",
        "📓 บทที่ 6: การอุปนัยและนิรนัย (โจทย์ฝึกหัดและเฉลย)",
        
        "📐 สรุปสูตรทั้งหมด",
        "📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ",
        "⚡ เครื่องมือคำนวณอัจฉริยะ"
    ]
)

# Progress Bar status
st.sidebar.markdown("---")
st.sidebar.markdown("📊 **สถานะการใช้งานระบบ**")
st.sidebar.progress(100)
st.sidebar.caption("โหลดเนื้อหาครบถ้วนพร้อมใช้งานแล้ว")

if st.sidebar.button("⬆️ กลับไปด้านบนสุด"):
    st.rerun()

# ---------------------------------------------------------
# บทที่ 1
# ---------------------------------------------------------
if "บทที่ 1: ประพจน์และการให้เหตุผล" in main_menu:
    st.markdown('<div class="main-header">📘 บทที่ 1: ประพจน์และการให้เหตุผล</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p>ตรรกศาสตร์เชิงคณิตศาสตร์ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล <b>ประพจน์ (Proposition)</b> คือประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริงเป็นจริง ($\text{True}$) หรือเท็จ ($\text{False}$) อย่างใดอย่างหนึ่งเท่านั้น[cite: 8]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$p, p \rightarrow q \vdash q \quad (\text{Modus Ponens})$$[cite: 8]")
        st.markdown("$$p \rightarrow q, \neg q \vdash \neg p \quad (\text{Modus Tollens})$$[cite: 9]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 1.1: การวิเคราะห์ประพจน์ซับซ้อน"):
            st.markdown("จงพิจารณาว่าประโยค 'ถ้า $x^2 < 0$ แล้ว $x$ เป็นจำนวนจริง' มีค่าความจริงเป็นอย่างไร?")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> เหตุ ($x^2 < 0$) เป็นเท็จเสมอในจำนวนจริง และผลสรุป ($x$ เป็นจำนวนจริง) เป็นจริง ตามนิยามประพจน์เงื่อนไข $F \rightarrow T$ จะได้ค่าความจริงเป็น <b>จริง ($\text{True}$)</b></div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 1.2: การใช้กฎ Modus Ponens ขั้นสูง"):
            st.markdown("กำหนดเหตุ: $(p \wedge q) \rightarrow r$ และ $(p \wedge q)$ จงหาค่าความจริงของ $r$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> กำหนดให้สัญลักษณ์ใหม่ $A = (p \wedge q)$ จะได้รูปสมการเป็น $A \rightarrow r$ และ $A$ สรุปผลได้ว่า $r \equiv \text{True}$</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 1.3: การพิสูจน์ทางอ้อม"):
            st.markdown("กำหนดเหตุ $p \rightarrow (q \rightarrow r)$ และสมมติให้ $\neg r \wedge q$ เป็นจริง จงหาค่าความจริงของ $p$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> จาก $\neg r \wedge q \equiv T$ จะได้ $q \equiv T$ และ $r \equiv F$ นำไปแทนค่าในเงื่อนไขจะได้ข้อสรุปว่า $p$ ต้องเป็นเท็จ ($\text{False}$)</div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. ประโยค 'สำหรับทุกจำนวนจริง $x$ ถ้า $x > 2$ แล้ว $x^2 > 4$' เป็นประพจน์หรือไม่?")
        st.markdown("2. กำหนดเหตุ: $p \rightarrow (q \rightarrow r)$, $p$, และ $q$ จงหาข้อสรุปที่สมเหตุสมผล")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 1"):
            st.markdown("1. เป็นประพจน์ เพราะมีค่าความจริงเป็นจริงแน่นอนบนโดเมนจำนวนจริง<br>2. ข้อสรุปคือ $r$ โดยใช้กฎ Modus Ponens ซ้อนกันสองครั้ง", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 2
# ---------------------------------------------------------
elif "บทที่ 2: ตัวเชื่อมและตารางค่าความจริง" in main_menu:
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #059669, #047857);">📗 บทที่ 2: ตัวเชื่อมและตารางค่าความจริง</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p>ตัวเชื่อมหลักประกอบด้วย นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การimplie ($\rightarrow$), และสมมูล ($\leftrightarrow$) ตารางค่าความจริงสำหรับประพจน์ $n$ ตัวแปรจะมีจำนวนแถวทั้งหมดเท่ากับ $2^n$ แถว[cite: 10]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$A \rightarrow B \equiv \neg A \vee B$$[cite: 10]")
        st.markdown("$$\neg(A \wedge B) \equiv \neg A \vee \neg B \quad (\text{De Morgan})$$[cite: 10]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 2.1: การสร้างตารางค่าความจริง 3 ตัวแปร"):
            st.markdown("จงสร้างตารางค่าความจริงของประพจน์ $(p \wedge q) \rightarrow r$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> มี 3 ตัวแปร ($p, q, r$) มีทั้งหมด $2^3 = 8$ แถว ประพจน์นี้จะเป็นเท็จเฉพาะกรณีที่ $p \wedge q \equiv T$ และ $r \equiv F$ เท่านั้น</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 2.2: การจัดรูปประพจน์ซับซ้อน"):
            st.markdown("จงลดรูปประพจน์ $\neg(p \rightarrow \neg q)$ ให้เหลือตัวเชื่อมพื้นฐาน")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> เปลี่ยน $\rightarrow$ เป็น $\vee$ จะได้ $\neg(\neg p \vee \neg q)$ จากนั้นใช้กฎเดอมอร์แกนจะได้ $p \wedge q$</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 2.3: การตรวจสอบสมมูลเชิงตรรกะ"):
            st.markdown("จงพิสูจน์ว่า $p \leftrightarrow q$ สมมูลกับ $(p \rightarrow q) \wedge (q \rightarrow p)$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> จากตารางค่าความจริงจะพบว่าคอลัมน์สุดท้ายของทั้งสองประพจน์มีค่าความจริงตรงกันในทุกกรณี จึงสมมูลกัน</div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. จงหาประพจน์ที่สมมูลกับ $\neg(p \leftrightarrow q)$ โดยใช้เฉพาะตัวเชื่อม $\neg, \wedge, \vee$")
        st.markdown("2. สร้างตารางค่าความจริงของประพจน์ $[p \wedge (q \vee r)] \leftrightarrow [(p \wedge q) \vee (p \wedge r)]$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 2"):
            st.markdown("1. $(p \wedge \neg q) \vee (\neg p \wedge q)<br>2. เป็นสัจนิรันดร์ (กฎการแจกแจง Distributive Law)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 3
# ---------------------------------------------------------
elif "บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง" in main_menu:
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #D97706, #B45309);">📙 บทที่ 3: สัจนิรันดร์และข้อขัดแย้ง</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p><b>สัจนิรันดร์ (Tautology)</b> คือประพจน์ที่มีค่าความจริงเป็นจริงทุกกรณี ส่วน<b>ข้อขัดแย้ง (Contradiction)</b> เป็นเท็จทุกกรณี[cite: 14]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$p \vee \neg p \equiv T \quad (\text{Law of Excluded Middle})$$")
        st.markdown("$$A_1, ..., A_n \models C \iff (A_1 \wedge ... \wedge A_n) \rightarrow C \text{ เป็นสัจนิรันดร์}$$[cite: 14]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 3.1: การพิสูจน์สัจนิรันดร์โดยวิธีหาข้อขัดแย้ง"):
            st.markdown("จงตรวจสอบว่าประพจน์ $[(p \rightarrow q) \wedge p] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> สมมติให้ประพจน์เป็นเท็จ จะได้หน้าจริง หลังเท็จ ($[(p \rightarrow q) \wedge p] \equiv T$ และ $q \equiv F$) จากหน้าจริงจะได้ $p \equiv T$ และ $p \rightarrow q \equiv T \rightarrow F \equiv F$ ขัดแย้งกับข้อสมมติ ดังนั้น <b>เป็นสัจนิรันดร์</b></div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 3.2: การตรวจสอบประพจน์เงื่อนไขซับซ้อน"):
            st.markdown("จงตรวจสอบว่า $[(p \rightarrow q) \wedge (q \rightarrow r)] \rightarrow (p \rightarrow r)$ เป็นสัจนิรันดร์หรือไม่")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> สมมติให้เป็นเท็จ จะได้เหตุเป็นจริงและผลสรุปเป็นเท็จ ($p \rightarrow r \equiv F \implies p \equiv T, r \equiv F$) นำไปแทนในเหตุจะเกิดข้อขัดแย้ง ดังนั้นเป็นสัจนิรันดร์ (กฎ Hypothetical Syllogism)</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 3.3: การวิเคราะห์ข้อขัดแย้ง"):
            st.markdown("จงตรวจสอบว่า $(p \wedge q) \wedge \neg(p \vee q)$ เป็นข้อขัดแย้งหรือไม่")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> แปลง $\neg(p \vee q)$ เป็น $\neg p \wedge \neg q$ จะได้ $(p \wedge \neg p) \wedge (q \wedge \neg q) \equiv F \wedge F \equiv F$ ทุกกรณี จึงเป็นข้อขัดแย้ง</div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. จงตรวจสอบว่า $[p \wedge (p \rightarrow q)] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
        st.markdown("2. ตรวจสอบว่า $[(p \vee q) \wedge \neg p] \rightarrow q$ เป็นสัจนิรันดร์หรือไม่")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 3"):
            st.markdown("1. เป็นสัจนิรันดร์ (Modus Ponens)<br>2. เป็นสัจนิรันดร์ (Disjunctive Syllogism)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 4
# ---------------------------------------------------------
elif "บทที่ 4: การอ้างเหตุผล" in main_menu:
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #DC2626, #B91C1C);">📕 บทที่ 4: การอ้างเหตุผลและความสมเหตุสมผล</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p>การอ้างเหตุผลจะ<b>สมเหตุสมผล ($\text{Valid}$)</b> เมื่อกรณีที่เหตุทุกข้อเป็นจริง ผลสรุปต้องเป็นจริงด้วย[cite: 20]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$A \rightarrow B, B \rightarrow C \vdash A \rightarrow C \quad (\text{Hypothetical Syllogism})$$[cite: 20]")
        st.markdown("$$(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r \quad (\text{Constructive Dilemma})$$[cite: 16]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 4.1: การตรวจสอบการอ้างเหตุผล 3 บรรทัด"):
            st.markdown("เหตุ: 1) $p \rightarrow q$, 2) $q \rightarrow r$, 3) $\neg r$ | ผลสรุป: $\neg p$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> จาก 1 และ 2 ได้ $p \rightarrow r$ (H.S.) จากนั้นใช้ร่วมกับ 3 ($\neg r$) ได้ข้อสรุป $\neg p$ (Modus Tollens) <b>สมเหตุสมผล</b></div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 4.2: การอ้างเหตุผลด้วยกฎ Constructive Dilemma"):
            st.markdown("เหตุ: 1) $p \rightarrow q$, 2) $r \rightarrow s$, 3) $p \vee r$ | ผลสรุป: $q \vee s$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> เป็นรูปแบบมาตรฐานของกฎ Constructive Dilemma ดังนั้นจึง <b>สมเหตุสมผล</b></div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 4.3: การตรวจสอบความสมเหตุสมผลขั้นสูง"):
            st.markdown("เหตุ: 1) $p \vee q$, 2) $p \rightarrow r$, 3) $q \rightarrow s$ | ผลสรุป: $r \vee s$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> สมมติให้ข้อสรุปเป็นเท็จ ($r \vee s \equiv F \implies r \equiv F, s \equiv F$) แทนค่าในเหตุจะบังคับให้ $p$ และ $q$ เป็นเท็จ ขัดแย้งกับเหตุที่ 1 ($p \vee q \equiv T$) ดังนั้น <b>สมเหตุสมผล</b></div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. เหตุ: $p \rightarrow (q \rightarrow r)$, $p$, $q$ | ผลสรุป: $r$ สมเหตุสมผลหรือไม่?")
        st.markdown("2. เหตุ: $p \vee q$, $p \rightarrow \neg r$, $q \rightarrow \neg s$ | ผลสรุป: $\neg r \vee \neg s$ สมเหตุสมผลหรือไม่?")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 4"):
            st.markdown("1. สมเหตุสมผล (Modus Ponens ซ้อน)<br>2. สมเหตุสมผล (Constructive Dilemma)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 5
# ---------------------------------------------------------
elif "บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ" in main_menu:
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #7C3AED, #6D28D9);">🟣 บทที่ 5: ประโยคเปิดและตัวบ่งปริมาณ (Quantifiers)</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p>ประโยคเปิด $P(x)$ จะมีตัวแปรเสรี ตัวบ่งปริมาณประกอบด้วยสำหรับทุกตัว ($\forall x$) และสำหรับบางตัว ($\exists x$)[cite: 24]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$\neg \forall x P(x) \equiv \exists x \neg P(x)$$[cite: 24]")
        st.markdown("$$\neg \exists x P(x) \equiv \forall x \neg P(x)$$[cite: 24]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 5.1: นิเสธของตัวบ่งปริมาณซ้อน"):
            st.markdown("จงหานิเสธของประพจน์ $\forall x \exists y (x^2 + y^2 > 10)$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> กระจายเครื่องหมายนิเสธผ่านตัวบ่งปริมาณจะได้ $\exists x \forall y \neg(x^2 + y^2 > 10) \equiv \exists x \forall y (x^2 + y^2 \le 10)$</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 5.2: การวิเคราะห์ค่าความจริงตัวบ่งปริมาณซ้อน"):
            st.markdown("บนเอกภพสัมพัทธ์จำนวนจริง ค่าความจริงของ $\forall x \exists y (x + y = 0)$ คืออะไร?")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> เป็นจริง เพราะสำหรับทุกจำนวนจริง $x$ จะมี $y = -x$ ซึ่งเป็นจำนวนจริงเช่นกันทำให้สมการเป็นจริง</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 5.3: นิเสธของประพจน์เงื่อนไขที่มีตัวบ่งปริมาณ"):
            st.markdown("จงหานิเสธของ $\forall x [P(x) \rightarrow Q(x)]$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> $\neg \forall x [P(x) \rightarrow Q(x)] \equiv \exists x \neg[\neg P(x) \vee Q(x)] \equiv \exists x [P(x) \wedge \neg Q(x)]$</div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. จงหานิเสธของประพจน์ $\exists x \forall y [P(x) \leftrightarrow Q(y)]$")
        st.markdown("2. กำหนดเอกภพสัมพัทธ์เป็นเซตของจำนวนเต็ม จงหาค่าความจริงของ $\exists x \forall y (x \cdot y = y)$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 5"):
            st.markdown("1. $\forall x \exists y [(P(x) \wedge \neg Q(y)) \vee (\neg P(x) \wedge Q(y))]<br>2. เป็นจริง (เมื่อเลือก $x = 1$)", unsafe_allow_html=True)

# ---------------------------------------------------------
# บทที่ 6
# ---------------------------------------------------------
elif "บทที่ 6: การอุปนัยและนิรนัย" in main_menu:
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #0EA5E9, #0284C7);">📓 บทที่ 6: การอุปนัยและนิรนัยเชิงคณิตศาสตร์</div>', unsafe_allow_html=True)
    
    if "เนื้อหาและแนวคิดหลัก" in main_menu:
        st.markdown("""
        <div class="card-box">
            <h3>📖 เนื้อหาและแนวคิดหลัก</h3>
            <p>การอุปนัยเชิงคณิตศาสตร์ประกอบด้วย ขั้นฐาน ($\text{Base case}$ สำหรับ $n=1$) และขั้นอุปนัย ($\text{Inductive step}$)[cite: 27]</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif "สูตรและตัวอย่างขั้นสูง" in main_menu:
        st.markdown('<div class="sub-header">📐 สรุปสูตรและสมการสำคัญ</div>', unsafe_allow_html=True)
        st.markdown("$$1 + 3 + \dots + (2n-1) = n^2$$[cite: 27]")
        st.markdown("$$1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2$$[cite: 31]")
        
        st.markdown('<div class="sub-header">💡 ตัวอย่างระดับสูงพร้อมวิธีทำ</div>', unsafe_allow_html=True)
        with st.expander("ตัวอย่าง 6.1: การพิสูจน์ผลบวกเลขคี่"):
            st.markdown("จงแสดงว่าสูตร $1 + 3 + \dots + (2n-1) = n^2$ เป็นจริงเมื่อ $n=3$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> ฝั่งซ้าย $1 + 3 + 5 = 9$, ฝั่งขวา $3^2 = 9$ (เท่ากันและเป็นจริง)</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 6.2: การประยุกต์สูตรกำลังสาม"):
            st.markdown("จงหาผลotของอนุกรม $1^3 + 2^3 + 3^3 + 4^3$")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> ใช้สูตร $[\frac{4(5)}{2}]^2 = [10]^2 = 100$</div>', unsafe_allow_html=True)
            
        with st.expander("ตัวอย่าง 6.3: หลักการพิสูจน์ขั้นอุปนัย"):
            st.markdown("ในการพิสูจน์ด้วยอุปนัยเชิงคณิตศาสตร์ หากผ่านขั้นตอน Base case แล้ว ขั้นตอนถัดไปต้องสมมติสิ่งใด?")
            st.markdown('<div class="solution-box"><b>วิธีทำ:</b> สมมติให้ประพจน์เป็นจริงสำหรับ $n = k$ แล้วพิสูจน์ว่าจริงสำหรับ $n = k + 1$</div>', unsafe_allow_html=True)

    elif "โจทย์ฝึกหัดและเฉลย" in main_menu:
        st.markdown('<div class="sub-header">📝 โจทย์ฝึกหัดระดับสูง (2 ข้อ)</div>', unsafe_allow_html=True)
        st.markdown("1. จงใช้การอุปนัยพิสูจน์ว่า $2 + 4 + 6 + \dots + 2n = n(n+1)$")
        st.markdown("2. จงหาผลบวกของ $1^3 + 2^3 + \dots + 10^3$")
        
        with st.expander("👉 คลิกเพื่อดูเฉลยโจทย์ฝึกหัดบทที่ 6"):
            st.markdown("1. พิสูจน์สำเร็จตามหลักอุปนัยเชิงคณิตศาสตร์<br>2. คำตอบคือ 3,025", unsafe_allow_html=True)

# ---------------------------------------------------------
# สรุปสูตรทั้งหมด
# ---------------------------------------------------------
elif main_menu == "📐 สรุปสูตรทั้งหมด":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #9333EA, #C084FC);">📐 สรุปสูตรและกฎทางตรรกศาสตร์ทั้งหมด</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>📋 รวมสมการและกฎสำคัญทุกบท</h3>
        <ul>
            <li><b>บทที่ 1:</b> 
                $$p, p \rightarrow q \vdash q \quad (\text{Modus Ponens})$$
                $$p \rightarrow q, \neg q \vdash \neg p \quad (\text{Modus Tollens})$$
            </li>
            <li><b>บทที่ 2:</b> 
                $$A \rightarrow B \equiv \neg A \vee B$$
                $$\neg(A \wedge B) \equiv \neg A \vee \neg B$$
                $$\neg(A \vee B) \equiv \neg A \wedge \neg B$$
            </li>
            <li><b>บทที่ 3:</b> 
                $$p \vee \neg p \equiv T \quad (\text{Excluded Middle})$$
            </li>
            <li><b>บทที่ 4:</b> 
                $$A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$$
                $$(p \rightarrow r) \wedge (q \rightarrow r) \wedge (p \vee q) \vdash r$$
            </li>
            <li><b>บทที่ 5:</b> 
                $$\neg \forall x P(x) \equiv \exists x \neg P(x)$$
                $$\neg \exists x P(x) \equiv \forall x \neg P(x)$$
            </li>
            <li><b>บทที่ 6:</b> 
                $$1 + 3 + \dots + (2n-1) = n^2$$
                $$1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2$$
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# แบบทดสอบท้าทาย 10 ข้อ
# ---------------------------------------------------------
elif main_menu == "📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ":
    st.markdown('<div class="main-header" style="background: linear-gradient(90deg, #4F46E5, #3B82F6);">📝 แบบทดสอบท้าทายขั้นสูง 10 ข้อ (ระดับยากพิเศษ)</div>', unsafe_allow_html=True)
    st.markdown("คำชี้แจง: โปรดตอบคำถามทั้ง 10 ข้อด้านล่างนี้ ระบบจะนับคะแนนและแสดงปุ่มเปิดเฉลยเมื่อคุณส่งคำตอบครบแล้ว")

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
            st.warning("⚠️ กรุณาตอบให้ครบทั้ง 10 ข้อก่อนกดส่งคำตอบ!")
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
            score = sum(1 for user_ans, correct in zip(answers, correct_answers) if user_ans == correct)
            st.success(f"🎉 ส่งคำตอบสำเร็จ! คะแนนที่คุณทำได้คือ: **{score} / 10 คะแนน**")
            
            st.markdown("---")
            st.markdown("## 🔑 เฉลยละเอียดพร้อมเหตุผลประกอบ")
            for i, correct in enumerate(correct_answers, 1):
                st.markdown(f"**ข้อ {i} เฉลย:** `{correct}`")

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
