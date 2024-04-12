from contextlib import contextmanager

class FileCommon(object):
  def __init__(self, file_name, method) -> None:
    self.file_obj = open(file_name, method)
  def __enter__(self):
    return self.file_obj
  def __exit__(self, type, value, trace_back):
    self.file_obj.close()

@contextmanager
def FileDeco(file_name, method):
    file_obj = open(file_name, method)
    try:
        yield file_obj
    finally:
        file_obj.close()

with FileDeco('test1.txt', 'w') as file:
    file.write('Hello, World!')

with FileCommon('test2.txt', 'w') as file:
    file.write('Hello, World!')