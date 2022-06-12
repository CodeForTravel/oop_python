class A:
    def get_class_a_info(self):
        print("I am from class A")


class B:
    def get_class_b_info(self):
        print("I am from class B")


class C(B):
    '''Single inheritance '''

    def get_class_c_info(self):
        print("I am from class C")


class C(A, B):
    '''Multiple inheritance '''

    def get_class_d_info(self):
        print("I am from class D")


class E(C):
    '''Multilavel inheritance '''

    def get_class_e_info(self):
        print("I am from class E")
