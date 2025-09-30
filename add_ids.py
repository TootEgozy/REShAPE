# import csv
# import os
# from PIL import Image, ImageDraw, ImageFont

# def add_ids_to_images(base_folder_path):

#     analysis_dir = os.path.join(base_folder_path, "Analysis")
#     data_files = [f for f in os.listdir(analysis_dir) if "data" in f.lower() and f.lower().endswith(('.xls', '.xlsx', '.csv'))]
#     if not data_files:
#         raise Exception("No Excel/CSV file found with 'Data' in name")

#     data_path = os.path.join(analysis_dir, data_files[0])
#     print("Using data file:", data_path)

#     # read CSV or Excel
#     if data_path.lower().endswith('.csv'):
#         with open(data_path, 'r') as f:
#             reader = csv.reader(f)
#             header = next(reader)
#             xm_idx = header.index("XM")
#             ym_idx = header.index("YM")
#             data_rows = list(reader)
#     else:
#         import xlrd
#         book = xlrd.open_workbook(data_path)
#         sheet = book.sheet_by_index(0)
#         header = sheet.row_values(0)
#         xm_idx = header.index("XM")
#         ym_idx = header.index("YM")
#         data_rows = [sheet.row_values(i) for i in range(1, sheet.nrows)]

#     image_folder = os.path.join(base_folder_path, "Color Coded")
#     output_folder = image_folder 

#     # prepare font
#     try:
#         font = ImageFont.truetype("arial.ttf", 14)
#     except:
#         font = ImageFont.load_default()

#     images = [f for f in os.listdir(image_folder) if f.lower().endswith(".tif")]
#     images.sort()     

#     for img_name in images:
#         img_path = os.path.join(image_folder, img_name)
#         im = Image.open(img_path).convert("RGB")
#         draw = ImageDraw.Draw(im)

#         # draw IDs
#         for i, row in enumerate(data_rows, 1):
#             xm = float(row[xm_idx])
#             ym = float(row[ym_idx])
#             draw.text((xm, ym), str(i), fill=(255, 0, 0), font=font)

#     out_path = os.path.join(output_folder, img_name)
#     im.save(out_path)
