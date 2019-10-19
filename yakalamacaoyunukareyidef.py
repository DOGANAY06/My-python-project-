import turtle
import random 
turtle.setup(500,500) #oyun alanı
ok=turtle.Turtle()    #ok isminde turtle ürettik
ok.penup()
hedef=turtle.Turtle()   # hedef isminde kare seklinde bir turtle ürettik
hedef.shape("square") 
def rastgelekonum():   #hedefin rastgele yerlere konumlanmasını sağlayan fonksiyon
    hedef.penup()   
    hedef.setpos(random.randint(-400,400)),random.randint(-400,400)
    hedef.showturtle()
    
def ileri():     #okun yukarı gitmesi
    ok.right(15)
def geri():
    ok.left(15)   #okun aşağı gitmesi

turtle.onkeypress(ileri,"Up")   #tuş atama islemleri yukarı ve aşağı için 
turtle.onkeypress(geri,"Down")
turtle.listen()     #bilgisayarın bunu takip etmesi için gerekli
rastgelekonum()
while True: 
    ok.fd(2)    #okun gidiş hızı 
    x=(ok.xcor()-hedef.xcor())   #uzaklık hesaplamak içindir hedef x den normalde ki okun x i çıksın
    y=(ok.ycor()-hedef.ycor())   #uzaklık hesaplamak içindir hedef y den okun y sini çıkarırız
    uzaklik=((x*x)+(y*y))**0.5    #pisagor bağıntısı x ve y nin kareleri ve karekökü
    if uzaklik<15:    
        hedef.hideturtle()  #15 den kücüksek uzaklık gizle ve başka bir konuma gönder hedefi 
        rastgelekonum()
