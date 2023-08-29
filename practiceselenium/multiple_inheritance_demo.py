#Multiple Inheritance - A class can inherit attributes and methods from more than one class 

class MoveCharacter:
    def movefwd(self):
        print("Move forward 1 step")

    def movebwd(self):
        print("Move backward 1 step")

class JumpCharacter:
    def jump1level(self):
        print("Jump character 1 level")

    def jump2level(self):
        print("Jump character 2 Level")

# class Momo(MoveCharacter, JumpCharacter):
class Momo(JumpCharacter, MoveCharacter):
    def movebwd(self):
        print("moving")

m = Momo()
m.movebwd()
m.jump1level()
print(Momo.mro())

# class Micky(MoveCharacter, JumpCharacter):
#     pass

# x = Micky()
# x.movebwd()
# x.jump2level()