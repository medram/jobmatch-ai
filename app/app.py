import os
import tempfile

import pandas as pd
import streamlit as st
from docx import Document
from PyPDF2 import PdfReader

# Configuration de la page
st.set_page_config(page_title="CV Sorter", layout="wide")


def main():
    st.title("📄 Système Intelligent de Tri de CVs")

    # Barre latérale pour les paramètres
    with st.sidebar:
        st.header("Configuration")

        # Clé API OpenAI
        openai_api_key = st.text_input("Clé API OpenAI", type="password")

        # Description du poste
        job_description = st.text_area(
            "Description du poste",
            height=200,
            placeholder="Coller la description du poste ici...",
        )

        # Upload de fichier de description
        uploaded_jd_file = st.file_uploader(
            "Ou uploader une description de poste", type=["txt", "pdf", "docx"]
        )

        if uploaded_jd_file:
            try:
                if uploaded_jd_file.type == "application/pdf":
                    reader = PdfReader(uploaded_jd_file)
                    job_description = " ".join(
                        [
                            page.extract_text()
                            for page in reader.pages
                            if page.extract_text()
                        ]
                    )

                elif (
                    uploaded_jd_file.type
                    == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                ):
                    doc = Document(uploaded_jd_file)
                    job_description = " ".join(
                        [para.text for para in doc.paragraphs if para.text]
                    )

                else:
                    job_description = str(uploaded_jd_file.read(), "utf-8")

                st.success("Description de poste chargée avec succès!")

            except Exception as e:
                st.error(f"Erreur lors de la lecture du fichier: {e}")

        # Upload des CVs
        uploaded_cvs = st.file_uploader(
            "Uploader les CVs (PDF/DOCX)",
            accept_multiple_files=True,
            type=["pdf", "docx"],
        )

    # Section principale
    if openai_api_key and job_description and uploaded_cvs:

        # Fonction pour extraire le texte d'un fichier
        def extract_text_from_file(file_path, file_type):
            # try:
            #     if file_type == "pdf":
            #         reader = PdfReader(file_path)
            #         return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

            #     elif file_type == "docx":
            #         doc = Document(file_path)
            #         return " ".join([para.text for para in doc.paragraphs if para.text])

            # except Exception as e:
            #     st.error(f"Erreur lecture {file_path}: {e}")
            #     return ""
            pass

        # Traitement des CVs
        # if st.button("🚀 Analyser les CVs", type="primary"):

        #     results = []

        #     with st.spinner("📊 Analyse des CVs en cours..."):

        #         for uploaded_file in uploaded_cvs:
        #             try:
        #                 # Sauvegarder temporairement le fichier
        #                 with tempfile.NamedTemporaryFile(
        #                     delete=False, suffix=os.path.splitext(uploaded_file.name)[1]
        #                 ) as tmp_file:
        #                     tmp_file.write(uploaded_file.read())
        #                     tmp_path = tmp_file.name

        #                 # Déterminer le type de fichier
        #                 file_type = (
        #                     "pdf" if uploaded_file.type == "application/pdf" else "docx"
        #                 )

        #                 # Extraire le texte
        #                 cv_text = extract_text_from_file(tmp_path, file_type)

        #                 if cv_text:
        #                     # Simulation d'évaluation (à remplacer par OpenAI)
        #                     score = len(cv_text) % 100  # Simulation simple
        #                     match_percent = min(score + 20, 100)  # Simulation

        #                     results.append(
        #                         {
        #                             "Fichier": uploaded_file.name,
        #                             "Score": score,
        #                             "Match %": match_percent,
        #                             "Points forts": (
        #                                 "Expérience pertinente"
        #                                 if score > 50
        #                                 else "Compétences de base"
        #                             ),
        #                             "Points faibles": (
        #                                 "Manque d'expérience"
        #                                 if score <= 50
        #                                 else "Peu d'infos"
        #                             ),
        #                         }
        #                     )

        #                 # Nettoyer le fichier temporaire
        #                 os.unlink(tmp_path)

        #             except Exception as e:
        #                 st.error(f"Erreur avec {uploaded_file.name}: {e}")

        #     if results:
        #         # Créer et afficher le tableau de résultats
        #         results_df = pd.DataFrame(results).sort_values("Score", ascending=False)

        #         st.subheader("🎯 Résultats de l'analyse")
        #         st.dataframe(results_df, use_container_width=True)

        #         # Métriques
        #         col1, col2, col3 = st.columns(3)
        #         with col1:
        #             st.metric("📊 Score moyen", f"{results_df['Score'].mean():.1f}/100")
        #         with col2:
        #             st.metric("⭐ Meilleur score", f"{results_df['Score'].max()}/100")
        #         with col3:
        #             st.metric("📋 CVs analysés", len(results_df))

        #         # Graphique
        #         st.subheader("📈 Performance des CVs")
        #         st.bar_chart(results_df.set_index("Fichier")["Score"])

        #         # Téléchargement des résultats
        #         csv = results_df.to_csv(index=False).encode("utf-8")
        #         st.download_button(
        #             "💾 Télécharger les résultats (CSV)",
        #             csv,
        #             "resultats_analyse_cvs.csv",
        #             "text/csv",
        #             key="download-csv",
        #         )
        #     else:
        #         st.warning("❌ Aucun CV n'a pu être analysé")

    else:
        # Message d'instructions
        st.info(
            """
        ## 📋 Instructions
        1. Entrez votre clé API OpenAI
        2. Saisissez ou uploader une description de poste
        3. Uploader les CVs à analyser (PDF ou DOCX)
        4. Cliquez sur 'Analyser les CVs'
        """
        )

        if not openai_api_key:
            st.warning("🔑 Clé API OpenAI requise")
        if not job_description:
            st.warning("📝 Description de poste requise")
        if not uploaded_cvs:
            st.warning("📄 CVs à analyser requis")


# Point d'entrée
if __name__ == "__main__":
    main()
