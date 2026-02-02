import os
import datetime

class ReportWriter:
  def __init__(self, filename, column_headers):
    self.filename = f"{filename}.md"
    self.column_headers = column_headers
    self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self._initialize_file()

  def _initialize_file(self):
    file_exists = os.path.exists(self.filename)
    headers_line = f"| {' | '.join(self.column_headers)} |\n"
    
    should_create_headers = True

    if file_exists:
      with open(self.filename, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        content = f.read()
        if headers_line in [first_line] or headers_line in content:
            should_create_headers = False
            print(f"📂 File '{self.filename}' already exists with correct headers. Skipping initialization.")

    if should_create_headers:
      with open(self.filename, 'w', encoding='utf-8') as f:
        f.write(f"# Report: {self.filename.replace('.md', '')}\n")
        f.write(f"**Generated on:** {self.timestamp}\n\n")
        
        separator = " | ".join([":---"] * len(self.column_headers))
        
        f.write(headers_line)
        f.write(f"| {separator} |\n")
      print(f"🚀 Report '{self.filename}' created and initialized with headers.")

  def append_row(self, row_values):
    if len(row_values) != len(self.column_headers):
      print(f"⚠️ Warning: Column count mismatch for row {row_values}")
        
    formatted_row = " | ".join(map(str, row_values))
    
    with open(self.filename, 'a', encoding='utf-8') as f:
      f.write(f"| {formatted_row} |\n")