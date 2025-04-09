import re

def count(xml):
    count = 0
    with open (xml, 'r', encoding='utf-8') as file:
        content = file.read()
        total_l = len(content)
        closing_tags = re.findall(r'</[^>]+>', content)
        tag_count = len(closing_tags)
        closing_chars = sum(len(tag) for tag in closing_tags)
        percentage = (closing_chars / total_l) * 100 if total_l > 0 else 0
        print(f"percentage: {percentage}")
        return tag_count

xml = "XML/xml_sample.xml"
closing_tags = count(xml)
print(f"Number of closing tags: {closing_tags}")