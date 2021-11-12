# MergePDF
Portable Python application to merge all PDFs from a folder only using command line parameters

5 nessecary parameters:
  1. SourcePath
  2. DestinationPath
  3. Filename (Without .pdf)
  4. autoDelete [1/0]
  5. AutoOpen [1/0]

MergePDF.exe SourcePath DestinationPath Filename autoDelete AutoOpen

Example: MergePDF.exe "C:\OriginalPDFs" "C:\MergedPDF" "MergedPDF" 1 0 

The SourcePath must not be the same as the DestinationPath
