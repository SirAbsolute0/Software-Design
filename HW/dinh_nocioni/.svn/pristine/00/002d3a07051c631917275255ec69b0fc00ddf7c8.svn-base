def common_code():
  print("common")

def f1_wet():
  common_code()
  print("f1 wet called")

def f2_wet():
  common_code()
  print("f2 wet called")

#f1_wet()
#f2_wet()



def dry(func):
  def run():
    common_code()
    func()
    print("tsetting")
  return run

@dry
def f1():
  print("f1 called")

@dry
def f2():
  print("f2 called")
  print("f2 processed")


f1()
f2()

