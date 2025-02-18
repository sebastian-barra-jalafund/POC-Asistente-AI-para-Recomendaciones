import streamlit as st
import requests

st.title("🏢 Asistente AI para Recomendaciones de Negocios")

preference = st.text_input("🔍 ¿Qué tipo de evento quieres organizar?", "")

if st.button("Buscar negocios"):
    if preference:
        response = requests.get("http://127.0.0.1:8000/recommendations/", params={"preference": preference})
        
        if response.status_code == 200:
            businesses = response.json()
            
            if isinstance(businesses, list) and businesses:
                st.subheader("🏢 Negocios recomendados:")
                for business in businesses:
                    st.write(f"📍 **{business['name']}** - Ubicación: {business['location']} ({business['category']})")
            else:
                st.warning("⚠ No se encontraron negocios para este tipo de evento.")
        else:
            st.error("❌ Error al obtener datos del servidor.")
    else:
        st.warning("⚠ Por favor, ingresa un tipo de evento antes de buscar.")
