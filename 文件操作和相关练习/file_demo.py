"""
文件操作示例
"""
import os


class FileReader:
    def __init__(self):
        self._file_handles = {}  # 存储文件对象和位置 {filename: (file_obj, position)}
        self.resume = False  # 类属性控制是否续读

    def _read_file(self, filename, mode='read'):
        """内部文件读取核心逻辑"""
        try:
            if filename not in self._file_handles or not self.resume:
                file_obj = open(filename, 'r', encoding='utf-8')
                self._file_handles[filename] = (file_obj, 0)

            file_obj, position = self._file_handles[filename]
            file_obj.seek(position)

            if mode == 'read':
                content = file_obj.read()
            elif mode == 'readline':
                content = file_obj.readline()

            self._file_handles[filename] = (file_obj, file_obj.tell())
            return content

        except FileNotFoundError:
            return "文件没找到"
        except PermissionError:
            return "错误：无文件访问权限"
        except UnicodeDecodeError:
            return "错误：文件编码不匹配"
        except Exception as e:
            return f"未知错误：{str(e)}"

    def readtxtfile(self, filename):
        """读取整个文件内容"""
        return self._read_file(filename, mode='read')

    def readlinetxtfile(self, filename):
        """读取文件单行内容"""
        return self._read_file(filename, mode='readline')

    def close_all(self):
        """关闭所有打开的文件"""
        for file_obj, _ in self._file_handles.values():
            file_obj.close()
        self._file_handles.clear()


reader = FileReader()
reader.resume = True  # 开启续读模式
str1 = reader.readlinetxtfile(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
), 'document', '子文件夹', 'testfile.txt'))  # 第一行
str2 = reader.readlinetxtfile(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
), 'document', '子文件夹', 'testfile.txt'))  # 第二行
reader.close_all()
print(str1)
print(str2)
