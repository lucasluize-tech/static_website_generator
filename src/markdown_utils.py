import re


def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    sections = markdown.split("\n")
    blocks = []
    whole_section = []
    for section in sections:
        section = section.strip()
        if section == "":
            continue
        if section.startswith("*"):
            whole_section.append(section + " ")
            continue
        blocks.append(section)

    if len(whole_section) > 0:
        blocks.append(tuple(whole_section))

    return blocks


def block_to_block_type(block):
    re_heading = re.compile(r"^#+")
    re_code_block = re.compile(r"```(.*?)```", re.DOTALL)
    re_ordered_list = re.compile(r"^\d+\. ")

    if re_heading.match(block):
        return "heading"
    elif re_code_block.match(block):
        return "code"
    elif block.startswith("*"):
        return "unordered_list"
    elif block.startswith("-") or re_ordered_list.match(block):
        return "ordered list"
    elif block.startswith(">"):
        return "quote"
    else:
        return "paragraph"
