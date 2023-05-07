from docxtpl import DocxTemplate

doc = DocxTemplate("template/new_template.docx")
context = {'Text1': "хуй"}
doc.render(context)
doc.save("template/out.docx")
