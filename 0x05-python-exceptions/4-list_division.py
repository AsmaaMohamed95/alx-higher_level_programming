#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
            try:
                div = (my_list_1[i] / my_list_2[i])
            except(TypeError, ValueError):
                div = 0
                print("wrong type")
                continue
            except ZeroDivisionError:
                div = 0
                print("division by 0")
                continue
            except IndexError:
                div = 0
                print("out of range")
                continue
            finally:
                new.append(div)
    return new
