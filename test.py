
# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(type(a))
# a = list(map(lambda x : str(int(x) + 1), a))
# print(a)

# a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer','soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball','base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']

# b = set(a)
# print(b)
# for key in b:
#   count = 0 
#   for value in a:
#     if (key == value):
#       count += 1
#     else:
#       continue
  
#   print(key, count)

# class Foo:
#   def __init__(self, name):
#     self.name = name

#   def speak(self):
#     print('I Am' + self.name)

# class Bar(Foo):
#   def __init__(self, name):
#     super().__init__(name)

#   def speak(self):
#     print('You are ' + self.name)

# bar = Bar('John')
# bar.speak()

# import csv

# temp_list = []
# result_list = []

# with open("./a.csv", "r") as f:
#     reader = csv.reader(f, delimiter = ",")
#     for item in reader:
#       temp_list.append(item)
#     for index in range(len(temp_list)):
#       result_list = temp_list[index]

# result_list = list(map(lambda x : int(x), result_list))
# print(sum(result_list))

# class Median:
#     def __init__(self):
#         self.result_list = []
 
#     def get_item(self, item):
#         self.result_list.append(item)
 
#     def clear(self):
#         self.result_list.clear()
 
#     def show_result(self):
#         self.result_list.sort()
#         if len(self.result_list) % 2 != 0:
#           print(self.result_list[int((len(self.result_list))/2)])
#         else:
#           print(
#             (self.result_list[int((len(self.result_list))/2)] + self.result_list[int((len(self.result_list))/2)-1])/2
#             )
 
# median = Median()
# for x in range(10):
#     median.get_item(x)
# median.show_result()
 
# median.clear()
# for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
#     median.get_item(x)
# median.show_result()

# class Animal:
#     def __init__(self, name):
#         self.name = name
 
#     def speak(self):
#         print(self.name + ' cannot speak.')
 
#     def move(self):
#         print(self.name + ' cannot move.')
 
 
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
 
#     def move(self):
#         print(self.name + ' moves like a jagger.')
 
# class Retriever(Dog):
#     def __init__(self, name):
#         super().__init__(name)
 
#     def speak(self):
#         print(self.name + ' is smart enough to speak.')
 
# dog = Dog('Nancy')
# dog.speak()
# dog.move()
 
# super_dog = Retriever('Michael')
# super_dog.speak()
# super_dog.move()

class Foo:
    bar = "A"
    def __init__(self):
        self.bar = "B"
    
    class Bar():
        bar = "C"
        def __init__(self):
            self.bar = "D"

print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력

# import csv

# temp_list = []
# result_list = []

# with open("./a.csv", "r") as f:
#     reader = csv.reader(f, delimiter = ",")
#     for i in reader:
#       temp_list.append(i)
#     for index in range(len(temp_list)):
#       result_list = temp_list[index]
      
# result_list = list(map(lambda x : int(x), result_list))
# print(sum(result_list))






















