import re
import random
from tqdm import tqdm
import xml.etree.ElementTree as ET
from configs.logging import logging

def process_posts(f_in, f_out_train, f_out_test, target_tag, split):
    line_num = 1
    for line in tqdm(f_in):
        try:
            f_out = f_out_train if random.random() > split else f_out_test
            attribute = ET.fromstring(line).attrib

            pid = attribute.get('Id', "")
            label = 1 if target_tag in attribute.get('Tags', "") else 0
            title = re.sub(r"\s+", " ", attribute.get('Title', "")).strip()
            body = re.sub(r"\s+", " ", attribute.get('Body', "")).strip()
            text = title + " " + body

            f_out.write(f"{pid}\t{label}\t{text}\n")
            line_num += 1
        except Exception as e:
            msg = f"Skipping the broken line {line_num}: {e}\n"
            logging.exception(msg)