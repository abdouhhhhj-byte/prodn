import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from config import TARGET

def section_reports(df):
    st.markdown("### 📤 Export & Rapports")
    c1, c2, c3 = st.columns(3)
    with c1:
        csv = df.to_csv(index=True).encode("utf-8")
        st.download_button("⬇️ CSV", csv, "rapport.csv", "text/csv", use_container_width=True)
    with c2:
        df_export = df.copy()
        if isinstance(df_export.index, pd.DatetimeIndex) and df_export.index.tz is not None:
            df_export.index = df_export.index.tz_localize(None)
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df_export.to_excel(writer, sheet_name="Données")
        st.download_button("⬇️ Excel", output.getvalue(), "rapport.xlsx",
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                           use_container_width=True)
    with c3:
        # PDF (optionnel)
        st.info("Génération PDF disponible si ReportLab installé")