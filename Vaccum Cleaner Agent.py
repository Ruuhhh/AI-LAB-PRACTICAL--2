
is_Room1_clean =input("is Room1 clean yes/no:"). lower()
is_Room2_clean =input("is Room2 clean yes/no:"). lower()
if is_Room1_clean == "no" and is_Room2_clean == "yes":
  print("Clean Room1")
elif is_Room1_clean == "yes" and is_Room2_clean == "no":
 print("Clean Room2")
elif is_Room1_clean == "no" and is_Room2_clean == "no":
 print("clean Room1 and Room2 ")
else:
 print("Your job is done !!!!!!!! ") 