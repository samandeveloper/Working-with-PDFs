# In this project we want to work on pdf files
import PyPDF2
import sys

with open ('dummy.pdf','rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)	#number of pages
	print(reader.getPage(0))	#get one of the pages of pdf

	#rotate dummy.pdf and write it in a created new file (tilt.pdf)
	page = reader.getPage(0)	#specify the page that we want to rotate
	print(page.rotateCounterClockwise(90))
	writer = PyPDF2.PdfFileWriter()
	with open ('tilt.pdf','wb') as new_file:
		writer.addPage(page)
		writer.write(new_file)

# Combine as many pdf files as we want and write it in a created new file (super2.pdf)
inputs = sys.argv[1:]
def pdf_combine(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	with open ('super2.pdf','wb') as file:
			merger.write(file)
	# or:
	# merger.write('super.pdf')
pdf_combine(inputs)

# Add watermarker (wtr.pdf) to each page of super.pdf and write it in watermark_output.pdf
template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
#or:
# for i in range(0,3):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)
	with open ('watermark_output.pdf', 'wb') as file:
		output.write(file)