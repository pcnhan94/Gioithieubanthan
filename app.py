from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Giới thiệu bản thân | Phan Công Nhân",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
AVATAR = ROOT / "assets" / "avatar.png"
CV_FILE = ROOT / "assets" / "cv_phan_cong_nhan.pdf"

PROFILE = {
    "name": "Phan Công Nhân",
    "role": "Giám đốc chi nhánh · Giáo viên tiếng Anh",
    "tagline": "Trách nhiệm, trung thực, có năng lực và thích ứng nhanh.",
    "birthday": "17/12/1994",
    "location": "P. Bình Thạnh, TP. Hồ Chí Minh",
    "email": "pcnhan17@gmail.com",
    "phone": "0977257877",
    "about": (
        "Xin chào, mình là Phan Công Nhân. Mình làm việc trong lĩnh vực Giáo dục và Đào tạo, "
        "từng đảm nhiệm vị trí Giám đốc chi nhánh tại Trung tâm Ngoại ngữ (SME) và giáo viên tiếng Anh. "
        "Mình đề cao trách nhiệm, sự trung thực, năng lực chuyên môn và khả năng thích ứng nhanh."
    ),
    "highlights": [
        "IELTS 7.5; giảng dạy và quản lý lớp học.",
        "Kinh nghiệm quản lý chi nhánh, nhân sự và hành chính.",
        "Am hiểu bảo hiểm, kế toán, thuế; thành thạo tin học văn phòng và sử dụng AI.",
        "Mục tiêu: Giám đốc Phòng Hành chính — Nhân sự.",
    ],
    "job_expect": {
        "industry": "Giáo dục / Đào tạo",
        "level": "Giám sát / Phó phòng / Trợ lý Ban Giám đốc",
        "salary": "Thỏa thuận",
        "place": "TP. Hồ Chí Minh",
        "type": "Toàn thời gian",
        "goal": "Giám đốc Phòng Hành chính, Nhân sự",
    },
    "skills": {
        "Chuyên môn": [
            "Tiếng Anh — IELTS 7.5",
            "Giảng dạy / quản lý lớp",
            "Quản lý và sắp xếp nhân sự",
            "Bảo hiểm — Kế toán — Thuế",
            "Tổ chức sự kiện / lễ hội cho học sinh",
        ],
        "Công cụ": [
            "Word, Excel, PowerPoint (thành thạo)",
            "Công cụ AI",
            "Python (cơ bản)",
        ],
        "Chứng nhận khác": [
            "Phòng cháy chữa cháy và Sơ cấp cứu",
            "Bằng lái xe B2",
        ],
    },
    "skill_levels": [
        ("Tiếng Anh (IELTS 7.5)", 90),
        ("Giảng dạy / quản lý lớp", 85),
        ("Tin học văn phòng", 85),
        ("Quản lý nhân sự", 80),
        ("Bảo hiểm — Kế toán — Thuế", 75),
        ("Công cụ AI", 70),
        ("Python cơ bản", 40),
    ],
    "experience": [
        {
            "title": "Giám đốc chi nhánh, Giáo viên tiếng Anh",
            "org": "Chi nhánh CTCP Anh Ngữ Quốc Tế Việt Mỹ",
            "period": "01/2018 — 10/2026",
            "detail": "Phụ trách vận hành chi nhánh, giảng dạy tiếng Anh và quản lý hoạt động đào tạo.",
        },
        {
            "title": "Quản lý nhân sự, Giáo viên tiếng Anh",
            "org": "Công ty Cổ phần Anh Ngữ Quốc Tế Việt Mỹ",
            "period": "03/2017 — 12/2017",
            "detail": "Quản lý nhân sự kết hợp giảng dạy tiếng Anh tại công ty.",
        },
        {
            "title": "Nhân viên hành chính",
            "org": "Công ty Cổ phần Công Nghệ Việt Á",
            "period": "10/2016 — 02/2017",
            "detail": "Hỗ trợ công tác hành chính văn phòng.",
        },
        {
            "title": "Lễ tân, gia sư, chủ cơ sở PS4",
            "org": "Tự do, hộ kinh doanh",
            "period": "01/2014 — 09/2016",
            "detail": "Làm lễ tân, gia sư và tự vận hành cơ sở kinh doanh.",
        },
    ],
    "education": [
        {
            "school": "Đại học Kinh tế TP.HCM",
            "degree": "Ngành Tài chính — loại tốt nghiệp Xuất sắc",
            "period": "01/2024 — 12/2026 (3 năm)",
        },
        {
            "school": "ĐH Khoa học Xã hội và Nhân văn TP.HCM",
            "degree": "Chứng chỉ Nghiệp vụ Sư phạm — loại hoàn thành Giỏi",
            "period": "02/2023 — 08/2023 (6 tháng)",
        },
        {
            "school": "Đại học Mở Hà Nội",
            "degree": "Ngành Ngôn ngữ Anh — loại tốt nghiệp Giỏi",
            "period": "01/2018 — 11/2020 (3 năm)",
        },
        {
            "school": "Viện Nghiên cứu Châu Á (IAS)",
            "degree": "Chứng nhận Kế toán — Khai báo thuế — loại hoàn thành Giỏi",
            "period": "11/2017 — 01/2018 (3 tháng)",
        },
        {
            "school": "Đại học Nông Lâm TP.HCM",
            "degree": "Ngành Nông nghiệp — loại tốt nghiệp Khá",
            "period": "09/2012 — 10/2016 (4 năm)",
        },
    ],
}


