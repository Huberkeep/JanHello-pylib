import time
horline = "─"
class confirm:
  def doubleconfirm(prompt,options1,options2,inputting_prompt,1_handling,2_handling):
    horlineWidthNumber = horline * len(prompt) + 2
    print("┌",horlineWidthNumber,"┐")
    print(prompt)
    print("┌",horlineWidthNumber,"┬"horlineWidthNumber,"┐")
    print(options1,options2)
    print("└",horlineWidthNumber,"┘")
    r = input(input_prompt)
    if r == options1:
      oodr = input("Reconfirm your option,please")
      if oodr == options1:
        eval(inputed_options1_handling)
      else:
        print("Please check your typing")
    elif r == options2:
      osdr = input("Reconfirm your option,please")
      if osdr == options2:
        eval(inputed_options2_handling)
      else:
        print("Please check your typing")
    else:
      print("\"",r,"\"","is not a option!")
class useless:
  POTATOS = 0 #POTATOES → POTATOS,because ↓ 
  #"useless"
  null = None#very useless,null → none
  def veryuselessfunction(🤖):
    print("veryuselessfunction❗️")
    for i in range(10):
      time.sleep(180)
      print(f"get:{i + 1}🔥🥔")
    print("✅ 10🔥🥔,You can eat them now.")
    eatornoeat = input("EAT POTATOS(10/",POTATOS,"YES OR NO)")
    if eatornoeat == "YES":
      for uselessvar in range(10):
        time.sleep(90)
        POTATOS -= 1
      print("ALL:EATED")
    elif eatornoeat == "NO":
      return "🥔🚯"
      PlantR = input("Are You Wanna Plant it?(Yes or No)")
      if PlantR == "YES":
        nowYes = time.time()
        for nousevar in range(3):
          time.sleep(1080)
          POTATOS += 1
          print(POTATOS + 1,"POTATOS")
        print("💥:🥔✅")  
      
      elif PlantR == "NO":
        print("😊")
    else:
      print("📄❌:🥔")
      POTATOS == null
    
