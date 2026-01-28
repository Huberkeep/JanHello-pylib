def ceicfirmbar(things_name,prompt,choice_name,handlingback,do):
  print(f"""-----{prompt}-----
  {things_name}
  |{choice_name}||back|""")
  r == input("choice:")
  if r == null:
    print("choice cannot be empty!please try again")
  elif r == no:
    eval(handlingback)
  else:
    eval(do)
def icrinputbar(title,prompt):
  input(f"""{title}--------}
  {prompt}
  _reply_:
  """)
