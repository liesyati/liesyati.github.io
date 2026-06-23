import networkx as nx
import matplotlib.pyplot as plt
import uuid
import re
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# Anda bisa MENGEDIT nama-nama di bawah ini dengan fleksibel!
# Ganti huruf a, b, c atau titik-titik dengan nama asli jika sudah diketahui.
tree_text = """
1. Jalur Keturunan MUTMA'INAH + NUR HASAN
2. Jalur Keturunan KHOSIM MUSTOFA + MUNJIYAH
1. Qosidah + Bastomi (Alm)
   * a. Vivin
   * b. 
   * c. 
2. Kholifah + Nur Fadil
   * a. Ika
   * b. 
3. Khoirul Anwar + Hartatik
   * a. Hardi
   * b. 
4. Kun Faizah + M. Suqi Manan
   * a. Zainudin Hanif
   * b. Linda Hanafiah
5. Kamilah + Suwandi
   * a. 
   * b. 
6. Kholid Mustofa + …...
   * a. 
7. Jadid Mustofa + Nur Aini
   * a. 
   * b. 
8. Jawad Mustofa + Nur Azizah
   * a. 
   * b. 
3. Jalur Keturunan MARDIYAH + M. MUZAIYEN BAKRI
1. Dzakwan Ambara + Nur Aini
   * a. 
   * b. 
   * c. 
   * d. 
2. Muthohharul Jannan + Neng Ati-ati…..
   * a. 
   * b. 
3. Ulumiyah + Nafiq Ridwan
   * a. Ninis
      * 1. ….
      * 2. …..
   * b. Wildana Widad Fitriana
   * c. Marsha Laila….
4. Chamidah Hanum + Eriwanto
   * a. Riris
   * b. Dawas…..
5. Luluk Jamilah + ….
   * a. 
   * b. 
4. Jalur Keturunan MOETASLIMAH + SHOELKHAN
1. Nadhiroh + Ahmad Maimun
   * a. Niswatul Mustafidah + Ali Budiarto
      * 1. Luna
   * b. Ahmad Zidny Yusron +
      * 1. …..
      * 2. …..
      * 3. ….
   * c. M. Ismet Amrillah + Jihan
      * 1. Ghisna
2. Aunur Rofik + Amik Suparwati Nengseh
   * a. Amelia Syuafitri + Akhmal Musafa
      * 1. Rama
      * 2. Farzan
   * b. Dias Deva Ardani
      * 1. Zara
      * 2. Atta
   * c. Faisal Charis
   * d. M. Aldi Risaldi
      * 1. Yusuf
   * c. Tasbita …...
3. Mas'di + Lilis Nurhayati
   * a. Ahmad Fakhrurrozi Amrillah + Nursiva Fitriani
      * 1. Mikail Fawwaz Ruziva
   * b. Ailsa Nabilah Tsani Mas'ud + Cakra Birahmadhika
      * 1. Kianara Anindya Putri Birahmadhika
   * c. Alwan Hakim Ramadhani
4. Ahmad Rif'an + Umi Rahayu
   * a. Nadia Ariesta Azzarin
   * b. Nadinda Itsna Suhaela
5. Nurul Muttaqin + Siti Isngadah
   * a. Adi Rizky Hasan Muttaqin + Prilly
      * 1. 
      * 2. 
   * b. Isal
6. Awam Abdullah + Ipung Purwati
   * a. Avadata Firdausin
   * b. Gibron Khoiruzade Attaqi
7. Hadayati Rohmatun + Dwi Febriyanto
   * a. M. Wildan Aufar Ilman
   * b. M. Nailul Yusril Al ghifari
   * c. Mayda Alimatunisa
5. Jalur Keturunan NUR JANNAH + NUR KASAN MANAN
1. Lailatul Latifah + Mardi
   * a. Haqqi Annazil
   * b. Rizky
2. Iffa Maulidia (Alm.) + Yurid …...
   * a. Shella
   * b. ….
3. Rahmad Aminudin + Yuli (Alm)
   * a. Kafi
   * b. ….
4. Sholehudin + 
   * a. …
   * b. …
5. Alwin + Sari
   * a. ….....
6. Jalur Keturunan NUR FADILAH + M. MUKIM ASAD
1. Maqomatul Ithoah + Nano Artono
   * a. Hakam
   * b. …...
2. M. Makki Nuruddin + Emma …....
   * a. 
   * b. 
3. Qoulul Jadidah + Abdul Rochim
   * a. Qolbi ….
   * b. Salsabila
4. Annas
7. Jalur Keturunan MAHMUDAH + KHUSAIN ROFI'I
1. Khoiro Umma + Ahmad Heriyanto
   * a. 
2. Khoirul Anam + Didin
   * a. …
   * b. ….
3. Lukmanul Hakim (Alm) + Devi
   * a. …
   * b. 
4. Husni (Alm) + .,…
   * a. …..
5. Ghoni…..
"""

