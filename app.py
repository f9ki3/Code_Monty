from flask import Flask, render_template

app = Flask(__name__)

#banner data
banner1 = "Unlock Your Coding Potential with Code Monty: Where Learning Meets Mastery for Every Filipino"
banner2 = "Join Us! now for free python course."


#footer data
about_dev = "Fyke Lleva, a dedicated solo web developer, envisions a more inclusive digital landscape for Filipinos. The creative force behind Code Monty, the developer channels his passion for coding and design into building an accessible platform."
about_codemonty = "Discover the power of Code Monty, your gateway to the exciting world of coding with Python. Tailored for Filipinos, our learning platform offers free, accessible, and engaging IT courses. Elevate your skills, embrace the digital future, and code your success with Code Monty - where learning meets innovation."

@app.route ('/')
def home():
    return render_template('base.html', about_dev=about_dev, about_codemonty=about_codemonty, banner1=banner1, banner2=banner2)

