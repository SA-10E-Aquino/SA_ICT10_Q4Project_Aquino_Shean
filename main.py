from pyscript import document


# Class definition
class Classmate:
    def __init__(self, name, section, favorite_subject, birthstone):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
        self.birthstone = birthstone

    def introduce(self):
        return (
            f"Hi! I'm {self.name} from {self.section}. "
            f" My favorite subject is {self.favorite_subject}. "
            f" My birthstone is {self.birthstone}."
        )

# Initial classmates
classmates = [
    Classmate("Alotaya", "Emerald", "ICT", "Emerald"),
    Classmate("Alwit", "Emerald", "Filipino", "Sapphire"),
    Classmate("Aquino", "Emerald", "English", "Peridot/Spinel/Sardonyx"),
    Classmate("Brar", "Emerald", "P.E. & Health", "Diamond"),
    Classmate("Chavez", "Emerald", "Social Studies", "Citrine/Topaz"),
    Classmate("Chua", "Emerald", "Filipino", "Diamond"),
    Classmate("De Los Santos", "Emerald", "P.E. & Health", "Pearl/Moonstone/Alexandrite"),
    Classmate("Estabillo", "Emerald", "Music & Arts", "Emerald"),
    Classmate("Faner", "Emerald", "Music & Arts", "Ruby"),
    Classmate("Fernandez", "Emerald", "Filipino", "Emerald"),
    Classmate("Gale", "Emerald", "P.E. & Health", "Pearl/Moonstone/Alexandrite"),
    Classmate("Garcia", "Emerald", "Science", "Amethyst"),
    Classmate("Gill", "Emerald", "Mathematics", "Amethyst"),
    Classmate("Kaur", "Emerald", "Filipino", "Sapphire"),
    Classmate("Laeda", "Emerald", "Mathematics", "Sapphire"),
    Classmate("Lusica", "Emerald", "Music & Arts", "Pearl/Moonstone/Alexandrite"),
    Classmate("Macala", "Emerald", "P.E. & Health", "Garnet"),
    Classmate("Macas", "Emerald", "Science", "Diamond"),
    Classmate("Maranan", "Emerald", "Mathematics", "Pearl/Moonstone/Alexandrite"),
    Classmate("Montemayor", "Emerald", "Music & Arts", "Diamond"),
    Classmate("Musor", "Emerald", "Music & Arts", "Pearl/Moonstone/Alexandrite"),
    Classmate("Omnes", "Emerald", "Mathematics", "Citrine/Topaz"),
    Classmate("Oreiro", "Emerald", "Social Studies", "Emerald"),
    Classmate("Platon", "Emerald", "P.E. & Health", "Pearl/Moonstone/Alexandrite"),
    Classmate("Ramirez", "Emerald", "ICT", "Amethyst"),
    Classmate("Razonable", "Emerald", "Science", "Diamond"),
    Classmate("Salvador E.", "Emerald", "ICT", "Sapphire"),
    Classmate("Salvador T.", "Emerald", "P.E. & Health", "Pearl/Moonstone/Alexandrite"),
    Classmate("Silleza", "Emerald", "Music & Arts", "Garnet"),
    Classmate("Tiwari", "Emerald", "P.E. & Health", "Garnet"),
    Classmate("Villanueva", "Emerald", "Science", "Garnet"),
]

# ADD
def add_classmate(e):
    name = document.getElementById("classmate1").value.strip()
    section = document.getElementById("section").value.strip()
    subject = document.getElementById("subject").value.strip()
    birthstone = document.getElementById("birthstone").value.strip()

    # Validation
    if name == "" or section == "" or subject == "" or birthstone == "":
        document.getElementById("output").innerHTML = (
            '<div class="alert alert-danger">'
            '⚠️ Please fill out all fields.'
            '</div>'
        )
        return
    for c in classmates:
        if c.name.lower() == name.lower():
            document.getElementById("output").innerHTML = (
                '<div class="alert alert-warning">'
                '⚠️ Classmate with this name already exists.'
                '</div>'
            )
            return

    classmates.append(Classmate(name, section, subject, birthstone))


    document.getElementById("output").innerHTML = (
        f'<div class="alert alert-success">'
        f'✅ {name} added successfully!'
        '</div>'
    )
    
    # Auto Refresh List
    render_list(classmates)

    # Clear inputs
    document.getElementById("classmate1").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""
    document.getElementById("birthstone").value = ""

# SHOW LIST
def show_classmates(e):
    render_list(classmates)

# SEARCH
def search_classmates(e):
    keyword = document.getElementById("search").value.lower().strip()

    filtered = []
    for student in classmates:
        if keyword in student.name.lower():
            filtered.append(student)

    if len(filtered) == 0:
        document.getElementById("output").innerHTML = (
            '<div class="alert alert-warning">'
            '⚠️ No classmates found.'
            '</div>'
        )

    else:
        render_list(filtered)

# DELETE
def delete_classmate_by_name(name):
    global classmates

    classmates = [c for c in classmates if c.name != name]
    render_list(classmates)

# HANDLER
def handle_delete(e):
    name = e.currentTarget.getAttribute("data-name")
    delete_classmate_by_name(name)

# RENDER
def render_list(data):
    html = '<ul class="list-group">'

    for student in data:
        html += f'''
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
            {student.introduce()}
            </div>
            
            <button class="btn btn-danger btn-sm"
                data-name="{student.name}"
                py-click="handle_delete">
                Delete
            </button>
        </li>
        '''

    html += '</ul>'

    document.getElementById("output").innerHTML = html