# Proses pembuatan graf
G = nx.DiGraph()
root_id = "root"
G.add_node(root_id, label="NACHROWI\n&\nDEWI MARIAM")

def clean_label(text):
    text = text.replace('+', '\n&').strip()
    text = re.sub(r'^[0-9a-z]\.\s*(Jalur Keturunan )?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\.{2,}', '', text).strip()
    if text == "" or text == "&":
        return "(...)"
    if text.endswith("\n&"):
        text += " (...)"
    return text

current_path = {1: root_id}

for line in tree_text.strip().split('\n'):
    if not line.strip(): continue
    
    if "Jalur Keturunan" in line:
        level = 2
    elif line.startswith("   * a.") or line.startswith("   * b.") or line.startswith("   * c.") or line.startswith("   * d."):
        level = 4
    elif line.startswith("      * 1.") or line.startswith("      * 2.") or line.startswith("      * 3."):
        level = 5
    elif line[0].isdigit():
        level = 3
    else:
        continue
        
    raw_name = line.strip().replace('* ', '')
    label = clean_label(raw_name)
    
    node_id = str(uuid.uuid4())
    G.add_node(node_id, label=label)
    
    parent_id = current_path.get(level - 1)
    if parent_id:
        G.add_edge(parent_id, node_id)
        
    current_path[level] = node_id

# Algoritma penataan letak (layout)
def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parsed=None):
        if pos is None: pos = {}
        if parsed is None: parsed = set()
        pos[root] = (xcenter, vert_loc)
        parsed.add(root)
        children = list(G.successors(root))
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width=dx, vert_gap=vert_gap, 
                                    vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parsed=parsed)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

pos = hierarchy_pos(G, "root", width=1.0, vert_gap=0.3)

leaves = [node for node in G.nodes() if G.out_degree(node) == 0]
leaves.sort(key=lambda n: pos[n][0])
leaf_x = {leaf: i / (len(leaves)-1) for i, leaf in enumerate(leaves)}

def update_x(node):
    if G.out_degree(node) == 0:
        return leaf_x[node]
    children = list(G.successors(node))
    xs = [update_x(child) for child in children]
    new_x = sum(xs) / len(xs)
    pos[node] = (new_x, pos[node][1])
    return new_x

update_x("root")

# Pengaturan visual
labels = nx.get_node_attributes(G, 'label')

# Hitung lebar gambar yang dinamis agar gap memadai dan tidak berdekatan
num_leaves = len(leaves)
fig_width = max(60, num_leaves * 2.5) # Lebar menyesuaikan jumlah anak di tingkat terbawah
plt.figure(figsize=(fig_width, 40)) # Ubah angka ini untuk mengubah ukuran gambar

nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=False, width=2)

# Load default icon
try:
    img = mpimg.imread('default_icon.png')
except Exception:
    img = None

for node, (x, y) in pos.items():
    # Menambahkan Foto / Icon jika ada
    if img is not None:
        # zoom factor disesuaikan dengan ukuran gambar. Bisa diubah jika foto terlalu besar/kecil.
        imagebox = OffsetImage(img, zoom=0.08) 
        ab = AnnotationBbox(imagebox, (x, y), frameon=True, bboxprops=dict(edgecolor='lightblue', facecolor='white', boxstyle="circle,pad=0.1"))
        plt.gca().add_artist(ab)
    
    # Menambahkan Text (Nama) di bawah icon
    plt.text(x, y - 0.05, labels[node], fontsize=12, ha='center', va='top', fontweight='bold', bbox=dict(facecolor='white', edgecolor='lightblue', boxstyle='round,pad=0.5'))

plt.title("Silsilah Keluarga Lengkap Nachrowi & Dewi Mariam", fontsize=50, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Menyimpan hasil dan menampilkannya di layar Anda
plt.savefig("hasil_silsilah_saya.png", dpi=100, bbox_inches='tight')
print("Visualisasi berhasil dibuat! Silakan cek file hasil_silsilah_saya.png")
plt.show() # Ini akan memunculkan jendela interaktif di PC Anda