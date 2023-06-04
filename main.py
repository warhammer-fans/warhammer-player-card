from pypdf import PdfReader

reader = PdfReader("assets/kant_schwindel_karta.pdf")

for id in 1,2:
    page = reader.pages[id]
    print(page.extract_text())

from pypdf import PdfWriter


writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.append(reader)

writer.update_page_form_field_values(
    writer.pages[0], {"fieldname": "some filled in text"}
)

# write "output" to pypdf-output.pdf
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)