import time

def writetxt(filename:str, txtinput:str):
    """
        将字符串写入到指定文件中，每个字符写入后暂停一秒。

        Args:
            filename (str): 要写入的文件名。
            txtinput (str): 要写入的字符串。

        Returns:
            无返回值。

        Raises:
            FileNotFoundError: 如果指定的文件名不存在，将引发 FileNotFoundError 异常。
        """
    # 打开文件，以写入模式打开
    with open(filename, 'w') as fileObj:
        # 遍历输入的字符串
        for i in txtinput:
            # 将每个字符写入文件
            fileObj.write(i)
            # 暂停1秒
            time.sleep(1)


def readtxt(filename:str):
    """
    读取文本文件内容。

    Args:
        filename (str): 要读取的文件名。

    Returns:
        str: 文件内容，以字符串形式返回。

    Raises:
        FileNotFoundError: 如果指定的文件不存在，则引发此异常。
        IOError: 如果读取文件时发生I/O错误，则引发此异常。
    """
    with open(filename,'r') as fileObj:
        return fileObj.read()
