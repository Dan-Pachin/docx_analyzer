from docx import Document

def run(doc):

    # open selected document
    try:
        this_document = Document(doc)
    except:
        return print('Not a valid docx document!')

    # Name paragraphs and tables lists
    all_paragraphs = this_document.paragraphs
    all_tables = this_document.tables

    # Prompt user for outout type
    mode_selector = input('Show without empty paragraphs? (y/n):')
    while mode_selector != 'y' and mode_selector != 'n':
        mode_selector = input("Please select 'y' or 'n' : ")

    # list all paragraphs with their respective text
    for index, paragraph in enumerate(all_paragraphs):
        if paragraph.text:
            print('Paragraph[' + str(index) + '] text: ' + str(paragraph.text.strip()))
        else:
            if mode_selector == 'y':
                print('Paragraph[' + str(index) + '] text: ' + 'This paragraph is empty!')
            else:
                pass


if __name__ == '__main__':
    run(input('Please enter document path: '))
