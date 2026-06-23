from docx import Document

doc = Document("data/job_description.docx")

text = ""

for para in doc.paragraphs:
    text += para.text + "\n"

print(text[:3000])

with open(
    "output/jd_text.txt",
    "w",
    encoding="utf8"
) as f:
    f.write(text)

print("\nJD Saved Successfully")