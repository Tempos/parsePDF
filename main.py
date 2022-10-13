import contextlib
import json
import re

import tabula

SPLITS = ['aws', 'com', 'com.cn']


def process_pdf(pdf_file_path: str, out_file_path: str, split_by: list = None) -> None:
    converted_file = 'data/out.json'
    split = sorted(split_by or SPLITS, reverse=True)
    domains = '|'.join(split).replace('.', r'\.')
    pattern = re.compile(fr'([<>\w.:/-]+\.(?:{domains}))[\"*]*')

    print('Converting PDF to JSON, using:'
          f'\n\t Splits: {split}\n\tPattern: {pattern}'.replace(r'\\', '\\'))
    tabula.convert_into(pdf_file_path, converted_file, output_format="json", pages='all')
    print(f"\nConverted '{pdf_file_path}' => '{converted_file}'")

    with open(converted_file, 'r') as tables, open(out_file_path, 'w') as out:
        results, counter = set(), 0

        for table in json.load(tables):
            for i, row in enumerate(table['data']):  # list of rows
                if not i: continue  # skip headers

                with contextlib.suppress(IndexError):
                    cell = parse(row[2]['text'], split)
                    if result := re.findall(pattern, cell):
                        [results.add(f'{line}\n') for line in result]

        out.writelines(sorted(results))
        print(f"Saved {len(results)} unique lines to '{out_file_path}' file")


def parse(line: str, splits: list = None) -> str:
    old_line = new_line = line
    if splits:
        for s in splits:
            old_line = new_line = old_line.replace(f'{s}\r', f'{s}\n')  # split urls

    return new_line.replace('\r', '')  # delete caret returns


if __name__ == '__main__':
    process_pdf(
        pdf_file_path='data/aws-general.pdf',
        out_file_path='result'
    )
