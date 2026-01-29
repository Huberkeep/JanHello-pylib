def ceicfirmbar(things_name,prompt,choice_name,handlingback,do):
  print(f"""-----{prompt}-----
  {things_name}
  |{choice_name}||back|""")
  r == input("choice:")
  if r == null:
    print("choice cannot be empty!please try again")
  elif r == back:
    eval(handlingback)
  elif r == choice_name:
    er = input("Are you sure?(input again)")
    if ar == choice_name:
      eval(do)
    elif er == 'back':
      br == input("R u sure?(yes or no)")
      if br == 'yes'
        eval(handlingback)
      else:
         eval(handlingback)
  else:
      print("?")
def icrinputbar(title,prompt):
  input(f"""{title}--------}
  {prompt}
  _reply_:
  """)
