d={'tej':98,'keerthi':97,'tejaswini':99,'indhu':67,'thappi':74}
defaulters=[name for name,percent in d.items() if percent<75]
print(defaulters)