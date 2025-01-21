def make_line_less_70(func):
  def wrapper(file_name, text):
    result = []
    left = 0
    right = 70
    text = text.encode("ascii", errors="ignore").decode()
    while left < len(text):
      result.append(text[left:right])
      left += 70
      right += 70
    for text in result:
      func(file_name, text)
  return wrapper