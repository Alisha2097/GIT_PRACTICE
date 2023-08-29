class MoveCharacter:
    def movefwd(self):
        print("Move forward 1 step")

    def movebwd(self):
        print("Move backward 1 step")

class JumpCharacter(MoveCharacter):
    def jump1level(self):
        print("Jump character 1 level")

    def jump2level(self):
        print("Jump character 2 Level")

class Momo(JumpCharacter):
    def movebwd(self):
        print("moving")

m = Momo()
m.movebwd()
m.jump1level()
print(Momo.mro())
