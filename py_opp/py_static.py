class MyStatic:
    def reset(self): # 파이선에서 메소드 선언방식
        self.x =0
        self.y =0
a = MyStatic()
# MyStatic.reset(a) # 클래스 메소드
a.reset # 인스턴스 메소드
print('x값:' ,a.x)
print('y값:' ,a.y)
    

        #펑션은 클래스 바깥쪽에있어야하고 메소드는 클래스 안에 있어야 한다.