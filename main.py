from core.engine import Engine

eng = Engine()

print(eng.get_modo())

eng.mudar_modo("ACOMPANHANDO")
print(eng.get_modo())

eng.mudar_modo("TRABALHANDO")
print(eng.get_modo())