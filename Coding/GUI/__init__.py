# l = [3,5,2,6]
#
# 3   [(0,3), (1,5), (2,2), (3,6)]
#
# for i in range(len(l)):
#     l[i]
#
# for x, item in enumerate(l):
#     print(x, item)
#
#
# print ("---")
# dd = {"first": 234,
#       "second": "asdas",
#       "some_other_item": 43,
#       34: 234234,
#       (234,5,3,):34234}
#
# dd['second']

#dd.items()
# for key, value in dd.items():
#     print (key, value)
#



class my_dict(object):
    def my_hash(s):
        the_hash = 0
        for i in s:
            the_hash += ord(i)

        return the_hash % 1000

    def get(self, key):
        pass

    def set(self, key, value):
        self.my_hash(key)


a = my_dict()
a.set("deep", 32)
a.get("deep")


d= {}



d['deep'] = 32





