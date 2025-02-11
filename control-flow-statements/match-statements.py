# def http_error(status):
#     match status:
#         # case 400:
#         #     return "Bad request"
#         # case 404:
#         #     return "Not Found"
#         # case 418:
#         #     return "I'm a teapot"
#         case 400 | 404 | 418:
#             return "or conditon samjne ke liye"
#         case _:
#             return "Something's wrong with the internet"
            
# print(http_error(400))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")
                
Point()