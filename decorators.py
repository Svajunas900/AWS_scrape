def decor(func):
  def wrapper(file_name, text):
    result = []
    left = 0
    right = 70
    text = text.encode("ascii", errors="ignore").decode()
    print(left, right, len(text))
    while left < len(text):
      result.append(text[left:right])
      left += 70
      right += 70
    for text in result:
      print(len(text))
      func(file_name, text)
  return wrapper