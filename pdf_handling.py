import os
from PyPDF2 import PdfReader

pdf_folder = "pdf_files/"

pdf_categories = ['ACCOUNTANT/', 'ADVOCATE/','AGRICULTURE/', 'APPAREL/', 'ARTS/', 'AUTOMOBILE/', 'AVIATION/', 'BANKING/',
                  'BPO/', 'BUSINESS-DEVELOPMENT/', 'CHEF/', 'CONSTRUCTION/', 'CONSULTANT/', 'DESIGNER/', 'DIGITAL-MEDIA/', 'ENGINEERING/',
                  'FINANCE/', 'FITNESS/', 'HEALTHCARE/', 'HR/', 'INFORMATION-TECHNOLOGY/', 'PUBLIC-RELATIONS/', 'SALES/', 'TEACHER/']

output_folder = "output_folder/"

os.makedirs(output_folder, exist_ok=True)

for pdf_category in pdf_categories:
  for pdf_file in os.listdir(pdf_folder + pdf_category):
    if pdf_file.endswith(".pdf"):
      pdf_path = os.path.join(pdf_folder + pdf_category, pdf_file)
      reader = PdfReader(pdf_path)

      text = ""
      for page in reader.pages:
        text += page.extract_text()

      output_file = os.path.join(output_folder, pdf_file.replace(".pdf", ".txt"))
      with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
  
  print(f"Extracted text from {pdf_category} and saved to {output_file}")
