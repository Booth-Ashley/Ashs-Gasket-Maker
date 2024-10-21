import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import math
import os

try:
    import ezdxf
except ImportError:
    messagebox.showerror("Error", "Required library 'ezdxf' not found.")
    sys.exit(1)

class GasketMaker:
    def __init__(self, master):
        self.master = master
        master.title("Ash's Gasket Maker")
        
        # Set the window icon
        if getattr(sys, 'frozen', False):
            # We are running in a PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # We are running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        icon_path = os.path.join(base_path, 'ash.ico')
        master.iconbitmap(icon_path)

        # Input fields
        tk.Label(master, text="Outside Diameter:").grid(row=0, column=0, sticky="e", padx=10, pady=0)
        self.outside_diameter = tk.Entry(master)
        self.outside_diameter.grid(row=0, column=1)

        tk.Label(master, text="Inside Diameter:").grid(row=1, column=0, sticky="e", padx=10, pady=0)
        self.inside_diameter = tk.Entry(master)
        self.inside_diameter.grid(row=1, column=1)

        tk.Label(master, text="PCD:").grid(row=2, column=0, sticky="e", padx=10, pady=0)
        self.pcd = tk.Entry(master)
        self.pcd.grid(row=2, column=1)

        tk.Label(master, text="Number of Holes:").grid(row=3, column=0, sticky="e", padx=10, pady=0)
        self.num_holes = tk.Entry(master)
        self.num_holes.grid(row=3, column=1)

        tk.Label(master, text="Hole Diameter:").grid(row=4, column=0, sticky="e", padx=10, pady=0)
        self.hole_diameter = tk.Entry(master)
        self.hole_diameter.grid(row=4, column=1)

        # Button
        tk.Button(master, text="Create Gasket", command=self.create_gasket).grid(row=5, column=1, columnspan=2, pady=10)

        # Version
        self.version_label = tk.Label(master, text="V1.01", bg="#f4f4f4", fg="gray", font=("Arial", 6))
        self.version_label.place(relx=0.0, rely=1.0, x=10, y=-10, anchor="sw")

    def create_gasket(self):
        try:
            outside_dia = float(self.outside_diameter.get())
            inside_dia = float(self.inside_diameter.get())
            pcd = float(self.pcd.get())
            num_holes = int(self.num_holes.get())
            hole_dia = float(self.hole_diameter.get())

            if outside_dia <= inside_dia:
                raise ValueError("Outside diameter must be greater than inside diameter.")
            if pcd <= inside_dia or pcd >= outside_dia:
                raise ValueError("PCD must be between inside and outside diameters.")
            if num_holes <= 0:
                raise ValueError("Number of holes must be positive.")
            if hole_dia <= 0:
                raise ValueError("Hole diameter must be positive.")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            return

        # Create a new DXF file
        doc = ezdxf.new('R2010')
        msp = doc.modelspace()

        # Create outside circle
        msp.add_circle((0, 0), radius=outside_dia/2)

        # Create inside circle
        msp.add_circle((0, 0), radius=inside_dia/2)

        # Create holes in a polar array
        angle_step = 360 / num_holes
        for i in range(num_holes):
            angle = math.radians(i * angle_step)
            x = (pcd/2) * math.cos(angle)
            y = (pcd/2) * math.sin(angle)
            msp.add_circle((x, y), radius=hole_dia/2)

        # Save the DXF file
        save_filename = filedialog.asksaveasfilename(defaultextension=".dxf", filetypes=[("DXF files", "*.dxf")])
        if save_filename:
            doc.saveas(save_filename)
            messagebox.showinfo("Success", "Gasket created successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = GasketMaker(root)
    root.geometry("270x180")
    root.resizable(False, False) 
    root.mainloop()