
from varasto import Varasto


def luonnin_jalkeen(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def get_olut(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def lisaa_mehua(mehua, maara):
    print(f"Lisätään {maara}")
    mehua.lisaa_varastoon(maara)
    print(f"Mehuvarasto: {mehua}")


def ota_mehua(mehua, maara):
    print(f"Otetaan {maara}")
    mehua.ota_varastosta(maara)
    print(f"Mehuvarasto: {mehua}")


def mehu_setterit(mehua):
    print("Mehu setterit:")
    lisaa_mehua(mehua, 50.7)
    ota_mehua(mehua, 3.14)


def testaa_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def testaa_lisaaminen(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def testaa_ottaminen(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    luonnin_jalkeen(mehua, olutta)
    get_olut(olutta)
    mehu_setterit(mehua)
    testaa_virhetilanteet()
    testaa_lisaaminen(mehua, olutta)
    testaa_ottaminen(mehua, olutta)


if __name__ == "__main__":
    main()
