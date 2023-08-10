import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):
    path = "/about"
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay) 

        
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet tortor justo. Vestibulum in eros quis est finibus luctus et ut libero. Aliquam sit amet orci nec sem semper scelerisque ac in magna. Morbi ac malesuada lorem, sed tincidunt nibh. Donec hendrerit elit nec eleifend congue. Cras tincidunt cursus pretium. In suscipit libero nec gravida consequat. Vestibulum scelerisque tincidunt efficitur. Nunc porta suscipit nunc, quis pharetra sem tempus eu. Sed eleifend congue erat, a dapibus mi efficitur non. Sed ut sapien feugiat, bibendum tortor venenatis, aliquam libero. Aenean consectetur convallis ante in auctor.""",
               classes="text-lg")
        return wp
     
