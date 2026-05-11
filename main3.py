from pyscript import document

# Gallery Data
activities = [
    {"img": "10-Emerald Class Photos.jpg", "caption": "10-Emerald's Group Pictures"},
    {"img": "Food Fair & Minimart.jpg", "caption": "A school-wide fundraising initative and a day for delicious food, beverages, fresh products, and more, all the while supporting a great cause!"},
    {"img": "Christmas Party.jpg", "caption": "A joyful celebration with the holiday spirit held during the holiday season."},
    {"img": "LTCAT.jpeg", "caption": "Leadership Development, Citizenship, Discipline, Teamwork, Character Development, and Public Service."},
    {"img": "Project Hiraya.png", "caption": "10-Emerald Group#1's Peace Project. An initiative project to help focus on inspiring hope, creativity, and positive change within communities especially the youth."},
    {"img": "Lakad Ligtas.png", "caption": "10-Emerald Group#2's Peace Project. An initative project that promotes pedestrian safety, responsible road use, and safer public spaces for everyone."},
    {"img": "Intrams.jpg", "caption": "OBMC High School Intramurals serves as a practical application of the skills learned in P.E. Class. Develop sportsmanship and teamwork among students. Boost physical stamina. Strengthens self-discipline and determination."},
    {"img": "CAT Graduation.jpeg", "caption": "Graduating from C.A.T."}
]

container = document.getElementById("python-gallery")

html = ""

for item in activities:
    html += f"""
    <div>
        <div class="card gallery-card shadow-sm h-100" 
        onclick="openModal('{item['img']}', '{item['caption']}')">

        <img src="{item['img']}" class="card-img-top">

        <div class="card-body text-center">
            <p class="card-text fw-semibold">{item['caption']}</p>
        </div>
    </div>
 </div>
    """

container.innerHTML = html

# Modal Function
def openModal(img, caption):
    modal_img = document.getElementById("modalImage")
    modal_caption = document.getElementById("modalCaption")

    modal_img.src = img
    modal_caption.innerText = caption

    from js import bootstrap
    modal = bootstrap.Modal.getOrCreateInstance(
        document.getElementById("imageModal")
    )
    modal.show()

# Make Function Callable from HTML
import js
js.openModal = openModal
