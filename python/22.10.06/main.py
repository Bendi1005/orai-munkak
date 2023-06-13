from korcsoja import atlagAlattDb, atlagPontszam, birokPontszamai, gyoztesVersenyzo, pontszamGeneral, versenyzok, gyoztesPontszam

pontszamGeneral()
print(versenyzok)
print(f'A győztes pontszáma: {gyoztesPontszam()}')
print(f'A győztes versenyző rajtszáma: {gyoztesVersenyzo()+1}')
print(f'A versenyzők átlag pontszáma: {atlagPontszam()}')
print(f'Átlag alatt teljesített versenyzők száma: {atlagAlattDb()}')


# # # #     # # # # #   #        #  #  ##########
#       #   #           # #      #  #  #
#       #   #           #  #     #  #  #
# # # #     #           #   #    #  #  #
#           # # # #     #    #   #  #  ##########
#           #           #     #  #  #           #
#           #           #      # #  #           #
#           # # # # #   #        #  #  ##########