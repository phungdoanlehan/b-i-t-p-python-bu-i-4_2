
import random
def game_engine(tien_cuoc):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum_dice = dice1 + dice2 
   
    while True:
        select = int(input("Nhap lua chon ban muon cuoc 1 - Tai, 2 - Xiu, 3 - Tong bang 5"))
        if select in [1, 2, 3]:
            break

    if sum_dice > 5 and select == 1:
        print("Ban thang!")
        print(f"Dice1 = {dice1}, Dice2 = {dice2}, Tong xuc xac = {sum_dice}")
        return tien_cuoc
    if sum_dice < 5 and select == 2:
        print("Ban thang!")
        print(f"Dice1 = {dice1}, Dice2 = {dice2}, Tong xuc xac = {sum_dice}")
        return tien_cuoc
    if sum_dice==5 and select == 3:
        print("Ban thang gap 3 lan!")
        print(f"Dice1 = {dice1}, Dice2 = {dice2}, Tong xuc xac = {sum_dice}")
        return tien_cuoc*3
    else:
        print("Ban thua!")
        print(f"Dice1 = {dice1}, Dice2 = {dice2}, Tong xuc xac = {sum_dice}")
        return -tien_cuoc

if __name__ == "__main__":
   money = 100000
   so_luot_thang = 0
   so_luot_choi = 0
   print("Ban dang co 100.000VND, moi luot choi, ban dat cuoc 10.000VND, neu thua ban se mat tien, neu thang theo tung truong hop, ban se duoc cong tien thuong!")
   while money > 0:
       so_luot_choi += 1
       print(f"So du tien : {money}")
       cuoc = 10000
       if money < cuoc:
           print("Ban khong con du tien de tiep tuc")
           break
       ket_qua = game_engine(cuoc)
       if ket_qua>0:
           so_luot_thang += 1
       money += ket_qua
       tieptuc = input("Ban co muon tiep tuc choi khong? <n/N de ket thuc>").lower()
       if tieptuc == 'n':
           break
   print(f"So luot choi: {so_luot_choi}")
   print(f"So luot thang: {so_luot_thang}")
   print(f"So tien con lai: {money}")
       
