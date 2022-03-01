def fetch(command):
  store = []
  data = command
  data = data + "-"
  start = 0
  stop = 0
  temp = ""
  while stop < len(data):
      if data[stop] != "-":
          stop += 1
      else:
          temp = data[start:stop]
          store.append(temp)
          start = stop + 1
          stop += 1

  store.pop(0)
  return store