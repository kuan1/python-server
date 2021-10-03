def clean_object(dct):
  ret = {}
  for key,value in dct.items():
    if value != None:
      ret[key] = value
  return ret