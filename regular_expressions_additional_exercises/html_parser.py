import re


def extract_html_info(html):
    title_match = re.search(r'<title>(.*?)</title>', html)
    title = title_match.group(1) if title_match else "No title found"

    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    content = body_match.group(1) if body_match else "No content found"

    content = re.sub(r'<.*?>', '', content)

    # Print the results
    print(f"Title: {title}")
    print(f"Content: {content.strip()}")


html_input = input().strip()

extract_html_info(html_input)
