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
        eval(1_handling)
      elif oodr == options2:
        eval(2_handling)
      else:
        return "OPTIONS ERROR:TYPING NOT A OPTION"
    elif r == options2:
      osdr = input("Reconfirm your option,please")
      if osdr == options2:
        eval(2_handling)
      elif osdr == options1:
        eval(1_handling)
      else:
        return "\"",r,"\"","is not a option!"
    else:
      return "\"",r,"\"","is not a option!"
  def uselessexc(func,error):
    try:
      eval(func)
    except * as error:
      return error
