import codecs

def convert_encoding(input_file, output_file, from_enc='gbk', to_enc='utf-8'):
    with codecs.open(input_file, 'r', from_enc) as f_in:
        content = f_in.read()
    with codecs.open(output_file, 'w', to_enc) as f_out:
        f_out.write(content)

convert_encoding(
    'document/子文件夹/testfile.txt',
    'document/子文件夹/testfile_utf8.txt'
)
