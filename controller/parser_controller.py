import fitz
from docx import Document


def extract_pdf_text(file_path):

    text = ""

    try:
        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:
        print(f"PDF Error: {e}")

    return text


def extract_docx_text(file_path):

    try:

        doc = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    except Exception as e:

        print(f"DOCX Error: {e}")

        return ""


def extract_txt_text(file_path):

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp1252",
        "latin-1"
    ]

    for encoding in encodings:

        try:

            with open(
                file_path,
                "r",
                encoding=encoding,
                errors="ignore"
            ) as file:

                return file.read()

        except Exception:
            continue

    return ""


def extract_text(file_path):

    file_path = file_path.lower()

    if file_path.endswith(".pdf"):
        return extract_pdf_text(
            file_path
        )

    elif file_path.endswith(".docx"):
        return extract_docx_text(
            file_path
        )

    elif file_path.endswith(".txt"):
        return extract_txt_text(
            file_path
        )

    return ""