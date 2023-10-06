
def SoChiaKetCho5_Le(so):
    if so % 2 == 0:
        return False
    elif so % 5 == 0:
        return True
    return False
dayso=[2,3,4,5,6,7,8,9,15]
daySoMoi= list(filter(SoChiaKetCho5_Le,dayso))
print(f"Cac so chia het cho 5 va la so le trong day {dayso} la :",daySoMoi)
