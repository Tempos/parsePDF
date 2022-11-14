import contextlib
import json
import re
from pathlib import Path

import tabula

SPLITS = ['aws', 'com', 'com.cn', 'cn']


def process_pdf(pdf_file_path: str, out_file_path: str, col: int = 1, split_by: list = None) -> None:
    converted_file = f"/tmp/{Path(pdf_file_path).stem}.json"
    split = sorted(split_by or SPLITS, reverse=True)

    domains = '|'.join(split).replace('.', r'\.')
    # pattern = re.compile(fr'([<>\w.:/-]+(?:{domains})[\w\s\"/?=*•-]*)')
    # pattern = re.compile(fr'((?:\w+://)?[<>\w./\r\t-]+(?:{domains})[\w\s\"/?*=-]*)$')
    pattern = re.compile(fr'((?:\w+://)?[<>\w./\r\t-]+\.(?:{domains})/?[\w/\"*=?.&%+-]*)')

    print('Converting PDF to JSON, using:\n\t'
          f' Splits: {split}\n\tPattern: {pattern}'.replace(r'\\', '\\'))
    # tabula.convert_into(pdf_file_path, converted_file, output_format="json", pages='all')
    print(f"\nConverted '{pdf_file_path}' => '{converted_file}'")

    with open(converted_file, 'r') as tables, open(out_file_path, 'w') as out:
        results, counter = set(), 0

        for table in json.load(tables):
            for i, row in enumerate(table['data']):  # list of rows
                if not i and (len(row) > 1 and row[1] != 'Website Endpoint'):
                    continue  # skip headers

                with contextlib.suppress(IndexError):
                    cell_one = row[0]['text'].replace('\r', '')
                    for col in range(1, 3):
                        urls = split_url(row[col]['text'], split).split('\n')
                        for url in urls:
                            if result := re.findall(pattern, url):
                                for item in {'<registry-id>.', 'prefix-', 'prefix.', 'account-id.'}:
                                    result[0] = result[0].replace(item, '')
                                results.add(f"{result[0]},{cell_one or 'PLACEHOLDER'}\n")

        out.writelines(sorted(results))
        print(f"Saved {len(results)} unique lines to '{out_file_path}' file")


def split_url(line: str, splits: list = None) -> str:
    old_line = new_line = line
    if splits:
        for s in splits:
            old_line = new_line = old_line.replace('*', '').replace('�', '').replace('•', '').replace(' ', '')\
                .replace(f'{s}\r', f'{s}\n')  # split urls

    return new_line.replace('\r', '')  # delete caret returns


if __name__ == '__main__':
    process_pdf(
        # pdf_file_path='https://docs.amazonaws.cn/en_us/aws/latest/userguide/aws-ug.pdf',
        pdf_file_path='https://docs.aws.amazon.com/pdfs/general/latest/gr/aws-general.pdf', col=2,
        out_file_path='result.csv'
    )

    # s = "Valid endpoint name for this\rRegion:\r�s3.cn-\rnorthwest-1.amazonaws.com.c\r�s3.dualstack.cn-\rnorthwest-1.amazonaws.com.c\r� account-id.s3-control.cn-\rnorthwest-1.amazonaws.com.c\r� account-id.s3-\rcontrol.dualstack.cn-\rnorthwest-1.amazonaws.com.c\rAmazon S3 Access Points\rendpoints (HTTPS only):\r�s3-accesspoint.cn-\rnorthwest-1.amazonaws.com\r�s3-accesspoint.dualstack.cn-\rnorthwest-1.amazonaws.com"
    # print(
    #     split_url(s, SPLITS)
    # )

