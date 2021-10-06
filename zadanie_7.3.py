class BaseContact:
  def __init__(self, first_name, last_name, phone, e_mail):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.e_mail = e_mail
  
  def contact1(self):
    return f"Wybieram numer {self.phone} i dzwonię do {self.first_name}  {self.last_name}."

  @property
  def label_lenth(self):
    return len({self.first_name})
  
    


class BusinessContact(BaseContact):
  def __init__(self, job, company, business_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.job = job
       self.company=company
       self.business_phone= business_phone

  def contact2(self):
    return f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name}  {self.last_name}."
  
  @property
  def label_lenth(self):
    return len({self.first_name})

contacts=[]

contact1=BusinessContact(first_name ="Agnieszka",last_name="Kowlaska",phone= "+48 509 387 246", business_phone= "+48 398 356 287", company="Dolina Czerska",job="Handlowiec", e_mail="a.kowlaska@dolinaczerska.pl")
contacts.append(contact1)

contact2=BusinessContact(first_name="Krzysztof",last_name="Goliński", phone= "+48 509 387 246", business_phone= "+48 398 356 287",company="Jastrząb",job="Dyrektor Finansowy", e_mail="k.golinksi@jastrzab.com.pl")
contacts.append(contact2)

contact3=BusinessContact(first_name="Lucjan",last_name="Poniedziałek", phone= "+48 509 387 246", business_phone= "+48 398 356 287",company="Gacie Po Tacie",job="Dział kreatywny",e_mail="lucjanp@gpt.pl")
contacts.append(contact3)

contact4=BusinessContact(first_name="Hanna",last_name="Czerska", phone= "+48 509 387 246", business_phone= "+48 398 356 287", company="Tu i Tam Ltd.",job="Współpraca międzynarodowa",e_mail="hc@tuitam.com")
contacts.append(contact4)

contact5=BusinessContact(first_name="Pelagia",last_name="Kasnobrodzka", phone= "+48 509 387 246", business_phone= "+48 398 356 287", company="Bazylia Sp. z o.o.", job="Smakosz",e_mail="pelagiak@bazylia.pl")
contacts.append(contact5)

for i in range(len(contacts)):
  print(contacts[i].contact1())

for i in range(len(contacts)):
  print(contacts[i].contact2())

for i in range(len(contacts)):
  print( len(contacts[i].first_name)+len(contacts[i].last_name)+1)
