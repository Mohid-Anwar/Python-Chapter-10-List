import pyfiglet
import termcolor
def render(text):
    f = pyfiglet.Figlet()

    print(f.renderText(text))


"""render('Hello World')"""
for row in range(6):
    for col in range(7):
        if (row==0 and col %3 != 0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
            print(termcolor.colored("❤",color="magenta"),end = termcolor.colored("",color="magenta"))
        else:
            print(end=termcolor.colored(" ",color="magenta"))
    print(termcolor.colored(" ",color="magenta"))

z =pyfiglet.figlet_format("\️Anees", font= 'banner3-D')
print(termcolor.colored(z,'magenta',on_color="on_grey"))
