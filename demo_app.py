import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# Public Demo
# ---------------------------------------------------------
# This file intentionally contains only a demonstration
# version of the project.
#
# Production scraping engines, platform-specific parsers,
# selectors, API integrations, concurrency controls, and
# deployment logic are proprietary and are not included.
# ---------------------------------------------------------

st.set_page_config(
    page_title="Price Intelligence Platform",
    page_icon="🛍️",
    layout="wide",
)

# ---------------------------
# Demo dataset
# ---------------------------

DEMO_DATA = [
    {
        "Store": "Marketplace A",
        "Product": "Industrial Pump Model X",
        "Original Price": 12500000,
        "Final Price": 11900000,
        "Discount": "4.8%",
        "Vendor": "Supplier A",
    },
    {
        "Store": "Marketplace B",
        "Product": "Industrial Pump Model X Pro",
        "Original Price": 13200000,
        "Final Price": 12100000,
        "Discount": "8.3%",
        "Vendor": "Supplier B",
    },
    {
        "Store": "Marketplace C",
        "Product": "Industrial Pump Heavy Duty",
        "Original Price": 12950000,
        "Final Price": 12450000,
        "Discount": "3.9%",
        "Vendor": "Supplier C",
    },
    {
        "Store": "Marketplace D",
        "Product": "Industrial Pump 2HP",
        "Original Price": 14000000,
        "Final Price": 12800000,
        "Discount": "8.6%",
        "Vendor": "Supplier D",
    },
]

df = pd.DataFrame(DEMO_DATA)

# ---------------------------
# Styling
# ---------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 0px;
        }

        .subtitle {
            font-size: 18px;
            opacity: 0.75;
            margin-bottom: 30px;
        }

        .demo-note {
            padding: 14px 18px;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.25);
            margin-bottom: 25px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Header
# ---------------------------

st.markdown(
    '<div class="main-title">🛍️ Price Intelligence Platform</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Multi-source product search and price comparison demo'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="demo-note">
    <b>Public Demo:</b>
    This application demonstrates the user experience and
    data-normalization workflow of the platform.
    Production data-collection engines are intentionally excluded.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Search
# ---------------------------

col1, col2 = st.columns([4, 1])

with col1:
    keyword = st.text_input(
        "Search product",
        placeholder="Example: industrial pump",
    )

with col2:
    st.write("")
    st.write("")
    search_clicked = st.button(
        "🔎 Search",
        use_container_width=True,
        type="primary",
    )

# ---------------------------
# Search result demo
# ---------------------------

if search_clicked:

    if not keyword.strip():
        st.warning("Please enter a product name.")

    else:
        with st.spinner("Searching multiple marketplaces..."):
            pass

        st.success(
            f"Demo results for: {keyword}"
        )

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric(
                "Products Found",
                len(df),
            )

        with metric2:
            st.metric(
                "Marketplaces",
                df["Store"].nunique(),
            )

        with metric3:
            cheapest = df["Final Price"].min()
            st.metric(
                "Lowest Price",
                f"{cheapest:,.0f}",
            )

        st.subheader("📊 Comparison Results")

        display_df = df.copy()

        display_df["Original Price"] = (
            display_df["Original Price"]
            .map(lambda x: f"{x:,.0f}")
        )

        display_df["Final Price"] = (
            display_df["Final Price"]
            .map(lambda x: f"{x:,.0f}")
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

        # ---------------------------
        # Cheapest product
        # ---------------------------

        cheapest_row = df.loc[
            df["Final Price"].idxmin()
        ]

        st.subheader("💡 Price Insight")

        st.info(
            f"""
            Lowest demo price:

            **{cheapest_row['Product']}**

            Marketplace: **{cheapest_row['Store']}**

            Final Price: **{cheapest_row['Final Price']:,.0f}**
            """
        )

        # ---------------------------
        # Export
        # ---------------------------

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Download Demo Results",
            data=csv_data,
            file_name="demo_price_results.csv",
            mime="text/csv",
        )

else:

    st.subheader("How the production platform works")

    st.markdown(
        """
        The production system combines several data acquisition
        approaches depending on the target marketplace:

        - REST API integration
        - HTTP-based web scraping
        - HTML parsing
        - Browser automation
        - Data normalization
        - Price and discount processing
        - Multi-source result aggregation
        - Excel export

        The platform-specific implementation is not included
        in this public repository.
        """
    )

    st.subheader("Architecture")

    st.code(
        """
User Search
     |
     v
Streamlit Interface
     |
     v
Multi-Source Search Engine
     |
     +---- REST APIs
     |
     +---- Web Scraping
     |
     +---- Browser Automation
     |
     v
Data Normalization
     |
     v
Price Processing
     |
     v
Unified Results
     |
     v
Export / Analysis
        """,
        language="text",
    )

# ---------------------------
# Footer
# ---------------------------

st.divider()

st.caption(
    "Public portfolio demonstration — "
    "Production scraping and data-collection logic is proprietary."
)
