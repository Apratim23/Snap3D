# 🧠📸 Text or Photo → 3D Model | Prototype Submission

A Python-based prototype that converts **either a single photo** or a **short descriptive text** into a **basic 3D model** (`.obj` or `.stl`) with visualization. 

---

## 🚀 Features

- ✅ Accepts **image (.jpg/.png)** or **text prompt**
- ✅ Performs **background removal** (image input)
- ✅ Generates a **3D placeholder model** (using `trimesh`)
- ✅ Supports **exporting to `.stl` or `.obj`**
- ✅ **Visualizes** the model using `matplotlib`
- ✅ Clean, modular Python code — ready for model integration

---

## 🧠 Thought Process

> The objective was to build a working prototype demonstrating:
> 
> 1. Preprocessing image input (background removal)
> 2. Basic 3D generation logic from either photo or text
> 3. Clear output in standard 3D formats
> 
> Instead of trying to create complex geometry, I focused on writing clean, modular, extensible code that can later be connected to real 3D model generation models like TripoSR or Point-E.

---

## 🛠️ Setup Instructions

### 1. Create virtual environment

```
python -m venv venv  
 ```

# Windows
```
venv\Scripts\activate
```
# macOS/Linux
```
source venv/bin/activate
```

2. Install required libraries
```
pip install -r requirements.txt
```

# ⚙️ Usage
## 📷 Convert Image to 3D
 Place an image inside the inputs/ folder (e.g., chair.png) and run:
```
python main.py --image inputs/chair.png --format obj
```
* Background will be removed

* 3D box mesh will be created

* Output saved to outputs/

* Model preview will appear (unless disabled)

## ✏️ Convert Text to 3D
```
python main.py --text "A small toy car" --format stl
```
## 📦 Output Files
* 📁 outputs/<name>.stl or .obj – 3D model file

* 🖼️ outputs/bg_removed.png – background-free image

* 📈 3D preview (if enabled)

## 📚 Tech Stack & Libraries
* rembg – background removal

* trimesh – 3D mesh creation and export

* matplotlib – 3D model preview

* Pillow – image handling

## 🔮 Next Steps / Future Improvements
* 🔄 Integrate TripoSR or Point-E for realistic mesh generation

* 🌈 Add support for textured/colored meshes

* 🌐 Build a simple web UI (Streamlit or Flask)

* 🧪 Add unit tests and model validation logic

## ✅ Status
* 🧪 Prototype Complete

* ✅ Meets all assignment requirements

* 💡 Designed to be modular, scalable, and extensible

## 📈 Contributing

Contributions are welcome! Please feel free to submit a Pull Request 🎉.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Apratim23/Snap3D/blob/main/LICENSE) file for details 📝.

## 👨‍💻 Developer

Developed by [@Apratim23](https://github.com/Apratim23) 🌟

[LinkedIn](https://www.linkedin.com/in/apratim-dutta-78b5ba216/)
[GitHub](https://github.com/Apratim23)