def inject_css() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');

            html, body, .stApp, [data-testid="stMarkdownContainer"] {
                font-family: 'Be Vietnam Pro', sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(1200px 500px at 10% -10%, #1b4d6b33 0%, transparent 50%),
                    radial-gradient(900px 400px at 100% 0%, #0ea5e933 0%, transparent 45%),
                    linear-gradient(180deg, #0b1220 0%, #111827 55%, #0f172a 100%);
                color: #e5eef7;
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
                border-right: 1px solid #1f2a44;
            }

            [data-testid="stHeader"] { background: transparent; }
            .stAppDeployButton, [data-testid="stToolbar"],
            [data-testid="stElementToolbar"],
            [data-testid="stImage"] button { display: none !important; }
            .block-container {
                padding-top: 2.2rem;
                padding-bottom: 2rem;
                max-width: 1100px;
            }
            [data-testid="stImage"] img {
                border-radius: 50%;
                border: 3px solid #2dd4bf66;
            }

            .hero {
                background: linear-gradient(135deg, #12324a 0%, #0f766e 55%, #0369a1 100%);
                border: 1px solid #2dd4bf44;
                border-radius: 24px;
                padding: 28px 28px;
                box-shadow: 0 20px 50px #00000040;
            }

            .hero h1 {
                margin: 0 0 8px 0;
                font-size: 2.2rem;
                letter-spacing: -0.03em;
            }

            .hero .role {
                color: #99f6e4;
                font-weight: 600;
                margin-bottom: 10px;
            }

            .hero p { margin: 0; opacity: 0.95; line-height: 1.6; }

            .chip {
                display: inline-block;
                background: #0ea5e91a;
                border: 1px solid #38bdf866;
                color: #7dd3fc;
                padding: 6px 12px;
                border-radius: 999px;
                margin: 0 8px 8px 0;
                font-size: 0.85rem;
            }

            .card {
                background: #0b1628cc;
                border: 1px solid #1e3a5f;
                border-radius: 18px;
                padding: 20px 18px;
                height: 100%;
                margin-bottom: 12px;
            }

            .card h3, .card h4 { margin-top: 0; }

            .muted { color: #94a3b8; }

            .section-title {
                font-size: 1.45rem;
                font-weight: 700;
                margin: 8px 0 4px 0;
            }

            .footer {
                text-align: center;
                color: #94a3b8;
                padding: 24px 0 8px 0;
            }

            .stButton button,
            .stDownloadButton button,
            .stFormSubmitButton button,
            [data-testid="stBaseButton-secondary"],
            [data-testid="stBaseButton-primary"],
            [data-testid="stBaseButton-secondaryFormSubmit"],
            [data-testid="stBaseButton-primaryFormSubmit"] {
                background: linear-gradient(135deg, #0f766e 0%, #0369a1 100%) !important;
                color: #ffffff !important;
                border: 0 !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                letter-spacing: 0.02em;
                box-shadow: 0 8px 18px #0ea5e944 !important;
            }

            .stButton button p,
            .stDownloadButton button p,
            .stFormSubmitButton button p,
            .stButton button span,
            .stDownloadButton button span,
            .stFormSubmitButton button span {
                color: #ffffff !important;
                font-weight: 700 !important;
            }

            .stDownloadButton button {
                background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%) !important;
            }

            .stFormSubmitButton button {
                background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%) !important;
            }

            .stButton button:hover,
            .stDownloadButton button:hover,
            .stFormSubmitButton button:hover {
                filter: brightness(1.12);
                color: #ffffff !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def skill_level(name: str, percent: int) -> None:
    st.markdown(f"**{name}**")
    st.progress(percent)


inject_css()

with st.sidebar:
    if AVATAR.exists():
        st.image(str(AVATAR), width=180)
    st.markdown(f"### {PROFILE['name']}")
    st.caption(PROFILE["role"])
    st.markdown("---")
    st.caption(f"🎂 {PROFILE['birthday']}")
    st.caption(f"📍 {PROFILE['location']}")
    st.caption(f"✉️ {PROFILE['email']}")
    st.caption(f"📞 {PROFILE['phone']}")
    if CV_FILE.exists():
        st.download_button(
            "Tải CV (PDF)",
            data=CV_FILE.read_bytes(),
            file_name="CV_Phan_Cong_Nhan.pdf",
            mime="application/pdf",
            type="primary",
        )

tab_home, tab_exp, tab_edu, tab_skills, tab_contact = st.tabs(
    ["Trang chủ", "Kinh nghiệm", "Học vấn", "Kỹ năng", "Liên hệ"]
)

with tab_home:
    hero_left, hero_right = st.columns([0.9, 2.4], gap="large")
    with hero_left:
        if AVATAR.exists():
            st.image(str(AVATAR), width=200)
    with hero_right:
        st.markdown(
            f"""
            <div class="hero">
                <div class="role">{PROFILE['role']}</div>
                <h1>{PROFILE['name']}</h1>
                <p>{PROFILE['tagline']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.markdown('<div class="section-title">Về mình</div>', unsafe_allow_html=True)
        st.write(PROFILE["about"])
        for item in PROFILE["highlights"]:
            st.markdown(f"- {item}")
    with right:
        st.markdown("#### Thông tin nhanh")
        st.write(f"**Họ tên:** {PROFILE['name']}")
        st.write(f"**Ngày sinh:** {PROFILE['birthday']}")
        st.write(f"**Vị trí:** {PROFILE['role']}")
        st.write(f"**Nơi ở:** {PROFILE['location']}")
        st.write(f"**Email:** {PROFILE['email']}")
        st.write(f"**Điện thoại:** {PROFILE['phone']}")

    st.write("")
    st.markdown('<div class="section-title">Kỳ vọng công việc</div>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    expect = PROFILE["job_expect"]
    e1.markdown(f"**Ngành nghề**  \n{expect['industry']}")
    e2.markdown(f"**Cấp bậc mong muốn**  \n{expect['level']}")
    e3.markdown(f"**Mức lương**  \n{expect['salary']}")
    e1.markdown(f"**Địa điểm**  \n{expect['place']}")
    e2.markdown(f"**Loại hình**  \n{expect['type']}")
    e3.markdown(f"**Mục tiêu**  \n{expect['goal']}")

with tab_exp:
    st.markdown('<div class="section-title">Kinh nghiệm làm việc</div>', unsafe_allow_html=True)
    st.caption("Quá trình công tác theo CV.")
    for exp in PROFILE["experience"]:
        st.markdown(
            f"""
            <div class="card">
                <h4>{exp['title']}</h4>
                <div class="muted">{exp['org']} · {exp['period']}</div>
                <p>{exp['detail']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab_edu:
    st.markdown('<div class="section-title">Học vấn và bằng cấp</div>', unsafe_allow_html=True)
    st.caption("Bằng cấp, chứng chỉ và khóa đào tạo.")
    for edu in PROFILE["education"]:
        st.markdown(
            f"""
            <div class="card">
                <h4>{edu['school']}</h4>
                <div class="muted">{edu['period']}</div>
                <p>{edu['degree']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab_skills:
    st.markdown('<div class="section-title">Kỹ năng</div>', unsafe_allow_html=True)
    st.caption("Kỹ năng chuyên môn, công cụ và chứng nhận.")
    cols = st.columns(3, gap="large")
    for col, (group, items) in zip(cols, PROFILE["skills"].items()):
        with col:
            st.markdown(f"#### {group}")
            for item in items:
                st.markdown(f'<span class="chip">{item}</span>', unsafe_allow_html=True)

    st.write("")
    st.markdown("#### Mức độ tự tin")
    c1, c2 = st.columns(2)
    levels = PROFILE["skill_levels"]
    mid = (len(levels) + 1) // 2
    with c1:
        for name, percent in levels[:mid]:
            skill_level(name, percent)
    with c2:
        for name, percent in levels[mid:]:
            skill_level(name, percent)

with tab_contact:
    st.markdown('<div class="section-title">Kết nối với mình</div>', unsafe_allow_html=True)
    st.write(
        "Mình sẵn sàng trao đổi về cơ hội trong giáo dục, đào tạo, hành chính và nhân sự tại TP. Hồ Chí Minh."
    )

    a, b, c = st.columns(3)
    a.markdown(f"**Email**  \n[{PROFILE['email']}](mailto:{PROFILE['email']})")
    b.markdown(f"**Điện thoại**  \n[{PROFILE['phone']}](tel:{PROFILE['phone']})")
    c.markdown(f"**Địa chỉ**  \n{PROFILE['location']}")
    if CV_FILE.exists():
        st.download_button(
            "Tải CV (PDF)",
            data=CV_FILE.read_bytes(),
            file_name="CV_Phan_Cong_Nhan.pdf",
            mime="application/pdf",
            key="cv_contact",
            type="primary",
        )

    st.write("")
    with st.form("contact_form"):
        st.markdown("#### Gửi lời nhắn")
        name = st.text_input("Tên của bạn")
        email = st.text_input("Email")
        message = st.text_area("Nội dung")
        submitted = st.form_submit_button("Gửi", type="primary")
        if submitted:
            if name and email and message:
                st.success(
                    f"Cảm ơn {name}! Mình đã nhận lời nhắn (demo — vui lòng liên hệ trực tiếp qua {PROFILE['email']})."
                )
            else:
                st.warning("Vui lòng điền đủ tên, email và nội dung.")

st.markdown(
    f'<div class="footer">© 2026 {PROFILE["name"]} · Được xây bằng Streamlit</div>',
    unsafe_allow_html=True,
)
