import re

def chunking(pages):
    chunks=[]

    current_chapter=""
    current_article=""
    current_section=""
    current_title=""
    current_text=""

    article_pattern = r"ARTICLE\s+([\d\.]+)"
    section_pattern=r"SECTION\s+\d+:\s+.*"
    chapter_pattern=r"CHAPTER\s+(\d+)"

    for page in pages:
        lines=page["text"].split("\n") #--> split each sentence in an line
        for i,line in enumerate(lines):
            line=line.strip()
            chapter_match= re.match(chapter_pattern,line)
            if chapter_match:
                chapter_num=chapter_match.group(1)
                chapter_title=""
                for j in range(i+1,len(lines)):
                    next_line=lines[j].strip()
                    if next_line:
                        chapter_title=next_line
                        break

                current_chapter = f"CHAPTER {chapter_num}"
                current_chapter_title = chapter_title
            elif re.match(section_pattern,line):
                current_section=line

            article_match= re.match(article_pattern,line)
            if article_match:
                if current_article and current_text:
                    chunks.append({
                        "chapter_number":current_chapter,
                        "chapter_title":current_chapter_title,
                        "section":current_section,
                        "article":current_article,
                        "title":current_title,
                        "page":page["page"],
                        "text":current_text.strip()

                    })
                current_article=article_match.group(1)
                current_title = ""
                for j in range(i + 1, len(lines)):

                    next_line = lines[j].strip()

                    if next_line.startswith("("):
                        current_title = next_line
                        break
                current_text=""

            else:
                current_text+=line+"\n"
    if current_article and current_text:
        chunks.append({
            "chapter_number": current_chapter,
            "chapter_title": current_chapter_title,
            "section": current_section,
            "article": current_article,
            "title": current_title,
            "page": page["page"],
            "text": current_text.strip()

        })
    print(f"Total chunks: {len(chunks)}")
    return chunks

