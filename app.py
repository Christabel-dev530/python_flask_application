from flask import Flask, render_template
app=Flask(__name__)
def add():
   a=1500
   b=50
   c=a*b
   #return "This is the result " + str(c)
   return c

@app.route('/')
def welcome():
    return "<h3>welome to my python class</h3>"

@app.route('/openings')
def openings():
    openings = ["Receptionist","Managers", "Help desk", "Engineers", "Technicians", "Developers", "Doctors", "Nurse"]
    return render_template("vaccant.html", openings=openings)

@app.route('/states')
def states():
    states = ["Imo", "Abia", "Rivers", "Akwaibom", "CrossRiver", "Anambra", "Delta"] 
    return render_template("states.html", states=states)

@app.route('/subjects')
def subjects():
    subjects = ["maths", "english", "physics", "chemistry", "biology", "geography", "economics"]
    return render_template("subjects.html", subjects=subjects)

@app.route('/tasks')
def tasks():
    jobsavailable = True
   
    if jobsavailable:
        tasks = [
            "cleaning",
            "gathering",
            "client support",
            "data manipulation",
            "cloud support",
            "marketing",
            "fumigation"
        ]
       
        score = add()  # assuming you have defined an add() function elsewhere
       
        return render_template(
            "tasks.html",
            jobsavailable=jobsavailable,
            tasks=tasks,
            score=score
        )
    else:
        return render_template(
            "no_jobs.html",
            jobsavailable=jobsavailable
        )

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=3001, debug =True)  
