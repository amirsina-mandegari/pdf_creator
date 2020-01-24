import os
import img2pdf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_path",
    type=str,
    default=".",
    help="input folder path"
    )
parser.add_argument(
    "--output_path",
    type=str,
    default=".",
    help="output file path"
    )
parser.add_argument(
    "--output_name",
    type=str,
    default="output.pdf",
    help="output file name"
    )

args = parser.parse_args()
base_path = os.path.abspath(args.input_path)
files = os.listdir(base_path)
files.sort()

output_name = args.output_name
if not output_name.endswith(".pdf"):
    output_name = output_name + ".pdf"

output_file = os.path.join(os.path.abspath(args.output_path), output_name)
with open(output_file, "wb") as f:
    f.write(img2pdf.convert([os.path.join(base_path,i) for i in files if i.endswith(".jpg")]))
    
print('done')
